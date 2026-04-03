# Curriculum TODO

Prioritized improvement list generated from full curriculum audit. Work through these over time — check boxes as completed. All items include the specific file(s) to edit.

**Priority key:**
- **P1** — Structural bug or CLAUDE.md violation; fix before learner reaches this block
- **P2** — High-value content improvement; meaningfully better experience
- **P3** — Polish and long-term consistency; nice-to-have

---

## P1 — Structural Bugs & Rule Violations

### Broken / Mismatched Links

- [ ] **Block 5–6 Before You Start:** Link labeled "The 5 French Mother Sauces, Explained" points to `seriouseats.com/bechamel-white-sauce-recipe` (a single sauce recipe, not an overview). Find and replace with a verified SE overview article or a reliable alternative that actually covers all 5 sauces.
  - File: `docs/blocks/01-foundational-skills/05-06-mother-sauces/index.md` line 15

- [ ] **Block 5–6 Go Deeper — YouTube channel links:** Pépin omelette link points to `@JPCuisine` channel homepage, not a specific video. Gordon Ramsay link points to `@gordonramsay` channel homepage. Replace both with verified specific video URLs or remove and substitute SE articles.
  - File: `docs/blocks/01-foundational-skills/05-06-mother-sauces/index.md` (Go Deeper section)

- [ ] **Block 19–20 Go Deeper — YouTube search links:** "How to shuck oysters" and "how to sear scallops" point to generic YouTube search results, not specific videos. Find and verify specific video URLs.
  - File: `docs/blocks/02-building-flavor/` (shellfish block index, Go Deeper section)

- [ ] **Block 25–26 Go Deeper — YouTube search link:** "Cassoulet technique" points to a YouTube search result, not a specific video. Find a verified cassoulet video (Kenji, Pépin, or Serious Eats).
  - File: French classics block index, Go Deeper section

### Numbering Errors

- [ ] **Block 13–14 index — internal block numbers wrong:** Index labels its two halves "Block 11 — Pasta Dough" and "Block 12 — Grains" (should be Block 13 and Block 14). Also ends with a section headed "Block 7 Capstone" (should be "Unit 1 Capstone" or similar).
  - File: `docs/blocks/01-foundational-skills/` pasta & grains block `index.md`

- [ ] **Block 17–18 quick-ref — header mislabeled:** File header says "Block 15–18" but contains only Block 17–18 content. Interior section headers labeled "Block 19" and "Block 20" when they mean sessions within Block 17–18. Also contains Block 19–20 shellfish content mixed in — move that content to the Block 19–20 quick-ref.
  - File: fish block `quick-ref.md`

### Misplaced Content

- [ ] **Sessions 58–61 and Service 15 — capstone content in wrong block:** These Unit 1 capstone sessions (menu planning, dry run, knife benchmark, 3-course dinner for guests) appear inside Block 13–14 (pasta & grains) and are also referenced in Block 23–24 (poultry). They belong at the end of Unit 1 (after Block 12). Either move to a dedicated `unit-1-capstone` folder, or clearly separate them within Block 13–14 under a heading that explains why they're here.
  - Files: pasta & grains block `index.md`; poultry block `quick-ref.md`

- [ ] **Block 7–8 — orphaned session fragments at end of index:** The index for Stocks & Eggs ends with stray fragments for Sessions 34–35 (Vichyssoise and Gazpacho cold soups). These belong in Block 9–10 (Seasoning & Flavor), not Block 7–8. Remove from Block 7–8 index and verify they exist properly in Block 9–10.
  - File: `docs/blocks/01-foundational-skills/07-08-stocks-and-eggs/index.md`

### Missing Content

- [ ] **Session 113 — no recipe link:** Pork Meatballs + Tomato Sugo + Pasta. Quick-ref shows "—" with no link. Either find a verified recipe link (SE pork meatball + sugo) or add an explicit note in the session file that this is technique-only and no recipe is provided.
  - Files: pork block `session-113` file; pork block `quick-ref.md`

---

## P2 — High-Value Content Improvements

### "Compare Notes" Video Coverage

Block 1–2 has a specific `🎥 Compare Notes:` video in every session — this is one of the most engaging features of the curriculum. Later blocks do this inconsistently. Audit each block below and add a verified specific video to any session that's missing one.

- [ ] **Block 3–4 (Heat & Cooking):** Audit all sessions (9–16) for missing Compare Notes videos. Priority: Session 9 (sauté), Session 10 (roasting), Session 11 (braise), Session 13 (searing steak).

- [ ] **Block 5–6 (Mother Sauces):** Audit sessions 17–24. Hollandaise (S21) and pan sauce (S24) especially benefit from a side-by-side video.

- [ ] **Block 7–8 (Stocks & Eggs):** Audit sessions 25–33. French omelette (S32) and poached eggs (S31) are natural candidates for Pépin's classic videos.

- [ ] **Block 9–10 (Seasoning & Flavor):** Audit sessions 34–41. Salt Fat Acid Heat episodes map well to several sessions here.

- [ ] **Block 11–12 (Vegetables):** Audit sessions 42–49. Strong candidates: blanching, charring, braising legumes.

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

*Last updated: 2026-04-03*
*Source: Full curriculum audit across all 5 block units (Blocks 1–52).*
