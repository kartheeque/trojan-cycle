# ISSUE 3 — PANEL PROMPTS (pages 1–32) · self-contained format
Same rules as Issues 1–2. Guard clause on every earthly scene; [STYLE-TABLET] register on pg02 ONLY (per master-plan ruling v0.5.3); divine radiance clause on god scenes. Ref-births marked REF-BIRTH (crops are verification-side pipeline steps, committed to refs/ before dependent panels generate). Every prompt is fully self-contained — paste exactly as written. Panels are TEXTLESS.
Reusable refs already in refs/: singer.png, neleid-prince.png, zeus.png, themis.png, muse.png, poseidon.png, apollo.png (background gods at the wedding may echo these).

> **TWO-LLM WORKFLOW (standing instructions for the image-generation session):**
> 1. You have READ access to this repository. For each panel below, fetch every file on its ATTACH line from the repo's `refs/` folder (same branch as this prompts file) and attach those images to the generation request together with the PROMPT text, used verbatim.
> 2. Generate at the stated aspect ratio. Output must be completely TEXTLESS.
> 3. You cannot commit. Hand the finished image to the human operator under its exact panel filename (iNN-pgNN-pnN.png); the operator relays it to the verification side (Claude), which reviews it against prompt and refs and commits it to `issues/issue-NN/art/`.
> 4. Panels marked REF-BIRTH create a new reference face: after that panel passes verification, the verification side crops and commits the new ref to `refs/`. Do NOT generate any later panel that ATTACHes that ref until the ref file exists in the repo.


