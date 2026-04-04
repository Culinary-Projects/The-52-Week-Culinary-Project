# Curriculum TODO

Prioritized improvement list generated from full curriculum audit. Work through these over time — check boxes as completed. All items include the specific file(s) to edit.

**Priority key:**
- **P1** — Structural bug or CLAUDE.md violation; fix before learner reaches this block
- **P2** — High-value content improvement; meaningfully better experience
- **P3** — Polish and long-term consistency; nice-to-have

---

## P1 — Structural Bugs & Rule Violations

### Broken / Mismatched Links

- [x] **Block 5–6 Before You Start:** ~~Link labeled "The 5 French Mother Sauces, Explained" points to `seriouseats.com/bechamel-white-sauce-recipe`.~~ Fixed: SE has no overview article; changed link text to honestly label the béchamel recipe destination. Inline text already explains all 5 sauces.
  - File: `docs/blocks/01-foundational-skills/05-06-mother-sauces/index.md` line 15

- [x] **Block 5–6 Go Deeper — YouTube channel links:** ~~Pépin/Ramsay channel homepages.~~ Fixed: replaced with verified SE articles (French omelette, pan sauce guide). Section renamed "Technique in Practice".
  - File: `docs/blocks/01-foundational-skills/05-06-mother-sauces/index.md` (Go Deeper section)

- [x] **Block 19–20 Go Deeper — YouTube search links:** ~~Generic YT search URLs.~~ Fixed: scallop sear replaced with verified SE article (Kenji’s Best Seared Scallops); oyster shucking marked `<!-- URL needed -->` for future video verification.
  - File: `docs/blocks/03-the-proteins/19-20-shellfish/index.md` (Go Deeper section)

- [x] **Block 25–26 Go Deeper — YouTube search link:** ~~Generic YT search URL.~~ Fixed: replaced with verified SE article (Kenji’s Traditional French Cassoulet). Section renamed "The Cassoulet Deep Dive".
  - File: `docs/blocks/04-worlds-kitchens/25-26-french/index.md` (Go Deeper section)

### Numbering Errors

- [x] **Block 13–14 index — internal block numbers wrong:** ~~Block 11→13, Block 12→14, Block 7 Capstone→Unit 2 Capstone.~~ Fixed.
  - File: `docs/blocks/02-building-flavor/13-14-pasta-and-grains/index.md`

- [x] **Block 17–18 quick-ref — header mislabeled:** ~~Block 15-18→17-18, Block 19/20→17/18.~~ Fixed. Orphaned Sessions 94-97 shellfish content removed (no session files exist; Block 19-20 has its own quick-ref).
  - File: `docs/blocks/03-the-proteins/17-18-fish/quick-ref.md`

### Misplaced Content

- [x] **Sessions 58–61 and Service 15 — capstone content placement:** ~~Capstone content in Block 13-14 confusingly headed "Block 7 Capstone".~~ Fixed: relabeled as "Unit 2 Capstone" with clear separation. Content stays in Block 13-14 (end of Unit 2) which is correct placement.
  - Files: `docs/blocks/02-building-flavor/13-14-pasta-and-grains/index.md`

- [x] **Block 7–8 — orphaned session fragments at end of index:** ~~Sessions 34-35 fragments at end of index.~~ Fixed: removed. These were stray stubs with no session files; Block 9-10 has its own Sessions 34-41.
  - File: `docs/blocks/01-foundational-skills/07-08-stocks-and-eggs/index.md`

### Missing Content

- [x] **Session 113 — no recipe link:** ~~Quick-ref showed "—" with no link.~~ Fixed: added verified SE tomato sugo recipe link to quick-ref. Session file already had the link.
  - Files: `docs/blocks/03-the-proteins/21-22-pork-and-charcuterie/quick-ref.md`

---

## P2 — High-Value Content Improvements

### "Compare Notes" Video Coverage

Block 1–2 has a specific `🎥 Compare Notes:` video in every session — this is one of the most engaging features of the curriculum. Later blocks do this inconsistently. Audit each block below and add a verified specific video to any session that's missing one.

- [x] **Block 3–4 (Heat & Cooking):** All sessions (9–16) now have Compare Notes videos. Resolved across CN commits 566deb3–7ca63dc.

- [x] **Block 5–6 (Mother Sauces):** All sessions (17–24) now have Compare Notes videos. Resolved across CN commits.

- [x] **Block 7–8 (Stocks & Eggs):** All sessions (25–33) now have Compare Notes videos. Resolved across CN commits.

- [x] **Block 9–10 (Seasoning & Flavor):** All sessions (34–41) now have Compare Notes videos. Resolved across CN commits.

- [x] **Block 11–12 (Vegetables):** All sessions (42–49) now have Compare Notes videos. Resolved across CN commits.

### "Go Deeper" — Add Pro Video to Each Block

Block 1–2 leads Go Deeper with a Pépin KQED video. These blocks have weak or missing video references:

- [ ] **Block 3–4 Go Deeper:** Add one "Watching a Pro Do It" video — Kenji or Sohla doing a sear, braise, or roast at real speed. Verify specific URL before adding.

