# The 52-Week Culinary Project — Copilot Instructions

A 52-week home culinary school structured as a MkDocs site. The curriculum is self-correcting: the learner completes blocks, fills in feedback files, and those files drive content revisions.

**Public repo:** `docs/` — session files, service files, quick-refs, shopping lists, index pages
**Private submodule:** `private/` — feedback logs, pre-start checklists, photos

---

## Non-Negotiable Rules

### 1. Always commit and push when done

After every set of content changes, commit and push without being asked.

- Stage only the files you changed (never `git add -A` blindly — the private submodule has its own repo)
- Write a clear, specific commit message listing what changed per file
- Push immediately after commit

### 2. Cascade changes to ALL related files

A session change is never isolated. When a session's recipe, ingredients, or meal structure changes, also update:

| Changed | Must also update |
|---|---|
| Session recipe or ingredients | `shopping-list.md` for that block |
| Session dish name or skill | `quick-ref.md` for that block |
| Session dish name | `index.md` session list (if the title changes) |
| Service meal structure | `shopping-list.md` + `quick-ref.md` |
| Any block-level change | Check cross-block references (e.g., "use thighs from Block 1–2 breakdown in Block 3–4") |

Do all of these in the same commit. Never split a session change and its shopping list update across separate commits.

### 3. Link hygiene — verify before using

- **Never invent URLs.** If you can't verify a URL exists, do not include it.
- **Fetch every new recipe URL before touching the shopping list.** Load the actual page and extract the full ingredient list. Do not assume you know what a recipe contains based on its name.
- YouTube links must point to a **specific video**, not a channel homepage.
- If a recipe swap requires a URL you can't verify, either omit the link and describe the dish, or add: `<!-- URL unverified — check before publishing -->`
- Note in the commit message whether each new link was verified or is unverified.

### 4. Recipe changes require a full ingredient audit

When any recipe is added or swapped:

1. Fetch the recipe page and extract the **complete** ingredient list — every item, including garnishes, aromatics, and uncommon pantry staples
2. Diff the ingredient list against the current shopping list
3. Update the shopping list with all missing ingredients
4. Remove or adjust any ingredients that no longer apply
5. Only then commit — session file, shopping list, and quick-ref together

The recipe page is the source of truth, not memory.

### 5. Feedback drives curriculum

The `private/feedback/` directory contains post-block feedback logs. When reviewing or revising curriculum:

1. Read the relevant feedback file first — `private/feedback/[block].md`
2. Treat specific complaints as curriculum bugs to fix, not preferences to note
3. Apply changes across all affected files (session, shopping list, quick-ref, index)
4. If feedback flags a recipe as a swap candidate, either make the swap or add `<!-- SWAP CANDIDATE: [reason] -->` in the session file

---

## Curriculum Design Principles

**Audience:** A home cook who already cooks 5 nights a week. Technically capable, has opinions, gets bored by drills that feel like school.

- **Every drill must become dinner.** If a technique produces something the cook doesn't eat, it will be skipped. The drill IS the meal prep.
- **Recipes should reward the skill being taught.** If a session teaches julienne, the meal must *require* julienned vegetables — not as an optional add-on.
- **Don't pad the plate.** A side that doesn't cohere with the dish is worse than no suggestion. Only recommend sides that actually belong.
- **Time matters.** Sessions should land under 90 minutes. Project meals (Service sessions) can run 2 hours.

### 6. Every session = a full meal with linked recipes

Every session and service file **must** include at least one reputable, linked recipe that constitutes dinner for that night. "Described inline" is not acceptable — the student does not have time to hunt for recipes. Link to the actual source (Serious Eats, Bon Appétit, King Arthur, Just One Cookbook, Maangchi, Woks of Life, etc.).

- The recipe link is the source of truth for ingredient lists and method
- If a session teaches a technique, the linked recipe must **require** that technique — it is the vehicle for the drill
- Side dishes, salads, and accompaniments should also be linked when they are part of the meal plan
- The only exceptions are **challenge sessions** explicitly designed as freestyle/no-recipe exercises (e.g., "Cook Without a Recipe," capstone freestyle sessions). These must be clearly marked as challenges in the session file.

If a recipe cannot be linked (no reputable free source exists), describe the dish with enough detail to cook from AND add `<!-- RECIPE NEEDED: [dish name] — no free source found -->` so it gets flagged for resolution.

### 7. Every session and service must have Compare Notes

Every session and service file **must** include a `🎥 Compare Notes` section with at least one YouTube video showing a professional or respected home cook preparing the same (or closely related) dish. The point is for the student to compare their result against someone else's approach.

- Videos must be from a **specific video URL**, not a channel homepage
- Prefer: Jacques Pépin, Kenji López-Alt, Helen Rennie, Claire Saffitz, Ethan Chlebowski, Adam Ragusea, Pailin's Kitchen, Maangchi, Chinese Cooking Demystified, Ranveer Brar, Italia Squisita, Pasta Grannies, Internet Shaquille, ATK/Lan Lam, Food Wishes, and similar reputable creators
- The same exceptions apply as Rule 6 — challenge/freestyle sessions may omit Compare Notes if no meaningful comparison exists
- All YouTube links must be verified (use `yt-dlp --skip-download` or equivalent)

---

## File Structure

```
docs/blocks/[block-folder]/[session-folder]/
├── index.md              ← block overview, Go Deeper, navigation
├── quick-ref.md          ← one-row-per-session table; always in sync
├── shopping-list.md      ← always in sync with sessions
├── session-N-[slug].md   ← skill + full meal + component table
└── service-N-[slug].md   ← project meal (Service sessions)

private/feedback/[block].md  ← post-block feedback; source of truth for revisions
```

### Quick-ref files

One row per session. Columns: Session | Dish | Skill | Link(s). Recipe links must match the session file exactly. When a dish changes, this row changes in the same commit.

### Shopping lists

Organized by: Proteins → Produce → Dairy → Pantry & Dry Goods → Bread → Equipment → Notes.

- Every ingredient in every session must appear
- Annotations explain which session uses each ingredient
- Cross-block carry-overs must appear in both blocks' lists

---

## Commit Message Format

```
[Verb] [scope]: [what changed]

- File 1: specific change
- File 2: specific change
- Shopping list: what was added/removed/updated
- Quick-ref: what row changed
```

Good verbs: `Revise`, `Fix`, `Add`, `Replace`, `Update`, `Remove`

---

## Private Submodule

- `private/` is a git submodule pointing to a separate private repo
- Never stage `private/` changes with the main repo — they commit separately
- `git add private` stages the submodule pointer — only do this if intentional

---

## What Never Changes Without Asking

- The block structure (26 blocks, 2 weeks each)
- The MkDocs site configuration (`mkdocs.yml`)
- The public/private repo split
- Session numbering within a block
