from pathlib import Path
import shutil
import re
import argparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BLOCKS_NEW = DOCS / "blocks_new"
BLOCKS = DOCS / "blocks"
BLOCKS_BACKUP = DOCS / "blocks_backup"


def is_block_nav_line(line: str) -> bool:
    return bool(
        re.search(r"\]\(\.\./[^)]*index\.md\)", line)
        or re.search(r"\]\(\.\./\.\./[^)]*index\.md\)", line)
        or re.search(r"\]\(\.\./\.\./\.\./[^)]*index\.md\)", line)
    )


def set_nav(filepath: Path, prev_label=None, prev_path=None, next_label=None, next_path=None):
    content = filepath.read_text()
    parts = []
    if prev_label and prev_path:
        parts.append(f"← [{prev_label}]({prev_path})")
    if next_label and next_path:
        parts.append(f"[{next_label} →]({next_path})")
    nav_line = " | ".join(parts)

    lines = content.split("\n")
    out = []
    placed = False

    for line in lines:
        if line.strip() == "*Navigation:*":
            continue
        if is_block_nav_line(line):
            if not placed:
                out.append(nav_line)
                placed = True
            continue
        out.append(line)

    if not placed:
        out.append("")
        out.append(nav_line)

    filepath.write_text("\n".join(out))


def append_session_block(path: Path, heading: str, body: str):
    content = path.read_text()
    if heading in content:
        return
    content = content.rstrip() + "\n\n" + heading + "\n\n" + body.rstrip() + "\n"
    path.write_text(content)


def write_file(path: Path, content: str):
    path.write_text(content.rstrip() + "\n")


def fix_navs(base: Path):
    fs = base / "01-foundational-skills"
    bf = base / "02-building-flavor"
    proteins = base / "03-the-proteins"
    wk = base / "04-worlds-kitchens"
    mastery = base / "05-mastery-and-pastry"

    fixes = [
        (fs / "01-02-knife-skills/index.md", None, None, "Block 3–4: Heat & Cooking", "../03-04-heat-and-cooking/index.md"),
        (fs / "03-04-heat-and-cooking/index.md", "Block 1–2: Knife Skills", "../01-02-knife-skills/index.md", "Block 5–6: Mother Sauces", "../05-06-mother-sauces/index.md"),
        (fs / "05-06-mother-sauces/index.md", "Block 3–4: Heat & Cooking", "../03-04-heat-and-cooking/index.md", "Block 7–8: Stocks & Eggs", "../07-08-stocks-and-eggs/index.md"),
        (fs / "07-08-stocks-and-eggs/index.md", "Block 5–6: Mother Sauces", "../05-06-mother-sauces/index.md", "Block 9–10: Seasoning & Flavor", "../../02-building-flavor/09-10-seasoning-and-flavor/index.md"),
        (bf / "09-10-seasoning-and-flavor/index.md", "Block 7–8: Stocks & Eggs", "../../01-foundational-skills/07-08-stocks-and-eggs/index.md", "Block 11–12: Vegetables", "../11-12-vegetables-plant-forward/index.md"),
        (bf / "11-12-vegetables-plant-forward/index.md", "Block 9–10: Seasoning & Flavor", "../09-10-seasoning-and-flavor/index.md", "Block 13–14: Pasta & Grains", "../13-14-pasta-and-grains/index.md"),
        (bf / "13-14-pasta-and-grains/index.md", "Block 11–12: Vegetables", "../11-12-vegetables-plant-forward/index.md", "Block 15–16: Lamb & Game", "../../03-the-proteins/15-16-lamb-and-game/index.md"),
        (proteins / "15-16-lamb-and-game/index.md", "Block 13–14: Pasta & Grains", "../../02-building-flavor/13-14-pasta-and-grains/index.md", "Block 17–18: Beef", "../17-18-beef/index.md"),
        (proteins / "17-18-beef/index.md", "Block 15–16: Lamb & Game", "../15-16-lamb-and-game/index.md", "Block 19–20: Fish", "../19-20-fish/index.md"),
        (proteins / "19-20-fish/index.md", "Block 17–18: Beef", "../17-18-beef/index.md", "Block 21–22: Shellfish", "../21-22-shellfish/index.md"),
        (proteins / "21-22-shellfish/index.md", "Block 19–20: Fish", "../19-20-fish/index.md", "Block 23–24: Pork & Charcuterie", "../23-24-pork-and-charcuterie/index.md"),
        (proteins / "23-24-pork-and-charcuterie/index.md", "Block 21–22: Shellfish", "../21-22-shellfish/index.md", "Block 25–26: Poultry", "../25-26-poultry/index.md"),
        (proteins / "25-26-poultry/index.md", "Block 23–24: Pork & Charcuterie", "../23-24-pork-and-charcuterie/index.md", "Block 27–28: French Classics", "../../04-worlds-kitchens/27-28-french/index.md"),
        (wk / "27-28-french/index.md", "Block 25–26: Poultry", "../../03-the-proteins/25-26-poultry/index.md", "Block 29–30: Italian", "../29-30-italian/index.md"),
        (wk / "29-30-italian/index.md", "Block 27–28: French Classics", "../27-28-french/index.md", "Block 31–32: Japanese", "../31-32-japanese/index.md"),
        (wk / "31-32-japanese/index.md", "Block 29–30: Italian", "../29-30-italian/index.md", "Block 33–34: Korean", "../33-34-korean/index.md"),
        (wk / "33-34-korean/index.md", "Block 31–32: Japanese Cuisine", "../31-32-japanese/index.md", "Block 35–36: Chinese", "../35-36-chinese/index.md"),
        (wk / "35-36-chinese/index.md", "Block 33–34: Korean Cuisine", "../33-34-korean/index.md", "Block 37–38: Mexican", "../37-38-mexican/index.md"),
        (wk / "37-38-mexican/index.md", "Block 35–36: Chinese Cuisine", "../35-36-chinese/index.md", "Block 39–40: Indian", "../39-40-indian/index.md"),
        (wk / "39-40-indian/index.md", "Block 37–38: Mexican", "../37-38-mexican/index.md", "Block 41–42: Middle Eastern", "../41-42-middle-eastern/index.md"),
        (wk / "41-42-middle-eastern/index.md", "Block 39–40: Indian", "../39-40-indian/index.md", "Block 43–44: Southeast Asian", "../43-44-southeast-asian/index.md"),
        (wk / "43-44-southeast-asian/index.md", "Block 41–42: Middle Eastern", "../41-42-middle-eastern/index.md", "Block 45–46: Bread", "../../05-mastery-and-pastry/45-46-bread/index.md"),
        (mastery / "45-46-bread/index.md", "Block 43–44: Southeast Asian", "../../04-worlds-kitchens/43-44-southeast-asian/index.md", "Block 47–48: Pastry", "../47-48-pastry/index.md"),
        (mastery / "47-48-pastry/index.md", "Block 45–46: Bread", "../45-46-bread/index.md", "Block 49–50: Signature Dishes & Menus", "../49-50-signature-dishes-and-menus/index.md"),
        (mastery / "49-50-signature-dishes-and-menus/index.md", "Block 47–48: Pastry", "../47-48-pastry/index.md", "Block 51–52: Final Exam", "../51-52-final-exam/index.md"),
        (mastery / "51-52-final-exam/index.md", "Block 49–50: Signature Dishes & Menus", "../49-50-signature-dishes-and-menus/index.md", None, None),
    ]

    for args in fixes:
        set_nav(*args)


