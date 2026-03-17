from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def iter_md_files(base: Path):
    for path in base.rglob("*.md"):
        if "/.git/" in str(path):
            continue
        if "blocks_backup" in str(path):
            continue
        yield path


def should_check_target(target: str) -> bool:
    if target.startswith("http://") or target.startswith("https://"):
        return False
    if target.startswith("mailto:"):
        return False
    if target.startswith("#"):
        return False
    return True


def normalize_target(target: str) -> str:
    return target.split("#", 1)[0].strip()


def main():
    errors = []
    checked = 0

    for md in iter_md_files(DOCS):
        text = md.read_text(errors="ignore")
        for m in LINK_RE.finditer(text):
            raw = m.group(1).strip()
            if not should_check_target(raw):
                continue
            target = normalize_target(raw)
            if not target:
                continue

            candidate = (md.parent / target).resolve()
            checked += 1
            if not candidate.exists():
                errors.append((md, raw))

    print(f"Checked {checked} relative links.")
    if errors:
        print(f"Found {len(errors)} broken links:")
        for src, link in errors:
            print(f"- {src.relative_to(ROOT)} -> {link}")
        sys.exit(1)

    print("No broken relative links found.")


if __name__ == "__main__":
    main()