# ISSUE 6 — PANEL PROMPTS (pages 1–32) · self-contained format
Per master-plan v0.5.4. Same rules as Issues 1–5. Guard clause on earthly scenes; divine clause on god scenes; twilight palette on frame panels. Ref-births marked REF-BIRTH (crops are verification-side pipeline steps, committed to refs/ before dependent panels generate). Panels are TEXTLESS. Restraint clauses are load-bearing on pgs 8, 13, 23, 24.
Reusable refs: singer, neleid-prince, muse, agamemnon, menelaus, odysseus, clytemnestra, calchas, achilles, patroclus, palamedes, helen, paris, priam, hector, antenor, nestor.

> **TWO-LLM WORKFLOW (standing instructions for the image-generation session):**
> 1. You have READ access to this repository. For each panel below, fetch every file on its ATTACH line from the repo's `refs/` folder (same branch as this prompts file) and attach those images to the generation request together with the PROMPT text, used verbatim.
> 2. Generate at the stated aspect ratio. Output must be completely TEXTLESS.
> 3. You cannot commit. Hand the finished image to the human operator under its exact panel filename (iNN-pgNN-pnN.png); the operator relays it to the verification side (Claude), which reviews it against prompt and refs and commits it to `issues/issue-NN/art/`.
> 4. Panels marked REF-BIRTH create a new reference face: after that panel passes verification, the verification side crops and commits the new ref to `refs/`. Do NOT generate any later panel that ATTACHes that ref until the ref file exists in the repo.


