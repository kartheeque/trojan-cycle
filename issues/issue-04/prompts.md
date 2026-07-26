# ISSUE 4 — PANEL PROMPTS (pages 1–32) · self-contained format
Same rules as Issues 1–3. Guard clause on earthly scenes; divine radiance clause on god scenes; twilight palette on frame panels. Ref-births marked REF-BIRTH (crops are verification-side pipeline steps, committed to refs/ before dependent panels generate). Panels are TEXTLESS.
Reusable refs: singer, neleid-prince, muse, zeus, hera, athena, aphrodite, hermes, paris, agelaus, priam, hecuba, hector, cassandra, antenor, helen, menelaus, castor, polydeuces, tyndareus.

> **TWO-LLM WORKFLOW (standing instructions for the image-generation session):**
> 1. You have READ access to this repository. For each panel below, fetch every file on its ATTACH line from the repo's `refs/` folder (same branch as this prompts file) and attach those images to the generation request together with the PROMPT text, used verbatim.
> 2. Generate at the stated aspect ratio. Output must be completely TEXTLESS.
> 3. You cannot commit. Hand the finished image to the human operator under its exact panel filename (iNN-pgNN-pnN.png); the operator relays it to the verification side (Claude), which reviews it against prompt and refs and commits it to `issues/issue-NN/art/`.
> 4. Panels marked REF-BIRTH create a new reference face: after that panel passes verification, the verification side crops and commits the new ref to `refs/`. Do NOT generate any later panel that ATTACHes that ref until the ref file exists in the repo.


