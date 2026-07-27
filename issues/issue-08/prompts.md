# ISSUE 8 — PANEL PROMPTS (pages 1–32) · self-contained format
Iliad 4–6, Tier A. Same rules as Issues 1–7. Guard clause on earthly scenes; divine clause on god scenes; twilight palette on frame panels. Ref-births marked REF-BIRTH (crops are verification-side pipeline steps, committed to refs/ before dependent panels generate). Panels are TEXTLESS. Restraint clauses load-bearing on pgs 8, 13, 19, 21; ichor is golden light, never red.
Reusable refs: singer, neleid-prince, muse, agamemnon, menelaus, odysseus, nestor, diomedes, ajax, idomeneus, achilles(idle), athena, aphrodite, apollo, zeus, hera, iris, hector, andromache, helen, paris, hecuba, helenus, glaucus, sarpedon, aeneas.

> **TWO-LLM WORKFLOW (standing instructions for the image-generation session):**
> 1. You have READ access to this repository. For each panel below, fetch every file on its ATTACH line from the repo's `refs/` folder (same branch as this prompts file) and attach those images to the generation request together with the PROMPT text, used verbatim.
> 2. Generate at the stated aspect ratio. Output must be completely TEXTLESS.
> 3. You cannot commit. Hand the finished image to the human operator under its exact panel filename (iNN-pgNN-pnN.png); the operator relays it to the verification side (Claude), which reviews it against prompt and refs and commits it to `issues/issue-NN/art/`.
> 4. Panels marked REF-BIRTH create a new reference face: after that panel passes verification, the verification side crops and commits the new ref to `refs/`. Do NOT generate any later panel that ATTACHes that ref until the ref file exists in the repo.