### i03-pg01-pn1.png — full page 3:4 — COVER — LIGHTS ON THE MOUNTAIN
ATTACH: none
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cover composition: Mount Ida above Troy: high pine forests and open upland pastures, cold streams, herds of cattle, the Trojan plain and the sea far below at golden evening; small on a high pasture, seen from behind, a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing with his cattle; and high above him, descending the sky toward the mountain, FOUR points of divine golden radiance trailing light; leave the upper quarter of the sky calm for title lettering. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg02-pn1.png — full page 3:4 — THE TABLET PROLOGUE
ATTACH: none
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Single full-page image styled as an ancient incised clay tablet: warm fired-clay tones only, the entire image rendered as shallow low-relief carving pressed into clay, bordered with abstract cuneiform-like decorative wedge bands (purely decorative, no legible script), pictorial scenes arranged in horizontal registers in the manner of ancient Near Eastern relief. Pictorial registers: UPPER register — a great mountain empire of many fortress silhouettes; MIDDLE register — a single walled city with sloping ramparts on a plain beside a narrow strait; LOWER register — a sea with oared raider ships with bird-head prows advancing from the left; small stylized relief figures of kings, spearmen and rowers in each register; decorative wedge-bands separating the registers. Leave calm band-spaces above and below the registers for caption plates. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg03-pn1.png — wide 16:9 — FRAME — THE PACKED HALL
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot of an early Iron Age Ionian megaron hall at evening: timber columns, central hearth fire, hanging oil lamps, noble audience seated on benches, dark doorway open to a starry Aegean night, packed to the walls, listeners standing along the columns: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre seated with the phorminx, a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face leaning forward on the high seat. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg03-pn2.png — standard 4:3 — FRAME — THE PROMISE CLAIMED
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the young noble, eager (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face eager, palm out in friendly demand, firelight on his face. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg03-pn3.png — standard 4:3 — FRAME — FIRST, TROY
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bard nodding slowly (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre nodding slowly, one hand rising toward the east, the fire beneath him. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg04-pn1.png — standard 4:3 — THE INVOCATION
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/muse.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'the bard's face lifted (refs/singer.png) - reproduce that face, hair and apparent age exactly; the second attached image is the Muse faint in the smoke above.' (refs/muse.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre with face lifted and fingers on the strings; above the hearth-smoke, faint and luminous, a Muse: luminous woman of unearthly beauty, dark hair crowned with laurel, flowing pale gold robe, softly radiant against darkness half-manifest. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg04-pn2.png — standard 4:3 — THE VISION KINDLES
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Transitional shot: the sepia twilight hall dissolving upward into warm gold light, the hearth-flame streaming into a river of color. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg04-pn3.png — wide 16:9 — TROY IN ITS GREATNESS
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide morning vista in full color: Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond, rich and rebuilt, bright roofs, busy gates, herds on the plain, ships at the shore. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg05-pn1.png — standard 4:3 — THE KING (births PRIAM: crop refs/priam.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot in the palace court of Troy: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face enthroned under a painted canopy, receiving his people — petitioners, herdsmen, a merchant with samples of cloth; ordered, prosperous, just. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/priam.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg05-pn2.png — standard 4:3 — THE QUEEN (births HECUBA: crop refs/hecuba.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Warm shot on a palace colonnade: Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face among her women, two small royal children at her skirts, giving instructions to a steward; commanding and beloved. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/hecuba.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg05-pn3.png — standard 4:3 — THE TERRACE AT EVENING
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/hecuba.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each together at the rail.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Evening two-shot on the high palace terrace: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face and Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face side by side at the rail, the lamps of the city kindling below them, the dark sea beyond. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg06-pn1.png — wide 16:9 — THE COUNCIL — THE TABLET FROM THE EAST (births ANTENOR: crop refs/antenor.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference image exactly: it is the king on the low dais (refs/priam.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot of the council chamber of Troy: painted mudbrick and cedar timber, Anatolian columns, a low dais, racks of clay tablets, a gate-shrine niche with small standing stones: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face seated on the low dais; elders and princes on benches; Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face standing with his staff; before the dais a SCRIBE reading from a clay tablet held flat on both palms. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/antenor.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg06-pn2.png — standard 4:3 — ANTENOR COUNSELS
ATTACH (fetch from repo refs/ and attach to the generation): refs/antenor.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the old counselor speaking, finger raised (refs/antenor.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face speaking with measured authority, one finger raised, the council listening. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg06-pn3.png — standard 4:3 — THE YOUNG NOBLE'S ANGER
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: a hot-eyed YOUNG TROJAN NOBLE in a fine Anatolian tunic gesturing angrily toward the bright sea visible through the great doorway; older councilors frowning at his heat. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg07-pn1.png — standard 4:3 — THE KING RISES
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the king rising from the dais, calm (refs/priam.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face rising from the dais with calm authority, the council coming to stillness. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg07-pn2.png — standard 4:3 — EAST AND WEST
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is one hand toward the east window, one toward the sea (refs/priam.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face standing with one hand extended toward an eastern window and the other toward the sea-facing doorway, the balanced gesture of a king weighing two worlds. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg07-pn3.png — wide 16:9 — THE COUNCIL ASSENTS
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/antenor.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot: the council bowing assent to the standing king; Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face satisfied; through the great doorway beyond them, the calm bright sea. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg08-pn1.png — full page 3:4 — SPLASH — THE DREAM OF THE FIREBRAND
ATTACH (fetch from repo refs/ and attach to the generation): refs/hecuba.png
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Match the attached reference image exactly: it is the sleeping queen (refs/hecuba.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page night dream composition, terrible and dignified: in the lower part, the quiet dark royal bedchamber with Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face asleep, heavy with child; rising from her sleeping form into the upper part of the page, a dream made visible — a great BURNING TORCH, and from it fire spreading in a vast arc through a ghostly dream-image of Troy: walls, towers and ships all taken by flame, the dream-fire wheeling above the untouched dark bedchamber. No gore, no figures burning; the horror is the burning city itself. Leave a calm band at the very top for an ornate caption plate. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg09-pn1.png — standard 4:3 — THE SEERS' ANSWER
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/hecuba.png, refs/antenor.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each; the seer casting lots before them.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Morning shot in the gate-shrine forecourt: an old SEER casting marked lots on a hide before the smoking altar; King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face and Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face grey-faced before him; Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face and elders grave behind; the lots falling ill. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg09-pn2.png — standard 4:3 — THE IMPOSSIBLE CHOICE
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/hecuba.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the queen turned away (refs/priam.png) - reproduce that face, hair and apparent age exactly; the second attached image is the king rigid (refs/hecuba.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium two-shot: Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face turned away with her hands over her face; King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face standing rigid, aged years in one moment, his hand half-raised toward her and stopping. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg09-pn3.png — standard 4:3 — THE ORDER GIVEN (births AGELAUS: crop refs/agelaus.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the king not looking at the kneeling herdsman (refs/priam.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Painful quiet shot: Agelaus, chief herdsman of Ida, weathered kindly mountain man, grizzled beard, rough wool cloak and leggings, herding staff kneeling, receiving a small wrapped bundle from a weeping NURSE; King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face standing apart with his face turned away, unable to watch; torchlight low. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/agelaus.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

---

### i03-pg10-pn1.png — wide 16:9 — INTO THE WILDS
ATTACH (fetch from repo refs/ and attach to the generation): refs/agelaus.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference image exactly: it is the herdsman climbing with the bundle (refs/agelaus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot of Mount Ida above Troy: high pine forests and open upland pastures, cold streams, herds of cattle, the Trojan plain and the sea far below: Agelaus, chief herdsman of Ida, weathered kindly mountain man, grizzled beard, rough wool cloak and leggings, herding staff climbing alone into high misty pine forest, the small bundle held against his chest, his face wretched. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg10-pn2.png — standard 4:3 — THE SHE-BEAR
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Hushed forest shot in a sheltered hollow among great pine roots: a swaddled INFANT lying safe on moss — and standing over the child, calm and vast and gentle, a SHE-BEAR with her muzzle lowered tenderly toward it; morning mist, no menace anywhere, an image of guardianship. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg10-pn3.png — standard 4:3 — WHAT HEAVEN KEEPS
ATTACH (fetch from repo refs/ and attach to the generation): refs/agelaus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the herdsman returned, staff fallen, staring (refs/agelaus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: Agelaus, chief herdsman of Ida, weathered kindly mountain man, grizzled beard, rough wool cloak and leggings, herding staff returned to the hollow, his staff fallen from his hand, staring in awe at the living infant lifting its arms to him; the bear gone; a shaft of morning light on the child. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg11-pn1.png — wide 16:9 — THE DEFENDER OF MEN (births PARIS: crop refs/paris.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide action shot on a high pasture: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing, in his mid-teens here, driving off three rough CATTLE-RAIDERS with staff and sling, the herd safe behind him; the raiders stumbling away downslope; bright mountain air. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/paris.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg11-pn2.png — standard 4:3 — THE FIRE ON THE MOUNTAIN
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png, refs/agelaus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the youth at ease (refs/paris.png) - reproduce that face, hair and apparent age exactly; the second attached image is the old man watching with troubled love (refs/agelaus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Evening fire shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing at ease among laughing herdsmen at a mountain campfire; at the circle's edge Agelaus, chief herdsman of Ida, weathered kindly mountain man, grizzled beard, rough wool cloak and leggings, herding staff watching the young man with troubled love. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg11-pn3.png — standard 4:3 — THE CITY BELOW
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the youth alone on a crag at dusk (refs/paris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing alone on a crag at dusk, looking down at the far small glitter of Troy on its plain, an unnamed longing on his beautiful face; the first stars. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg12-pn1.png — standard 4:3 — THE BULL CONTEST
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the young herdsman with his garlanded champion (refs/paris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Festival shot on the pasture: a contest ring of low stones; a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing standing proudly with his own great garlanded CHAMPION BULL; facing them across the ring a strange PERFECT WHITE BULL that no man recognizes; herdsmen arguing and pointing; autumn light. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg12-pn2.png — wide 16:9 — THE WHITE BULL PREVAILS
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dynamic wide shot in the stone ring: the two bulls shoulder to shoulder in the pushing contest, the WHITE BULL prevailing with uncanny effortless power, the champion bull giving ground, dust and divots flying; herdsmen shouting from the ring stones. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg12-pn3.png — standard 4:3 — THE FAIR JUDGMENT
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the youth garlanding the stranger's bull with his own hands (refs/paris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The key shot, quiet and formal: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing placing the victor's garland on the horns of the WHITE BULL with his own hands, his face honest and a little sad; his beaten champion behind him; the white bull's dark eye deep and knowing; herdsmen murmuring at such fairness. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg13-pn1.png — standard 4:3 — FRAME — THE TWO WHO DO NOT KNOW
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the young noble, moved (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot by ember-light: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face moved and thoughtful, speaking slowly, firelight low. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg13-pn2.png — standard 4:3 — FRAME — COME WEST WITH ME
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bard, gently (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre answering gently, one hand beginning to rise westward. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg13-pn3.png — standard 4:3 — FRAME — GOLD RISING
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the vision-light rising around the bard (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Transitional shot: gold light rising and flooding the sepia around an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre, the hall dissolving at the edges into the coming vision. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg14-pn1.png — tall 2:3 — THETIS OF THE SEA (births THETIS: crop refs/thetis.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 2:3 tall portrait panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tall dawn sea shot: Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face rising luminous from a wave-trough among leaping dolphins, half of the sea and half of light, her robes and hair flowing like water into water. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/thetis.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg14-pn2.png — standard 4:3 — THE DECREE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/themis.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the veiled goddess with hand raised in warning.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Divine shot in Olympus above the clouds: an open pillared hall of pale stone on a mountain summit floating over a sea of clouds, golden light, distant peaks: Themis goddess of divine order: serene matronly beauty, veiled head, silver-grey archaic robes, measured wise expression with one hand raised in solemn warning before Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle enthroned, the golden loom of fate faint behind them. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg14-pn3.png — standard 4:3 — DESIRE SET DOWN
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the king of the gods, sober, setting down desire like a cup (refs/zeus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Divine close shot: Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle, sober and sovereign, slowly setting down a golden cup on the arm of his throne — the gesture of desire renounced — his eyes already calculating far ahead. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg15-pn1.png — standard 4:3 — THE PIOUS KING (births PELEUS: crop refs/peleus.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dawn shot at a simple hillside stone altar: Peleus king of Phthia, mature steadfast hero, brown beard, plain noble bearing, bronze-trimmed tunic and travel cloak, patient devout face alone, making offering with exact reverent care, barley falling from his hand into the small flame; his kingdom's valley waking below. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/peleus.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg15-pn2.png — wide 16:9 — HOLDING THE GODDESS
ATTACH (fetch from repo refs/ and attach to the generation): refs/peleus.png, refs/thetis.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference images exactly: the first attached image is he holds (refs/peleus.png) - reproduce that face, hair and apparent age exactly; the second attached image is she transforms (refs/thetis.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dramatic night shore shot, one image containing transformation: Peleus king of Phthia, mature steadfast hero, brown beard, plain noble bearing, bronze-trimmed tunic and travel cloak, patient devout face with arms locked around Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face as she SHAPE-SHIFTS in his grip — her form flowing at once into rushing water, white flame, the forequarters of a lioness and a great serpent coil, all streaming from the one figure he holds; his face set and enduring; moonlit surf around their feet. Dignified, mythic, nothing sensual — a trial of endurance. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg15-pn3.png — standard 4:3 — THE VICTOR KNEELS
ATTACH (fetch from repo refs/ and attach to the generation): refs/peleus.png, refs/thetis.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is she stands free in her own form (refs/peleus.png) - reproduce that face, hair and apparent age exactly; the second attached image is he kneels, head bowed (refs/thetis.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dawn shot on the shore: Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face standing free in her own form, wonder breaking through her coldness; before her Peleus king of Phthia, mature steadfast hero, brown beard, plain noble bearing, bronze-trimmed tunic and travel cloak, patient devout face on one knee, head bowed, exhausted — having won, offering the victory back as reverence. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg16-pn1.png — close-up 4:3 — WONDER AND SORROW
ATTACH (fetch from repo refs/ and attach to the generation): refs/thetis.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is her immortal face moving from cold to wonder to sorrow (refs/thetis.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close divine shot: the face of Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face, cold melting into wonder and wonder into sorrow, dawn light on the sea behind her. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg16-pn2.png — wide 16:9 — THE DAWN SHORE
ATTACH (fetch from repo refs/ and attach to the generation): refs/peleus.png, refs/thetis.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each walking together, not touching.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide gentle shot: Peleus king of Phthia, mature steadfast hero, brown beard, plain noble bearing, bronze-trimmed tunic and travel cloak, patient devout face and Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face walking the long dawn shore side by side, not touching, deep in speech; their two lines of footprints behind them, one fading where the surf reaches it. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg16-pn3.png — standard 4:3 — THE SEA'S GRIEF
ATTACH (fetch from repo refs/ and attach to the generation): refs/thetis.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is her face out to sea, the grief of all the sea in it (refs/thetis.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet close shot: Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face looking out over the open sea, the grief of all the sea gathered in her beautiful immortal face; wind in her water-dark hair. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg17-pn1.png — wide 16:9 — PELION MADE READY (births CHIRON: crop refs/chiron.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide festive shot of Mount Pelion: a wooded sacred mountain, the great cave-hall of the centaur opening onto a broad terrace with feasting tables under ancient plane trees, the Aegean far below: nymphs and mountain folk dressing long feast tables under the ancient plane trees, garlands going up between the trunks; Chiron the wise centaur, upper body of a grey-bearded sage with kind deep eyes, lower body of a chestnut horse, a healer's satchel at his side directing the preparations with quiet joy, one hand full of flowers. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/chiron.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg17-pn2.png — standard 4:3 — THE HERALD FLIES (births HERMES: crop refs/hermes.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Sky shot: Hermes messenger of the gods, swift slender youthful god, winged golden sandals and a winged traveler's cap, herald's staff twined with serpents, quick clever face flying swift against towering sunset clouds, herald's staff before him, a long streak of golden light behind his winged sandals. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/hermes.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg17-pn3.png — standard 4:3 — THE UNINVITED (births ERIS: crop refs/eris.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Shadow shot at the margin of the bright preparations: among the dark pines beyond the torchlight, Eris goddess of strife, gaunt pale goddess in night-dark robes, wild black hair, beautiful bitter face watching the joyful work, utterly still, her bitter beautiful face half in darkness. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/eris.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

---

### i03-pg18-pn1.png — wide 16:9 — HEAVEN DESCENDS (births HERA, ATHENA, APHRODITE: crop refs/hera.png, refs/athena.png, refs/aphrodite.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference image exactly: it is the king of the gods foremost (refs/zeus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide glory shot: the gods descending through the evening sky toward the mountain terrace in a river of radiance — Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle foremost with Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face beside him; behind them Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face, Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face, a wild-bearded sea-god with a trident, a golden-haired archer god, and a singing cluster of laurel-crowned Muses. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/hera.png, refs/athena.png, refs/aphrodite.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg18-pn2.png — standard 4:3 — THE MORTAL HOST
ATTACH (fetch from repo refs/ and attach to the generation): refs/peleus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is one mortal man standing very straight to receive them (refs/peleus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot at the terrace edge: Peleus king of Phthia, mature steadfast hero, brown beard, plain noble bearing, bronze-trimmed tunic and travel cloak, patient devout face in his plain best clothing, standing very straight and alone to receive the descending radiance, mortal courage in the face of glory, the divine light breaking over him. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg18-pn3.png — standard 4:3 — THE BRIDE LED IN
ATTACH (fetch from repo refs/ and attach to the generation): refs/thetis.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bride veiled in sea-silver between torches (refs/thetis.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Processional shot: Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face led in as bride, veiled in sea-silver, between lines of torches, sea-nymph attendants bearing her train; her beauty enormous; her eyes within the veil already grieving. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg19-pn1.png — full page 3:4 — SPLASH — THE WEDDING ON PELION
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/hera.png, refs/athena.png, refs/aphrodite.png, refs/peleus.png, refs/thetis.png, refs/chiron.png, refs/eris.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

map each: Zeus presiding; the couple at the head; the centaur presenting a great ash spear; the strife-goddess tiny in the outer dark.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page feast of heaven on the torchlit mountain terrace under the plane trees: gods and goddesses radiant at the long boards — Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle presiding with Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face; Peleus king of Phthia, mature steadfast hero, brown beard, plain noble bearing, bronze-trimmed tunic and travel cloak, patient devout face and the veiled Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face at the head of the feast; Chiron the wise centaur, upper body of a grey-bearded sage with kind deep eyes, lower body of a chestnut horse, a healer's satchel at his side standing as host presenting a GREAT ASH SPEAR; a wild-bearded sea-god presenting TWO IMMORTAL WHITE HORSES with manes like sea-foam; laurel-crowned Muses singing; golden cups going round; the mountain night jeweled with divine light — and at the far edge of the torchlight, small between two dark pines, the gaunt night-robed figure of Eris goddess of strife, gaunt pale goddess in night-dark robes, wild black hair, beautiful bitter face watching. Leave calm space at top for an ornate caption plate. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg20-pn1.png — standard 4:3 — THE ASH SPEAR
ATTACH (fetch from repo refs/ and attach to the generation): refs/chiron.png, refs/peleus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the centaur laying the spear in the king's hands.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Ceremonial shot: Chiron the wise centaur, upper body of a grey-bearded sage with kind deep eyes, lower body of a chestnut horse, a healer's satchel at his side laying the GREAT ASH SPEAR — plainly beyond mortal make, its shaft perfect and heavy — across the open hands of Peleus king of Phthia, mature steadfast hero, brown beard, plain noble bearing, bronze-trimmed tunic and travel cloak, patient devout face; firelight running down the polished wood. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg20-pn2.png — standard 4:3 — THE DEATHLESS HORSES
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Shot of wonder: TWO IMMORTAL WHITE HORSES presented at the feast, manes and tails moving like surf in wind that touches nothing else, hooves not quite pressing the grass; a wild-bearded sea-god's hand on one proud neck; guests turning in awe. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg20-pn3.png — standard 4:3 — THE BRIDE'S TWO FACES
ATTACH (fetch from repo refs/ and attach to the generation): refs/thetis.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is her smile and her grief in one face (refs/thetis.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot at the head of the feast: Thetis the sea-goddess, slender luminous divine woman, silver-touched dark hair flowing like water, sea-grey and silver robes that ripple like the tide, beautiful sorrowful immortal face, unveiled now, receiving the gifts meant for her unborn son — her gracious smile and her fathomless grief present in the one immortal face. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg21-pn1.png — standard 4:3 — STRIFE AT THE EDGE OF THE LIGHT
ATTACH (fetch from repo refs/ and attach to the generation): refs/eris.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the strife-goddess stepping to the rim of the torchlight (refs/eris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dramatic shot: Eris goddess of strife, gaunt pale goddess in night-dark robes, wild black hair, beautiful bitter face stepping from the outer dark to the very rim of the torchlight, the bright feast beyond her; in her raised pale hand, catching all the light of the feast at once, A GOLDEN APPLE. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg21-pn2.png — close-up 4:3 — THE APPLE
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot: a perfect APPLE OF SOLID GOLD held in pale fingers, gleaming with gathered torchlight, its surface flawless and unmarked; darkness around the hand. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg21-pn3.png — close-up 4:3 — HER FACE
ATTACH (fetch from repo refs/ and attach to the generation): refs/eris.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bitter beautiful face, the feast reflected small in her eyes (refs/eris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot: the face of Eris goddess of strife, gaunt pale goddess in night-dark robes, wild black hair, beautiful bitter face, bitter and beautiful, the entire golden feast reflected tiny and doubled in her dark eyes. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg22-pn1.png — wide 16:9 — THE THROW
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dramatic shot over the feast: the GOLDEN APPLE in mid-flight above the boards, turning slowly, blazing in the torchlight, a faint golden arc behind it; below, the upturned radiant faces of gods beginning to track it; the thrower already gone from the darkness at the edge. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg22-pn2.png — standard 4:3 — WHERE IT STOPPED
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tense close shot along the feast board: the golden apple rolled to rest on the cloth among cups and garlands — and THREE jeweled hands reaching for it at the same instant from three directions. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg22-pn3.png — wide 16:9 — THE MUSIC DIES
ATTACH (fetch from repo refs/ and attach to the generation): refs/hera.png, refs/athena.png, refs/aphrodite.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each risen to her feet.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide frozen shot of the feast: the Muses' mouths closed mid-song, every god gone still, cups halted halfway — and three goddesses risen to their feet over the apple: Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face, Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face, Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg23-pn1.png — standard 4:3 — HERA CLAIMS
ATTACH (fetch from repo refs/ and attach to the generation): refs/hera.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is crowned, terrible in majesty (refs/hera.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Regal shot: Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face standing at full majesty, one hand extended over the apple in claim, crown blazing. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg23-pn2.png — standard 4:3 — ATHENA CLAIMS
ATTACH (fetch from repo refs/ and attach to the generation): refs/athena.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is calm and absolute, spear grounded (refs/athena.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Composed shot: Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face standing calm and absolute, spear-butt grounded, grey eyes level, her claim made without heat. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg23-pn3.png — standard 4:3 — APHRODITE CLAIMS
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is smiling, and the smile itself the argument (refs/aphrodite.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Radiant shot: Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face not reaching for the apple at all — simply standing, smiling, doves settling at her shoulders, her beauty itself the entire argument. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg24-pn1.png — wide 16:9 — JUDGE, HUSBAND
ATTACH (fetch from repo refs/ and attach to the generation): refs/hera.png, refs/athena.png, refs/aphrodite.png, refs/zeus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each: the three turned as one to the enthroned king.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot: the three goddesses turned as one toward Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle enthroned at the feast's head, the whole silent feast waiting on him; the apple small and blazing on the board between. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg24-pn2.png — standard 4:3 — THE WISEST REFUSAL
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is sovereign and unreadable, slowly shaking his head (refs/zeus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot: Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle, sovereign and unreadable, slowly shaking his head — the refusal of a king who sees every consequence, and one more besides. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg24-pn3.png — standard 4:3 — THE JUDGE NAMED
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is looking away east and down through the night (refs/zeus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Divine shot: Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle looking away to the east and downward — through parted night clouds far below, tiny and moonlit, a dark mountain above a sleeping walled city. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg25-pn1.png — standard 4:3 — THE CHARGE
ATTACH (fetch from repo refs/ and attach to the generation): refs/hermes.png, refs/zeus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the herald receiving the apple, his quick face grave.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Ceremonial shot: Hermes messenger of the gods, swift slender youthful god, winged golden sandals and a winged traveler's cap, herald's staff twined with serpents, quick clever face receiving the GOLDEN APPLE into both cupped hands from the hand of Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle, the herald's quick clever face for once entirely grave. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg25-pn2.png — wide 16:9 — EAST OVER THE SEA
ATTACH (fetch from repo refs/ and attach to the generation): refs/hermes.png, refs/hera.png, refs/athena.png, refs/aphrodite.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each in the night sky.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide night shot: four divine figures crossing the starry sky eastward high over the black Aegean — Hermes messenger of the gods, swift slender youthful god, winged golden sandals and a winged traveler's cap, herald's staff twined with serpents, quick clever face leading with the apple glowing like a carried lamp, Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face, Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face and Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face behind him — a slow comet of light above the dark water. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg25-pn3.png — standard 4:3 — THE FIRE ON THE SHOULDER OF IDA
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Night shot from high air: moonlit Ida rising above the dark Trojan plain, the sea a sheet of black silver — and on the mountain's high shoulder one tiny herdsman's campfire. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg26-pn1.png — standard 4:3 — THE FULL HOUSE (births HECTOR: crop refs/hector.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/hecuba.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each on the terrace; behind them the grown crown prince.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Night terrace shot at Troy: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face and Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face at the rail, older now; behind them, grown, Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak — tall, open-faced, a young man other men already follow. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/hector.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg26-pn2.png — standard 4:3 — THE ONE WHO SEES (births CASSANDRA: crop refs/cassandra.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Unsettling quiet shot at the terrace rail, apart from the others: Cassandra, young princess of Troy, wild dark hair, wide haunted far-seeing eyes, white and saffron Anatolian gown, a laurel sprig at her belt staring fixedly out at dark Mount Ida, her hands white-knuckled on the stone, night wind in her wild hair. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/cassandra.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i03-pg26-pn3.png — close-up 4:3 — TORCHES ON IDA
ATTACH (fetch from repo refs/ and attach to the generation): refs/cassandra.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is her wide haunted eyes (refs/cassandra.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot: the wide haunted far-seeing eyes of Cassandra, young princess of Troy, wild dark hair, wide haunted far-seeing eyes, white and saffron Anatolian gown, a laurel sprig at her belt, and reflected tiny in each dark pupil, a point of moving golden light on a black mountain. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg27-pn1.png — wide 16:9 — THE ROUTINE OF EMPIRE
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/antenor.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each attending the reading.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Sunlit wide shot of the council chamber of Troy: painted mudbrick and cedar timber, Anatolian columns, a low dais, racks of clay tablets, a gate-shrine niche with small standing stones: the SCRIBE reading a new clay tablet; King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face and Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face attending; stewards with tally-tablets; order, daylight, routine. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg27-pn2.png — standard 4:3 — THE ACCOUNTS BALANCE
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/antenor.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each exchanging a satisfied look.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium two-shot: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face and Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face exchanging the quiet satisfied look of two old men whose accounts balance; sunlight on the tablet racks behind them. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg27-pn3.png — standard 4:3 — THE FOURTH DIRECTION
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Deep-focus shot through the council-chamber doorway, past the shoulders of the councilors at the edge of frame: far beyond the city roofs, small and serene in summer light, Mount Ida. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg28-pn1.png — wide 16:9 — THE EMPTY HALL OF HEAVEN
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/themis.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each alone by the golden loom.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide divine shot of Olympus above the clouds: an open pillared hall of pale stone on a mountain summit floating over a sea of clouds, golden light, distant peaks, the great hall nearly empty after the feast: Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle and Themis goddess of divine order: serene matronly beauty, veiled head, silver-grey archaic robes, measured wise expression alone beside the great golden loom strung with shining threads. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg28-pn2.png — standard 4:3 — THEMIS AT THE LOOM
ATTACH (fetch from repo refs/ and attach to the generation): refs/themis.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is her hand on the shining threads (refs/themis.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium divine shot: Themis goddess of divine order: serene matronly beauty, veiled head, silver-grey archaic robes, measured wise expression with one hand laid on the taut shining threads of the golden loom, reading them like a weaver, her veiled face measured and grave. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg28-pn3.png — standard 4:3 — THE PLAN WITHOUT HANDS
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is looking down through the cloud-floor, the scepter at rest (refs/zeus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Divine shot: Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle gazing down through a rift in the cloud-floor at the small bright world, the eagle-scepter resting against his shoulder, his sovereign face without triumph and without mercy — only certainty. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg29-pn1.png — wide 16:9 — THE PIPING HERDSMAN
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference image exactly: it is alone with his herds, playing a reed pipe, utterly at peace (refs/paris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide golden-hour shot of Mount Ida above Troy: high pine forests and open upland pastures, cold streams, herds of cattle, the Trojan plain and the sea far below: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing seated on a stone among his grazing cattle, playing a reed pipe, utterly at peace; the plain and the shining sea far below. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg29-pn2.png — standard 4:3 — THE LIGHT ON THE PATH
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is behind him, up the darkening path, a golden radiance beginning (refs/paris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Ominous beautiful shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing still piping, unaware, in the foreground; behind him, far up the darkening path between the pines, a golden radiance beginning — four distinct points of approaching divine light. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg29-pn3.png — wide 16:9, letterbox — THE HINGE OF THE WORLD
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference image exactly: it is the tiny piping figure; the four lights nearly upon him (refs/paris.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Letterbox wide shot, the whole dark mountainside: the tiny figure of the piping herdsman at his fire; the four divine lights nearly upon him on the path; Troy glittering minute on the plain far below; the first stars above. Stillness before everything. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg30-pn1.png — wide 16:9 — FRAME — VERY LATE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot of the hall, very late and very still, the fire down to a red core: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre lowering the phorminx; a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face with his chin on his fist, troubled. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg30-pn2.png — standard 4:3 — FRAME — HOW DOOM WALKS
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bard, grave (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre speaking gravely, the ember-light deep in the lines of his face. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg30-pn3.png — standard 4:3 — FRAME — THE QUESTION TO THE PRINCE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'the bard's hand flat on the silent strings (refs/singer.png) - reproduce that face, hair and apparent age exactly; the second attached image is the prince struck silent.' (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium two-shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre with his hand laid flat on the silenced strings, his blind face turned exactly toward a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face, who sits struck silent by the question. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg31-pn1.png — wide 16:9 — FRAME — THE HALL EMPTIES
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Match the attached reference images exactly: the first attached image is the bard rising with his boy's help (refs/singer.png) - reproduce that face, hair and apparent age exactly; the second attached image is the prince still seated (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot: the hall emptying, embers low, servants moving; an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre rising with the help of a boy; a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face still seated on the high seat, shaken and thoughtful. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg31-pn2.png — standard 4:3 — FRAME — TOMORROW, THE JUDGMENT
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the prince, quietly (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face speaking quietly, the weight of the tale on his young face. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i03-pg31-pn3.png — standard 4:3 — FRAME — A SHIP FOR SPARTA
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the bard at the doorway, face to the stars (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Close shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre paused at the dark doorway, blind face lifted to the white stars over the sea, the promise of tomorrow's song on his lips. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i03-pg32-pn1.png — full page 3:4 — THE GNOME PAGE
ATTACH: none
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Full-page quiet composition: the Iron Age Ionian hall empty of people, the hearth down to red embers, the carved stool with the silent phorminx leaning against it in a pool of lamplight; through the open doorway the star-white night sky over a dark calm sea. Leave the upper third of the image calm and uncluttered for a large ornamented text panel. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---
END OF ISSUE 3 PROMPTS. When all art through pg32 exists: send the art+refs zip and say "build issue 3." Issue 3 builds to its own separate issue-03.pdf.