### i04-pg01-pn1.png — full page 3:4 — COVER — THE APPLE OFFERED
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'the herdsman lit by divine radiance.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Cover composition, night on the mountain: in the foreground a god's open radiant palm offering a gleaming GOLDEN APPLE toward a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing, whose beautiful face is lit with wonder and terror; behind the light three towering veiled radiant female figures; dark pines and firelight; leave the upper quarter calm for title lettering. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg02-pn1.png — wide 16:9 — FRAME — FATHERS AND CHILDREN
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH LINE: map each.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot of an early Iron Age Ionian megaron hall at evening: timber columns, central hearth fire, hanging oil lamps, noble audience seated on benches, dark doorway open to a starry Aegean night: the fullest crowd yet, grey heads and children on shoulders among the listeners; an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre settling on his stool; a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face waiting on the high seat. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg02-pn2.png — standard 4:3 — FRAME — HALF AFRAID
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
MATCH LINE: 'quiet, almost reluctant.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face quiet and almost reluctant, hands loosely clasped, firelight on a sober young face. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg02-pn3.png — standard 4:3 — FRAME — RIGHT TO BE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'grave assent.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre nodding grave assent, both hands still on the silent phorminx. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg03-pn1.png — standard 4:3 — THE INVOCATION
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/muse.png
MATCH LINE: 'the bard's face lifted; the Muse faint above.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre with blind face lifted, fingers touching the strings; a Muse: luminous woman of unearthly beauty, dark hair crowned with laurel, flowing pale gold robe, softly radiant against darkness faint and luminous in the hearth-smoke above. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg03-pn2.png — standard 4:3 — GOLD RISES
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Transitional shot: the sepia hall flooding upward with warm gold vision-light from the hearth. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg03-pn3.png — wide 16:9 — BACK TO THE FIRE
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'the herdsman by his fire as the lights arrive.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide night shot of Mount Ida above Troy: high pine forests and open upland pastures, cold streams, herds of cattle, the Trojan plain and the sea far below: the herdsman's small fire in a clearing, a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing risen to his feet beside it, and entering the clearing four figures of divine golden light, their radiance washing the pines. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg04-pn1.png — standard 4:3 — TERROR
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'fallen back against a pine, arm across his eyes.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing fallen back against a pine trunk, one arm flung across his eyes against overwhelming radiance from off-panel; around him his cattle KNEELING on the grass, not fleeing. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg04-pn2.png — standard 4:3 — STAND UP, SON OF THE MOUNTAIN
ATTACH (fetch from repo refs/ and attach to the generation): refs/hermes.png, refs/paris.png
MATCH LINE: map each: the herald drawing him up by the wrist.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium two-shot: Hermes messenger of the gods, swift slender youthful god, winged golden sandals and a winged traveler's cap, herald's staff twined with serpents, quick clever face, kindly and quick, drawing the dazed a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing up by the wrist; beyond them, waiting in a wash of gold, three tall radiant female figures. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg04-pn3.png — close-up 4:3 — THE APPLE IN ROUGH HANDS
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'his face in its glow.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot: the GOLDEN APPLE being placed into the rough calloused hands of a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing, its glow lighting his stunned beautiful face from below; the herald's slender hand withdrawing. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg05-pn1.png — standard 4:3 — HERA STEPS FORWARD
ATTACH (fetch from repo refs/ and attach to the generation): refs/hera.png, refs/paris.png
MATCH LINE: map each: majesty entire; the herdsman small before her.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Shot of majesty: Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face stepping forward into the firelight at divine scale, crown blazing; a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing small and awed before her. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg05-pn2.png — wide 16:9 — THE VISION OF THRONES
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'the herdsman throned in gold in the dream.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dream-vision panel, edges dissolving in golden mist: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing rendered throned in gold above a panorama of a hundred cities, crowned kings bowing before the dais, fleets and armies arrayed tiny below — the whole image a vision unfolding from a goddess's raised hand at the frame's edge. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg05-pn3.png — standard 4:3 — THE WEIGHT OF KINGDOMS
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'staring into the vision, the apple heavy.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing staring upward into off-panel golden light, the apple held against his chest, hunger and fear crossing his face. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg06-pn1.png — standard 4:3 — ATHENA STEPS FORWARD
ATTACH (fetch from repo refs/ and attach to the generation): refs/athena.png
MATCH LINE: 'calm, grey eyes level, unhurried.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Composed shot: Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face stepping forward, utterly calm, spear grounded, grey eyes level on the judge. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg06-pn2.png — wide 16:9 — THE VISION OF VICTORY AND WISDOM
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'the herdsman in shining armor; and grey among elders.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dream-vision panel in silvery-gold mist, split composition: on one side a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing rendered in shining bronze armor breaking an enemy line unwounded and victorious; on the other side the same man grey-templed and robed, seated among elders who lean toward his words; both visions streaming from a goddess's open hand at the frame's edge. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg06-pn3.png — close-up 4:3 — THE BETTER GIFT
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'shaken; hands tighten on the apple.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing shaken to the core, his hands tightening on the golden apple, this temptation biting deeper than the first. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg07-pn1.png — standard 4:3 — APHRODITE DOES NOT STEP FORWARD
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png
MATCH LINE: 'simply smiling; the air gone warm.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Radiant shot: Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face not advancing at all — simply standing and smiling, doves settling at her shoulders, the cold mountain night going warm and golden around her. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg07-pn2.png — wide 16:9 — THE VISION OF HELEN
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png
MATCH LINE: 'a veiled woman of unbearable radiance by a far hearth.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dream-vision panel, all soft golden mist: within the mist, far and small as if across the world, a hearth — and beside it, half-veiled, the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem, her beauty rendered as pure light gathering about a serene half-seen face; the vision flowing from a goddess's fingertips at the frame edge. Chaste, luminous, devastating. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg07-pn3.png — close-up 4:3 — UNDONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'his face, undone.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot: the face of a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing, undone — the visions of thrones and victories visibly fading behind his eyes, replaced by firelit longing. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg08-pn1.png — full page 3:4 — SPLASH — THE JUDGMENT
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png, refs/aphrodite.png, refs/hera.png, refs/athena.png, refs/hermes.png
MATCH LINE: map each: the apple passing to the smiling goddess; the two turning away COLD; the herald pitying.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page night tableau in the mountain clearing: at center a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing placing the GOLDEN APPLE into the open hands of Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face, whose smile is at full triumph; turning away from the firelight into the outer dark, Hera queen of the gods, majestic mature goddess, dark braided hair under a high golden crown, white and royal purple archaic robes with peacock motifs, proud sovereign face and Athena goddess of wisdom and war, tall grey-eyed goddess, dark hair under a crested bronze helmet pushed back from her brow, aegis cloak fringed with small serpents, tall spear, keen calm face — their faces not raging but utterly COLD; at the side Hermes messenger of the gods, swift slender youthful god, winged golden sandals and a winged traveler's cap, herald's staff twined with serpents, quick clever face watching with a herald's pity; the small human campfire at the center of the towering divine figures; kneeling cattle in the shadows. Leave calm space top and bottom for ornate caption plates. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg09-pn1.png — standard 4:3 — WHAT I PROMISED, I PERFORM
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png, refs/paris.png
MATCH LINE: map each: the goddess remaining; the judge kneeling, changed.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet aftermath shot: the clearing empty of gods except Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face, the apple now a soft glow at her belt; a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing kneeling before her, changed and frightened by his own fortune. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg09-pn2.png — close-up 4:3 — BE KNOWN
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png, refs/paris.png
MATCH LINE: 'lifting his chin with one finger.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close two-shot: Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face lifting the kneeling man's chin with one finger, reading his beautiful face like a craftsman appraising a made thing; his eyes wide. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg09-pn3.png — wide 16:9 — THE ROAD DOWN
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'alone at dawn, Troy far below.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide grey dawn shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing standing alone by his dead fire with his cattle, looking down the long mountain slopes at far small Troy on its plain; the goddess gone; a changed man at the top of a road. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg10-pn1.png — standard 4:3 — THE KING'S MEN TAKE THE BULL
ATTACH (fetch from repo refs/ and attach to the generation): refs/agelaus.png
MATCH LINE: 'protesting, waved aside.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Pasture shot: men in Trojan livery driving off chosen cattle — among them a great garlanded CHAMPION BULL; Agelaus, chief herdsman of Ida, weathered kindly mountain man, grizzled beard, rough wool cloak and leggings, herding staff protesting with raised staff, waved aside by the king's officer with a tally-board. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg10-pn2.png — standard 4:3 — I WILL WIN HIM BACK
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'arriving too late, decision hardening.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing arrived too late on the emptied pasture, staring down the road where dust hangs, decision hardening his face; his herd uneasy behind him. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg10-pn3.png — standard 4:3 — THE UNFINISHED WARNING
ATTACH (fetch from repo refs/ and attach to the generation): refs/agelaus.png, refs/paris.png
MATCH LINE: 'the old man gripping his arm, dread naked.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close two-shot: Agelaus, chief herdsman of Ida, weathered kindly mountain man, grizzled beard, rough wool cloak and leggings, herding staff gripping the young man's forearm with both old hands, dread naked in his weathered face, words failing; a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing gently puzzled, already half-turned toward the road. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg11-pn1.png — wide 16:9 — THE GAMES OF TROY (births DEIPHOBUS: crop refs/deiphobus.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/hector.png, refs/paris.png
MATCH LINE: map each among the competitors.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide festival shot on the games-field before the walls of Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond: footraces and boxing before a great crowd; among the competitors Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak foremost and beside him Deiphobus, prince of Troy, proud hot-tempered young warrior, dark beard, rich Anatolian tunic, quick angry eyes; and outstripping them all at the line, the unknown a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing in his plain herdsman's kilt. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
REF-BIRTH: refs/deiphobus.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i04-pg11-pn2.png — standard 4:3 — THE STRANGER CROWNED
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png, refs/priam.png, refs/hecuba.png
MATCH LINE: map each: the victor before the royal stand; the king and queen staring.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing crowned with the victor's wreath before the royal stand, breathing hard, shining; above him King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face and Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face staring down at the beautiful stranger with a disquiet neither can name. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg11-pn3.png — standard 4:3 — THE DRAWN SWORD
ATTACH (fetch from repo refs/ and attach to the generation): refs/deiphobus.png, refs/paris.png
MATCH LINE: map each: the shamed prince drawing; the victor springing back.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Sudden shot: Deiphobus, prince of Troy, proud hot-tempered young warrior, dark beard, rich Anatolian tunic, quick angry eyes, shamed and hot-eyed, drawing his sword on the games-field; a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing springing back light-footed; the crowd surging and shouting; officials rushing in. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg12-pn1.png — standard 4:3 — CASSANDRA BETWEEN THEM
ATTACH (fetch from repo refs/ and attach to the generation): refs/cassandra.png, refs/deiphobus.png, refs/paris.png
MATCH LINE: map each: her arms flung wide between the blade and the stranger.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dramatic shot at a stone altar at the field's edge: a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing at bay against the altar; Deiphobus, prince of Troy, proud hot-tempered young warrior, dark beard, rich Anatolian tunic, quick angry eyes advancing with drawn sword; and thrown between them with arms flung wide, wild-haired, blazing-eyed, Cassandra, young princess of Troy, wild dark hair, wide haunted far-seeing eyes, white and saffron Anatolian gown, a laurel sprig at her belt in full prophetic cry. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg12-pn2.png — standard 4:3 — THE TOKENS
ATTACH (fetch from repo refs/ and attach to the generation): refs/agelaus.png, refs/priam.png
MATCH LINE: map each: the old herdsman kneeling, holding up the tokens.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Hushed shot: Agelaus, chief herdsman of Ida, weathered kindly mountain man, grizzled beard, rough wool cloak and leggings, herding staff on his knees before King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face, holding up in both trembling hands a worn scrap of ROYAL SWADDLING CLOTH and a TINY SEAL on a cord; the stunned crowd pressing in a ring; the king's face beginning to break. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg12-pn3.png — standard 4:3 — MY SON
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/paris.png, refs/hecuba.png
MATCH LINE: map each: the king taking the young man's face in both hands; the queen weeping.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The recognition: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face holding the face of a strikingly beautiful young herdsman, clean-shaven, dark curling hair bound with a leather band, herdsman's kilt and light cloak, graceful careless bearing in both hands like a man in a dream; Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face already past them both, weeping, her arms going around her son; the crowd erupting in joy behind. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg13-pn1.png — wide 16:9 — THE FEAST OF RESTORATION
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png, refs/priam.png, refs/hecuba.png, refs/hector.png
MATCH LINE: map each: the restored prince in princely robes between his parents; the crown prince embracing him.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide joyful feast in the palace hall of Troy: a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing radiant between King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face and Queen Hecuba of Troy, stately Anatolian queen, dark hair under a jeweled headdress with a light veil, layered richly embroidered gown with a wide belt, strong loving sorrow-touched face at the high table; Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak clasping his new brother in a strong guarded embrace; the hall garlanded and rejoicing. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg13-pn2.png — standard 4:3 — THE SECOND CRY
ATTACH (fetch from repo refs/ and attach to the generation): refs/cassandra.png
MATCH LINE: 'pointing at the feast, voice breaking against the joy.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Desperate shot at the hall's edge: Cassandra, young princess of Troy, wild dark hair, wide haunted far-seeing eyes, white and saffron Anatolian gown, a laurel sprig at her belt pointing across the bright feast toward the high table, screaming her warning, her voice visibly breaking against a wall of celebration; two gentle attendants already reaching for her arms. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg13-pn3.png — standard 4:3 — LED AWAY KINDLY
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/cassandra.png
MATCH LINE: map each: the king gentle and immovable; the seeress led out.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Painful quiet shot: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face gentle and immovable, one hand raised in a soft command; Cassandra, young princess of Troy, wild dark hair, wide haunted far-seeing eyes, white and saffron Anatolian gown, a laurel sprig at her belt being led from the hall by attendants with great kindness, her face over her shoulder still crying the unheard truth; the feast unbroken around them. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg14-pn1.png — standard 4:3 — FRAME — OVERRULED
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
MATCH LINE: 'hands pressed together, disbelieving.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot by ember-light: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face with his hands pressed together before his mouth, disbelief and understanding fighting in his face. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg14-pn2.png — standard 4:3 — FRAME — A DOOM POSTPONED
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'gently explaining the most dangerous feeling.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre explaining gently, one open hand rising and falling like a scale-pan. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg14-pn3.png — standard 4:3 — FRAME — A SHIP IS BUILDING
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'grave, the gold light rising.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre gone grave, the vision-gold beginning to rise around him. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg15-pn1.png — standard 4:3 — THE FATAL SHIPS
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'the prince watching the ship grow; a golden shimmer at his shoulder.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Shore shot below Troy: a beautiful new galley rising on the stocks, the master-shipwright and his crew at work with adze and cord; a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing watching it grow with shining eyes; at his shoulder, visible to no one, a faint golden feminine shimmer in the air. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg15-pn2.png — standard 4:3 — THE TWIN SEERS (births HELENUS: crop refs/helenus.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/cassandra.png, refs/priam.png
MATCH LINE: map each: the two seers together before the king.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Formal shot in the council chamber: Helenus, seer-prince of Troy, slender grave young man, dark hair under a white seer's band across his brow, priestly Anatolian robe, calm sorrowful eyes and Cassandra, young princess of Troy, wild dark hair, wide haunted far-seeing eyes, white and saffron Anatolian gown, a laurel sprig at her belt standing together before King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face — the twin seers, both marked with the white band of sight, both grave; the king's face weary between love and duty. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
REF-BIRTH: refs/helenus.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i04-pg15-pn3.png — standard 4:3 — SAIL, ALEXANDROS
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/paris.png
MATCH LINE: map each: the king choosing the joy; the son bowing.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face with his hand raised in decision and blessing; a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing bowing with his hand over his heart, victory in his lowered eyes; behind them the two seers turning away. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg16-pn1.png — wide 16:9 — THE FLEET SAILS (births AENEAS: crop refs/aeneas.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'the prince at the stem.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot: the new Trojan ships standing out to sea under sail from the shore below Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond; at the lead stem a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing, wind in his cloak; beside him Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face, steady and watchful. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
REF-BIRTH: refs/aeneas.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i04-pg16-pn2.png — standard 4:3 — TELL ME THAT IS ALL
ATTACH (fetch from repo refs/ and attach to the generation): refs/aeneas.png, refs/paris.png
MATCH LINE: map each at the rail.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Two-shot at the ship's rail: Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face studying his kinsman with open doubt on his steady devout face; a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing gazing ahead at the horizon. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg16-pn3.png — close-up 4:3 — I SAILED THE DAY I JUDGED
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'the apple-light in his eyes.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot: a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing smiling faintly at the sea horizon, a golden apple-light quality in his dark eyes, wind moving his bound hair; a man who has handed over his own steering-oar. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg17-pn1.png — wide 16:9 — THE WRIST-CLASP OF TRUST
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/paris.png, refs/aeneas.png
MATCH LINE: map each: the host clasping the guest's wrist on the palace steps.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide arrival shot at Bronze Age Sparta in the Eurotas valley: a Mycenaean palace of timber columns and painted plaster on a low hill, the reed-lined river Eurotas below, the great wall of Mount Taygetus's peaks beyond: Trojan ships at the river-mouth beyond; on the palace steps a sturdy young war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak clasping the wrist of a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing in formal welcome, Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face and the embassy behind with gift-chests; banners, honor, open gates. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg17-pn2.png — standard 4:3 — THE GUEST-FEAST
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/paris.png
MATCH LINE: map each at the high table.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Warm feast shot in the Spartan hall: a sturdy young war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak and a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing at the high table exchanging gifts — a golden cup passing between their hands; correct, golden, doomed hospitality. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg17-pn3.png — standard 4:3 — THE QUEEN AT THE HEARTH
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png
MATCH LINE: 'looking up from among her women.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet shot across the hall: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem seated at the great hearth among her women with wool and spindle — looking up, once, toward the high table; firelight on the most beautiful face in the world. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg18-pn1.png — standard 4:3 — THE VISION MADE FLESH
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'frozen mid-word at the sight of her.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot at the feast: a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing frozen mid-word, a cup halfway to his lips, staring across the hall at something off-panel with recognition and awe — the look of a man seeing a remembered vision standing alive. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg18-pn2.png — standard 4:3 — THE INVOLUNTARY LOOK
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png
MATCH LINE: 'returning the look once — then down at her spindle.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot at the hearth: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem caught in one involuntary answering look toward the off-panel table — then her eyes dropping to her spindle, a fine line of trouble between her perfect brows. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg18-pn3.png — wide 16:9 — THE THIRD FIGURE
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png, refs/helen.png, refs/aphrodite.png
MATCH LINE: map each: the two mortals small at either side; the goddess faint between them.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide hall shot: a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing at the table on one side, the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem at the hearth on the other — and rendered faint as heat-shimmer in the air between and above them, visible to no one, Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face with one hand hovering over each mortal. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg19-pn1.png — full page 3:4 — SPLASH — THE COMPULSION
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png, refs/paris.png, refs/helen.png, refs/menelaus.png
MATCH LINE: map each: the goddess vast and translucent above the hall; golden threads to the two mortals; the host threadless and laughing.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Full-page composition: the great hall of Sparta at night, the feast small and golden below — and above and behind it at divine scale, translucent against the rafters and the night, Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face with her arms spread over the whole room like a weaver over a loom, fine golden threads of light running from her spread fingers down to two small bright figures: a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing at the table and the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem at the hearth; a sturdy young war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak laughing among his guests, touched by no thread, unaware. Leave calm space at top for an ornate caption plate. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg20-pn1.png — standard 4:3 — THE SUMMONS TO CRETE
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png
MATCH LINE: 'a dusty herald kneeling with news.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: a travel-stained HERALD kneeling before a sturdy young war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak with heavy news; the king's open face going solemn with duty; household around. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg20-pn2.png — standard 4:3 — AS IF I STOOD IN IT
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png, refs/paris.png, refs/helen.png
MATCH LINE: map each: the leave-taking of full trust.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Formal leave-taking shot: a sturdy young war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak clasping the wrist of a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing in farewell trust, his other hand extended in gentle instruction toward the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem who stands with lowered eyes; the whole grammar of trust, complete. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg20-pn3.png — wide 16:9 — THE KING SAILS
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png
MATCH LINE: 'on the shore, watching it go: the guest.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dawn shot: the king's ship going out small on a bright sea — and on the shore in the foreground, back to the viewer, watching it go: a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing, his cloak moving in the offshore wind. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg21-pn1.png — standard 4:3 — THE GODDESS AT THE HEARTH
ATTACH (fetch from repo refs/ and attach to the generation): refs/aphrodite.png, refs/helen.png
MATCH LINE: map each: the goddess seated beside her like kin.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Night interior, the hall emptied, the hearth low: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem seated staring into the embers — and beside her, fully present now, seated like a sister with an arm along the bench, Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face, golden, gentle, inescapable; the queen's face lit by two fires. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg21-pn2.png — standard 4:3 — THE TREASURE GOES ABOARD
ATTACH (fetch from repo refs/ and attach to the generation): refs/aeneas.png
MATCH LINE: 'standing apart, arms folded, dark with shame.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Deep-night courtyard shot: Trojan porters carrying CHESTS AND CAULDRONS of treasure from the open storerooms toward the shore by torchlight; standing apart with folded arms, watching, his steady face dark with shame, Aeneas, young Dardanian noble, sturdy pious warrior, short dark beard, plain strong bronze armor with a studded belt, steady devout face. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg21-pn3.png — standard 4:3 — THE LOOK BACK
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png, refs/paris.png, refs/aphrodite.png
MATCH LINE: map each: the veiled queen pausing on the gangplank; the prince's hand; the goddess behind.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Moonlit shore shot, restrained and grave: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem veiled for travel, pausing on a ship's gangplank to look back at the dark sleeping palace — her moonlit face unreadable and wet; before her the outstretched hand of a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing; behind her, radiant, patient, Aphrodite goddess of love, goddess of overwhelming beauty, golden hair loosely bound, rose-gold and seafoam-white robes, white doves about her, smiling irresistible face. Nothing sensual; the gravity of a threshold being crossed. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg22-pn1.png — wide 16:9 — HERA'S FIRST INSTALLMENT
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide storm shot at sea: Trojan galleys hammered by a sudden black tempest, mountainous seas, torn sail, tiny straining rowers; lightning splitting the dark. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg22-pn2.png — standard 4:3 — THE WATCHER IN THE CLOUDS
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png, refs/paris.png
MATCH LINE: map each at the mast.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Storm shot on the pitching deck: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem gripping the mast-stay, drenched, veil plastered; a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing shielding her with his body — and above the mast-head, formed briefly in the boiling clouds, a vast crowned female shape, watching, not striking. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg22-pn3.png — wide 16:9 — BY STRANGE COASTS
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Calm-after-storm shot: battered Trojan ships limping east under a low copper sun on a long swell, rigging frayed, crews bailing; a strange southern coastline distant. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg23-pn1.png — wide 16:9 — THE DOOM COMES ASHORE
ATTACH (fetch from repo refs/ and attach to the generation): refs/paris.png, refs/helen.png
MATCH LINE: map each on the gangplank.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide harbor shot at Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond: the ships come in; dense crowds on the shore; a strikingly beautiful young Trojan prince, clean-shaven, dark curling hair bound now with a thin gold band, rich embroidered Anatolian princely tunic and light cloak, graceful bearing leading the veiled the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem down the gangplank, her beauty moving through the crowd like wind through wheat — faces turning row by row. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg23-pn2.png — standard 4:3 — THE CRY FROM THE WALL
ATTACH (fetch from repo refs/ and attach to the generation): refs/cassandra.png, refs/helenus.png
MATCH LINE: map each on the wall above the harbor.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Shot on the wall above the cheering harbor: Cassandra, young princess of Troy, wild dark hair, wide haunted far-seeing eyes, white and saffron Anatolian gown, a laurel sprig at her belt with both fists pressed against her temples, screaming down unheard into the noise; beside her Helenus, seer-prince of Troy, slender grave young man, dark hair under a white seer's band across his brow, priestly Anatolian robe, calm sorrowful eyes, not screaming — simply closing his eyes. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg23-pn3.png — standard 4:3 — THE COUNTERSIGNATURE
ATTACH (fetch from repo refs/ and attach to the generation): refs/priam.png, refs/antenor.png, refs/hector.png
MATCH LINE: map each in council.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Council shot: King Priam of Troy, dignified Anatolian great-king in his strong middle years, long dark beard in formal curls streaked with grey, tall felt crown, rich long embroidered Anatolian robe, a small gold pendant on a cord at his throat, wise grave noble face aged in an hour on the dais; Antenor, elder counselor of Troy, lean old nobleman, white beard, plain dark Anatolian robe, tall staff, shrewd honest face grim with his staff mid-argument; Hector, crown prince of Troy, tall young warrior of noble bearing, short dark beard, strong open honorable face, bronze corslet over an Anatolian tunic, dark blue cloak with both fists on the table, jaw set; through the doorway the distant sound-image of the cheering city. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg24-pn1.png — standard 4:3 — THE COLD HEARTH
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png
MATCH LINE: 'standing in his own doorway; the hall dim and bare.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Desolate shot: a sturdy young war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak standing motionless in the doorway of his own great hall — the hearth cold, the treasure-room beyond standing open and bare, a steward kneeling with his face down, unable to speak. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg24-pn2.png — close-up 4:3 — POURED BRONZE
ATTACH (fetch from repo refs/ and attach to the generation): refs/menelaus.png
MATCH LINE: 'not raging; going very still.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot: the face of a sturdy young war-king with red-gold hair and short red beard, open honest face, bronze corslet under a crimson cloak — not raging; going very still, the honest open features setting like cooling bronze; a single vein at the temple. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg24-pn3.png — wide 16:9 — TWO WORDS
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dusk shot: a single horseman at full gallop through a stony hill pass toward the north, sparks off the flints, his cloak straight out behind him; the light dying red along the ridges. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg25-pn1.png — standard 4:3 — FRAME — HER BROTHERS!
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
MATCH LINE: 'on his feet in protest.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face on his feet in the murmuring hall, arm flung out in protest, the question burning in him. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg25-pn2.png — standard 4:3 — FRAME — THE SADDEST SMALL SONG
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'a long silence; an old sorrow.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre in a long silence, his blind face full of an old and personal-seeming sorrow, hands quiet on the strings. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg25-pn3.png — standard 4:3 — FRAME — WINTER LIGHT
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'the vision-light rising, but colder.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Transitional shot: the vision-gold rising around an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre — but paler and colder than before, a winter light. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg26-pn1.png — wide 16:9 — THE OLD QUARREL (births IDAS & LYNCEUS: crop refs/idas.png, refs/lynceus.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/castor.png, refs/polydeuces.png
MATCH LINE: map each driving the herd below.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide hill-country shot at dusk: Castor the horseman, lean athletic young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, short riding kilt mounted and Polydeuces the boxer, broad-shouldered young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, leather boxing thongs bound on his forearms afoot driving a raided cattle herd through a stony defile — and above them on the ridgeline, watching, two armed figures: Idas of Messene, massive black-bearded warrior in a boar-hide cloak with a great spear, harsh proud face and Lynceus of Messene, lean sharp warrior with strange piercing pale far-seeing eyes, grey-brown cloak, hunting spear. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.
REF-BIRTH: refs/idas.png, refs/lynceus.png — not the image generator's task: after this panel passes verification, the verification side crops and commits the ref(s) to the repo. Do not generate any panel that ATTACHes these ref(s) until they exist in refs/.

### i04-pg26-pn2.png — standard 4:3 — THE HOLLOW OAK
ATTACH (fetch from repo refs/ and attach to the generation): refs/castor.png
MATCH LINE: 'hidden in the hollow of a great oak, spear ready.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Night ambush shot: Castor the horseman, lean athletic young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, short riding kilt pressed into the hollow of a huge ancient oak, spear ready across his chest, moonlight barred by branches; the plan visible in his taut stillness. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg26-pn3.png — standard 4:3 — THE EYES OF LYNCEUS
ATTACH (fetch from repo refs/ and attach to the generation): refs/lynceus.png
MATCH LINE: 'pale eyes catching moonlight, seeing through the oak; arm flinging out.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Chilling shot on the far ridge: Lynceus of Messene, lean sharp warrior with strange piercing pale far-seeing eyes, grey-brown cloak, hunting spear, his strange pale eyes catching the moonlight and fixed with impossible precision on a distant oak, his arm flinging out to point; beside him the dark mass of his brother hefting a great spear. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg27-pn1.png — standard 4:3 — THE SPEAR THROUGH THE OAK
ATTACH (fetch from repo refs/ and attach to the generation): refs/castor.png
MATCH LINE: 'fallen from the hollow, hand at the wound.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Grave shot, no gore: the great spear of Idas transfixing the ancient oak trunk; fallen at its roots, Castor the horseman, lean athletic young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, short riding kilt, one hand pressed at his side, his white cap fallen, face turned to the sky; moon behind branches. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg27-pn2.png — standard 4:3 — THE VENGEANCE
ATTACH (fetch from repo refs/ and attach to the generation): refs/polydeuces.png
MATCH LINE: 'arriving like weather; the sky opening white above the fleeing slayer.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Dynamic shot: Polydeuces the boxer, broad-shouldered young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, leather boxing thongs bound on his forearms arriving at a dead run into the defile, terrible in grief; beyond him one enemy already fallen at the rocks' base, and above the far fleeing figure of the great-speared man, the night sky splitting with the white fire of a descending THUNDERBOLT. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg27-pn3.png — standard 4:3 — OUTLIVING
ATTACH (fetch from repo refs/ and attach to the generation): refs/polydeuces.png, refs/castor.png
MATCH LINE: map each: the immortal cradling the mortal.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. The still center: Polydeuces the boxer, broad-shouldered young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, leather boxing thongs bound on his forearms kneeling in the defile with the dying Castor the horseman, lean athletic young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, short riding kilt gathered in his arms, forehead bent to his brother's, the scattered cattle standing quiet in the dark around them. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg28-pn1.png — standard 4:3 — OLYMPUS IS OPEN TO YOU
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/polydeuces.png, refs/castor.png
MATCH LINE: map each: the sky opened in majesty above the kneeling brothers.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Divine shot: the night sky opened in golden majesty above the defile — Zeus king of the gods: powerful mature build, dark curling hair and full dark beard, calm sovereign face, deep crimson archaic robe, golden radiance, holding a scepter tipped with a golden eagle manifest in the light, looking down; below, small and human, Polydeuces the boxer, broad-shouldered young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, leather boxing thongs bound on his forearms kneeling with Castor the horseman, lean athletic young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, short riding kilt in his arms. The gods are radiant heroic figures: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg28-pn2.png — standard 4:3 — HALVE IT
ATTACH (fetch from repo refs/ and attach to the generation): refs/polydeuces.png, refs/castor.png
MATCH LINE: 'not rising; his brother's head against his shoulder.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot from slightly above: Polydeuces the boxer, broad-shouldered young Spartan hero, clean-shaven, dark cropped hair under a white felt cap, leather boxing thongs bound on his forearms not rising, his face lifted into the divine light with his answer already made, his brother's head against his shoulder; grief and absolute resolve in one young face. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg28-pn3.png — wide 16:9 — THE TWIN STARS
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide night sky shot over dark Peloponnesian hills: TWO bright stars close together rising above the ridgeline, their light doubled in a still mountain tarn below; the defile and its quiet cattle tiny in the dark. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg29-pn1.png — standard 4:3 — THE DARK HEARTH OF TYNDAREUS
ATTACH (fetch from repo refs/ and attach to the generation): refs/tyndareus.png
MATCH LINE: 'an old man alone in the doorway of the empty exercise-ground.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Desolate quiet shot at Bronze Age Sparta in the Eurotas valley: a Mycenaean palace of timber columns and painted plaster on a low hill, the reed-lined river Eurotas below, the great wall of Mount Taygetus's peaks beyond: the brothers' empty exercise-ground, their gear hung on the wall, dust settling in a shaft of light; the aging Mycenaean king of Sparta with grey-white beard, olive-green mantle with a gold pin, careworn kingly face, an old man now, standing alone in the doorway. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg29-pn2.png — standard 4:3 — THE QUESTION ON THE WALL (foretold)
ATTACH (fetch from repo refs/ and attach to the generation): refs/helen.png
MATCH LINE: 'years hence, searching the host from the high wall.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Flash-forward vision panel, edges soft as the singer's visions: the most beautiful woman of the age: long golden hair in soft waves, luminous calm unearthly beautiful face, white and gold flounced Mycenaean dress, gold diadem standing on a high wall of Bronze Age Troy: sloping cyclopean limestone walls, a great northeast bastion tower, mudbrick upper city, Anatolian gate shrine with standing stones, the plain and sea beyond, years older, scanning an immense besieging host encamped on the plain below, searching face after face for two she cannot find; wind in her veil. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, timber, no columned temples, no tiled roofs, no classical-era anachronisms. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg29-pn3.png — wide 16:9, letterbox — THE LIFE-GIVING EARTH
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Letterbox elegy shot: the same great plain composition emptied of armies — only wind in the grass; and inset small and quiet at one side, in a far green country, a double grave-mound beneath two low bright stars. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg30-pn1.png — standard 4:3 — FRAME — IS HEAVEN MOCKING US?
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
MATCH LINE: 'wiping his eyes, angry at himself.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face wiping his eyes with the heel of his hand, angry at his own tears, the question flung out. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg30-pn2.png — standard 4:3 — FRAME — HEAVEN IS TIMING US
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'shaking his head slowly.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre shaking his head slowly, one finger marking the beat of an argument older than himself. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg30-pn3.png — standard 4:3 — FRAME — THE OATH IS AWAKE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'rising, weary.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre rising wearily from the stool with the phorminx under his arm, ember-light long across the floor. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg31-pn1.png — wide 16:9 — FRAME — NO ONE MOVES TO LEAVE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH LINE: map each in the hushed hall.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot: the hall very quiet, listeners not moving to leave, the fire a red heart; an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre standing, a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face subdued on the high seat. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg31-pn2.png — standard 4:3 — FRAME — AND TOMORROW?
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png
MATCH LINE: 'subdued.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot: a young Ionian Greek nobleman, black curled hair bound with a fillet, fine wool chiton, gold armband, attentive noble face asking quietly, all eagerness gone, only need remaining. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i04-pg31-pn3.png — standard 4:3 — FRAME — TWO STARS OVER THE SEA
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: 'at the doorway; two stars low over the water.'
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Close shot: an elderly blind Greek bard, gaunt dignified face, long white hair and full white beard, closed sightless eyes, plain undyed wool mantle over one shoulder, holding a four-stringed wooden phorminx lyre at the dark doorway, blind face toward the night sea — where low over the horizon two stars burn close together, brighter than all the rest. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---

### i04-pg32-pn1.png — full page 3:4 — THE GNOME PAGE
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Full-page quiet composition: the Iron Age Ionian hall empty of people, the hearth down to red embers, the carved stool with the silent phorminx leaning against it in a pool of lamplight; through the open doorway the star-white night over a dark calm sea, and low above the horizon two bright stars close together. Leave the upper third calm and uncluttered for a large ornamented text panel. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

---
END OF ISSUE 4 PROMPTS. When all art exists: send the art+refs zip and say "build issue 4." Builds to its own separate issue-04.pdf.
