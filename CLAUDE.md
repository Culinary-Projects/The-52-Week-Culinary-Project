# CLAUDE.md — The 52-Week Culinary Project

This file governs how Claude Code works in this repository. Follow these rules without being asked.

---

## Project Overview

A 52-week home culinary school structured as a MkDocs site, built for a cook who already cooks 5 nights a week. The curriculum is self-correcting: the learner completes blocks, fills in feedback files, and those files drive content revisions.

**Public repo:** `docs/` — session files, service files, quick-refs, shopping lists, index pages
**Private submodule:** `private/` — feedback logs, pre-start checklists, photos (never commit secrets here)

---

## Non-Negotiable Rules

### 1. Always commit and push when done

After every set of content changes, commit and push without being asked. No exceptions.

- Stage only the files you changed (never `git add -A` blindly — the private submodule has its own repo)
- Write a clear, specific commit message — list what changed per file
- Push immediately after commit
- Always co-author: `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>`

### 2. When any session or service file changes, cascade to ALL related files

A session change is never isolated. Every time a session's recipe, ingredients, or meal structure changes, update:

| Changed | Must also update |
|---|---|
| Session recipe or ingredients | `shopping-list.md` for that block |
| Session dish name or skill | `quick-ref.md` for that block |
| Session dish name | `index.md` session list (if the title changes) |
| Service meal structure | `shopping-list.md` + `quick-ref.md` |
| Any block-level change | Check cross-block references (e.g., "use thighs from Block 1–2 breakdown in Block 3–4") |

Do all of these in the same commit. Never split a session change and its shopping list update across separate commits.

### 3. Link hygiene

- **Never invent URLs.** If you don't have high confidence a URL exists, do not include it.
- When adding a new link, note in the commit message whether it was verified or is a best-guess URL pattern.
- YouTube links must point to a **specific video**, not a channel homepage.
- Serious Eats URLs follow the pattern: `seriouseats.com/[recipe-slug]-recipe` — use this to sanity-check before adding.
- If a recipe swap requires a new URL you can't verify, either omit the link and describe the dish, or add a comment: `<!-- URL unverified — check before publishing -->`.

### 4. Feedback drives curriculum

The `private/feedback/` directory contains post-block feedback logs. When reviewing or revising curriculum:

1. Read the relevant feedback file first — `private/feedback/[block].md`
2. Treat specific complaints as curriculum bugs to fix, not preferences to note
3. Apply changes across all affected files (session, shopping list, quick-ref, index)
4. If feedback flags a recipe as a swap candidate, either make the swap (if a better recipe is clear) or add a `<!-- SWAP CANDIDATE: [reason] -->` comment in the session file

---

## Curriculum Design Principles

**Audience:** A home cook who already cooks 5 nights a week. Technically capable, has opinions, gets bored by drills that feel like school.

Implications:
- **Every drill must become dinner.** If a knife skill, dice exercise, or technique produces something the cook doesn't eat, it will be skipped or resented. The drill IS the meal prep.
- **Recipes should reward the skill being taught.** If a session teaches julienne, the meal should *require* julienned vegetables — not have them as an optional add-on.
- **Don't pad the plate.** A salad or side suggestion that doesn't cohere with the dish (e.g., garlic bread with a Provençal tian) is worse than no suggestion at all. Only recommend sides that actually belong.
- **Time matters.** Sessions should land under 90 minutes. Flag sessions that historically run long (see feedback logs). Project meals (Service sessions) can run 2 hours.

---

## File Structure

```
docs/
└── blocks/
    └── [block-folder]/
        └── [session-folder]/
            ├── index.md              ← block overview, Go Deeper, navigation
            ├── quick-ref.md          ← one-row-per-session table; always in sync
            ├── shopping-list.md      ← always in sync with sessions
            ├── session-N-[slug].md   ← skill + full meal + component table
            └── service-N-[slug].md  ← project meal (Service sessions)

private/
└── feedback/
    └── [block].md                    ← post-block learner feedback; primary source of truth for revisions
```

### Index files

Each block `index.md` contains:
- Navigation links to all sessions and services in order
- "Before You Start" reading list
- "Go Deeper" section (keep trimmed — Pépin video first, specific article links only, no redundancy)
- Food Safety Fundamentals section (raw proteins handled in that block)

### Quick-ref files

One row per session. Columns: Session | Dish | Skill | Link(s).
- Recipe links must match what's in the session file exactly
- Skill descriptions must match the session's **Skill:** line
- When a dish changes, this row changes in the same commit

### Shopping lists

Organized by: Proteins → Produce (Block 1 / Block 2) → Dairy → Pantry & Dry Goods → Bread → Equipment → Notes.

Rules:
- Every ingredient in every session must appear here
- Annotations explain which session uses the ingredient — keep these current when sessions change
- The Notes section at the bottom gets a brief entry for any session with unusual timing, sourcing, or technique requirements
- Cross-block carry-overs (e.g., "freeze thighs from Block 1 breakdown for Block 3 braising") must appear in both blocks' lists

---

## Commit Message Format

```
[Verb] [scope]: [what changed]

- File 1: specific change
- File 2: specific change
- Shopping list: what was added/removed/updated
- Quick-ref: what row changed

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Good verbs: `Revise`, `Fix`, `Add`, `Replace`, `Update`, `Remove`

---

## Working With the Private Submodule

- `private/` is a git submodule pointing to a separate private repo
- Never stage `private/` changes with the main repo changes — they commit separately
- When feedback files are updated, that's a private submodule commit, not a public one
- `git add private` stages the submodule pointer update — only do this if intentional

---

## What Never Changes Without Asking

- The block structure (26 blocks, 2 weeks each)
- The MkDocs site configuration (`mkdocs.yml`)
- The public/private repo split
- Session numbering within a block