- [ ] **Block 7–8 Go Deeper:** Add a Pépin egg video — his French omelette demo is definitive and freely available on YouTube. Verify specific URL.

- [ ] **Block 11–12 Go Deeper:** Add a vegetable-focused pro video. Samin Nosrat's vegetable episode or a Sohla El-Waylly technique video would fit the block's voice well. Verify specific URL.

### Source Diversity — Reduce Serious Eats Monoculture

SE is the right anchor but 70–85% concentration creates risk (URL rot) and limits learner exposure to other voices. Add one non-SE source per affected block:

- [ ] **Block 5–6 (Mother Sauces):** Add a Jacques Pépin primary source reference — his *New Complete Techniques* has the definitive mother sauce recipes and technique photos. Link to a specific recipe or Amazon page.

- [ ] **Block 7–8 (Stocks & Eggs):** Add an NYT Cooking or Julia Child reference for egg technique (poached eggs, omelettes). Julia Child's egg guidance is culturally significant here.

- [ ] **Block 25–26 (French Classics):** Reduce SE dominance; add Pépin recipe references, possibly a Larousse Gastronomique mention. French block relying entirely on SE when Pépin exists is a missed opportunity.

- [ ] **Block 33–34 (Japanese):** Add Just One Cookbook (Nami — `justonecookbook.com`) as a trusted Japanese cooking source alongside SE. Widely regarded as the most reliable English-language Japanese cooking resource.

- [ ] **Block 37–38 (Mexican):** Add a Rick Bayless or NYT Cooking Mexican reference alongside SE. Cultural authenticity matters more in world cuisines blocks.

- [ ] **Block 39–40 (Indian):** Add Madhur Jaffrey reference or a dedicated Indian cooking resource. SE has good Indian content but regional specificity requires specialist sources.

### Before You Start — Quality Audit

- [ ] **Block 3–4 Before You Start:** Review and ensure the reading sets up the Maillard reaction concept fully before learners hit their first sear. Currently 1 article — consider whether a second resource on heat transfer (conduction vs. convection vs. radiation) would add value without bloat.

- [ ] **Block 7–8 Before You Start:** Ensure the stock-vs-broth article is paired with a note about retrieving the carcass from Block 1–2's freezer. This cross-block connection is pedagogically important. Verify it's explicit.

- [ ] **All world cuisines blocks (29–44):** Each should have a Before You Start section that includes at least one cultural context resource alongside the technique prep — not just "here's the pantry to buy" but "here's why this cuisine works the way it does." Audit each block for this.

---

## P3 — Polish & Long-Term Consistency

### Shopping List Annotation Depth

Blocks 1–2 and 9–10 have the best shopping list annotations (every ingredient tagged with session numbers). Later blocks are complete but less specific. Low-priority pass:

- [ ] **Block 5–6 shopping list:** Add session-level annotations to any ingredient missing them.
- [ ] **Block 7–8 shopping list:** Same.
- [ ] **Block 13–14 shopping list:** Same, especially the pasta-making staples (00 flour, semolina, ricotta).
- [ ] **Block 15–16 shopping list:** Beef cuts can be confusing — add butcher guidance notes where missing.

### Experimental Blocks — Post-Cook Validation

These blocks are flagged experimental and have not been cooked through. No changes needed now — after cooking each, use the feedback log to revise timing, ingredient quantities, and sourcing notes.

- [ ] **Block 7–8 (Stocks & Eggs):** Cook through and validate. Flag: Service 7 is an all-day beef stock project — timing notes may need adjustment.
- [ ] **Block 19–20 (Shellfish):** Cook through and validate. Flag: live shellfish sourcing and freshness windows are the main risk.
- [ ] **Block 41–42 (Fermentation):** Cook through and validate. Flag: Service 53 won't be ready until ferments mature (5+ days into block) — the session order may need resequencing.

### Meal Completeness — Final Pass

Nearly all sessions have a complete meal (protein + veg + starch). A final pass to confirm no session leaves the learner without a full plate:

- [ ] **Block 7–8:** Egg sessions (S30–S33) are intentionally lighter — confirm each has at least one substantial accompaniment suggested, even if simple.
- [ ] **Block 11–12:** Plant-forward sessions should have a protein option noted (burrata, egg, legumes) so the cook isn't left with just vegetables.
- [ ] **Block 41–42:** Fermentation sessions don't produce a full meal by default — confirm each service session has a complete meal plan attached.

### Go Deeper — Trim Redundancy Check

As blocks were written over time, some Go Deeper sections may have accumulated links that overlap with what's already in sessions. A final audit:

- [ ] **Block 9–10 Go Deeper:** Check that the acid and salt articles don't duplicate what's already in the Before You Start section.
- [ ] **Block 15–16 Go Deeper:** Check that the beef science section doesn't repeat technique notes already in sessions 74–77.

---

## Completed

*(Move items here as done, with the date.)*

---

*Last updated: 2026-04-04*
*Source: Full curriculum audit across all 5 block units (Blocks 1–52).*
*Recipe links: all gaps resolved (commit 2042946). Compare Notes: all gaps resolved (commits 566deb3–7ca63dc).*
