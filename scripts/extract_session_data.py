#!/usr/bin/env python3
"""Extract recipe links and compare notes from all session/service files.

Outputs a JSON file and a human-readable summary for rebuilding the review-index.
"""

import json
import os
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).resolve().parent.parent / "docs" / "blocks"

# Domains that indicate a recipe link (not a YouTube video or generic reference)
RECIPE_DOMAINS = [
    "seriouseats.com",
    "bonappetit.com",
    "kingarthurbaking.com",
    "simplyrecipes.com",
    "justonecookbook.com",
    "thewoksoflife.com",
    "epicurious.com",
    "maangchi.com",
    "sipandfeast.com",
    "thekitchn.com",
    "bbcgoodfood.com",
    "recipetineats.com",
    "food52.com",
    "budgetbytes.com",
    "indianhealthyrecipes.com",
    "vietworldkitchen.com",
    "mykoreankitchen.com",
    "koreanbapsang.com",
    "hungryhuy.com",
    "woksoflife.com",
    "rasamalaysia.com",
    "mexicoinmykitchen.com",
    "chinasichuanfood.com",
    "ricenflour.com",
]


def domain_matches(url: str) -> bool:
    """Check if URL matches a known recipe domain."""
    url_lower = url.lower()
    return any(d in url_lower for d in RECIPE_DOMAINS)


def is_youtube(url: str) -> bool:
    return "youtube.com" in url or "youtu.be" in url


def extract_markdown_links(text: str):
    """Extract all markdown links from text. Returns list of (display_text, url)."""
    return re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)


def get_session_id_and_title(content: str):
    """Extract session/service number and title from H1."""
    m = re.search(r'^#\s+(?:⏰\s+)?(?:Session|Service)\s+(\d+)\s*[—–-]\s*(.+)', content, re.MULTILINE)
    if m:
        num = int(m.group(1))
        title = m.group(2).strip()
        # Check if it's a service file
        is_service = bool(re.search(r'^#\s+(?:⏰\s+)?Service', content, re.MULTILINE))
        prefix = "Svc" if is_service else "S"
        return prefix, num, title
    return None, None, None


def extract_compare_notes(content: str):
    """Extract compare notes from 🎥 Compare Notes blockquote."""
    # Pattern: > 🎥 **Compare Notes:** [Title](URL) ...
    pattern = r'>\s*🎥\s*\*\*Compare Notes:?\*\*\s*(.*?)(?:\n(?!>)|$)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        cn_text = m.group(1).strip()
        # Continue capturing if the blockquote spans multiple lines
        # Look for all lines starting with > after the match
        lines = content[m.start():].split('\n')
        full_text = ""
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('>'):
                full_text += " " + stripped.lstrip('> ').strip()
            elif full_text and stripped == "":
                break
            elif full_text and not stripped.startswith('>'):
                break
        if full_text:
            cn_text = full_text.strip()

        links = extract_markdown_links(cn_text)
        yt_links = [(t, u) for t, u in links if is_youtube(u)]
        if yt_links:
            return yt_links
    return []


def extract_recipe_links(content: str):
    """Extract recipe links, trying to distinguish 'dinner' recipes from 'read first' references.

    Returns: dict with keys 'full_meal', 'read_first', 'table', 'all_recipes'
    """
    result = {
        'full_meal': [],
        'read_first': [],
        'table': [],
        'all_recipes': [],
    }

    # Split into sections
    lines = content.split('\n')

    # Track which section we're in
    in_read_first = False
    in_full_meal = False
    in_table = False
    in_numbered_list = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect section headers
        if re.match(r'\*\*(?:Read first|Read|📖 Read):?\*\*', stripped):
            in_read_first = True
            in_full_meal = False
            in_table = False
            in_numbered_list = False
        elif re.match(r'\*\*Full Meal:?\*\*', stripped):
            in_read_first = False
            in_full_meal = True
            in_table = False
            in_numbered_list = False
        elif stripped.startswith('|') and '---' not in stripped and i > 0:
            # Table row
            in_table = True
            in_read_first = False
        elif re.match(r'^\d+\.', stripped):
            in_numbered_list = True
            in_read_first = False
        elif stripped.startswith('#') or stripped.startswith('---'):
            in_read_first = False
            in_full_meal = False
            in_table = False
            in_numbered_list = False
        elif stripped == '' and not in_table:
            if in_full_meal:
                in_full_meal = False
            if in_numbered_list:
                in_numbered_list = False

        # Extract links from this line
        links = extract_markdown_links(stripped)
        recipe_links = [(t, u) for t, u in links if domain_matches(u) and not is_youtube(u)]

        for text, url in recipe_links:
            entry = {'text': text, 'url': url}
            if in_read_first:
                result['read_first'].append(entry)
            elif in_full_meal:
                result['full_meal'].append(entry)
            elif in_table or in_numbered_list:
                result['table'].append(entry)
            else:
                result['all_recipes'].append(entry)

        # Also handle Full Meal on same line as header
        if re.match(r'\*\*Full Meal:?\*\*', stripped):
            for text, url in recipe_links:
                entry = {'text': text, 'url': url}
                if entry not in result['full_meal']:
                    result['full_meal'].append(entry)

    return result


