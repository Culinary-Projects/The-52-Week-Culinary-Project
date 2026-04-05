# The 52-Week Culinary Project — Copilot Instructions

A 52-week home culinary school structured as a MkDocs site. The curriculum is self-correcting: the learner completes blocks, fills in feedback files, and those files drive content revisions.

**Public repo:** `docs/` — session files, service files, quick-refs, shopping lists, index pages
**Private submodule:** `private/` — feedback logs, pre-start checklists, photos

---

## Sourcing Rules

### Approved recipe sources

**Reputable sources only.** Every recipe link must point to a reputable, editorially maintained source. No personal blogs, AI-generated recipe sites, or unverified sources.

#### Tier 1 — Primary recipe authorities

Use these as the default recipe source for their domain. When a Tier 1 source covers a dish well, prefer it over Tier 2.

| Source | Domain | Use for |
|--------|--------|---------|
| **Serious Eats** | Technique-first cooking, food science | Foundational skills, searing, roasting, emulsions, braises, core methods. The curriculum backbone — but cap at **<75% of any single block's recipe links.** |
| **King Arthur Baking** | Bread and pastry | All bread, pastry, and baking sessions (Unit 5). Co-authority with SE for baking. |
| **Just One Cookbook** (Nami) | Japanese | All Japanese sessions (Block 29–30) and Japanese techniques elsewhere. |
| **Maangchi** | Korean | All Korean sessions (Block 31–32). |
| **The Woks of Life** | Chinese | All Chinese sessions (Block 33–34). |

#### Tier 2 — Strong secondary sources

Use these to diversify blocks, fill gaps, or provide a second perspective. Always appropriate alongside Tier 1.

| Source | Domain | Use for |
|--------|--------|---------|
| **Bon Appétit** | General, technique | When SE doesn't cover a dish, or to add a second voice. |
| **BBC Good Food** | European, general | Reliable for British, French, and general European recipes. |
| **Simply Recipes** | Accessible home cooking | Clear, well-tested recipes for everyday dishes. |
| **RecipeTin Eats** (Nagi) | Global home cooking | Australian site with validated worldwide recipes. |
| **The Perfect Loaf** | Sourdough and artisan bread | Complements King Arthur for advanced bread technique. |
| **Spice Up the Curry** | Indian | Indian home cooking with regional specificity. |
| **Indian Healthy Recipes** (Swasthi) | Indian | South Indian and vegetarian Indian cooking. |
| **Love and Lemons** | Vegetable-forward | Plant-based technique and seasonal cooking. |
| **The Kitchn** | General technique | Technique explainers and how-to guides. |

#### Tier 3 — Specialist and cultural authorities (Use when available)

These sources should be preferred over SE when their cuisine is the subject. If a block teaches Mexican food and Rick Bayless has a verified free recipe, use it over a SE version.

| Source | Domain | When to use |
|--------|--------|-------------|
| **Rick Bayless** / mexicoinmykitchen.com | Mexican | Block 35–36 and any Mexican technique. Authoritative, culturally rooted. |
| **Pati Jinich** (patijinich.com) | Mexican | Alternative Mexican authority. Regional specialties. |
| **Madhur Jaffrey** | Indian | When referenced recipes are freely available. The canonical Indian cooking voice in English. |
| **Hebbar's Kitchen** | Indian (vegetarian) | South Indian and vegetarian Indian. |
| **Hot Thai Kitchen** (Pailin) | Thai / SE Asian | Block 39–40 Thai sessions. Written recipes accompany her videos. |
| **Italia Squisita** | Italian | Block 27–28 when technique-level Italian content is needed. |
| **Pasta Grannies** | Italian (traditional) | Traditional pasta technique and regional variation. |
| **Jacques Pépin** | French classical | Block 25–26 and any classical French technique. Definitive voice for mother sauces, eggs, and foundational technique. |
| **De Mi Rancho a Tu Cocina** | Mexican (traditional) | Traditional rural Mexican technique — YouTube with written recipes. |

### Sourcing concentration rules

These rules apply whenever content is added or recipes are swapped:

1. **No block may exceed 75% recipe references from any single source.** If a swap would push a source above 75%, find an alternative from a different approved source.
2. **World cuisine blocks must center a cuisine-native authority.** In Blocks 29–40, the primary recipe source should be a Tier 1 or Tier 3 specialist for that cuisine — not Serious Eats. SE can supplement but should not dominate. Target: culture-native source provides ≥40% of recipe links.
3. **Every block must draw from at least 4 distinct recipe domains.** YouTube and Amazon don't count toward this minimum.
4. **When a Tier 3 specialist covers the dish, prefer them over SE.** A French block session on cassoulet should link to Pépin before SE. A Mexican session on mole should link to Rick Bayless before SE.

### Approved Compare Notes video creators

Every session and service file must have a `🎥 Compare Notes` section. Prefer these creators by domain:

**Technique & General:** J. Kenji López-Alt, Jacques Pépin, Helen Rennie, Ethan Chlebowski, America's Test Kitchen / Lan Lam, Claire Saffitz, Adam Ragusea, Food Wishes (Chef John), Joshua Weissman, Brian Lagerstrom, Internet Shaquille

**Cuisine-Specific:**
- **Italian:** Italia Squisita, Pasta Grannies
- **Japanese:** Just One Cookbook (Nami), Jun's Kitchen, Sudachi Recipes
- **Korean:** Maangchi, Soy and Pepper
- **Chinese:** Chinese Cooking Demystified, Made With Lau
- **Mexican:** Rick Bayless, De Mi Rancho a Tu Cocina
- **Indian:** Chef Ranveer Brar, Hebbar's Kitchen
- **SE Asian:** Pailin's Kitchen / Hot Thai Kitchen, Marion Grasby, Noms by Nancy

**Baking & Pastry:** Claire Saffitz, Preppy Kitchen, ChainBaker, Bake with Jack, The Bread Code, Proof Bread

**Food Science & Theory:** Adam Ragusea, Ethan Chlebowski, Tasting History (Max Miller)

### Source diversity tracking

- The canonical source diversity report lives at `private/source-diversity-report.md`
- The extraction script at `scripts/extract_session_data.py` generates `scripts/session_data.json` for analysis
- Open diversification tasks are tracked in `TODO.md` under “Source Diversity — Reduce Serious Eats Monoculture”
- After any batch of recipe swaps, regenerate `session_data.json` and update the diversity report

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

