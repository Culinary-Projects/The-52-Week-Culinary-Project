#!/usr/bin/env python3
"""
Split block index.md files into individual session/service pages.

Each `### Session N — Title` and `### ⏰ Service N — Title` section is
extracted into its own file. The index.md is rebuilt with the preamble,
block intros + session link lists, and the Go Deeper section.

Usage:
    # Dry-run on one block (shows what would be created, no writes):
    python scripts/split_sessions.py --dry-run --block 01-02-knife-skills

    # Run on one block (writes files):
    python scripts/split_sessions.py --block 01-02-knife-skills

    # Run on all blocks:
    python scripts/split_sessions.py
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS_DIR = ROOT / "docs"
BLOCKS_DIR = DOCS_DIR / "blocks"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Convert a heading title to a URL-safe filename slug."""
    # Strip emojis / symbols
    text = "".join(
        c for c in text
        if unicodedata.category(c) not in ("So", "Sk", "Sm", "Mn")
    )
    # Normalize and drop non-ASCII
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    text = re.sub(r"-+", "-", text)
    return text


def parse_session_heading(heading_text: str):
    """
    Determine whether a ### heading is a Session or Service.

    Returns (kind, num, title, nav_title) or None.
    kind: 'session' | 'service'
    """
    h = heading_text.strip()
    h = re.sub(r"^⏰\s*", "", h)  # strip leading clock emoji

    m = re.match(r"Service\s+(\d+)\s*[—–-]+\s*(.+)", h)
    if m:
        num, title = m.group(1), m.group(2).strip()
        return ("service", num, title, f"⏰ Service {num}: {title}")

    m = re.match(r"Session\s+(\d+)\s*[—–-]+\s*(.+)", h)
    if m:
        num, title = m.group(1), m.group(2).strip()
        return ("session", num, title, f"Session {num}: {title}")

    return None


