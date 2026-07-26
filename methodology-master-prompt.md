# THE EPIC-TO-COMIC MASTER PROMPT
## A generalized methodology for adapting any traditional epic into a serial graphic cycle
### Distilled from the Trojan Cycle project (v1.0). Fill the [BRACKETS], then execute the phases in order.

---

## HOW TO USE THIS DOCUMENT

Paste this entire document into a fresh session with a capable model, fill in Phase 0's brackets, and say "execute Phase 0." Each phase produces named artifact files; do not advance a phase until its artifacts exist and you have signed off. The output of the full pipeline is a project repository identical in shape to `trojan-cycle/`:

```
[epic-slug]/
  master-plan.md          (story bible: vision, frame, fidelity tiers, lexicon, issue architecture, ledger)
  characters.md           (locked visual descriptors, versioned; style blocks)
  refs/                   (cropped character reference images, born in-panel)
  issues/issue-NN/
    script.md             (panel-by-panel script: captions, dialogue, footnotes, gnomē, back matter)
    prompts.md            (one self-contained image prompt per panel)
    art/                  (generated panels, iNN-pgNN-pnN.png)
  tools/build_all.py      (programmatic lettering & page assembly → per-issue PDF)
  methodology-master-prompt.md   (this file)
```

The division of labor that makes this work: **the model writes everything textual and assembles everything mechanical; the image generator paints textless panels; lettering is always programmatic** (image models render text unreliably; programmatic balloons give consistent typography and let dialogue be revised without regenerating art).

---

## PHASE 0 — DECLARE THE EPIC

Fill in:

- **EPIC:** [name, e.g., Vālmīki Rāmāyaṇa / Mahābhārata / Śrīmad Bhāgavata / Cilappatikāram / Shahnameh / Kalevala / Beowulf-cycle]
- **NATIVE DIVISIONS:** [the text's own index units, largest to smallest — e.g., kāṇḍa → sarga → śloka; parvan → upaparvan → adhyāya; skandha → adhyāya; runo; fitt. THE TEXT'S OWN ARCHITECTURE IS THE ADAPTATION'S ARCHITECTURE — never impose a foreign act-structure on a text that carries its own.]
- **BASE TEXT / RECENSION:** [which edition is canon — e.g., BORI critical edition vs. southern vulgate for Mbh; Baroda critical edition vs. Kamba/Tulsī for Rāmāyaṇa. Pick ONE as Tier A; the rest become tiers below.]
- **TARGET CULTURE-PERIOD:** [the material-culture horizon for all earthly scenes — e.g., late Vedic Gangetic (painted grey ware, timber-and-daub cities, Sinauli-type carts) — the analog of the Trojan Cycle's LH IIIB commitment. One period, held absolutely.]
- **VISUAL TRADITION:** [the art grammar — ACK house style, Mughal miniature grammar, Ajanta-derived line, etc.]
- **AUDIENCE REGISTER:** [all-ages dignified (ACK default) / adult]
- **ESTIMATED SCALE:** [issues × pages; see Phase 2 for the sizing rule]

**Phase 0 output:** a one-page project declaration at the head of `master-plan.md`.

---

## PHASE 1 — SOURCE FIDELITY TIERS (the single most important ruling)

Define the tier ladder for THIS epic, by analogy but never by copy:

- **Tier A — the canonical text.** Plot, scene order, speeches adapted directly; nothing invented that contradicts it. Dialogue freshly rendered from the source language — never lifted from copyrighted translations.
- **Tier B — the attested penumbra.** For Greek epic this was the lost Cycle via Proclus; for the Mahābhārata it is the Harivaṃśa and the text's own appendix passages; for the Rāmāyaṇa, the Uttarakāṇḍa if your Tier A excludes it, plus purāṇic parallels. Plot skeleton fixed by attestation; scene detail reconstructed in-style.
- **Tier C — later fill, always flagged.** Regional retellings (Kamba, Tulsī, Kṛttibās), tradition-crystallizations, folk episodes (e.g., the Lakṣmaṇa-rekhā, which is NOT in Vālmīki — the Indian equivalent of the golden apple's inscription). Used only where A and B are silent; never overrides them; every use flagged in back matter.
- **Tier F — the frame.** The recitation device. **Check first whether the epic carries its own frame natively** — the itihāsa-purāṇas do (Sauti at Naimiṣa; Vaiśampāyana–Janamejaya; Śuka–Parīkṣit; Lava-Kuśa before Rāma; Nārada's proem to Vālmīki). Where native, the frame is Tier A and this tier records only your staging choices (which frame level to foreground; the Mbh has three nested ones — pick the innermost that gives you a royal listener, the Janamejaya level, exactly as the Trojan Cycle built its Neleid prince). Where absent, construct one from historically grounded materials and mark it F, rendered in a visually distinct register (the sepia rule).
- **Tier H — the documentary/archaeological frame.** Epigraphy, archaeology, historical geography. **Bounded by the standing ruling:** never narrative canon; four uses only — (1) material authenticity, unrestricted; (2) constructive grammar for scenes the text never wrote (court procedure, ritual sequence — dharmaśāstra and gṛhyasūtra serve here natively, as Hittite treaty diction served Wilusa); (3) at most ONE documentary-register prologue page in the entire cycle, in its own style block, which speaks once and never again; (4) back matter. Tier H may never date, corroborate, or annotate anything the Singer sings. (For Indian epics this discipline matters doubly: it keeps the adaptation out of historicity controversies by construction — the page never claims archaeology proves the text or vice versa.)

**Also rule now on:**
- **Embedded-tale policy (upākhyāna policy).** Traditional epics carry vast interpolated story-cycles (Nala, Sāvitrī, Śakuntalā; the Odyssey's apologoi are the Greek case). Options: (a) inline where the frame audience hears them, told by an in-story teller — the native mechanism; (b) spin off as side-issues in a separate numbered track; (c) defer with a narrator's promissory note. Decide the default and the exceptions.
- **The quotation-sanctity rule.** If parts of the source are liturgically sensitive to depict or quote (śruti passages, the Gītā), decide the treatment: the Trojan-Cycle gnomē mechanism (freshly rendered gnomic close per issue, ornamented panel) generalizes perfectly to śloka/phala-śruti closes — this is native ACK practice anyway.

**Phase 1 output:** the tier table + rulings section of `master-plan.md`.

---

## PHASE 2 — MAP THE NATIVE INDEX TO THE SERIAL ARCHITECTURE

The sizing rule discovered in the Trojan Cycle: **one issue = one complete dramatic movement of the source, sized so that its beats fit ~30 pages of ~3 panels each (~85–90 panels), with pages 1 (cover), 2–3 (frame + invocation), 30–31 (frame close), 32 (gnomē) fixed.** Work as follows:

1. Lay out the native divisions as PARTS (kāṇḍa → Part; parvan-cluster → Part).
2. Within each part, cut issues at the text's own seams — day-boundaries of battle, journey stages, court sessions. For very dense books use the Iliad rule (fixed n chapters per issue); for uneven books cut by episode.
3. Produce the ISSUE TABLE: number, title, tier declaration, one-paragraph scope, and the explicit list of episodes it must contain. **The audit in Phase 9 checks this table against the source index — every sarga/adhyāya must be accounted for: included, merged, or consciously omitted with a note.**
4. Worked sizing anchors: Vālmīki Rāmāyaṇa ≈ 24–28 issues (Bāla 2–3, Ayodhyā 4, Araṇya 3–4, Kiṣkindhā 2–3, Sundara 2–3 — Sundara is a gift: one hero, one arc, natively splash-structured — Yuddha 6–8, Uttara 2–3 if included, plus frame-opening and closing issues). Mahābhārata ≈ 40–48 issues minimum honest scale (ACK itself needed 42): Ādi 5–6, Sabhā 2–3 (the dice game gets a full issue; it is the Mbh's Issue-of-the-broken-oath), Vana 4–5 with upākhyāna policy doing heavy lifting, Virāṭa 2, Udyoga 3 (the embassy issue mirrors the Trojan Issue 6 embassy — same dharma-yuddha logic of war-as-last-resort), Bhīṣma→Sauptika 12–14 with the Gītā handled per the quotation rule, Strī/Śānti selectively 3–4, the ends 3–4.
5. **Bracket the whole cycle in ring form:** identify the epic's own opening and closing resonance (the two xenia crimes in the Greek cycle; for the Mbh, the snake-sacrifice frame that begins and the same sacrifice halted in mercy that ends) and let the first and final issues carry it.

**Phase 2 output:** the Volume Architecture section of `master-plan.md`.

---

## PHASE 3 — THE ETHICAL LEXICON & ANTI-MORALIZING POLICY

List the 8–15 untranslatable operating concepts of the epic's own moral system (for the Greek cycle: xenia, kleos, timē, moira, atē, miasma, aidōs...; for itihāsa: dharma, ṛṇa, śāpa, varā, satya-vrata, āpad-dharma, niyoga, prāyaścitta, kṣatra-dharma...). Rule that they appear **untranslated on the page**, italicized, footnoted at first use, glossaried per issue. Rule that the narrator speaks from INSIDE the epic's ethics — no apology, no modern translation of institutions (war-brides, varṇa, animal sacrifice, polyandry, ordeal), no sanitizing beyond the visual-restraint conventions of the chosen art grammar; the text's own pathos is the only editorial voice. Where the tradition itself debates an ethics point (the Mbh debates its own war constantly), the debate goes ON the page in the tradition's voice — that is fidelity, not commentary.

**Phase 3 output:** the lexicon + policy section of `master-plan.md`.

---

## PHASE 4 — THE CONSEQUENCE LEDGER

Traditional epics run on tracked causality: vow → fruit, curse → ripening, boon → bill, debt → collection (hubris→atē→nemesis; śāpa/vara → phala). Build the LEDGER as a first-class artifact inside `master-plan.md`: every planted cause gets a row — origin issue, nature (curse/oath/debt/boon/prophecy), and the booked payoff issue. Every issue's back matter lists the entries it opens and closes. **The Phase 9 audit fails any ledger row without a booked destination** (this catch is not theoretical: the Trojan audit found its best payoff — the wall breached at the mortal-built seam — unbooked). For the Mbh this ledger is enormous and IS the epic: Devavrata's vow, Amba's rebirth, Draupadī's laughter/vow, the dice, Karṇa's three curses, Aśvatthāman's gem. The ledger is also your continuity engine for planting payoffs early (the Trojan Cycle planted the olive-tree bed 24 issues before its payoff; plant Karṇa's kavaca-kuṇḍala with the same patience).

**Phase 4 output:** the ledger section of `master-plan.md`.

---

## PHASE 5 — THE CHARACTER & STYLE BIBLE

Create `characters.md`, versioned (v1, v2... with change notes; **descriptor strings are locked once used** — art consistency depends on verbatim reuse):

1. **Style blocks:** [STYLE-MAIN] (the full-color saga grammar, one sentence, reused verbatim in every prompt); [STYLE-FRAME] (the recitation frame's restricted palette); [STYLE-DIVINE] (deva-register: greater stature, radiance, the divine-architecture license — heaven exempt from the period rule, which visually separates loka from bhūloka); optional [STYLE-TABLET]-analog for the single Tier H page. Plus the GUARD CLAUSE — one sentence enforcing the target period against the generator's habits ("strictly [period] only: no [list the anachronisms the generator loves]") — baked into every earthly prompt.
2. **Locked descriptors:** one sentence per character — build, hair, face, signature costume, one signature object (the boar's-tusk-helmet principle: give each major hero one instantly readable prop — Gāṇḍīva, the gadā, the paraśu — and keep it in every appearance).
3. **Settings:** locked one-sentence descriptors per recurring location.
4. **The refs pipeline:** characters are BORN in a designated panel ("births refs/name.png"); their face is cropped from that panel into `refs/` and ATTACHED to every subsequent prompt with a MATCH LINE. Iconographically fixed figures (deities with dhyāna-śloka-level canonical forms) get their descriptor written FROM the iconographic canon, which does half the consistency work for free.

**Phase 5 output:** `characters.md` v1.

---

## PHASE 6 — THE PER-ISSUE SCRIPT FORMAT

For each issue, `script.md` in PLAIN REGISTER (short sentences, no unglossed jargon, confident in-tradition voice):

- Page/panel structure with fixed furniture: PAGE 1 cover (single image, calm zone reserved for programmatic title); PAGES 2–3 frame + invocation (the reciter resumes, the listener prompts, the invocation to the memory-goddess — Muse/Vāk/Sarasvatī — then the FRAME CUT into full color); interior pages ~3 panels; one or two FULL-PAGE SPLASHES at the issue's hinge moments; PAGES 30–31 frame close with the hook for the next issue; PAGE 32 the gnomē/śloka page — ornamented panel, freshly rendered gnomic verse, small attribution, END PLATE naming the next issue.
- Per panel: shot description referencing locked descriptors; CAPTIONS (narrator, epic voice); DIALOGUE tagged by speaker; FOOTNOTES for lexicon first-uses; the reciter's interjections to his listener at act-turns (the device that carries the epic's own didactic voice — "mark this, princes" — Vaiśampāyana's "śṛṇu rājan").
- BACK MATTER per issue: source notes with tier flags for every C-level choice and every version ruling; ledger entries opened/closed; glossary.
- The frame-listener is a real character with an arc: his questions voice the reader's objections, and the reciter's answers are where the epic's theology of fate-and-free-will lives (daiva vs. puruṣakāra — leave it as unresolved as the tradition leaves it).

**Phase 6 output:** `issues/issue-NN/script.md`.

---

## PHASE 7 — THE PANEL-PROMPT FORMAT

For each panel of the script, one **fully self-contained** prompt in `prompts.md` (paste-ready; no prompt may depend on another being read):

```
### iNN-pgNN-pnN.png — [aspect: wide 16:9 / standard 4:3 / tall 2:3 / full page 3:4 / close-up] — TITLE
ATTACH: refs/x.png, refs/y.png        (or "none")
MATCH LINE: 'map each: ...'            (tells the generator which figure is which ref)
PROMPT: [STYLE block verbatim] + [scene: settings descriptor + character descriptors verbatim + action + composition notes, including "leave calm space at top/bottom for caption plates" on splash pages] + [GUARD CLAUSE if earthly] + [divine clause if deva-register] + "Absolutely no text, no lettering, no speech balloons anywhere in the image."
THEN CROP: refs/new.png — (only on ref-birth panels)
```

Content-safety grammar carried from the Trojan Cycle: violence by aftermath and implication (the horror in faces and scattered garlands, never gore); the art tradition's own modesty conventions for all figures; children in peril rendered as crime-and-rescue with total restraint; sacred scenes with the gravity the tradition gives them.

**Phase 7 output:** `issues/issue-NN/prompts.md`.

---

## PHASE 8 — GENERATION, REVIEW, AND BUILD LOOP

1. Human generates art per prompts (any image model); multiple options allowed per contested panel (`-optionN` suffix).
2. Model reviews every panel against prompt + bible: style consistency, ref-match, count-checks (the five-babies class of error), guard-clause violations, option adjudication with stated reasons. Crops due are executed before dependent panels generate.
3. Model letters programmatically (`tools/build_all.py`): captions as page bands, dialogue as in-art balloons placed by face-zone geometry (balloons never cover faces; tails unambiguous; reading order by stagger), footnote strips, page numbers, gnomē plate, cover title.
4. Per-issue PDF; no combined master until a milestone.
5. Panel-level corrections iterate on the lettering layer without touching art wherever possible.

**Phase 8 output:** `issue-NN.pdf`.

---

## PHASE 9 — THE AUDIT PASSES (run before scripting each new issue, and at every milestone)

1. **Source-order audit:** the issue table vs. the source's own index — every unit accounted for; ordering never silently inverted (the audit that caught the Cypria's two-muster structure).
2. **Version-conflict audit:** every place two attested versions collide gets an explicit ruling row (chosen version, rejected version, tier, note).
3. **Ledger audit:** no planted cause without a booked payoff; no payoff without its plant.
4. **Lexicon audit:** every term footnoted at first use only.
5. **Anachronism audit:** earthly scenes vs. the period commitment.
6. **Descriptor drift audit:** characters.md strings vs. actual prompt usage, verbatim.
7. **Frame-integrity audit:** the reciter's knowledge never exceeds the tradition; the Tier H voice appears exactly once in the whole cycle.

---

## APPENDIX — WORKED STARTER: VĀLMĪKI RĀMĀYAṆA (sketch to be superseded by a real Phase 0–2 run)

Frame: natively double — Nārada's proem + Lava-Kuśa singing the poem before Rāma at the aśvamedha: the most devastating recitation frame in world literature (the audience of the song is its own protagonist, hearing his own story including the fate of the singers' mother). Foreground the Lava-Kuśa level as the Trojan Cycle foregrounded the Neleid court; it natively supplies the royal listener, the Iron-Age elegy (sung after the heroic events), and a closing frame with real dramatic stakes. Tier A: Baroda critical edition. Tier C: Kamba/Tulsī beauties flagged (Lakṣmaṇa-rekhā is the canonical example of a C-element the audience will demand — include, flag). Target period: a declared early-historic Gangetic horizon, held with the same absolutism as LH IIIB. Lexicon starters: dharma, satya, vana-vāsa, śaraṇāgati, maryādā, śāpa, tapas, rākṣasa (untranslated, never "demon"). Ledger starters: Daśaratha's śāpa (the blind ascetic's parents) → booked to his death-grief; Mantharā's poisoned counsel; Kaikeyī's two boons (planted in the Śambara war flashback long before spent); Vālin's death-debt; Sītā's agni-parīkṣā → Uttara's fruit if included. Ring: the poem opens with Nārada asked "who is the ideal man?" and closes with the poem itself being sung to that man — sing the first question in Issue 1 and let the final issue land its answer.

*End of master prompt. Version 1.0 — extracted from the Trojan Cycle at Issues 1–4.*