### i08-pg01-pn1.png — full page 3:4 — COVER — DIOMEDES BLAZING
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Match the attached reference image exactly: it is fire streaming from helmet and shield; gods giving ground behind (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cover composition: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar at full charge across the windy plain, unquenchable divine FIRE streaming back from his helmet-crest and shield-rim, spear leveled — and vast, dim and half-seen in the storm-light above and behind him, towering god-shapes giving ground; leave the upper quarter calm for title lettering. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg02-pn1.png — wide 16:9 — FRAME — BRACED FOR A BREAKING
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot of an early Iron Age Ionian megaron hall at evening: timber columns, central hearth fire, hanging oil lamps, noble audience seated on benches, dark doorway open to a starry Aegean night: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre seated with the phorminx, the packed hall grim and ready; a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face on the high seat, jaw set. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg02-pn2.png — standard 4:3 — FRAME — HOW DOES A SWORN THING BREAK
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the question about the oath (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face asking with genuine bewilderment, one hand open as over an invisible altar. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg02-pn3.png — standard 4:3 — FRAME — THREE TERRORS
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is counting the night's three terrors on his fingers (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre counting slowly on three raised fingers, his blind face gravest at the third. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg03-pn1.png — standard 4:3 — THE INVOCATION
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/muse.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'face lifted (refs/singer.png) - reproduce that face, hair and apparent age exactly; the second attached image is the Muse attending.' (refs/muse.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre with sightless face lifted, fingers on the strings; a Muse: luminous woman of unearthly beauty, dark hair crowned with laurel, flowing pale gold robe, softly radiant against darkness attending luminous in the hearth-smoke. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg03-pn2.png — standard 4:3 — THE COUNCIL ABOVE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/hera.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the needling king of gods; the rigid queen; the plain tiny below.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Divine council shot in Olympus above the clouds: an open pillared hall of pale stone on a mountain summit floating over a sea of clouds, golden light, distant peaks: gods at golden cups around the cloud-floor, through which the plain of Troy shows tiny and bright far below; Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle speaking sidelong with deliberate mischief; Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face rigid with fury opposite. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg03-pn3.png — standard 4:3 — THREE CITIES PAWNED
ATTACH (fetch from repo refs/ and attach to the generation): refs/hera.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bargain that damns her own three cities (refs/hera.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cold close shot: Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face making her terrible offer, one hand extended palm-down as over unseen cities, her proud face absolute; peacock-eyed robes stirring. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg04-pn1.png — wide 16:9 — THE FALLING STAR
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Portent shot: a blazing STAR falling from heaven onto the space between two vast seated armies — a burning track shedding sparks, striking the empty dueling ground — both hosts surging to their feet in awe down the whole width of the panel. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg04-pn2.png — standard 4:3 — TWO READINGS
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Murmur shot along both front ranks at once, split composition: Trojan spearmen and Achaean spearmen mirrored, leaning to each other, faces divided man by man between hope and dread; the fading star-track reflected in helmets on both sides. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg04-pn3.png — standard 4:3 — THE HUNTER IN THE RANKS
ATTACH (fetch from repo refs/ and attach to the generation): refs/athena.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is in the likeness of a spearman, hunting one man through the press (refs/athena.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Sinister quiet shot: Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face folded into the likeness of an ordinary Trojan SPEARMAN — her radiance leaking faintly at the outline's edges — moving through the dense Trojan ranks, searching face after face for one particular man. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg05-pn1.png — standard 4:3 — THE TEMPTATION (births PANDARUS: crop refs/pandarus.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Whisper shot in the Trojan press: Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn among his shield-bearers — and leaning close at his ear a Trojan spearman whose edges leak faint divine radiance, one hand sketching glory in the air; the archer's head beginning to turn. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/pandarus.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i08-pg05-pn2.png — close-up 4:3 — THE POISON TAKES
ATTACH (fetch from repo refs/ and attach to the generation): refs/pandarus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is vanity, glory-hunger, the arithmetic of gifts (refs/pandarus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot: the keen face of Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn as the temptation lands — vanity kindling, the arithmetic of gifts and glory moving visibly behind the eyes; persuasion completing itself. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg05-pn3.png — standard 4:3 — THE BOW'S BIOGRAPHY
ATTACH (fetch from repo refs/ and attach to the generation): refs/pandarus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bow uncased; its history inset (refs/pandarus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Craft shot: Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn drawing the great recurved bow from its case with a craftsman's reverence — and inset along the panel's upper band, its history: a wild IBEX on a crag, the hunter's ambush shot, the sixteen-palm horns worked and joined and gold-tipped on a horn-wright's bench. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg06-pn1.png — standard 4:3 — THE CURTAIN OF SHIELDS
ATTACH (fetch from repo refs/ and attach to the generation): refs/pandarus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is companions closing shields in a wall around the crouched archer (refs/pandarus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Furtive shot: the companions of Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn closing their tall shields into a hiding wall around him as he crouches; between the shield-rims, glimpses of the unsuspecting Achaean lines beyond; the guilt of the geometry itself. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg06-pn2.png — standard 4:3 — THE VOW AND THE DRAW
ATTACH (fetch from repo refs/ and attach to the generation): refs/pandarus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is string to breast, iron to bow, the whispered vow (refs/pandarus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Rite-of-crime shot: Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn at full draw within the shield-ring — notch and string hauled to his breast, iron head to the bow, the great horn rounded to a full circle — his lips moving in the whispered vow; a shaft of light on the arrowhead. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg06-pn3.png — standard 4:3 — THE LOOSE
ATTACH (fetch from repo refs/ and attach to the generation): refs/pandarus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the release as sound made visible (refs/pandarus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Release shot: the instant after loose — the string still blurred and CRYING, the great horn bow leaping straight in the hands of Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn, the arrow already gone from the frame's edge; concentric shock-lines of the bow's deep note filling the shield-ring. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg07-pn1.png — wide 16:9 — THE FLIGHT
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Long dread shot: a single ARROW crossing the entire wide panel over the heads of two seated armies and the empty marked dueling-ground — a thin hungry line drawn across ten years of truce — every figure below still unaware; the sky holding its breath. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg07-pn2.png — standard 4:3 — AS A MOTHER BRUSHES A FLY
ATTACH (fetch from repo refs/ and attach to the generation): refs/athena.png, refs/menelaus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the goddess's flick (refs/athena.png) - reproduce that face, hair and apparent age exactly; the second attached image is the sleeping-child simile inset (refs/menelaus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Supernatural tenderness shot: Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face flashed to the side of unaware a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak, her hand FLICKING the incoming arrow's path aside with two fingers — and inset softly in one corner, the simile made image: a mother's hand brushing a fly from her sleeping child. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg07-pn3.png — close-up 4:3 — THE STRIKE
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is through belt and corslet-fold; the smallness and the worldsize (refs/menelaus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tight restrained impact shot: the arrowhead punching through the wrought gold BELT-BUCKLES of a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak where corslet doubles over plate — the shaft stopped mostly, the head just home — his body's first startled arch; nothing yet but the wound's terrible smallness. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg08-pn1.png — full page 3:4 — SPLASH — THE TRUCE DIES
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/agamemnon.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

map each: the struck man standing; the brother's horror; both armies rising like a sea.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page tableau of the instant after: at center a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak standing struck, the shaft jutting from his gold belt, DARK BLOOD running down his white thighs — with an inset cameo rendering the song's simile: a craftswoman's hands staining white IVORY with scarlet for a king's horse cheek-piece — beside him a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face gripping his brother's arm, face in horror, the scepter fallen at his feet; and around and beyond them BOTH ARMIES RISING off the ground like one breaking wave, hands reaching for stacked arms down the whole depth of the image; high above the field, small and cold, a departing track of starlight. Restraint: blood minimal and symbolic, a dark ribbon only. Leave calm space top and bottom for ornate caption plates. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg09-pn1.png — standard 4:3 — THE OATH WILL BE PAID
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png, refs/menelaus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the king holding his wounded brother, the speech torn out of him.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Grief-and-iron shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face kneeling, holding the standing wounded a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak by the shoulders, his face a storm of guilt and certainty mid-speech; around them captains closing in a worried ring; the Trojan lines dimly massing beyond. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg09-pn2.png — standard 4:3 — A GRAZE WITH A GREAT NOISE
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/agamemnon.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

'the wounded man comforting the whole king.'

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Steadying two-shot: a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak, grey with pain but wry, gripping his brother's forearm and speaking calm; a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face's panic visibly banking down under the wounded man's steadiness. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg09-pn3.png — standard 4:3 — MACHAON (births MACHAON: crop refs/machaon.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Healer shot: Machaon son of Asclepius, healer-warrior, trim grey-flecked beard, calm practical face, a leather satchel of salves and probes at his hip kneeling at the wound with his satchel open — drawing the barbed head back out through belt and plate with exact two-handed care, salves laid ready on a cloth; a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak enduring with set jaw; spearmen holding a shield-shade over both. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/machaon.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

---

### i08-pg10-pn1.png — wide 16:9 — THE EPIPOLESIS
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png, refs/idomeneus.png, refs/ajax.png, refs/nestor.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each: the king on foot down the re-arming front; the praised captains.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Review montage shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face walking the re-arming Achaean front on foot — passing Idomeneus king of Crete, grave veteran war-king, grizzled dark beard, zoned bronze armor, a double-axe standard grave at his Cretans' head, the gigantic Ajax son of Telamon, gigantic broad warrior, heavy jaw and calm deep-set eyes, massive tower shield of sevenfold oxhide with spearmen dense as a storm-cloud behind his tower shield, and old Nestor king of Pylos, very old but hale counselor-king, long white beard, clear bright undimmed eyes, fine wool mantle, a gold-studded staff marshaling chariots before footmen with his staff; the king's raised hand in praise at each. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg10-pn2.png — standard 4:3 — THE STING MISDELIVERED
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png, refs/odysseus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the unjust lash (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly; the second attached image is the dark look answering (refs/odysseus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Friction shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face mid-rebuke with a contemptuous flung hand at a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy wool cloak over a simple kilt, whose ranks stand in good order behind him — and the Ithacan's answering DARK LOOK, level and dangerous, one step forward taken; the king's face already beginning its retreat. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg10-pn3.png — standard 4:3 — THE STING THAT LANDS ON IRON
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png, refs/diomedes.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the taunt; the young king's respectful silence; his hot companion silenced by a level look.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Character-defining shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face taunting Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar, who stands in complete respectful SILENCE, eyes forward, taking it — while beside him a keen scarred young CHARIOTEER (Sthenelus) bristles hotly mid-retort — and Diomedes's hand and level side-glance silencing his own defender without a word. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg11-pn1.png — wide 16:9 — LIKE TWO WINTER TORRENTS
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Epic clash shot: the two armies MEETING at last — rendered as the simile demands: like two flooding winter rivers hurling their waters together where mountain ravines join — shield-lines colliding in a single white burst of spears and crests down the panel's center seam; restraint: impact and mass, no gore. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg11-pn2.png — standard 4:3 — FIRST BLOOD OF THE BROKEN OATH
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Grim ledger shot: a quick young Achaean spearman (Antilochus) striking down the first Trojan champion of the day — the fallen man's crest in the dust, the young killer's momentum carrying past — and behind them, pair by pair down the line, man answering man; dignity and speed, no gore. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg11-pn3.png — standard 4:3 — THE GODS IN THE HAZE (births ARES: crop refs/ares.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/athena.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Half-seen divine shot through battle-haze: Ares god of war, huge brazen god of terrible beauty, dark bronze armor, blood-red cloak and horsehair crest, wolfish hungry perfect face raging huge and brazen up and down the Trojan side; opposite, Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face steadying the Achaean line; and between them, sketched in the smoke, the dim striding shapes of Terror and Rout and insatiable Strife. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/ares.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

---

### i08-pg12-pn1.png — standard 4:3 — THE SECOND ARROW
ATTACH (fetch from repo refs/ and attach to the generation): refs/pandarus.png, refs/diomedes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the exultant archer (refs/pandarus.png) - reproduce that face, hair and apparent age exactly; the second attached image is the struck champion storming on (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wounding shot: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar at the front, an ARROW standing through his right shoulder-plate, blood on the corslet — restrained, a dark line only — and far behind cover, Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn risen with bow high in exultant boast to the Trojan ranks. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg12-pn2.png — standard 4:3 — THE PRAYER OF THE WOUNDED MAN
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the arrow drawn; the prayer war-hot, the wound ignored (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Iron shot: behind a shield-wall, the scarred charioteer drawing the arrow clean through and out of the shoulder of Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar — who does not sit, does not retreat: standing into the pain, face lifted, PRAYING war-hot with blood on his corslet. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg12-pn3.png — standard 4:3 — THE MIST LIFTED
ATTACH (fetch from repo refs/ and attach to the generation): refs/athena.png, refs/diomedes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the goddess beside him unseen (refs/athena.png) - reproduce that face, hair and apparent age exactly; the second attached image is the gift and the one commandment (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. License shot: Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face manifest at the shoulder of Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar, unseen by all others, one hand passing across his eyes — a veil of MIST visibly lifting from them, the world going terribly clear — her other hand raised in the single commandment; his face filling with his father's fire. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg13-pn1.png — wide 16:9 — THE TORRENT
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference image exactly: it is the rampage like a river bursting the dykes (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Rampage shot: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar falling on the Trojan line LIKE A RIVER IN SUDDEN FLOOD — the ranks scattering before him as built banks and vineyard walls go down before white water, rendered with the simile ghosted into the composition; champions reeling aside; restraint absolute, force not gore. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg13-pn2.png — standard 4:3 — THE CURSED BOW
ATTACH (fetch from repo refs/ and attach to the generation): refs/aeneas.png, refs/pandarus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the recruitment (refs/aeneas.png) - reproduce that face, hair and apparent age exactly; the second attached image is the archer's bitter reply (refs/pandarus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Recruitment shot: Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face leaning urgently from his chariot to Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn, pointing through the reeling line toward the distant terror; the archer answering with a bitter twisted face, one fist shaking his own great bow as if to snap it; the chariot team stamping. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg13-pn3.png — standard 4:3 — THE ACCOUNT CLOSES
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/aeneas.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'the answering spear ending the boast (refs/diomedes.png) - reproduce that face, hair and apparent age exactly; the second attached image is the truce-breaker down.' (refs/aeneas.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Closure shot, restrained: the chariot of Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face swerving — and Pandarus of Lycia-under-Ida, master archer, wiry keen-eyed warrior, short black beard, a great recurved bow of polished ibex horn falling from it, the great ibex-horn bow spinning from his hands, the boast dying on his face; Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar's cast spear completing its arc; dust rising to receive the archer of the broken oath; no gore, the fall and the bow the whole story. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg14-pn1.png — standard 4:3 — THE LION OVER THE BODY
ATTACH (fetch from repo refs/ and attach to the generation): refs/aeneas.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is bestriding the fallen ally, spear and shield (refs/aeneas.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Valor shot: Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face leapt down and BESTRIDING the fallen archer's body — shield up, long spear leveled, teeth set — like a lion over its kill against the ring of enemies; loyalty made stance. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg14-pn2.png — standard 4:3 — THE STONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/aeneas.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the boundary-stone wielded alone (refs/diomedes.png) - reproduce that face, hair and apparent age exactly; the second attached image is the hero down on one knee (refs/aeneas.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Titanic shot: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar heaving up a huge BOUNDARY-STONE in one hand — a weight two men of a later age could not lift — mid-hurl; and Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face going down on one knee under its crushing arc, one fist driven into the earth, darkness starting across his eyes; restraint: impact and collapse, no wound shown. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg14-pn3.png — standard 4:3 — THE MOTHER'S ROBE
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png, refs/aeneas.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the white arms around the son (refs/aphrodite.png) - reproduce that face, hair and apparent age exactly; the second attached image is the fold of robe against the spears (refs/aeneas.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Rescue shot: Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face descended into the battle-light, pouring her white arms around the fallen Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face, wrapping him in a shining FOLD of her robe held against the flying bronze — the goddess of desire carrying her son up out of the press, doves scattering. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg15-pn1.png — standard 4:3 — THE PURSUIT
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/aphrodite.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the hunter through the press (refs/diomedes.png) - reproduce that face, hair and apparent age exactly; the second attached image is the soft immortal in the iron field (refs/aphrodite.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Hunt shot: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar shouldering through the thick of the fighting after the retreating radiance of Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face with her burden — his lifted-mist eyes fixed on her, KNOWING her — the license burning in his face; the crowd parting off both of them. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg15-pn2.png — standard 4:3 — ICHOR
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/aphrodite.png, refs/apollo.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the graze at the wrist (refs/diomedes.png) - reproduce that face, hair and apparent age exactly; the second attached image is the golden immortal blood (refs/aphrodite.png) - reproduce that face, hair and apparent age exactly; the third attached image is the dark-cloud catch below (refs/apollo.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The impossible wound: the spear-point of Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar grazing the base of the palm of Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face through the Grace-woven robe — and welling from the immortal skin not blood but ICHOR, golden-pale LIGHT — her head thrown back in the shriek, her arms failing — and below, Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face falling — caught mid-fall in a DARK BLUE CLOUD forming into the arms of Apollo the far-shooter, radiant young god of terrible beauty, long unshorn golden hair, silver bow, dark-silver quiver, cold perfect face. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg15-pn3.png — standard 4:3 — THE TAUNT AFTER
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/aphrodite.png, refs/iris.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the goddess fleeing supported; the great voice hurled after.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Exit shot: Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face fleeing the field cradling her wounded wrist, Iris the rainbow messenger, slight swift goddess, wind-blown pale robes with a rainbow shimmer, golden wings at her sandals, bright eager face supporting and leading her out of the throng — and behind them, planted and roaring his taunt across the battle, Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar, spear high; the field itself seeming to flinch at a mortal's voice chasing a goddess. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg16-pn1.png — standard 4:3 — THE BORROWED CHARIOT
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png, refs/ares.png, refs/iris.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the plea at the battle's edge; the gold-frontleted team.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Battle's-edge shot: Ares god of war, huge brazen god of terrible beauty, dark bronze armor, blood-red cloak and horsehair crest, wolfish hungry perfect face seated huge in mist at the fighting's left, spear leaning on cloud — and Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face before him, wounded wrist cradled, begging; behind her Iris the rainbow messenger, slight swift goddess, wind-blown pale robes with a rainbow shimmer, golden wings at her sandals, bright eager face already gathering the reins of the god's gold-frontleted horses. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg16-pn2.png — standard 4:3 — DIONE'S LAP
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the mother's comfort; the wrist healed under the stroking hand (refs/aphrodite.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Comfort shot on Olympus: Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face gathered like a hurt child into the lap of a stately gentle GODDESS-MOTHER (Dione: silver-veiled, calm ancient beauty, inline) — the old goddess stroking the wounded wrist, which heals golden under her hand; the daughter's tears bright and already half-forgotten. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg16-pn3.png — standard 4:3 — THE SMILE OF ZEUS
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/aphrodite.png, refs/hera.png, refs/athena.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the father drawing her close; the needling pair across the hall.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Gentle-rebuke shot: Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle SMILING, drawing golden Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face close with one great arm, his sentence visibly setting her right; and across the golden hall Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face and Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face exchanging one silken satisfied look. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg17-pn1.png — standard 4:3 — THE PHANTOM
ATTACH (fetch from repo refs/ and attach to the generation): refs/apollo.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the eidolon laid in the battle's midst; the true man healed on the height (refs/apollo.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cold split shot: on the field, Apollo the far-shooter, radiant young god of terrible beauty, long unshorn golden hair, silver bow, dark-silver quiver, cold perfect face shaping a PHANTOM — an exact armored image of Aeneas laid in the battle's midst, around which Trojans and Achaeans hammer each other's shields — and above in a corner inset, the TRUE man lying in a shining hilltop shrine, two radiant goddesses (Leto and Artemis) healing him. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg17-pn2.png — standard 4:3 — THRICE AGAINST THE GOD
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/apollo.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the three assaults against the sheltering shield.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Trespass shot: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar charging Apollo the far-shooter, radiant young god of terrible beauty, long unshorn golden hair, silver bow, dark-silver quiver, cold perfect face HIMSELF — the mortal's spear against the god's bright warding shield — rendered as a triple-exposure of three assaults in one frame, each closer, each turned; the god's cold perfect face unmoved above the third. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg17-pn3.png — standard 4:3 — NOT OF THE SAME ORDER
ATTACH (fetch from repo refs/ and attach to the generation): refs/apollo.png, refs/diomedes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the fourth charge stopped by the voice (refs/apollo.png) - reproduce that face, hair and apparent age exactly; the second attached image is the giving back (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The boundary-stone of the heroic world: Apollo the far-shooter, radiant young god of terrible beauty, long unshorn golden hair, silver bow, dark-silver quiver, cold perfect face at full terrible aspect — no rage, worse: cold totality — one hand raised, the VOICE rendered as a pressure flattening the air; and Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar, mid-fourth-charge, giving ground — back, back — his fury bending at last before the law. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg18-pn1.png — standard 4:3 — SARPEDON'S REBUKE
ATTACH (fetch from repo refs/ and attach to the generation): refs/sarpedon.png, refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the fair flaying (refs/sarpedon.png) - reproduce that face, hair and apparent age exactly; the second attached image is the prince who answers with deeds (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Rebuke shot: Sarpedon king of Lycia, son of Zeus, tall grave dark-bearded warrior-king of great dignity, silver-studded armor with a lion device confronting Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak face to face amid the reeling line — the Lycian's hand flung back toward his own far country, every word landing fair and hard; and Hector answering NOTHING — already turning, spear rising, into the ranks to answer with the rally itself. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg18-pn2.png — standard 4:3 — AENEAS RESTORED; ARES IN FRONT
ATTACH (fetch from repo refs/ and attach to the generation): refs/aeneas.png, refs/hector.png, refs/ares.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the wonder of the return; the god and the prince advancing together.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Turn-of-battle shot: Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face walking WHOLE out of nowhere into his people's astonishment, comrades gripping his arms in disbelief — and before the stiffening Trojan front, advancing together, Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak and, huge and half-veiled in battle-dark beside him, Ares god of war, huge brazen god of terrible beauty, dark bronze armor, blood-red cloak and horsehair crest, wolfish hungry perfect face. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg18-pn3.png — standard 4:3 — THE SHUDDER OF THE WISE
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the one man who can see, choosing retreat in good order (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wisdom shot: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar — the day's god-wounder — seeing WHO walks at Hector's shoulder and SHUDDERING; his arm sweeping the Greeks back with him, faces to the enemy, backs never; deliberate ground given by the one man on the field with eyes. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg19-pn1.png — full page 3:4 — SPLASH — THE WOUNDING OF ARES
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/athena.png, refs/ares.png
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Match the attached reference images exactly: the first attached image is the goddess unseeable in the car driving the spear deeper (refs/diomedes.png) - reproduce that face, hair and apparent age exactly; the second attached image is the god's bellow (refs/athena.png) - reproduce that face, hair and apparent age exactly; the third attached image is both armies clapping hands over ears (refs/ares.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page impossible summit: the chariot of Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar driven straight onto the war-god — Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face herself in the car behind him, rendered VOID-DARK and unseeable beneath the cap of Hades, her two hands LEANING the mortal's spear deeper home into the flank of Ares god of war, huge brazen god of terrible beauty, dark bronze armor, blood-red cloak and horsehair crest, wolfish hungry perfect face below the war-belt — the god's head thrown back in THE BELLOW, rendered as vast concentric shock-rings flattening the battle-haze across the whole image — and below, both armies to the horizon dropping shields to clap hands over their ears, a visible tremble running the field; the wound smoking golden; the god already beginning to rise off the earth. Restraint: golden ichor-light, no gore. Leave calm space top and bottom for ornate caption plates. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg20-pn1.png — standard 4:3 — THE STORMCLOUD ASCENDS
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Ascension shot: a vast BLACK STORMCLOUD in the shape of a rising armored god going up out of the battle-haze into a hot troubled sky — dark, huge, trailing — while below the entire field visibly exhales; tiny spears lowering. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg20-pn2.png — standard 4:3 — MOST HATEFUL, AND MOST MINE
ATTACH (fetch from repo refs/ and attach to the generation): refs/ares.png, refs/zeus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the whining exhibit of the wound (refs/ares.png) - reproduce that face, hair and apparent age exactly; the second attached image is the father's contempt entire (refs/zeus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Judgment shot on Olympus: Ares god of war, huge brazen god of terrible beauty, dark bronze armor, blood-red cloak and horsehair crest, wolfish hungry perfect face presenting his smoking golden wound to enthroned Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle with the aggrieved face of the cosmos's bully — and the father's answering look: contempt total, unhidden, and beneath it, ineradicable, the fatherhood. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg20-pn3.png — standard 4:3 — ALL WOUNDS CLOSED IN HEAVEN
ATTACH (fetch from repo refs/ and attach to the generation): refs/ares.png, refs/hera.png, refs/athena.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the healing quick as curdling milk; the two queens resuming their thrones content.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cold-comfort shot: the flank of Ares god of war, huge brazen god of terrible beauty, dark bronze armor, blood-red cloak and horsehair crest, wolfish hungry perfect face closing golden under a healer-god's sprinkled simples, Hebe waiting with bath and fresh raiment — the war-god already magnificent and unteachable again — while across the hall Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face and Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face resume their thrones with the satisfaction of a day's work done. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg21-pn1.png — wide 16:9 — THE GODLESS FIELD
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Level-light shot: the two armies fighting on alone beneath a suddenly EMPTY sky between two gleaming rivers — no radiance in the haze but bronze; the struggle swaying; great crested figures falling on both sides in terrible even daylight. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg21-pn2.png — standard 4:3 — THE SUPPLIANT AT THE KNEES
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the wrecked charioteer clasping his knees; the heart moved (refs/menelaus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Mercy-poised shot: a young Trojan (Adrestus), chariot wrecked behind him, on his knees CLASPING the knees of a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak in the full suppliant grip, his plea pouring up — and the wronged king's face, ten years hard, visibly MOVING, the spear-point wavering aside. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg21-pn3.png — standard 4:3 — THE DARKENING
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png, refs/menelaus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'the counsel that curdles the war (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly; the second attached image is aftermath only.' (refs/menelaus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Aftermath-only shot, restraint absolute: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face arrived at a run, his pointing arm and blackened face mid-counsel; a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak's arm pushing the suppliant away from his knees; the king's long shadow fallen across both — and the deed itself outside the frame entirely; the field darker in the panel's very light. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg22-pn1.png — standard 4:3 — THE SEER'S ERRAND
ATTACH (fetch from repo refs/ and attach to the generation): refs/helenus.png, refs/hector.png, refs/aeneas.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the counsel under the reeling line.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Counsel shot: Helenus, seer-prince of Troy, slender grave young man, dark hair under a white seer's band across his brow, priestly Anatolian robe, calm sorrowful eyes, white seer's band bright in the battle-murk, gripping Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak's arm and speaking urgent counsel; Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face steadying the line at their backs; the seer's other hand pointing away toward the distant city on its hill. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg22-pn2.png — standard 4:3 — THE SHIELD-RIM TAPPING
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the commander running for the city, oxhide rim at neck and ankles (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Beloved detail shot: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak RUNNING alone across the plain toward the far gate in full armor — the great body-shield slung at his back, its dark oxhide rim tapping at his neck and his ankles with every stride; one man carrying a city, rendered at full sprint. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg22-pn3.png — standard 4:3 — THE WALL OF ASKING FACES
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the women flooding round him at the gate; five words of truth (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Gate shot: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak halted just inside the Scaean gate, engulfed by a crowd of Trojan WOMEN — wives, mothers, daughters, every face upturned and asking — his two hands raised, gentle and empty, unable to answer any of them singly and refusing to lie to all of them together. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg23-pn1.png — standard 4:3 — WHO ARE YOU, MAGNIFICENT ONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/glaucus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each advancing alone in the space between.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Duel-opening shot: Glaucus of Lycia, keen loyal young war-captain, short brown beard, Lycian armor with a golden double-spiral device and Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar advancing on each other ALONE in the space between the armies — the challenge already flung, spears couched, the day's blood up in both young faces; the hosts dim walls on either side. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg23-pn2.png — standard 4:3 — THE LEAVES
ATTACH (fetch from repo refs/ and attach to the generation): refs/glaucus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the answer that outlived every spear on the field (refs/glaucus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The immortal panel: Glaucus of Lycia, keen loyal young war-captain, short brown beard, Lycian armor with a golden double-spiral device standing at ease into the wind to make his answer — and behind and around him, filling the panel, a great tree streaming LEAVES across the battlefield light, generations of them, falling and blowing through the space between the armies; the young captain's face calm inside the truth he is speaking. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg23-pn3.png — standard 4:3 — BELLEROPHON
ATTACH (fetch from repo refs/ and attach to the generation): refs/glaucus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the lineage rising as a told-vision (refs/glaucus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Told-vision shot: Glaucus of Lycia, keen loyal young war-captain, short brown beard, Lycian armor with a golden double-spiral device speaking on — and rising translucent behind his words the tale itself: a rider on a WINGED WHITE HORSE stooping on a lion-fronted fire-breathing CHIMAERA; folded death-tablets in a traveler's hand; an ambush overcome; a crown and a king's daughter; and at the vision's dim edge, the same hero old and darkened, wandering alone. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg24-pn1.png — standard 4:3 — THE SPEAR PLANTED
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is point-down in the earth; the glad voice (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Recognition shot: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar driving his spear POINT-DOWN into the earth between them and stepping past it — the fighting stance dissolved entire — his scarred face opening into gladness, one arm already extending; the abandoned spear standing like a boundary-mark behind him. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg24-pn2.png — standard 4:3 — THE WRIST-CLASP IN NO-MAN'S LAND
ATTACH (fetch from repo refs/ and attach to the generation): refs/diomedes.png, refs/glaucus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the pledge between the staring armies.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The law made visible: Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar and Glaucus of Lycia, keen loyal young war-captain, short brown beard, Lycian armor with a golden double-spiral device leapt down together, hands locked at the wrist in the full pledge — TWO ENEMIES KIN — in the open killing-ground; and on either side, rendered as walls of staring faces, both armies watching the guest-bond outrank the war. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg24-pn3.png — standard 4:3 — GOLD FOR BRONZE
ATTACH (fetch from repo refs/ and attach to the generation): refs/glaucus.png, refs/diomedes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the exchange (refs/glaucus.png) - reproduce that face, hair and apparent age exactly; the second attached image is the celestial audit in the composition's dry light (refs/diomedes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dry-audit shot: the armor exchange in progress — the GOLDEN panoply of Glaucus of Lycia, keen loyal young war-captain, short brown beard, Lycian armor with a golden double-spiral device passing into the hands of Diomedes king of Argos, compact powerful young war-king, short dark beard, fierce direct eyes, bronze corslet, a round shield blazoned with a boar, the plain BRONZE going back the other way — rendered with absolute ceremonial dignity and one sly compositional imbalance: the gold blazing, the bronze frankly dull; both faces perfectly content. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg25-pn1.png — standard 4:3 — UNWASHED HANDS
ATTACH (fetch from repo refs/ and attach to the generation): refs/hecuba.png, refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the wine offered (refs/hecuba.png) - reproduce that face, hair and apparent age exactly; the second attached image is the refusal that measures him (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Threshold shot at the great house: Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face lifting a two-handled cup of dark wine to her towering son; Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak, filthy with the field, refusing with a gentle firm hand — his blood-and-dust-marked palms held up between himself and the libation, the piety exact. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg25-pn2.png — standard 4:3 — THE ROBE TO THE GODDESS
ATTACH (fetch from repo refs/ and attach to the generation): refs/hecuba.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the procession; the finest robe laid on the knees of the image (refs/hecuba.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Procession shot at the hilltop shrine: Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face and the elder women of Troy bearing a folded ROBE — Sidonian work, star-bright — up the shrine steps; within, a stately PRIESTESS (Theano, inline) laying it across the knees of the seated goddess-image; incense, lamplight, the vow rising. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg25-pn3.png — standard 4:3 — THE REFUSAL
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The coldest small motion: the seated image of the goddess in the lamplight above the kneeling unseeing women — and the head of the image LIFTED MINUTELY AWAY, the incense-smoke bending aside as from a turned cheek; only the viewer shown; the shrine's shadows deepening by one degree. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg26-pn1.png — standard 4:3 — THE CHAMBER OF PARIS
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/paris.png, refs/helen.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the weary rebuke (refs/hector.png) - reproduce that face, hair and apparent age exactly; the second attached image is the sleek brother among his splendid arms (refs/paris.png) - reproduce that face, hair and apparent age exactly; the third attached image is the women's handiwork (refs/helen.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Interior friction shot: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak filling the doorway in full battle-filth; within the fragrant chamber a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound with a thin gold band, rich embroidered Anatolian princely tunic, graceful bearing sleek and untouched, turning his splendid bow in his hands; the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem among her women at their fine handiwork, her eyes going to Hector; two worlds in one room. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg26-pn2.png — standard 4:3 — DOG THAT I AM
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png, refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is her self-naming (refs/helen.png) - reproduce that face, hair and apparent age exactly; the second attached image is the one man who never reproached her (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Confession shot: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem speaking to seated weary Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak — her face open in merciless self-accusation and strange calm, one hand inviting him to rest a moment — the only man in Troy she honors wholly, hearing the only speech in Troy with no lie in it. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg26-pn3.png — standard 4:3 — SONGS FOR MEN TO COME
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the sentence reaching out of the poem; the frame bleeding in (refs/helen.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The two worlds pressed to one pane: close on the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem's face as the sentence leaves her — and around the panel's edges the vision thinning to sepia: the timbers and firelight of the Miletus hall bleeding through, listeners' rapt faces faint in the borders — the woman in the song looking out at the hall that is her doom fulfilled. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg27-pn1.png — standard 4:3 — RUNNING TO MEET HIM
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/andromache.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each at the Scaean gate; the nurse and the starlike child behind.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Meeting shot at the Scaean gate: Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown RUNNING to Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak, her veil loose with haste; behind her a NURSE carrying a bright infant like a fair star; the great gate and the war's light framing all four; his hand already reaching for hers. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg27-pn2.png — standard 4:3 — FATHER AND MOTHER AND BROTHERS
ATTACH (fetch from repo refs/ and attach to the generation): refs/andromache.png, refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'her hand clinging to his (refs/andromache.png) - reproduce that face, hair and apparent age exactly; the second attached image is the complete arithmetic of her losses.' (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The plea: Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown clinging to the hand of Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak, her face lifted through tears in the terrible complete accounting — and ghosted faint along the panel's upper band, her lost world: a mounded grave ringed with young elms, seven fallen brothers, a burning citadel under Plakos. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg27-pn3.png — standard 4:3 — WHERE HER HAND POINTS
ATTACH (fetch from repo refs/ and attach to the generation): refs/andromache.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the tactical plea; the arm flung toward the fig tree and the weak stretch (refs/andromache.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The pointing shot: Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown's arm flung out along the rampart toward ONE visible stretch of wall by a wild FIG TREE — the masonry there subtly different, older-jointed, mortal — the child in the nurse's arms behind her; her face fierce with the soldier's argument; the stretch itself holding the light strangely. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg28-pn1.png — standard 4:3 — SHAME, AND THE TRAINED HEART
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the refusal and its true engine (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Answer shot: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak holding his wife's hands in both of his, the refusal grave and gentle in his face — behind him, faint on the panel's edge, the watching women of Troy with their trailing robes, the shame-court before which he cannot hide. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg28-pn2.png — standard 4:3 — I KNOW IT IN MY HEART
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/andromache.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

'the knowledge entire, spoken quietly on the wall.'

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The quiet apocalypse: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak speaking the knowledge — and rendered dim and translucent across the sky behind the two figures, the future he names: a burning citadel, a weeping woman led away among spearmen to the ships; Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown's face receiving it; the two of them small and holding on beneath what he sees. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg28-pn3.png — standard 4:3 — THE CHILD AND THE CREST
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/andromache.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'the reach (refs/hector.png) - reproduce that face, hair and apparent age exactly; the second attached image is the shriek at the nodding horsehair.' (refs/andromache.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The turn: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak reaching out both arms for his son — and the INFANT shrinking back SCREAMING against the nurse's breast, terrified of the bronze and the horsehair CREST nodding dreadful from his father's helmet-peak; Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown's hand flying toward the child; the helmet's shadow across the panel. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg29-pn1.png — standard 4:3 — THE ONLY SHARED LAUGH
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/andromache.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'both parents laughing aloud (refs/hector.png) - reproduce that face, hair and apparent age exactly; the second attached image is the helmet set shining on the ground.' (refs/andromache.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The mercy: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak and Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown LAUGHING ALOUD TOGETHER — the war's one shared laugh — as he sweeps the flashing helmet off and sets it on the ground, the child already reaching wonderingly for his bared father; the bronze shell of the world's war sitting empty on the stones beside them. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg29-pn2.png — standard 4:3 — THE PRAYER FOR THE BOY
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the child held up to the sky between his father's hands (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Blessing shot: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak holding the infant HIGH between both hands against the open sky above the rampart, his face lifted in the father's whole prayer; the child's small arms out; the light of the panel gathered entirely on the two of them. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg29-pn3.png — standard 4:3 — THE SMILE THROUGH TEARS
ATTACH (fetch from repo refs/ and attach to the generation): refs/andromache.png, refs/hector.png, refs/paris.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'the child received against her breast (refs/andromache.png) - reproduce that face, hair and apparent age exactly; the second attached image is the parting (refs/hector.png) - reproduce that face, hair and apparent age exactly; the third attached image is the stallion-bright brother at the gate.' (refs/paris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The parting triptych in one frame: Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown receiving the child against her breast SMILING THROUGH HER TEARS, Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak's hand at her cheek in last gentleness — she already turned half away, looking back — and at the gate's shadow beyond, arriving gleaming and laughing in splendid war-gear like a stallion broken loose, a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound with a thin gold band, rich embroidered Anatolian princely tunic, graceful bearing; the open gate and the waiting plain framing the brothers' exit. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg30-pn1.png — standard 4:3 — FRAME — WHY IS IT WORSE?
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is fists on knees; many in the hall openly weeping (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face with his fists on his knees, eyes bright, the question forced out; behind him listeners openly wiping their faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg30-pn2.png — standard 4:3 — FRAME — NO PAEEON FOR THE WALL
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the gods healed; the mortals promised (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre answering with terrible gentleness, one hand closing slowly over his own heart. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg30-pn3.png — standard 4:3 — FRAME — POINTED OUT IN LOVE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is rising; the door of Troy's death first shown in love (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre risen, the phorminx cradled, his blind face turned aside as from something he can see too well. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg31-pn1.png — wide 16:9 — FRAME — THE TALLY
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each in the settling hall.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot: the hall settling in low murmurs, embers deep red; an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre standing with the phorminx; a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face quiet on the high seat. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg31-pn2.png — standard 4:3 — FRAME — AND TOMORROW?
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the nightly question, softly (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face asking the nightly question softly, chin on his fist. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i08-pg31-pn3.png — standard 4:3 — FRAME — THE WRATH IS OFFERED EVERYTHING
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is at the doorway; the promise of the proudest sentence (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Close shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre at the dark doorway against the starry sea, one hand lifted in the night's last promise. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i08-pg32-pn1.png — full page 3:4 — THE GNOME PAGE
ATTACH: none
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Full-page quiet composition: the Iron Age Ionian hall empty of people, the hearth down to red embers, the carved stool with the silent phorminx leaning against it in a pool of lamplight; and blowing in across the threshold-stone from the dark doorway, a scatter of dry LEAVES — several still adrift in the lamplight, one just touching the phorminx's strings; through the doorway the star-white night over a dark calm sea. Leave the upper third calm and uncluttered for a large ornamented text panel. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---
END OF ISSUE 8 PROMPTS. When all art exists: send the art+refs zip and say "build issue 8." Builds to its own separate issue-08.pdf.