def strip_fences(text: str) -> str:
    """Remove leading/trailing blank lines and bare `---` separators."""
    text = text.strip()
    text = re.sub(r"^\s*---\s*\n", "", text)
    text = re.sub(r"\n\s*---\s*$", "", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

def parse_index(content: str):
    """
    Parse a block index.md into three parts:

    preamble   — everything before the first `## Block N` heading
    blocks     — list of dicts:
                   { num, title, heading_line, intro_lines, sessions }
                 each session: { kind, num, title, slug, filename,
                                 nav_title, heading_line, content_lines }
    go_deeper  — everything from `## Optional: Go Deeper` (or similar) onward

    Returns (preamble_str, blocks, go_deeper_str).
    """
    lines = content.split("\n")

    preamble_lines = []
    go_deeper_lines = []
    blocks = []

    current_block = None
    current_session = None
    state = "preamble"  # preamble | block_intro | in_session | go_deeper

    def finalize_session():
        nonlocal current_session
        if current_session and current_block is not None:
            current_block["sessions"].append(current_session)
        current_session = None

    def finalize_block():
        nonlocal current_block
        finalize_session()
        if current_block is not None:
            blocks.append(current_block)
        current_block = None

    for line in lines:
        # ── Level-2 heading ──────────────────────────────────────────────
        h2 = re.match(r"^## (.+)$", line)
        if h2:
            heading = h2.group(1).strip()

            # Block heading?
            bm = re.match(r"Block\s+(\d+)\s*[—–-]+\s*(.+)", heading)

            # Go-deeper heading?
            is_deeper = bool(
                re.search(r"go deeper|optional", heading, re.IGNORECASE)
            ) or (
                state in ("block_intro", "in_session")
                and not bm
                and not re.match(r"Before You", heading, re.IGNORECASE)
            )

            if is_deeper:
                finalize_block()
                state = "go_deeper"
                go_deeper_lines.append(line)

            elif bm:
                finalize_block()
                current_block = {
                    "num": bm.group(1),
                    "title": bm.group(2).strip(),
                    "heading_line": line,
                    "intro_lines": [],
                    "sessions": [],
                }
                state = "block_intro"

            else:
                # e.g. "## Before You Start Block 1" — stays in preamble / block_intro
                if state == "preamble":
                    preamble_lines.append(line)
                elif state in ("block_intro", "in_session"):
                    finalize_session()
                    state = "block_intro"
                    current_block["intro_lines"].append(line)
                elif state == "go_deeper":
                    go_deeper_lines.append(line)
            continue

        # ── Level-3 heading ──────────────────────────────────────────────
        h3 = re.match(r"^### (.+)$", line)
        if h3 and state in ("block_intro", "in_session"):
            heading = h3.group(1).strip()
            parsed = parse_session_heading(heading)

            if parsed:
                finalize_session()
                kind, num, title, nav_title = parsed
                prefix = "service" if kind == "service" else "session"
                slug = f"{prefix}-{num}-{slugify(title)}"
                current_session = {
                    "kind": kind,
                    "num": num,
                    "title": title,
                    "slug": slug,
                    "filename": f"{slug}.md",
                    "nav_title": nav_title,
                    "heading_line": line,
                    "content_lines": [],
                }
                state = "in_session"
                continue
            else:
                # Not a session — add to block intro or session content
                if state == "block_intro":
                    current_block["intro_lines"].append(line)
                else:
                    current_session["content_lines"].append(line)
                continue

        # ── Regular line — route to current state ───────────────────────
        if state == "preamble":
            preamble_lines.append(line)
        elif state == "block_intro":
            current_block["intro_lines"].append(line)
        elif state == "in_session":
            current_session["content_lines"].append(line)
        elif state == "go_deeper":
            go_deeper_lines.append(line)

    # Finalize anything still open
    finalize_block()

    return (
        "\n".join(preamble_lines),
        blocks,
        "\n".join(go_deeper_lines),
    )


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def build_session_file(session: dict, block_title: str, index_rel: str) -> str:
    """Build the content of an individual session/service file."""
    content = strip_fences("\n".join(session["content_lines"]))

    back_link = f"[← {block_title} Overview]({index_rel})"

    lines = [
        f"# {session['heading_line'].lstrip('#').strip()}",
        "",
        back_link,
        "",
        "---",
        "",
        content,
        "",
        "---",
        "",
        back_link,
    ]
    return "\n".join(lines) + "\n"


def build_updated_index(preamble: str, blocks: list, go_deeper: str) -> str:
    """Rebuild index.md with session content replaced by link lists."""
    parts = [preamble.rstrip()]

    for block in blocks:
        parts.append("")
        parts.append("")
        parts.append(block["heading_line"])

        intro = strip_fences("\n".join(block["intro_lines"]))
        if intro:
            parts.append("")
            parts.append(intro)

        if block["sessions"]:
            parts.append("")
            for s in block["sessions"]:
                parts.append(f"- [{s['nav_title']}]({s['filename']})")

        parts.append("")
        parts.append("---")

    if go_deeper.strip():
        parts.append("")
        parts.append(go_deeper.strip())

    return "\n".join(parts) + "\n"


# ---------------------------------------------------------------------------
# Nav YAML builder
# ---------------------------------------------------------------------------

def build_nav_entry(
    block_dir: Path, blocks_data: list, existing_nav_label: str, unit_prefix: str
) -> str:
    """
    Build the YAML nav fragment for one block directory.

    existing_nav_label: the label used in the current mkdocs.yml (with em-dash etc.)
    unit_prefix: relative path prefix like 'blocks/01-foundational-skills/01-02-knife-skills'
    """
    lines = [f'    - "{existing_nav_label}":']
    lines.append(f"      - Overview: {unit_prefix}/index.md")

    # quick-ref and shopping-list if they exist
    if (block_dir / "quick-ref.md").exists():
        lines.append(f"      - Quick Reference: {unit_prefix}/quick-ref.md")
    if (block_dir / "shopping-list.md").exists():
        lines.append(f"      - Shopping List: {unit_prefix}/shopping-list.md")

    for block in blocks_data:
        for s in block["sessions"]:
            lines.append(f'      - "{s["nav_title"]}": {unit_prefix}/{s["filename"]}')

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Per-block processor
# ---------------------------------------------------------------------------

def process_block(block_dir: Path, dry_run: bool, verbose: bool) -> list:
    """
    Process one block directory.

    Returns list of (nav_title, filename) pairs for nav generation,
    or empty list if the block has no recognised sessions.
    """
    index_path = block_dir / "index.md"
    if not index_path.exists():
        return []

    content = index_path.read_text(encoding="utf-8")
    preamble, blocks, go_deeper = parse_index(content)

    all_sessions = [s for b in blocks for s in b["sessions"]]
    if not all_sessions:
        if verbose:
            print(f"  [SKIP] {block_dir.name} — no sessions found")
        return []

    # Determine a display label for back-links (first H1 without emoji, or block dir name)
    h1_match = re.search(r"^# (.+)$", preamble, re.MULTILINE)
    if h1_match:
        block_title = re.sub(r"[^\w\s–—:&/]", "", h1_match.group(1)).strip()
        block_title = re.sub(r"\s+", " ", block_title)
    else:
        block_title = block_dir.name

    print(f"  {'[DRY-RUN] ' if dry_run else ''}Processing {block_dir.name}")

    nav_entries = []

    for session in all_sessions:
        out_path = block_dir / session["filename"]
        file_content = build_session_file(session, block_title, "index.md")

        if dry_run:
            print(f"    → {session['filename']} ({len(file_content)} bytes)")
        else:
            out_path.write_text(file_content, encoding="utf-8")
            if verbose:
                print(f"    → wrote {session['filename']}")

        nav_entries.append((session["nav_title"], session["filename"]))

    # Rewrite index.md
    new_index = build_updated_index(preamble, blocks, go_deeper)
    if dry_run:
        print(f"    → index.md (rewritten, {len(new_index)} bytes)")
        if verbose:
            print("    ---- NEW INDEX PREVIEW (first 60 lines) ----")
            for ln in new_index.split("\n")[:60]:
                print(f"    {ln}")
            print("    ---- END PREVIEW ----")
    else:
        index_path.write_text(new_index, encoding="utf-8")
        if verbose:
            print(f"    → rewrote index.md")

    return nav_entries


# ---------------------------------------------------------------------------
# mkdocs.yml updater
# ---------------------------------------------------------------------------

NAV_LABEL_RE = re.compile(
    r'^(\s+- ")([^"]+)":\s*$'  # lines like:  - "Block 1–2: Knife Skills":
)
FULL_GUIDE_RE = re.compile(
    r'^\s+- (Full Guide|Overview): (.+)$'
)

def update_mkdocs_nav(mkdocs_path: Path, all_nav_data: dict, dry_run: bool):
    """
    Inject session nav entries into mkdocs.yml.

    all_nav_data: { relative_block_path: [(nav_title, filename), ...], ... }
    e.g. { 'blocks/01-foundational-skills/01-02-knife-skills': [('Session 1: ...', 'session-1-...md'), ...] }
    """
    content = mkdocs_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Look for "Full Guide:" or "Overview:" lines pointing to a block index
        fg = re.match(r'^(\s+)- (Full Guide|Overview): (blocks/.+/index\.md)\s*$', line)
        if fg:
            indent = fg.group(1)
            label = fg.group(2)
            block_rel = fg.group(3)  # e.g. blocks/01-foundational-skills/01-02-knife-skills/index.md
            block_key = block_rel[: block_rel.rfind("/")]  # strip /index.md

            # Replace "Full Guide" with "Overview"
            result.append(f"{indent}- Overview: {block_rel}")

            if block_key in all_nav_data:
                for nav_title, filename in all_nav_data[block_key]:
                    result.append(f'{indent}- "{nav_title}": {block_key}/{filename}')

            i += 1
            continue

        result.append(line)
        i += 1

    new_content = "\n".join(result)

    if dry_run:
        print("\n  [DRY-RUN] mkdocs.yml would be updated (showing changed lines):")
        for ln in new_content.split("\n"):
            if "session-" in ln or "service-" in ln or "Overview:" in ln:
                print(f"    {ln}")
    else:
        mkdocs_path.write_text(new_content, encoding="utf-8")
        print("  → mkdocs.yml updated")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="Show what would be done without writing any files"
    )
    parser.add_argument(
        "--block", "-b",
        help="Process only the named block directory (e.g. 01-02-knife-skills)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print more detail"
    )
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN — no files will be written ===\n")

    # Collect block directories
    block_dirs = []
    for unit_dir in sorted(BLOCKS_DIR.iterdir()):
        if not unit_dir.is_dir() or unit_dir.name.startswith("."):
            continue
        for bd in sorted(unit_dir.iterdir()):
            if not bd.is_dir() or bd.name.startswith("."):
                continue
            if not (bd / "index.md").exists():
                continue
            if args.block and bd.name != args.block:
                continue
            block_dirs.append(bd)

    if not block_dirs:
        print(f"No matching block directories found.", file=sys.stderr)
        sys.exit(1)

    # Process each block
    all_nav_data = {}  # relative block path → [(nav_title, filename)]

    for bd in block_dirs:
        rel = bd.relative_to(DOCS_DIR)  # e.g. blocks/01-foundational-skills/01-02-knife-skills
        entries = process_block(bd, dry_run=args.dry_run, verbose=args.verbose)
        if entries:
            all_nav_data[str(rel)] = entries

    # Update mkdocs.yml
    mkdocs_path = ROOT / "mkdocs.yml"
    if mkdocs_path.exists() and all_nav_data:
        print("\nUpdating mkdocs.yml ...")
        update_mkdocs_nav(mkdocs_path, all_nav_data, dry_run=args.dry_run)

    print("\nDone." if not args.dry_run else "\nDry run complete.")


if __name__ == "__main__":
    main()
