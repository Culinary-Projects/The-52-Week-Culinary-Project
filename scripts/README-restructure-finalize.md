# Restructure Finalize Runner

Run dry-run first:

```bash
/opt/homebrew/bin/python3 scripts/restructure_52_weeks_finalize.py --dry-run
```

Then apply:

```bash
/opt/homebrew/bin/python3 scripts/restructure_52_weeks_finalize.py
```

What it does:

1. Normalizes block-to-block navigation in all 26 block `index.md` files under `docs/blocks_new`
2. Adds new sessions for cold soups, breads, frozen desserts, and chocolate
3. Updates Unit README files and top-level docs overview files
4. Swaps `docs/blocks_new` into `docs/blocks` and backs up old blocks to `docs/blocks_backup`

Then verify links:

```bash
/opt/homebrew/bin/python3 scripts/verify_docs_links.py
```