### i06-pg01-pn1.png — full page 3:4 — COVER — FIRST SIGHT OF TROY
ATTACH: none
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cover composition: the bows and stems of the Greek fleet in the foreground on a bright dawn sea — and across the strait on the horizon, small and golden and terrible, Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond; gulls; leave the upper quarter of sky calm for title lettering. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg02-pn1.png — wide 16:9 — FRAME — THE SILENT HALL
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot of an early Iron Age Ionian megaron hall at evening: timber columns, central hearth fire, hanging oil lamps, noble audience seated on benches, dark doorway open to a starry Aegean night: the hall utterly silent as an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre is led in; a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face on the high seat, subdued; even the children still. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg02-pn2.png — standard 4:3 — FRAME — DO NOT SPARE US
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is subdued (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face speaking low, jaw set, firelight on a face braced for grief. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg02-pn3.png — standard 4:3 — FRAME — WHERE THE PRIEST STOPS WALKING
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the night's map laid out (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre with one hand tracing a slow line through the air, mapping the night's long road. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg03-pn1.png — standard 4:3 — THE INVOCATION
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/muse.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is 'face lifted (refs/singer.png) - reproduce that face, hair and apparent age exactly; the second attached image is the Muse above.' (refs/muse.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre with sightless face lifted, fingers on the strings; a Muse: luminous woman of unearthly beauty, dark hair crowned with laurel, flowing pale gold robe, softly radiant against darkness luminous in the hearth-smoke. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg03-pn2.png — standard 4:3 — GOLD RISES
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Transitional shot: the vision-gold flooding the sepia hall. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg03-pn3.png — wide 16:9 — THE DEAD SAILS
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide morning shot of the bay of Aulis in Boeotia: a wide shallow strait crowded with beached black ships, a sacred spring under one great plane tree beside stone altars, low scrub hills around the water: the armada dressed for sailing, banners out — and every sail on a thousand masts hanging DEAD SLACK in glassy air; the wrongness palpable. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg04-pn1.png — standard 4:3 — THE SHOT
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is loosing at the hind in the grove-margin (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Flash-toned hunt shot at the oak-grove margin: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face at full draw loosing an arrow; mid-leap between the trees, struck clean, a white-flanked HIND falling; huntsmen behind. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg04-pn2.png — standard 4:3 — THE BOAST
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is over the fallen deer, arms spread, the boast leaving him (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face standing over the fallen hind, flushed with triumph, arms spread wide, head thrown back mid-boast; huntsmen beginning to grin. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg04-pn3.png — standard 4:3 — THE GROVE GOES STILL
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Chilling shot: the grove around the hunting party — every leaf motionless, the light gone subtly wrong, the huntsmen's smiles dying one by one on their faces; the fallen hind white at the frame's base. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg05-pn1.png — wide 16:9 — THE SEA OF POURED METAL
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide oppressive shot of the bay of Aulis in Boeotia: a wide shallow strait crowded with beached black ships, a sacred spring under one great plane tree beside stone altars, low scrub hills around the water weeks on: the bay glass-flat under white haze, a thousand slack sails, heat-shimmer, listless men poling a water-barge between hulls. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg05-pn2.png — standard 4:3 — THE CAMP FRAYS
ATTACH (fetch from repo refs/ and attach to the generation): refs/odysseus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is watching the slack sails, then the grove, and understanding (refs/odysseus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Camp shot: a fistfight over a water-skin being pulled apart; sick men in hut-shade; arguing kings in a knot; and in the foreground a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt looking from the dead sails toward the distant grove, understanding arriving in the grey eyes. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg05-pn3.png — standard 4:3 — THE LOCKED DOOR
ATTACH (fetch from repo refs/ and attach to the generation): refs/calchas.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is apart at the tide-line, eyes on the grove (refs/calchas.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Solitary shot: Calchas the seer, gaunt middle-aged diviner, shaved head bound with a white fillet, dark feather-trimmed mantle, staring pale-grey eyes standing apart at the tide-line, feather mantle limp in the dead air, pale eyes fixed on the grove, his gaunt face a locked door. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg06-pn1.png — standard 4:3 — THE PRICE NAMED
ATTACH (fetch from repo refs/ and attach to the generation): refs/calchas.png, refs/agamemnon.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the seer speaking with shut eyes (refs/calchas.png) - reproduce that face, hair and apparent age exactly; the second attached image is the king whitening (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Torchlit council-tent shot: Calchas the seer, gaunt middle-aged diviner, shaved head bound with a white fillet, dark feather-trimmed mantle, staring pale-grey eyes speaking with his eyes shut, both hands open before him; across the tent a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face whitening, the ring of kings frozen between them. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg06-pn2.png — standard 4:3 — I UNSAY THE WAR
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is on his feet, the scepter fallen (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Explosive shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face surging to his feet, the gold scepter clattering to the carpets, one arm sweeping in absolute refusal; torch-flames bending. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg06-pn3.png — standard 4:3 — THE MACHINE DOES NOT DISBAND
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png, refs/menelaus.png, refs/odysseus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: the ring of eyes closing on him.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Trap shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face standing amid the seated ring — a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak's naked need, a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt's watchfulness, the silent faces of kings on every side — the oath he built visibly closing on its builder. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg07-pn1.png — standard 4:3 — WEDDING CLOTHES (births IPHIGENIA: crop refs/iphigenia.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/clytemnestra.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Bright terrible shot on the Mycenae road: a garlanded mule-cart traveling party — a tall proud dark-haired queen, strong handsome face with watchful eyes, deep red and gold Mycenaean dress radiant with pride, and beside her Iphigenia, eldest daughter of Agamemnon, girl of about fourteen, dark-gold hair, clear brave young face, white and saffron dress in wedding saffron, laughing at something her mother has said; escort riders; morning light. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/iphigenia.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i06-pg07-pn2.png — standard 4:3 — MY NAME
ATTACH (fetch from repo refs/ and attach to the generation): refs/achilles.png, refs/patroclus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the white-then-terrible rage (refs/achilles.png) - reproduce that face, hair and apparent age exactly; the second attached image is the hand hard on his arm (refs/patroclus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Rage shot in the camp lanes: Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build having just learned, the beautiful face gone white and then terrible, half-turned toward the command tents; Patroclus son of Menoetius, gentle strong young warrior slightly older than Achilles, short dark hair, kind steady face, plain corslet's hand clamped hard on his sword-arm, holding him by main strength and love. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg07-pn3.png — standard 4:3 — THE GIRL DECIDES
ATTACH (fetch from repo refs/ and attach to the generation): refs/iphigenia.png, refs/agamemnon.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

'after the weeping: still, straight, looking at the fleet.'

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet pivotal shot in the king's tent: Iphigenia, eldest daughter of Agamemnon, girl of about fourteen, dark-gold hair, clear brave young face, white and saffron dress, the storm of weeping past, standing very straight and still, looking out through the tent door at the thousand slack sails; behind her, unable to look at her, a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face with his face ruined. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg08-pn1.png — full page 3:4 — SPLASH — THE ALTAR AND THE HIND (births ARTEMIS: crop refs/artemis.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/iphigenia.png, refs/calchas.png, refs/agamemnon.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

map each: the girl unbound and chin high; the averted knife-bearer; the king with covered head; the goddess breaking over all.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page dawn tableau at a stone altar at the grove's edge, the army ranked in dead silence down the shore: Iphigenia, eldest daughter of Agamemnon, girl of about fourteen, dark-gold hair, clear brave young face, white and saffron dress standing AT the altar unbound, chin high, saffron dress and wind; Calchas the seer, gaunt middle-aged diviner, shaved head bound with a white fillet, dark feather-trimmed mantle, staring pale-grey eyes beside her with the bronze knife lifted and his face utterly averted; a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face nearby with his purple cloak pulled over his head in the ancient gesture of unwatchable grief; and breaking over the scene from above like a wave of silver light, half-manifest with arms outstretched, Artemis goddess of the wild, slim swift huntress goddess, dark hair bound back, short silver-white hunting dress, great silver bow, cool remote beautiful face — beneath the falling knife, materializing on the altar stone in coiling mist, a white HIND, while the girl's form, gone faintly translucent and radiant, is already lifting away upward into the goddess's light. No blood anywhere. Leave calm space top and bottom for ornate caption plates. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/artemis.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

---

### i06-pg09-pn1.png — standard 4:3 — THE WIND COMES
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Release shot: the altar-mist still hanging — and down the whole bay beyond it, a thousand slack sails FILLING at once, banners cracking taut, water riffling dark; the first roar beginning. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg09-pn2.png — standard 4:3 — THE WOMAN ON THE SHORE
ATTACH (fetch from repo refs/ and attach to the generation): refs/clytemnestra.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is alone on the emptying shore, a bride's garland in her hand (refs/clytemnestra.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Devastating quiet shot: the embarkation's wild joy far in the background — and alone in the foreground on the emptying shore, a tall proud dark-haired queen, strong handsome face with watchful eyes, deep red and gold Mycenaean dress, motionless, a bride's garland hanging from one hand, wedding flowers scattered at her feet, watching the fleet go with a face going to stone. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg09-pn3.png — standard 4:3 — HE DOES NOT LOOK BACK
ATTACH (fetch from repo refs/ and attach to the generation): refs/agamemnon.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is at the flagship's stern, the shore dwindling (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Stern-deck shot: a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face standing at the flagship's stern rail facing forward, jaw locked, deliberately not turning; behind and below him the shore — and one small figure on it — dwindling in the wake. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg10-pn1.png — standard 4:3 — THE FEAST AT TENEDOS (births PHILOCTETES: crop refs/philoctetes.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Feast shot on an island beach, the fleet at anchor beyond: captains at a victory feast — prominent among them Philoctetes of Malis, rangy weathered master archer, shaggy dark hair and beard, plain hunting dress, bearing the great man-tall horn bow of Heracles, laughing, the great man-tall horn bow lying across his knees like a sleeping animal. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/philoctetes.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i06-pg10-pn2.png — standard 4:3 — THE BITE
ATTACH (fetch from repo refs/ and attach to the generation): refs/philoctetes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is struck at the foot at the spring-stones (refs/philoctetes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Sudden shot at the sacred spring's mossy stones: a WATER-SNAKE striking the bare ankle of Philoctetes of Malis, rangy weathered master archer, shaggy dark hair and beard, plain hunting dress, bearing the great man-tall horn bow of Heracles, his body arching in the first cry, wine-cup flying; feasters surging up in the background. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg10-pn3.png — standard 4:3 — THE CRYING ANCHORAGE
ATTACH (fetch from repo refs/ and attach to the generation): refs/philoctetes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the wound black; the cries; men covering their ears (refs/philoctetes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Grim shipboard shot days later: Philoctetes of Malis, rangy weathered master archer, shaggy dark hair and beard, plain hunting dress, bearing the great man-tall horn bow of Heracles half-delirious against the mast, the bound foot swollen and blackened; along the rowing benches men flinching and covering their ears; on a neighboring ship, kings conferring darkly across the water. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg11-pn1.png — standard 4:3 — THE COLD COUNSEL
ATTACH (fetch from repo refs/ and attach to the generation): refs/odysseus.png, refs/agamemnon.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the counsel given (refs/odysseus.png) - reproduce that face, hair and apparent age exactly; the second attached image is the nod (refs/agamemnon.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Council shot: a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt speaking the cold necessity with level eyes and open hands; a tall imperious king, dense black beard, gold-studded corslet and deep purple cloak, gold scepter, heavy-browed proud commanding face nodding once; the other kings looking anywhere else. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg11-pn2.png — standard 4:3 — LIKE THIEVES OF A WORLD
ATTACH (fetch from repo refs/ and attach to the generation): refs/philoctetes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is asleep under the cave-brow; the boats pulling away (refs/philoctetes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Shameful quiet shot on a wild shore: Philoctetes of Malis, rangy weathered master archer, shaggy dark hair and beard, plain hunting dress, bearing the great man-tall horn bow of Heracles deep in exhausted sleep beneath a cave-brow, the great bow beside him, supplies stacked neatly at his feet — and out on the water, the ships' boats pulling away with muffled oars. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg11-pn3.png — standard 4:3 — LEMNOS
ATTACH (fetch from repo refs/ and attach to the generation): refs/philoctetes.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is small on the empty shore, fist raised, the bow black against the sky (refs/philoctetes.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Desolate wide-feeling shot: Philoctetes of Malis, rangy weathered master archer, shaggy dark hair and beard, plain hunting dress, bearing the great man-tall horn bow of Heracles tiny on the empty volcanic shore, on his knees with one fist raised at the departing sails on the horizon; beside him, planted upright in the sand, the great bow of Heracles black against a cold sky. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg12-pn1.png — wide 16:9 — TROY, REAL AT LAST
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dawn shot from the sea: the whole fleet standing in toward a long pale beach — and beyond the windy plain, Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond at last, walls manned, spear-points glittering tiny along the ramparts. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg12-pn2.png — standard 4:3 — NO SHIP BEACHES
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tense shipboard shot along a crowded gunwale: armored warriors packed to leap — and not leaping; eyes sliding sideways man to man; hands adjusting perfectly adjusted straps; the beach empty and waiting beyond the bow. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg12-pn3.png — standard 4:3 — SOMEONE MUST BE THE DOOR
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Character shot at a ship's bow: a YOUNG LORD in plain good armor — square-jawed, newly-wed young face — looking from the stalled fleet down the line to the empty beach, and visibly setting his jaw; his hand closing on the rail. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg13-pn1.png — standard 4:3 — THE LEAP
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Heroic shot: the young lord vaulting the bow into the surf, first of a hundred thousand, spear high, spray sheeting — one man running up an empty enemy beach, his footprints the first marks of the war. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg13-pn2.png — standard 4:3 — TROY ANSWERS WITH ITS BEST
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is coming down the dune alone to meet him (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Closing-distance shot: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak coming down the dune-face alone at a run to meet the lone runner — no other Trojan moving on the crest — the two figures converging on empty sand. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg13-pn3.png — standard 4:3 — FIRST DEAD, FIRST SALUTED
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the salute over the fallen, before the roaring fleet (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Grave shot, no gore: the young lord fallen on the wet sand with dignity, face to the sky, spear beside his open hand; over him Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak standing — raising his own spear NOT in triumph but vertically, in salute, toward the incoming roaring fleet; the landing crashing ashore in the background. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg14-pn1.png — wide 16:9 — THE UNWOUNDABLE
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide beachhead chaos shot, restrained: the landing storm of hulls and spears stalling around one GIANT figure wading through it — a huge warrior white-skinned as sea-foam, bronze spears SHATTERING on his bare hide like reeds on rock; Greeks recoiling around him. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg14-pn2.png — standard 4:3 — WEIGHT AND WILL
ATTACH (fetch from repo refs/ and attach to the generation): refs/achilles.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is bearing the giant down into the surf by main force (refs/achilles.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Titanic wrestling shot in the surf: Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build, spear discarded, locked chest to chest with the sea-white giant, bearing him down into the churning shallows by main strength and fury, the giant's arms flailing at water; no blood — force against force. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg14-pn3.png — standard 4:3 — LAST THROUGH THE GATE
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is rearguard to his own retreat (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Rout shot before the walls: Trojans streaming back through the great gate of Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond — and last of all, walking backward with shield up, covering his own men, Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak; the gate-leaves closing past him. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg15-pn1.png — standard 4:3 — FRAME — DID HE BELIEVE IT?
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the question about the first man (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face asking with real urgency, leaning into the ember-light. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg15-pn2.png — standard 4:3 — FRAME — A LITTLE SILVER OF YOUR OWN
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is the answer about the other kind of glory (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre answering with quiet intensity, one hand closing as if around a small coin. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg15-pn3.png — standard 4:3 — FRAME — THE LAW MUST BE SATISFIED
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is gathering the thread toward the embassy (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre straightening, the vision-gold rising again at the frame edges. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg16-pn1.png — wide 16:9 — UNDER THE HERALD'S STAFF
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/odysseus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each entering the enemy gate unarmed.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot at the great gate of Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond swung open: a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak and a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt, unarmed, walking in behind a HERALD's raised staff between dense spear-lined streets; hate and awe on the packed walls above. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg16-pn2.png — standard 4:3 — ANTENOR'S HEARTH
ATTACH (fetch from repo refs/ and attach to the generation): refs/antenor.png, refs/menelaus.png, refs/odysseus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each at the guest-meal.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Warm interior shot: Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face receiving the two envoys at his own hearth, his household serving the guest-meal with full honor; the old man's shrewd honest face grave with the weight of the law he is keeping. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg16-pn3.png — standard 4:3 — MEASURING THE CITY
ATTACH (fetch from repo refs/ and attach to the generation): refs/odysseus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is at the guest-chamber window all night, filing the streets away (refs/odysseus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Night shot: a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt at the guest-chamber window, chin on his fist, looking out over torchlit Troy — streets, gates, wall-walks — the grey eyes moving methodically, memorizing; the sleeping city unaware of being measured. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg17-pn1.png — standard 4:3 — THE PLAIN DEMAND
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/priam.png, refs/paris.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each in the assembly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Assembly shot in the gate-court of Troy: a sturdy war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak speaking his short iron demand before the packed court; King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face grave on the dais; a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound with a thin gold band, rich embroidered Anatolian princely tunic, graceful bearing among his young faction, jaw set, arms folded; the crowd loud around. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg17-pn2.png — standard 4:3 — WORDS LIKE WINTER SNOW
ATTACH (fetch from repo refs/ and attach to the generation): refs/odysseus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is stock-still, staff planted, eyes down — and the voice (refs/odysseus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The speech shot: a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt standing oddly stock-still, herald's staff planted, eyes down at the ground — while the entire hostile assembly around him leans involuntarily inward, caught; even hard faces gone attentive; the voice made visible in the composition's pull. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg17-pn3.png — standard 4:3 — THE BOUGHT VOICE
ATTACH (fetch from repo refs/ and attach to the generation): refs/antenor.png, refs/priam.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference images exactly: the first attached image is the shielding (refs/antenor.png) - reproduce that face, hair and apparent age exactly; the second attached image is the staff striking for order (refs/priam.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Uproar shot: a heavy GOLD-HUNG NOBLE on his feet bellowing with arm flung at the envoys, new gold thick on his wrists; the court surging; Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face and his grown sons physically interposing themselves around the two Greeks; King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face's staff caught mid-strike on the dais stone. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg18-pn1.png — standard 4:3 — REFUSED, UNTOUCHED
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/odysseus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each walking out between the spear-lines.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Departure shot: the two envoys walking back down from the gate between spear-lines, unharmed and refused, faces set; behind them the great gate-leaves beginning to boom shut. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg18-pn2.png — standard 4:3 — THE CROSSROADS KING
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is alone at the parapet after the assembly, Ida beyond (refs/priam.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Solitary shot: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face alone at the wall parapet in late light, old hands flat on the stone, the crowd-noise gone; beyond him, serene and indifferent, Mount Ida. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg18-pn3.png — wide 16:9 — THE PLAIN BETWEEN
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dusk shot: the torchlit walls of Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond on one side, the first palisade stakes of the Achaean beach camp before Troy: a thousand ships drawn up stern-first in ranks along the shore, huts of timber and hide between them, a palisade and ditch landward, the windy plain and the walls of Troy beyond rising on the other, and between them the empty windy plain going dark — the war's whole geography in one image. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg19-pn1.png — full page 3:4 — SPLASH — THE NINE YEARS
ATTACH: none
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page composition of the turning years: at center, facing each other across the windy plain, the beach camp and the walls of Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond — and wheeling around and through the scene in curved seasonal bands: palisade timbers rising new and weathering silver; raid-fleets launching south and returning laden; funeral pyres and funeral games on the shore; snow on the hut-roofs, then poppies on the plain; camp boys growing into spearmen band by band — while through every band the walls of Troy stand identical, serene, closed. Leave calm space top and bottom for ornate caption plates. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg20-pn1.png — standard 4:3 — LYRNESSUS (births BRISEIS: crop refs/briseis.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Aftermath shot in a taken Anatolian town, smoke drifting, restraint absolute: among captives being led out, Briseis of Lyrnessus, gentle dark-haired young noblewoman, soft grieving dignified face, simple fine Anatolian dress — walking unbowed through the ruin of her world, eyes forward, grief carried like a queen's train. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/briseis.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i06-pg20-pn2.png — standard 4:3 — THE SURPRISE OF GENTLENESS
ATTACH (fetch from repo refs/ and attach to the generation): refs/briseis.png, refs/achilles.png, refs/patroclus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each in the Myrmidon camp.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet camp shot: Briseis of Lyrnessus, gentle dark-haired young noblewoman, soft grieving dignified face, simple fine Anatolian dress standing before Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build — and the terrible young man treating the grieving woman with grave, careful, unfeigned courtesy, offering a seat by the fire with his own hand; Patroclus son of Menoetius, gentle strong young warrior slightly older than Achilles, short dark hair, kind steady face, plain corslet near, kind-faced. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg20-pn3.png — standard 4:3 — THE PROMISE
ATTACH (fetch from repo refs/ and attach to the generation): refs/patroclus.png, refs/briseis.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each apart at dusk.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dusk two-shot apart from the fires: Patroclus son of Menoetius, gentle strong young warrior slightly older than Achilles, short dark hair, kind steady face, plain corslet speaking gently and earnestly to Briseis of Lyrnessus, gentle dark-haired young noblewoman, soft grieving dignified face, simple fine Anatolian dress, his open hand making a quiet vow; her face lifting a fraction for the first time, the first grain of a future taking hold. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg21-pn1.png — standard 4:3 — THEBE TAKEN (births CHRYSEIS: crop refs/chryseis.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Citadel-aftermath shot in a second taken town: Myrmidons in the upper court; among the captives, Chryseis daughter of the priest of Apollo, slight auburn-haired young woman, delicate face, white priestly-household dress with a laurel band — slight, out of place, a visitor swept up by the day; her laurel band askew. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/chryseis.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i06-pg21-pn2.png — standard 4:3 — THE HONOR OF EETION
ATTACH (fetch from repo refs/ and attach to the generation): refs/achilles.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is ordering the fallen king burned in his armor; elms planted (refs/achilles.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Strange-honor shot: Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build standing over a fallen OLD KING in fine armor — directing Myrmidons who are building a pyre and bearing the body WITH its armor, nothing stripped; to one side, men planting young elm saplings in a ring around a rising mound. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg21-pn3.png — standard 4:3 — THE NEWS COMES HOME (births ANDROMACHE: crop refs/andromache.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Grief shot in a Trojan chamber: Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown receiving the news, her hand finding the wall, the world tilting; and Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak coming to her fast across the room, catching her by the shoulders, his own face breaking for her. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/andromache.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

---

### i06-pg22-pn1.png — standard 4:3 — THE FIG ORCHARD
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Night-raid shot in a royal orchard below the walls: Greek raiders moving between fig trees — and a YOUNG TROJAN PRINCE of seventeen, caught alone by lamplight with an armful of cut fig-shoots, seized almost gently, too astonished to struggle. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg22-pn2.png — standard 4:3 — SOLD FOR A SILVER BOWL
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Slave-market shot on an island quay: the young prince standing stunned among traded goods; coins being counted into a Greek raider's palm beside a fine embossed SILVER BOWL changing hands; ships and commerce indifferent around him. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg22-pn3.png — close-up 4:3 — THE TWELFTH DAY, WAITING
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Portent close-up: the boy-prince's stunned young face filling the frame — and behind it, faint as a watermark across the whole panel, the ghost-image of a RIVER IN FLOOD, white water and tumbled trees. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg23-pn1.png — standard 4:3 — THE BOY AT THE FOUNTAIN
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Deceptive-peace shot at evening: a stone fountain-house outside the walls; a laughing BOY of perhaps thirteen in princely Anatolian dress exercising two beautiful horses in the dusk, unguarded; long safe-feeling shadows. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg23-pn2.png — standard 4:3 — THE RUN FOR SANCTUARY
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Chase shot, terror without wounds: the boy flat on his horse's neck at full desperate stretch, making for a small shrine on its knoll ahead — its steps, its rough stone, the god's emblem over the door; behind him on the darkening ground, long and gaining, a runner's shadow. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg23-pn3.png — standard 4:3 — AFTERMATH AT THE SHRINE
ATTACH: none
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Aftermath-only shot, full dark: the shrine steps; a riderless horse standing with hanging head; within the precinct doorway, torchlight and the moving shadows of Trojans lifting something with terrible care; and above the lintel, catching the torchlight, the god's sun-emblem — watching. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg24-pn1.png — standard 4:3 — THE FISHING PARTY
ATTACH (fetch from repo refs/ and attach to the generation): refs/palamedes.png, refs/odysseus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each in the skiff, faces pleasant.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Bright sea shot: a small fishing skiff on glittering water off the camp; Palamedes of Nauplia, elegant keen-faced young lord, neat dark beard, precisely ordered dress, quick inventive eyes hauling a net, at ease, laughing at something — and seated in the stern behind him, faces pleasant, a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt and a keen dark-bearded young war-king (Diomedes). Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg24-pn2.png — wide 16:9 — THE EMPTY BRIGHT WATER
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The refused deed: a wide empty shot of the bright sea from the distant beach — the skiff far and small, and in it now only TWO figures where there were three; gulls turning above the water; nothing else shown, nothing else needed. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg24-pn3.png — standard 4:3 — AN ORDINARY FACE
ATTACH (fetch from repo refs/ and attach to the generation): refs/odysseus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is walking away up the sand alone; the mound rising far down the shore (refs/odysseus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cold shot at evening: the beached skiff; a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt walking away up the sand alone, his face absolutely ordinary; and far down the shore, small, a grave-mound being raised with full and proper honors. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg25-pn1.png — standard 4:3 — THE ARRANGED SEEING
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png, refs/achilles.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each: she at the parapet above; he on the plain below; gold shimmer between.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dusk shot at the wall above the great gate: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem at the torchlit parapet — and far below on the darkening plain, drawn there, Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build looking up; between and about them both, faint gold in the air, the shimmer of divine arrangement. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg25-pn2.png — wide 16:9 — THE PRIZE AND THE PRICE
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png, refs/achilles.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each regarding the other across the distance.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide charged shot holding both: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem above on the wall and Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build below on the plain, regarding one another across the impossible distance in a goddess-made quiet — the world's beauty and the world's doom, each studying what the other has cost. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg25-pn3.png — standard 4:3 — THE LAMP ON THE WALL
ATTACH (fetch from repo refs/ and attach to the generation): refs/achilles.png, refs/patroclus.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each walking back in the dark.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Night shot: Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build walking back toward the camp fires in the dark, Patroclus son of Menoetius, gentle strong young warrior slightly older than Achilles, short dark hair, kind steady face, plain corslet fallen in wordlessly beside him; behind them the black walls — and at the parapet, one small lamp burning. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg26-pn1.png — wide 16:9 — THE NINTH-YEAR BREAK
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide mutiny shot: thousands of soldiers surging away from the siege-lines toward the ships — gear flung down, hulls being shoved at the water, officers swept aside like posts in a flood; the war dissolving in one afternoon. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg26-pn2.png — standard 4:3 — ONE MAN IN THE ROAD
ATTACH (fetch from repo refs/ and attach to the generation): refs/achilles.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is alone, unarmed, planted; the flood piling against his stillness (refs/achilles.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Iconic shot: Achilles son of Peleus and Thetis, the most beautiful and terrible of heroes, young and beardless, long red-gold hair, blazing sea-grey eyes, swift perfect build — alone, unarmed, feet planted — standing in the direct path of the routing thousands; the human flood piling up and stalling against his single blazing stillness like water against a stone; his arm flung out, ordering them BACK. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg26-pn3.png — standard 4:3 — THE LINES RE-FORM
ATTACH (fetch from repo refs/ and attach to the generation): refs/odysseus.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is watching from a distance, unreadable; a nine-scratch tally on a hull (refs/odysseus.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dusk shot: the siege-lines re-forming, sullen but re-formed; in the foreground a compact powerfully built hero, broad-chested but shorter than the great kings, russet-brown hair and short beard, keen grey observant eyes, plain sturdy traveler's wool cloak over a simple kilt watching the distant figure of Achilles with an unreadable expression; beside him on a ship's hull, a tally of NINE deep scratches, weathered. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg27-pn1.png — standard 4:3 — HECTOR SPENDS HIMSELF
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is everywhere at once — walls, granary, drill-yard (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Montage-feel shot inside Troy: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak in three vignettes of one panel — directing wall repairs, tallying at a granary door, correcting a boy-spearman's grip in the drill-yard — thinner than nine years ago, unbroken. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg27-pn2.png — standard 4:3 — THE SMALL HOURS
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/andromache.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each by the single lamp with the infant.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tender night shot: by a single lamp, Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak asleep sitting upright with a swaddled INFANT on his chest, one great hand covering the child entire; Andromache, young noblewoman of Thebe, wife of Hector, warm brave gentle face, dark hair under a light veil, deep blue Anatolian gown keeping the lamp, watching them both, memorizing. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg27-pn3.png — close-up 4:3 — THE KNOWLEDGE, HELD
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is watching the enemy camp wake; no hatred — measurement, endurance, knowledge (refs/hector.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dawn close shot on the bastion: the face of Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak watching the enemy camp wake across the plain, ten thousand smoke-threads rising in his eyes' reflection — no hatred in the face; only measurement, endurance, and, held deep where his city cannot see it, knowledge. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg28-pn1.png — wide 16:9 — THE ALLIES STREAM IN
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide procession shot within the walls: allied contingent standards streaming toward the citadel — Thracian horse-lords on white teams, Paeonian archers, Carians decked in gold, Phrygians, Maeonians, and a Mysian column under a tawny young commander; the city's streets lined and cheering. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg28-pn2.png — standard 4:3 — SARPEDON AND GLAUCUS (births SARPEDON & GLAUCUS: crop refs/sarpedon.png, refs/glaucus.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Formal honor shot at the citadel steps: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak clasping wrists as an equal with Sarpedon king of Lycia, son of Zeus, tall grave dark-bearded warrior-king of great dignity, silver-studded armor with a lion device, grave and kingly; at Sarpedon's shoulder, keen Glaucus of Lycia, keen loyal young war-captain, short brown beard, Lycian armor with a golden double-spiral device; Lycian standards behind. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/sarpedon.png, refs/glaucus.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i06-pg28-pn3.png — standard 4:3 — TWO HONORABLE MEN
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/sarpedon.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

map each over the sand-table.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. War-council shot: Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak and Sarpedon king of Lycia, son of Zeus, tall grave dark-bearded warrior-king of great dignity, silver-studded armor with a lion device bent together over a sand-table of the Troad, allied kings ringed around; two grave honorable faces bearing a war neither made. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg29-pn1.png — wide 16:9, letterbox — THE PRIEST ON THE SHORE (births CHRYSES: crop refs/chryses.png)
ATTACH: none
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Letterbox dusk shot on the long beach: the camp's fires kindling all down the shore — and walking up the tide-line toward them, alone and small against the wall of beached ships, Chryses, aged priest of Apollo, long white hair and beard, white robes, a gold staff wound with the god's scarlet fillets, the gold staff with its scarlet fillets in one hand; behind him two servants bearing a chest of ransom. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
REF-BIRTH: refs/chryses.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i06-pg29-pn2.png — close-up 4:3 — THE FILLETS TREMBLE
ATTACH (fetch from repo refs/ and attach to the generation): refs/chryses.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is dignity, dread; the firelit camp ahead (refs/chryses.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot: the aged face of Chryses, aged priest of Apollo, long white hair and beard, white robes, a gold staff wound with the god's scarlet fillets — dignity, dread, resolve — firelight beginning to touch it; the scarlet fillets on the raised staff trembling only slightly in the sea wind. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg29-pn3.png — standard 4:3 — AT THE THRESHOLD
ATTACH (fetch from repo refs/ and attach to the generation): refs/chryses.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is stopped at the firelight's edge, staff raised toward the shadowed kings (refs/chryses.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The held threshold: Chryses, aged priest of Apollo, long white hair and beard, white robes, a gold staff wound with the god's scarlet fillets stopped at the very edge of the firelight before the assembly-ground, staff and fillets raised high in supplication toward a half-circle of shadowed enthroned KINGS beyond the flames; everything about to begin. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg30-pn1.png — standard 4:3 — FRAME — THE VERY SONG?
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is half-risen, electric (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face half-risen from the high seat, the question breathless. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg30-pn2.png — standard 4:3 — FRAME — FIT TO HEAR IT
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is something like joy, the first in six nights (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre, and on the lined blind face, for the first time in six nights, something unmistakably like joy. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg30-pn3.png — standard 4:3 — FRAME — THE PHORMINX HELD SACRED
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is rising, the instrument held like a holy thing (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre rising, holding the phorminx now in both hands like a sacred vessel, the ember-light gone gold around him. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg31-pn1.png — wide 16:9 — FRAME — MURMURS OF ANTICIPATION
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH-REVIEW: the identity mapping could not be derived automatically. The original shorthand is preserved verbatim inside the block below - rewrite it as an explicit positional instruction ("the first attached image is ...") before generating.
PROMPT:
```text
Aspect ratio 16:9 wide landscape panel.

map each in the emptying hall.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot: the hall emptying in eager murmurs, fathers talking low to children on their shoulders; an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre standing by the embers; a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face lingering last at the door. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg31-pn2.png — standard 4:3 — FRAME — HAS ANYONE BEEN HAPPY?
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is last at the door, looking back with the question (refs/neleid-prince.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face paused in the dark doorway, looking back, the question asked simply, like a child's. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
### i06-pg31-pn3.png — standard 4:3 — FRAME — THE WHOLE CYCLE, IN ONE ANSWER
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
PROMPT:
```text
Aspect ratio 4:3 landscape (standard comic panel).

Match the attached reference image exactly: it is alone by the embers, answering the empty hall (refs/singer.png) - reproduce that face, hair and apparent age exactly.

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Close shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre alone by the embers, blind face lifted, answering the boy and the empty hall and the night all at once; the phorminx cradled. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---

### i06-pg32-pn1.png — full page 3:4 — THE GNOME PAGE
ATTACH: none
PROMPT:
```text
Aspect ratio 3:4 tall portrait (full page).

Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Full-page quiet composition: the Iron Age Ionian hall empty of people, the hearth down to red embers, the carved stool with the silent phorminx leaning against it in a pool of lamplight; through the open doorway the star-white night over a dark calm sea — and far out on the black water, one small sail catching starlight. Leave the upper third calm and uncluttered for a large ornamented text panel. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
```
---
END OF ISSUE 6 PROMPTS. When all art exists: send the art+refs zip and say "build issue 6." Builds to its own separate issue-06.pdf.