def source_domain(url: str) -> str:
    """Return a short label for the source domain."""
    url_lower = url.lower()
    if "seriouseats.com" in url_lower:
        return "SE"
    elif "bonappetit.com" in url_lower:
        return "BA"
    elif "kingarthurbaking.com" in url_lower:
        return "KA"
    elif "simplyrecipes.com" in url_lower:
        return "SR"
    elif "justonecookbook.com" in url_lower:
        return "JOC"
    elif "thewoksoflife.com" in url_lower or "woksoflife.com" in url_lower:
        return "WoL"
    elif "epicurious.com" in url_lower:
        return "Epi"
    elif "maangchi.com" in url_lower:
        return "Maangchi"
    elif "recipetineats.com" in url_lower:
        return "RT"
    elif "thekitchn.com" in url_lower:
        return "Kitchn"
    elif "bbcgoodfood.com" in url_lower:
        return "BBC"
    elif "sipandfeast.com" in url_lower:
        return "SF"
    elif "food52.com" in url_lower:
        return "F52"
    elif "koreanbapsang.com" in url_lower:
        return "KBS"
    elif "mykoreankitchen.com" in url_lower:
        return "MKK"
    elif "indianhealthyrecipes.com" in url_lower:
        return "IHR"
    elif "vietworldkitchen.com" in url_lower:
        return "VWK"
    elif "hungryhuy.com" in url_lower:
        return "HH"
    elif "rasamalaysia.com" in url_lower:
        return "RM"
    elif "mexicoinmykitchen.com" in url_lower:
        return "MiMK"
    elif "chinasichuanfood.com" in url_lower:
        return "CSF"
    elif "ricenflour.com" in url_lower:
        return "RnF"
    else:
        return url.split("/")[2] if "/" in url else "?"


def process_file(filepath: Path):
    """Process a single session/service file."""
    content = filepath.read_text(encoding='utf-8')
    prefix, num, title = get_session_id_and_title(content)
    if prefix is None:
        return None

    recipes = extract_recipe_links(content)
    compare_notes = extract_compare_notes(content)

    # Combine all dinner recipes (full_meal first priority, then table, then all_recipes)
    # read_first is reference material, not dinner
    dinner_recipes = []
    seen_urls = set()
    for category in ['full_meal', 'table', 'all_recipes']:
        for r in recipes[category]:
            if r['url'] not in seen_urls:
                dinner_recipes.append(r)
                seen_urls.add(r['url'])

    return {
        'id': f"{prefix}{num}",
        'prefix': prefix,
        'num': num,
        'title': title,
        'filepath': str(filepath),
        'dinner_recipes': dinner_recipes,
        'read_first': recipes['read_first'],
        'compare_notes': compare_notes,
    }


def find_all_session_files():
    """Find all session and service .md files."""
    files = []
    for root, dirs, filenames in os.walk(DOCS_ROOT):
        for f in filenames:
            if f.endswith('.md') and (f.startswith('session-') or f.startswith('service-')):
                files.append(Path(root) / f)
    return sorted(files)


def format_recipes_for_index(dinner_recipes):
    """Format recipe list for the review-index Recipes column."""
    if not dinner_recipes:
        return "*(described inline)*"
    parts = []
    for r in dinner_recipes:
        src = source_domain(r['url'])
        parts.append(f"[{r['text']}]({r['url']})")
    return " · ".join(parts)


def format_cn_for_index(compare_notes):
    """Format compare notes for the review-index Compare Notes column."""
    if not compare_notes:
        return "—"
    parts = []
    for title, url in compare_notes:
        parts.append(f"[{title}]({url})")
    return " · ".join(parts)


def main():
    files = find_all_session_files()
    print(f"Found {len(files)} session/service files", file=sys.stderr)

    results = []
    for f in files:
        data = process_file(f)
        if data:
            results.append(data)

    # Sort by prefix (S before Svc) then by number
    results.sort(key=lambda x: (0 if x['prefix'] == 'S' else 1, x['num']))

    # Output JSON
    json_path = Path(__file__).resolve().parent / "session_data.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Wrote {json_path}", file=sys.stderr)

    # Output summary
    print(f"\n{'='*100}")
    print(f"EXTRACTION SUMMARY: {len(results)} sessions/services processed")
    print(f"{'='*100}\n")

    has_dinner = sum(1 for r in results if r['dinner_recipes'])
    has_cn = sum(1 for r in results if r['compare_notes'])
    no_dinner = sum(1 for r in results if not r['dinner_recipes'])
    no_cn = sum(1 for r in results if not r['compare_notes'])

    print(f"Sessions with dinner recipes: {has_dinner}")
    print(f"Sessions without dinner recipes: {no_dinner}")
    print(f"Sessions with compare notes: {has_cn}")
    print(f"Sessions without compare notes: {no_cn}")
    print()

    # Print table output for each entry
    for r in results:
        recipes_str = format_recipes_for_index(r['dinner_recipes'])
        cn_str = format_cn_for_index(r['compare_notes'])
        print(f"| {r['id']} | {r['title']} | {recipes_str} | {cn_str} |")

    # Print entries that still have no data
    print(f"\n{'='*100}")
    print("ENTRIES STILL MISSING DINNER RECIPES:")
    print(f"{'='*100}")
    for r in results:
        if not r['dinner_recipes']:
            print(f"  {r['id']}: {r['title']} ({r['filepath']})")

    print(f"\n{'='*100}")
    print("ENTRIES STILL MISSING COMPARE NOTES:")
    print(f"{'='*100}")
    for r in results:
        if not r['compare_notes']:
            print(f"  {r['id']}: {r['title']} ({r['filepath']})")


if __name__ == '__main__':
    main()