def update_unit_readmes(base: Path):
    write_file(
        base / "01-foundational-skills/README.md",
        """# Unit 1: Foundational Skills (Blocks 1–8)

This unit builds core professional technique: knife control, heat management, foundational sauces, stocks, and egg cookery.

## Blocks

| Blocks | Topic |
|---|---|
| 1–2 | Knife Skills |
| 3–4 | Heat & Cooking |
| 5–6 | Mother Sauces |
| 7–8 | Stocks & Eggs |
""",
    )

    write_file(
        base / "02-building-flavor/README.md",
        """# Unit 2: Building Flavor (Blocks 9–14)

This unit develops seasoning judgment and composition, then expands into plant-forward cooking and pasta/grains.

## Blocks

| Blocks | Topic |
|---|---|
| 9–10 | Seasoning & Flavor |
| 11–12 | Vegetables (Plant-Forward) |
| 13–14 | Pasta & Grains |
""",
    )

    write_file(
        base / "03-the-proteins/README.md",
        """# Unit 3: The Proteins (Blocks 15–26)

This unit moves through major proteins with progressive butchery, doneness control, and sauce integration.

## Blocks

| Blocks | Topic |
|---|---|
| 15–16 | Lamb & Game |
| 17–18 | Beef |
| 19–20 | Fish |
| 21–22 | Shellfish |
| 23–24 | Pork & Charcuterie |
| 25–26 | Poultry |
""",
    )

    write_file(
        base / "04-worlds-kitchens/README.md",
        """# Unit 4: World’s Kitchens (Blocks 27–44)

This unit applies foundational technique across major global cuisines and closes with a regional capstone.

## Blocks

| Blocks | Topic |
|---|---|
| 27–28 | French |
| 29–30 | Italian |
| 31–32 | Japanese |
| 33–34 | Korean |
| 35–36 | Chinese |
| 37–38 | Mexican |
| 39–40 | Indian |
| 41–42 | Middle Eastern |
| 43–44 | Southeast Asian |
""",
    )

    write_file(
        base / "05-mastery-and-pastry/README.md",
        """# Unit 5: Mastery & Pastry (Blocks 45–52)

This unit consolidates advanced production: breads, pastry/frozen desserts, final menus, and the closing exam.

## Blocks

| Blocks | Topic |
|---|---|
| 45–46 | Bread |
| 47–48 | Pastry |
| 49–50 | Signature Dishes & Menus |
| 51–52 | Final Exam |
""",
    )


def update_docs_readmes(root: Path):
    write_file(
        root / "README.md",
        """# The 52-Week Culinary Project (Docs)

This curriculum is organized into 5 Units, 26 Blocks, and 52 Weeks.

## Unit Map

1. Unit 1 — Foundational Skills (Blocks 1–8)
2. Unit 2 — Building Flavor (Blocks 9–14)
3. Unit 3 — The Proteins (Blocks 15–26)
4. Unit 4 — World’s Kitchens (Blocks 27–44)
5. Unit 5 — Mastery & Pastry (Blocks 45–52)

## Block Index

- 01–02 Knife Skills
- 03–04 Heat & Cooking
- 05–06 Mother Sauces
- 07–08 Stocks & Eggs
- 09–10 Seasoning & Flavor
- 11–12 Vegetables (Plant-Forward)
- 13–14 Pasta & Grains
- 15–16 Lamb & Game
- 17–18 Beef
- 19–20 Fish
- 21–22 Shellfish
- 23–24 Pork & Charcuterie
- 25–26 Poultry
- 27–28 French
- 29–30 Italian
- 31–32 Japanese
- 33–34 Korean
- 35–36 Chinese
- 37–38 Mexican
- 39–40 Indian
- 41–42 Middle Eastern
- 43–44 Southeast Asian
- 45–46 Bread
- 47–48 Pastry
- 49–50 Signature Dishes & Menus
- 51–52 Final Exam
""",
    )

    write_file(
        root / "program-overview.md",
        """# Program Overview

The program runs for 52 weeks across 26 two-week blocks.

## Structure

- Naming: Unit → Block → Session
- Projects are called Service
- Labs remain Labs
- Content is cumulative across Units

## Units

- Unit 1 (Blocks 1–8): Foundational Skills
- Unit 2 (Blocks 9–14): Building Flavor
- Unit 3 (Blocks 15–26): The Proteins
- Unit 4 (Blocks 27–44): World’s Kitchens
- Unit 5 (Blocks 45–52): Mastery & Pastry
""",
    )


def add_new_sessions(base: Path):
    stocks = base / "01-foundational-skills/07-08-stocks-and-eggs/index.md"
    bread = base / "05-mastery-and-pastry/45-46-bread/index.md"
    pastry = base / "05-mastery-and-pastry/47-48-pastry/index.md"

    append_session_block(
        stocks,
        "## Session 34: Cold Soup Lab — Vichyssoise",
        "- Focus: temperature, texture, and smooth purée workflow\n- Output: classic potato-leek vichyssoise served chilled with garnish control",
    )
    append_session_block(
        stocks,
        "## Session 35: Cold Soup Lab — Gazpacho",
        "- Focus: raw blending, acid balance, and seasoning at cold temperature\n- Output: Andalusian-style gazpacho with precise texture and finish",
    )

    append_session_block(
        bread,
        "## Session 178: Baguette Lab",
        "- Focus: gluten development, fermentation timing, and steam baking\n- Output: baguettes with open crumb and crisp crust",
    )
    append_session_block(
        bread,
        "## Session 179: Buttermilk Biscuit Lab",
        "- Focus: lamination by folding, handling cold fat, and tenderness\n- Output: layered biscuits with even rise",
    )
    append_session_block(
        bread,
        "## Session 180: Cornbread Lab",
        "- Focus: batter balance, hydration, and pan heat management\n- Output: cornbread with controlled crumb and crust",
    )

    append_session_block(
        pastry,
        "## Session 186: Frozen Dessert Lab — No-Churn Ice Cream",
        "- Focus: base composition, aeration, and freeze behavior\n- Output: no-churn ice cream with stable scoop texture",
    )
    append_session_block(
        pastry,
        "## Session 187: Frozen Dessert Lab — Sorbet & Granita",
        "- Focus: sugar/acid ratio and crystal control\n- Output: one sorbet and one granita with clean flavor expression",
    )
    append_session_block(
        pastry,
        "## Session 188: Chocolate Lab — Tempering & Ganache",
        "- Focus: crystal structure, working curves, and emulsion stability\n- Output: tempered elements and a stable ganache for plated use",
    )


def swap_blocks_dirs(dry_run: bool):
    if not BLOCKS_NEW.exists():
        raise FileNotFoundError(f"Missing: {BLOCKS_NEW}")
    if not BLOCKS.exists():
        raise FileNotFoundError(f"Missing: {BLOCKS}")

    if dry_run:
        print(f"[DRY-RUN] Would move {BLOCKS} -> {BLOCKS_BACKUP}")
        print(f"[DRY-RUN] Would move {BLOCKS_NEW} -> {BLOCKS}")
        return

    if BLOCKS_BACKUP.exists():
        shutil.rmtree(BLOCKS_BACKUP)
    shutil.move(str(BLOCKS), str(BLOCKS_BACKUP))
    shutil.move(str(BLOCKS_NEW), str(BLOCKS))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without swapping directories")
    args = parser.parse_args()

    fix_navs(BLOCKS_NEW)
    add_new_sessions(BLOCKS_NEW)
    update_unit_readmes(BLOCKS_NEW)
    update_docs_readmes(DOCS)
    swap_blocks_dirs(args.dry_run)
    print("Finalize script complete.")


if __name__ == "__main__":
    main()