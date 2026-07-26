# ISSUE 1 — PANEL PROMPTS (pages 1–15) · v2 self-contained format
Each entry tells you everything: what to ATTACH (in that exact order), the MATCH line to paste above the prompt, and the PROMPT itself. Workflow per panel: set aspect → attach listed refs → paste match line + prompt → generate → inspect → save as the given filename into art/.

> **TWO-LLM WORKFLOW (standing instructions for the image-generation session):**
> 1. You have READ access to this repository. For each panel below, fetch every file on its ATTACH line from the repo's `refs/` folder (same branch as this prompts file) and attach those images to the generation request together with the PROMPT text, used verbatim.
> 2. Generate at the stated aspect ratio. Output must be completely TEXTLESS.
> 3. You cannot commit. Hand the finished image to the human operator under its exact panel filename (iNN-pgNN-pnN.png); the operator relays it to the verification side (Claude), which reviews it against prompt and refs and commits it to `issues/issue-NN/art/`.
> 4. Panels marked REF-BIRTH create a new reference face: after that panel passes verification, the verification side crops and commits the new ref to `refs/`. Do NOT generate any later panel that ATTACHes that ref until the ref file exists in the repo.


RULES
- If an entry says "then crop refs/x.png", that character is BORN in this panel: only accept a face you're happy to keep for 26 issues, then crop face+dress generously into refs/ under that name before moving on.
- If a listed ref doesn't exist yet because you skipped ahead, generate its birth panel first.
- Every image must contain NO text. Figured/painted pottery is tolerated on frame (sepia) pages only; regenerate if it appears prominently in saga pages.
- Aspects: wide 16:9 · standard 4:3 · tall 2:3 · full page 3:4.
- STANDING GUARD for any vista/cityscape panel: append "Strictly Bronze Age architecture only: no columned temples, no acropolis, no classical buildings, no red tiled roofs, no crosses or spires." Generators default to the Parthenon on aerial shots.

STATUS: pg01–pg02 complete · pg03-pn1 complete. Completed panels retain their prompts below for the permanent record (use these versions if a panel ever needs regeneration).

---

### i01-pg01-pn1.png — full page 3:4 — COVER ✅ DONE
ATTACH: none (cover was born first; if regenerating now, attach refs/singer.png and refs/gaia.png with a match line for each)
PROMPT:
Richly rendered comic book COVER art in classic Amar Chitra Katha tradition: bold ink outlines with fine texture and dramatic painted lighting permitted, heroic realistic anatomy, dignified expressive faces. Dramatic cover composition: in the foreground lower third, an elderly blind Greek bard with long white hair and full white beard, closed sightless eyes, plain undyed wool mantle, seated in warm lamplight holding up a four-stringed wooden phorminx lyre; rising behind and above him like a vision filling the sky, a colossal sorrowful Earth-mother goddess figure with hair flowing into green foliage and robes patterned like fields, and beyond her on the horizon the massive SLOPING cyclopean stone walls of a Bronze Age city with a great bastion tower burning against a night sky — Bronze Age architecture only, absolutely no crosses, no spires, no later-era buildings. Leave the top fifth of the image as calm dark sky for a title plate. Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image.

### i01-pg02-pn1.png — wide 16:9 ✅ DONE
ATTACH: none
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified realistic faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. An early Iron Age Greek coastal town at evening seen from a low hill: modest stone and timber houses with thatched and flat clay roofs descending to a small harbor with beached ships, one large megaron hall glowing with firelight at the town's heart, stars rising over a calm dark Aegean sea. Absolutely no text, no lettering, no captions anywhere in the image.

### i01-pg02-pn2.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png (if regenerating, also refs/neleid-prince.png and refs/hall-boy.png)
MATCH LINE: "Match the attached reference image exactly: the elderly blind bard — same face, hair, beard, and dress."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified realistic faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Interior of an early Iron Age Ionian megaron hall at evening: timber columns, central hearth fire, hanging oil lamps, Greek nobles seated on benches along the walls; an elderly blind bard with long white hair and beard, closed sightless eyes, plain wool mantle, holding a four-stringed phorminx lyre, being led to a carved stool by a boy; on a high seat a young Ionian nobleman with black curled hair bound with a fillet, fine wool chiton and gold armband, leaning eagerly forward. Absolutely no text, no lettering anywhere in the image.

### i01-pg02-pn3.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: "Match the attached reference image exactly: the elderly blind bard — same face, hair, beard, and dress."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified realistic faces. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Close-up portrait: the face of an elderly blind Greek bard, gaunt and dignified, long white hair and full white beard, closed sightless eyes, serene knowing expression, warm firelight playing on his face against a dark hall background. Absolutely no text, no lettering anywhere in the image.

### i01-pg03-pn1.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH LINE: "Match the attached reference images exactly: the first image is the elderly blind bard — same face, hair, beard, and dress; the second image is the young nobleman seated on the high seat — same face, hair, and blue mantle."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, dignified realistic faces. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. In a firelit Iron Age Greek hall, an elderly blind bard with white hair and beard rises to his feet holding a phorminx lyre against his chest, one hand lifted in invocation; seated nobles utterly still around him, firelight throwing his long shadow up a timber column. Absolutely no text, no lettering anywhere in the image.


---

### i01-pg03-pn2.png — tall 2:3 — THE MUSE APPEARS ✅ DONE (refs/muse.png cut)
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png — then crop refs/muse.png from the result
MATCH LINE: "Match the attached reference image exactly: the elderly blind bard — same face, hair, beard, and dress."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, dignified expressive faces, clean composition. An elderly blind Greek bard in a sepia-toned firelit Iron Age hall stands singing with lifted hand; above and behind him in the dark rafters, faintly visible and unseen by the mortals, a radiant Muse — a luminous woman of unearthly beauty, dark hair crowned with laurel, flowing pale gold robe — extends her hand toward his brow; where her radiance touches, warm full color blooms into the sepia scene, the two palettes meeting in one image. Absolutely no text, no lettering anywhere in the image.

### i01-pg03-pn3.png — wide 16:9 — THE VISION OPENS ✅ DONE (second pass; first failed on a classical acropolis)
ATTACH: none
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, vivid colors, clean composition. A god's-eye vista of the Bronze Age Aegean world from high above: deep blue sea scattered with islands, coastlines terraced with fields, many small hilltop citadels ringed with rough cyclopean stone walls, flat-roofed mudbrick and thatched houses, smoke of countless cookfires, tiny oared galleys with single sails crossing between islands, minute armies and herds on the plains — the whole world teeming and crowded with mankind, bathed in late golden light. Strictly Bronze Age architecture only: absolutely no columned temples, no acropolis, no classical Greek buildings, no red tiled roofs, no crosses or spires. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg04-pn1.png — wide 16:9 ✅ DONE
ATTACH: none
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, vivid colors, clean composition. Bronze Age landscape groaning with abundance and crowding: every plain plowed and terraced, every hilltop ringed with cyclopean walls, herds and marching spearmen and harvest wagons filling the valleys, a haze of smoke from countless fires dimming the sky. Absolutely no text, no lettering anywhere in the image.

### i01-pg04-pn2.png — standard 4:3 ✅ DONE
ATTACH: none
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, vivid colors, clean composition. A cracked and sagging hillside under the weight of a marching Bronze Age army; from the fissured earth of the hill a vast ancient feminine face is beginning to emerge, half-formed from soil and stone, eyes weary — the Earth-mother rising from the land itself. Absolutely no text, no lettering anywhere in the image.

### i01-pg04-pn3.png — tall 2:3 — GAIA RISES ✅ DONE
ATTACH: none — then crop refs/gaia.png from the result (use the cover's Gaia as a style memory; this panel makes her canonical at full height)
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, heroic scale, dignified expressive faces. Gaia the Earth-mother risen to colossal height against a golden sky: an ancient majestic motherly figure whose hair flows into green foliage and ripe grain, whose robes are patterned like fields, rivers and mountains falling from her shoulders, her beautiful face weary and sorrowful and grand, tears on her cheeks, arms lifted toward the heavens in appeal. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg05-pn1.png — wide 16:9 — OLYMPUS ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/gaia.png — then crop refs/zeus.png from the result
MATCH LINE: "Match the attached reference image exactly: the colossal Earth-mother goddess — same face, foliage hair, and field-patterned robes."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces. The gods depicted in radiant heroic style: slightly larger than mortal scale, luminous golden aura outlines, serene majestic faces, rich archaic robes. Olympus above the clouds: an open pillared hall of pale stone on a mountain summit floating over a sea of clouds; Zeus — powerful mature build, dark curling hair and full dark beard, deep crimson archaic robe, golden radiance, scepter tipped with a golden eagle — enthroned; beyond the cloud-sea rises the mountain-tall form of the Earth-mother goddess, her hands spread in solemn appeal to the enthroned god. Absolutely no text, no lettering anywhere in the image.

### i01-pg05-pn2.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/gaia.png
MATCH LINE: "Match the attached reference image exactly: the Earth-mother goddess — same face, foliage hair, and robes."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces. Close-up of the face of the Earth-mother goddess: ancient majestic feminine beauty, hair flowing into leaves and grain, deep weary grief in her eyes, golden sky behind. Absolutely no text, no lettering anywhere in the image.

### i01-pg05-pn3.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
MATCH LINE: "Match the attached reference image exactly: Zeus — same face, hair, beard, crimson robe, and eagle scepter."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, radiant divine styling with golden aura outline. Zeus enthroned in thought: powerful mature god, dark curling hair and beard, deep crimson archaic robe, chin resting on his fist, eyes distant and heavy with fateful deliberation; on his scepter a golden eagle that seems to watch with him; storm-light gathering faintly in the clouds behind the throne. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg06-pn1.png — standard 4:3 — THE COUNSEL ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png — then crop refs/themis.png from the result
MATCH LINE: "Match the attached reference image exactly: Zeus — same face, hair, beard, crimson robe, and eagle scepter."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, radiant divine styling with golden aura outlines. On a pale stone terrace of Olympus above a sea of clouds, two gods confer closely and privately: Zeus — dark-bearded, crimson-robed, eagle-tipped scepter — head bent toward Themis, goddess of divine order — serene matronly beauty, veiled head, silver-grey archaic robes; intimate conspiratorial composition, vast sky behind. Absolutely no text, no lettering anywhere in the image.

### i01-pg06-pn2.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/themis.png
MATCH LINE: "Match the attached reference image exactly: the veiled goddess Themis — same face, veil, and silver-grey robes."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, radiant divine styling with golden aura outline. Themis, goddess of right order: serene matronly beauty, veiled head, silver-grey archaic robes, speaking with calm gravity, one hand open before her as if setting invisible weights upon an unseen balance; clouds and pale gold light behind. Absolutely no text, no lettering anywhere in the image.

### i01-pg06-pn3.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
MATCH LINE: "Match the attached reference image exactly: Zeus — same face, hair, and beard."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, radiant divine styling with golden aura outline. Close profile of Zeus's face, resolved and sovereign and quietly terrible, dark curling beard, eyes fixed on far distance; behind him the first flicker of storm-light in high clouds. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg07-pn1.png — wide 16:9 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/themis.png
MATCH LINE: "Match the attached reference images exactly: the first image is Zeus — same crimson robe and scepter; the second image is the veiled goddess Themis — same veil and silver-grey robes. Both are seen from behind."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, clean composition, radiant divine styling. Viewed from behind two gods — a crimson-robed dark-haired god with an eagle scepter and a grey-veiled goddess — standing at the cloud-rim of Olympus: far below through a parting in the cloud-sea, two tiny distant lands picked out in shafts of light on the dark world — on one side a hilltop citadel with cyclopean walls in mainland Greece, on the other, across a painted sea, a walled city on a coastal plain in Asia. Absolutely no text, no lettering anywhere in the image.

### i01-pg07-pn2.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png
MATCH LINE: "Match the attached reference image exactly: Zeus — same face, hair, beard, crimson robe, and eagle scepter."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified faces, radiant divine styling with golden aura outline. Zeus extends his scepter over the cloud-rim of Olympus and the golden eagle launches from its tip, wings wide, plunging down through parting clouds toward the tiny sunlit world of men far below. Absolutely no text, no lettering anywhere in the image.

### i01-pg07-pn3.png — standard 4:3 — FRAME CUT ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png, refs/singer.png
MATCH LINE: "Match the attached reference images exactly: the first image is the young nobleman — same face, fillet, armband, and blue mantle; the second image is the elderly blind bard singing in the background — same face, hair, and beard."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified realistic faces. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. In a firelit Iron Age Greek hall, close on a young Ionian nobleman with black curled hair, gold fillet and armband and blue mantle, gripping his wine cup tightly, listening spellbound; beside and beyond him the blind white-bearded bard sings on, face lifted. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg08-pn1.png — full page 3:4 — SPLASH: THE TWO HOUSES ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png (for the feasting gods' style) — then crop refs/tantalus.png AND refs/laomedon.png from the result if their faces please you; otherwise they are born on pages 9 and 20
MATCH LINE: "Match the attached reference image exactly for the enthroned god at the feast: same face, hair, beard, and crimson robe."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, heroic realistic anatomy, dignified expressive faces, dramatic splash-page composition divided diagonally by a golden eagle in full flight from upper right to lower left. Upper left half: a richly dressed Anatolian-Lydian king with heavy gold jewelry and oiled ringleted black beard feasting in honor at a radiant table among larger-than-mortal glowing gods on Olympus. Lower right half: a proud aging Anatolian king with long formally curled grey-streaked beard, tall felt crown and long embroidered robe, standing arms akimbo before massive half-built SLOPING cyclopean stone walls with wooden scaffolding, Bronze Age architecture only, no crosses or spires anywhere, the sea plain beyond. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg09-pn1.png — wide 16:9 — TANTALUS AMONG THE GODS ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png (+ refs/tantalus.png if you cropped him from pg08) — if Tantalus is new here, crop refs/tantalus.png from the result
MATCH LINE: "Match the attached reference image exactly: Zeus at the head of the table — same face, hair, beard, and crimson robe." (add a second clause for Tantalus if attaching his ref)
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, radiant divine styling with golden aura outlines on the gods. A feast on Olympus: at a long radiant table of glowing gods in rich archaic robes sits one mortal man in the place of honor — a rich Anatolian-Lydian king, heavy gold jewelry, oiled black beard in formal ringlets, embroidered long robe, proud cunning face — raising a golden cup; Zeus enthroned at the table's head; cupbearers pouring nectar; clouds and golden light beyond the pillars. Absolutely no text, no lettering anywhere in the image.

### i01-pg09-pn2.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/tantalus.png
MATCH LINE: "Match the attached reference image exactly: the Lydian king — same face, ringleted beard, jewelry, and robe."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces. At the edge of a radiant divine feast, a rich Anatolian-Lydian king with oiled ringleted black beard gathers his embroidered robe and slyly slips a small golden flask beneath it, eyes sliding sideways; behind him the glowing gods converse, not yet noticing; marble pillars and cloud-light. Absolutely no text, no lettering anywhere in the image.

### i01-pg09-pn3.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/tantalus.png
MATCH LINE: "Match the attached reference image exactly: the Lydian king — same face, ringleted beard, jewelry, and robe."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces. A torchlit Bronze Age Anatolian palace hall: the rich Lydian king holds court among mortal cronies, pouring a glowing golden liquid from a small flask into their cups, whispering behind his hand; the men lean in laughing; plain burnished pottery, bronze lamps, no painted figures on the pottery. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg10-pn1.png — wide 16:9 — THE ABOMINABLE FEAST ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/tantalus.png, refs/zeus.png
MATCH LINE: "Match the attached reference images exactly: the first image is the Lydian king host — same face, beard, and robe; the second image is Zeus seated among the guests — same face, beard, and crimson robe."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces. A wrongness-laden banquet in a Bronze Age Anatolian palace hall: radiant gods seated at a mortal king's table, unsmiling and utterly still, none touching the covered bronze dishes before them; the rich Lydian king watches his divine guests with hidden testing eagerness; shadows unnaturally long, torch flames leaning; one veiled goddess at the table's end looks down in sorrow. Ominous restrained mood, nothing graphic shown. Absolutely no text, no lettering anywhere in the image.

### i01-pg10-pn2.png — standard 4:3 ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png, refs/tantalus.png
MATCH LINE: "Match the attached reference images exactly: the first image is Zeus rising in wrath — same face, beard, crimson robe; the second image is the Lydian king shrinking back — same face, beard, and robe."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, radiant divine styling. The gods on their feet as one in terrible wrath at a banquet table, divine light flaring white-gold, bronze dishes overturned and untouched; Zeus foremost, arm outstretched in judgment; the rich Lydian king shrinking back with his arm across his face; torches guttering flat in the divine wind. Nothing graphic shown. Absolutely no text, no lettering anywhere in the image.

### i01-pg10-pn3.png — standard 4:3 — PELOPS RESTORED ✅ DONE
ATTACH: none — a boy of about twelve; do NOT crop a ref (adult Pelops is born on page 12)
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, radiant divine styling. Gentle radiance gathered over a stone bier in a torchlit hall: a boy of about twelve restored whole and breathing, eyes just opening, his left shoulder gleaming with smooth new polished ivory; luminous divine hands withdrawing from the blessing; at the panel's edge a veiled goddess turns away in quiet sorrow. Tender reverent mood. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg11-pn1.png — tall 2:3 — THE PUNISHMENT (Od. 11) ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/tantalus.png
MATCH LINE: "Match the attached reference image exactly: the standing man — same face and ringleted beard, but haggard and ancient."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, muted underworld palette of grey-blue, ash, and pale gold, dignified expressive faces. The grey underworld of Hades: a haggard king stands to his chin in a clear dark pool beneath a fruit-laden tree — pear, pomegranate, apple; the water visibly shrinking away from his straining lips exposing dark earth at his feet, while wind whips the laden boughs up out of his reach toward a starless sky. Absolutely no text, no lettering anywhere in the image.

### i01-pg11-pn2.png — wide 16:9, will be used as a face strip ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/tantalus.png
MATCH LINE: "Match the attached reference image exactly: same face and ringleted beard, but haggard and ancient."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, muted underworld palette of grey-blue, ash, and pale gold. Extreme close-up of an ancient haggard king's face in the grey underworld, water at his chin, lips parted in endless thirst, eyes hollow with eternal craving, wind-whipped fruit boughs blurred above. Absolutely no text, no lettering anywhere in the image.

### i01-pg11-pn3.png — standard 4:3 — FRAME CUT ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH LINE: "Match the attached reference images exactly: the first image is the elderly blind bard — same face, hair, beard, and dress; the second image is the young nobleman — same face, fillet, and blue mantle."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified realistic faces. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. A firelit Iron Age Greek hall: listeners rigid with awe, an old noble making a superstitious averting hand-sign, the young nobleman on the high seat grave; the blind white-bearded bard stands implacable with his lyre, face lifted. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg12-pn1.png — wide 16:9 — PELOPS COMES TO PISA ✅ DONE
ATTACH: none — then crop refs/pelops.png from the result (this is his canonical adult face)
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, heroic realistic anatomy, dignified expressive faces. A Greek shore at rose-gold dawn: a handsome clean-shaven young hero with dark wavy hair, Mycenaean short kilt and belt, cape and spear, his left shoulder gleaming polished ivory white, standing beside a magnificent chariot with two white horses half-wrapped in sea-mist; behind him the sea still churns in a wide ring where a god has just withdrawn beneath the waves. Absolutely no text, no lettering anywhere in the image.

### i01-pg12-pn2.png — standard 4:3 — THE GATE OF SKULLS ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/pelops.png — then crop refs/hippodamia.png from the result (she watches from the wall)
MATCH LINE: "Match the attached reference image exactly: the young hero driving the chariot — same face, hair, ivory left shoulder, kilt."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, grim restrained mood. The gate road of a Bronze Age Greek citadel flanked by a row of tall wooden stakes, each bearing a weathered bronze-helmeted head rendered as dark dignified silhouettes; the young ivory-shouldered hero drives his white-horse chariot slowly between them, face set; above on the cyclopean wall a young Mycenaean noblewoman with long dark ringlets, flounced tiered skirt and fitted bodice in blue and saffron, gold diadem, watches him come. Nothing gory, silhouettes only. Absolutely no text, no lettering anywhere in the image.

### i01-pg12-pn3.png — wide 16:9, eyes-meeting strip ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/hippodamia.png, refs/pelops.png
MATCH LINE: "Match the attached reference images exactly: the first image is the princess on the wall — same face, ringlets, diadem, blue and saffron dress; the second image is the hero below — same face and ivory shoulder."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces. Split composition: on the upper wall of a Bronze Age citadel a princess with dark ringlets and gold diadem looks down, hope and dread in her eyes; below on the gate road a young hero looks up from his chariot; their gazes meeting across the stone. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg13-pn1.png — standard 4:3 — THE STABLES AT NIGHT ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/hippodamia.png, refs/pelops.png — then crop refs/myrtilus.png from the result
MATCH LINE: "Match the attached reference images exactly: the first image is the princess carrying the torch — same face, ringlets, and dress; the second image is the young hero beside her — same face and ivory shoulder."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, conspiratorial night mood. Bronze Age chariot stables by torchlight: a princess leads a young hero between the stalls toward a wiry weathered charioteer with a short beard, plain leather kilt and arm-guards, sharp restless eyes, who looks up from a chariot wheel; deep shadows, one torch, horses dim in the stalls. Absolutely no text, no lettering anywhere in the image.

### i01-pg13-pn2.png — standard 4:3 — THE OATH ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/pelops.png, refs/myrtilus.png
MATCH LINE: "Match the attached reference images exactly: the first image is the young hero — same face and ivory shoulder; the second image is the wiry charioteer — same face, beard, and leather kilt."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces. Torchlit close scene: the young ivory-shouldered hero grips the forearm of the wiry charioteer in a sealing oath-clasp, their eyes locked; the charioteer's eyes glitter with cunning and hunger; stable shadows behind. Absolutely no text, no lettering anywhere in the image.

### i01-pg13-pn3.png — wide 16:9, hands strip ✅ DONE
ATTACH: none
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills. Extreme close-up in flickering lamplight: weathered hands sliding a pale wax linchpin into a bronze chariot wheel-hub while palming the true bronze pin away; wheel spokes and axle filling the frame. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg14-pn1.png — wide 16:9 — THE RACE ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/pelops.png, refs/hippodamia.png, refs/myrtilus.png — then crop refs/oenomaus.png from the result
MATCH LINE: "Match the attached reference images exactly: the first image is the young hero driving the lead chariot — same face and ivory shoulder; the second image is the princess beside him — same face, ringlets, and dress; the third image is the charioteer driving the pursuing chariot — same face and leather kilt."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, heroic realistic anatomy, dynamic action. Full gallop along a Bronze Age Greek coast road at speed: ahead, a chariot with two white horses carrying a young hero and a princess, her ringlets streaming; behind and closing, a black-armored grim war-king with iron-grey beard and bronze zoned helmet leveling a spear for a killing cast from his chariot, his wiry charioteer at the reins; dust, sea cliffs, motion lines. Absolutely no text, no lettering anywhere in the image.

### i01-pg14-pn2.png — wide 16:9 — THE CRASH ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/oenomaus.png, refs/myrtilus.png
MATCH LINE: "Match the attached reference images exactly: the first image is the black-armored king tangled in the reins — same helmet and grey beard; the second image is the charioteer leaping clear — same face and leather kilt."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dynamic action, dignified restrained violence. A racing chariot catastrophically failing at full speed: a wheel bursting from the axle, wax pins shearing, the car slewing sideways into ruin; a wiry charioteer leaping clear mid-air; the black-armored grey-bearded king tangled in the reins being dragged; dust cloud, panicked horses, a single jagged impact burst, no gore. Absolutely no text, no lettering anywhere in the image.

### i01-pg14-pn3.png — standard 4:3 — THE FIRST CURSE ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/oenomaus.png, refs/myrtilus.png
MATCH LINE: "Match the attached reference images exactly: the first image is the dying king raised on one arm — same face and grey beard, helmet fallen; the second image is the charioteer standing apart — same face and kilt."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, tragic mood. Among chariot wreckage on a dusty coast road, a broken grey-bearded king raises himself on one arm, a thin trace of blood at his mouth, his shaking hand pointing in condemnation past the viewer at a wiry charioteer who stands frozen apart; overturned wheel, scattered tack, low harsh light. Minimal blood, nothing graphic. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg15-pn1.png — standard 4:3 — THE CLIFF ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/pelops.png, refs/myrtilus.png, refs/hippodamia.png
MATCH LINE: "Match the attached reference images exactly: the first image is the young hero, now wearing a king's cloak — same face and ivory shoulder; the second image is the charioteer arguing with him — same face and kilt; the third image is the princess standing apart by the chariot — same face and dress, face averted."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dignified expressive faces, tense dusk mood. A high sea-cliff at dusk: the young ivory-shouldered hero, now cloaked as a king, and the wiry charioteer argue at the brink, the charioteer's hand out demanding, the king's face cold; apart by the chariot a princess stands with her face averted; bruised purple and amber sky, white surf far below. Absolutely no text, no lettering anywhere in the image.

### i01-pg15-pn2.png — tall 2:3 — THE FALLING CURSE ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/myrtilus.png
MATCH LINE: "Match the attached reference image exactly: the falling man — same face, beard, and leather kilt."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, dramatic tragic composition. A wiry charioteer falling backward from a sea-cliff against a bruised dusk sky, arms flung wide, mouth open in a great final curse, hair and kilt whipped upward by the fall; far below the white surf waits among black rocks; above at the cliff edge a cloaked figure stands small against the sky. Absolutely no text, no lettering anywhere in the image.

### i01-pg15-pn3.png — wide 16:9 — THE SEA CLOSES ✅ DONE
ATTACH (fetch from repo refs/ and attach to the generation): refs/pelops.png
MATCH LINE: "Match the attached reference image exactly: the cloaked king half-turned away — same face and ivory shoulder."
PROMPT:
Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, somber mood. A sea-cliff top at last light: white rings of foam closing on the darkening sea far below; the young king half-turned away from the edge, the first shadow of guilt on his face, his cloak stirring; faint and half-formed in the storm clouds above the sea, barely visible, the suggestion of a watching divine face. Absolutely no text, no lettering anywhere in the image.

---
END OF BATCH. Pages 16–32 prompts will be added next session — say "extend prompts" when you near page 15.


# ISSUE 1 — PANEL PROMPTS, PAGES 16–32 (extension · drop into issues/issue-01/ alongside prompts.md)
Same rules as the main file. Shot grammar is declared per panel — it is part of the prompt. Guard clause is baked into every earthly city/architecture panel. Ref-births marked. Every prompt below is fully self-contained — paste it exactly as written. Every prompt ends with: "Absolutely no text, no lettering, no speech balloons, no captions anywhere in the image."

---

### i01-pg16-pn1.png — wide 16:9 — WIDE ESTABLISHING — MYCENAE
ATTACH: none — then crop refs/atreus.png AND refs/thyestes.png from the result if strong; else they are born in pn2/pn3
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide establishing shot of Bronze Age Mycenae: the Lion Gate — two rampant lionesses carved above a massive stone lintel — with a crowd of townsfolk gathered before it as a herald proclaims; above on the cyclopean wall stand two royal brothers with a cold gap between them: one heavy-browed powerful king-figure with squared black beard and deep purple mantle, one lean saturnine prince with pointed dark beard and dark green robe. Strictly Bronze Age architecture only: rough cyclopean stone, mudbrick, no columned temples, no tiled roofs. Absolutely no text, no lettering anywhere in the image.

### i01-pg16-pn2.png — standard 4:3 — MEDIUM INTERIOR — THE GOLDEN LAMB
ATTACH (fetch from repo refs/ and attach to the generation): refs/thyestes.png (if cut)
MATCH LINE: "Match the attached reference image exactly: the lean dark-green-robed prince — same face and pointed beard."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot inside a torchlit Bronze Age treasury of rough stone and timber: the lean saturnine prince in dark green triumphantly holds aloft a living lamb whose fleece is solid shining gold; behind him half in shadow a beautiful noblewoman in Mycenaean flounced dress, her hand still on an opened wooden chest, her expression guilty and infatuated; gold treasure dim around them. Absolutely no text, no lettering anywhere in the image.

### i01-pg16-pn3.png — wide 16:9 — WIDE EXTERIOR, DUSK — THE SUN REVERSES
ATTACH (fetch from repo refs/ and attach to the generation): refs/atreus.png, refs/thyestes.png (as available)
MATCH LINE: map each attached ref: "the purple-mantled king with arms raised" / "the green-robed prince staggering back."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dusk shot before the Lion Gate of Mycenae: a crowd gasps and points west where the setting sun is visibly dragging BACKWARD across the sky toward the east, its light streaming the wrong way, shadows bending reversed; in the foreground the heavy-browed purple-mantled king stands alone unafraid with both arms raised in triumph while the green-robed prince staggers back clutching the golden lamb. Strictly Bronze Age architecture only. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg17-pn1.png — standard 4:3 — MEDIUM TWO-SHOT — THE FALSE PARDON
ATTACH (fetch from repo refs/ and attach to the generation): refs/atreus.png, refs/thyestes.png
MATCH LINE: map each: "the enthroned purple-mantled king" / "the travel-worn green-robed suppliant."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium two-shot in a Bronze Age megaron throne room, timber columns and central hearth: the travel-worn lean prince kneels in formal supplication, both hands raised to clasp the knees of the enthroned heavy-browed king; the king smiles with his mouth only, eyes cold as stone; courtiers uneasy in shadow. Absolutely no text, no lettering anywhere in the image.

### i01-pg17-pn2.png — wide 16:9 — WIDE INTERIOR — THE FEAST
ATTACH (fetch from repo refs/ and attach to the generation): refs/atreus.png, refs/thyestes.png
MATCH LINE: map each: "the king seated at the table's head, not eating, watching" / "the lean prince eating heartily."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot of a Bronze Age feast hall hung with dark red cloth: the lean prince eats heartily at a laden table, wine cup raised; at the table's head the heavy-browed king sits before an empty place, not eating, watching his guest with a stillness worse than rage; servants' faces averted; at the panel's edge a large covered bronze dish waits on a side table. Ominous restrained mood, nothing graphic anywhere. Absolutely no text, no lettering anywhere in the image.

### i01-pg17-pn3.png — standard 4:3 — MEDIUM-CLOSE — THE HORROR
ATTACH (fetch from repo refs/ and attach to the generation): refs/thyestes.png, refs/atreus.png
MATCH LINE: map each: "the prince on his feet in horror" / "the king leaning back savoring."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium-close shot: the lean prince on his feet, the table overturning before him in a crash of vessels, his face a mask of absolute horror fixed on an uncovered bronze dish whose contents are BELOW the frame edge and never shown; the heavy-browed king leans back savoring the moment; lightning white in the high windows. Nothing graphic shown anywhere, the horror entirely in the face. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg18-pn1.png — wide 16:9 — WIDE NIGHT EXTERIOR — FLIGHT
ATTACH (fetch from repo refs/ and attach to the generation): refs/thyestes.png
MATCH LINE: "the fleeing green-robed man."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide night storm shot: a lone man in a whipping dark green cloak flees on foot down a rocky road away from the Lion Gate of Mycenae, which glares floodlit behind him in a lightning flash; rain slanting, trees bent. Strictly Bronze Age architecture only. Absolutely no text, no lettering anywhere in the image.

### i01-pg18-pn2.png — standard 4:3 — INTIMATE MEDIUM — THE LESSON
ATTACH (fetch from repo refs/ and attach to the generation): refs/thyestes.png
MATCH LINE: "the aged green-robed man, now grey-streaked and gaunt."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Intimate medium shot at a poor hearth in a humble stone hut, years later: the lean prince now aged and grey-streaked sits with his hand on the shoulder of a solemn boy of ten with old eyes; firelight on both faces; the boy recites, the old man's face fierce and patient. Absolutely no text, no lettering anywhere in the image.

### i01-pg18-pn3.png — standard 4:3 — FRAME CUT, MEDIUM — [STYLE-FRAME palette: sepia, umber, dusk-blue, lamplight gold]
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH LINE: "first image: the blind bard, face lifted; second image: the young nobleman, pale and grave."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium shot in the firelit Iron Age hall: the young noble on the high seat pale and grave, wine forgotten; the blind white-bearded bard stands with his lyre, sightless face lifted, mid-word; listeners hushed. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg19-pn1.png — full page 3:4 — MAP PANEL
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. A full-page painted map of the Bronze Age Aegean world in the style of an ancient illustrated chart with an ornamented border: mainland Greece at left with two marked hilltop citadels (one with a lion gate, one coastal), the island-scattered sea at center with tiny oared galleys, the Anatolian coast at right with a walled city on a plain by a strait at the top and a coastal city further south, and beyond them to the east a vast dark mountainous empire suggested by fortress silhouettes; a golden eagle in flight over the middle sea casting its small shadow on the water. Decorative compass motifs, no writing of any kind. Strictly Bronze Age architecture only. Absolutely no text, no lettering, no place-name labels anywhere in the image.

---

### i01-pg20-pn1.png — wide 16:9 — WIDE — GODS IN SERVITUDE (births APOLLO-MORTAL & POSEIDON-MORTAL: crop refs/apollo-mortal.png, refs/poseidon-mortal.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/laomedon.png (background), refs/poseidon-glimpse.png (for the mason's face echo)
MATCH LINE: "the crowned king may appear small on a distant platform; give the huge mason a hint of the attached bearded god's face."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide dawn shot of the walls of Troy under construction: massive SLOPING cyclopean limestone courses with wooden scaffolding and earthen ramps, mortal work gangs straining; among them two laborers who are more than they seem — a hugely muscled middle-aged mason with grey-streaked dark beard setting a colossal block SINGLE-HANDED while ten men strain at its twin, and on the ridge beyond a tall beautiful beardless golden-haired youth in a plain herdsman's kilt driving cattle, the grass brighter where he walks. Strictly Bronze Age architecture only. Absolutely no text, no lettering anywhere in the image.

### i01-pg20-pn2.png — standard 4:3 — MEDIUM — THE VIEWING PLATFORM
ATTACH (fetch from repo refs/ and attach to the generation): refs/laomedon.png
MATCH LINE: "the crowned Anatolian king on the platform."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: the proud Anatolian king in tall felt crown and embroidered robe stands on a timber viewing platform above the rising wall, gesturing impatiently; beside him a nervous steward holds clay tally-tablets; below and beyond, the two extraordinary laborers pause and look up at the king together — a long level look. Strictly Bronze Age architecture only. Absolutely no text, no lettering anywhere in the image.

### i01-pg20-pn3.png — wide 16:9, letterbox DETAIL SHOT — THE MORTAL STRETCH
ATTACH (fetch from repo refs/ and attach to the generation): refs/poseidon-mortal.png (if cut)
MATCH LINE: "the huge grey-bearded mason regarding the wall."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Letterbox detail shot along the base of the great wall: one short stretch where the blocks are set by ordinary human hands — good work but smaller, mortal work — beside the gigantic god-laid courses; a weathered pious mortal overseer wipes his brow beside it, and the huge grey-bearded mason regards that stretch with a strange knowing look. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg21-pn1.png — standard 4:3 — MEDIUM — THE WAGE DEMANDED
ATTACH (fetch from repo refs/ and attach to the generation): refs/laomedon.png, refs/poseidon-mortal.png, refs/apollo-mortal.png
MATCH LINE: map each: "the enthroned crowned king" / "the huge mason with hand out" / "the golden-haired herdsman beside him."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot in the Anatolian throne room of Troy, painted mudbrick and timber: the two laborers stand before the lounging crowned king with work-worn hands held out for payment; the court smirks behind fans; the king's face is bland contempt. Strictly Bronze Age Anatolian interior. Absolutely no text, no lettering anywhere in the image.

### i01-pg21-pn2.png — close-up 4:3 — THE THREAT
ATTACH (fetch from repo refs/ and attach to the generation): refs/laomedon.png
MATCH LINE: "the crowned king on his feet pointing."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Close shot: the crowned Anatolian king on his feet, finger stabbing forward, face a mask of contempt, gold earrings swinging; torchlight harsh on him. Absolutely no text, no lettering anywhere in the image.

### i01-pg21-pn3.png — tall 2:3 — LOW ANGLE — THE REVEAL BEGINS
ATTACH (fetch from repo refs/ and attach to the generation): refs/poseidon-mortal.png, refs/apollo-mortal.png
MATCH LINE: map each: "the huge mason" / "the golden youth."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tall low-angle shot: the two laborers straightening out of their disguise — not yet full gods, but the torchlight of the hall BENDING toward them, their shadows thrown suddenly enormous and wrong up the walls, courtiers falling back in dawning terror; the mason's eyes beginning to glow sea-green, the youth's hair beginning to shine like the sun; the king alone still not understanding. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg22-pn1.png — wide 16:9 — WIDE — PLAGUE
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide grim shot of a Bronze Age Anatolian city street at sickly noon: smoking funeral pyres, veiled mourners carrying biers, shafts of hard slanting light falling like invisible arrows from a burning white sun; doors marked, streets emptying. Dignified restrained mood, no graphic detail, death conveyed by pyres and veils only. Strictly Bronze Age architecture only. Absolutely no text, no lettering anywhere in the image.

### i01-pg22-pn2.png — wide 16:9 — WIDE — THE KETOS
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot of the Trojan shore: salt flood drowning green fields, and rearing from the waves a vast Bronze Age sea-monster — whale-bulked body, long serpent neck, crocodile jaws — smashing a fishing boat to splinters as tiny figures flee up the beach; storm light. Absolutely no text, no lettering anywhere in the image.

### i01-pg22-pn3.png — standard 4:3 — MEDIUM — THE ORACLE'S PRICE (births HESIONE: crop refs/hesione.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/laomedon.png
MATCH LINE: "the crowned king before the altar."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot in a Trojan temple forecourt with an Anatolian gate-shrine and standing stones, a smoking altar: priests casting marked lots recoil from the answer; the crowned king stands rigid; behind him, unnoticed, a young Anatolian noblewoman with long black hair, layered gown and wide belt goes white as death, her hand rising to her throat. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg23-pn1.png — tall 2:3 — FULL FIGURE — HESIONE AT THE ROCK
ATTACH (fetch from repo refs/ and attach to the generation): refs/hesione.png
MATCH LINE: "the chained princess."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tall full-figure shot: the young Anatolian princess chained by the wrists to a sea rock at the low tideline, gown whipped by wind, chin high, terrified and brave; behind her the sea lies ominously flat to the horizon; far behind on the walls, tiny watching figures. Absolutely no text, no lettering anywhere in the image.

### i01-pg23-pn2.png — wide 16:9 — SILHOUETTE WIDE — THE HERO ARRIVES (births HERACLES & TELAMON: crop refs/heracles.png, refs/telamon.png)
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot on a headland above the shore: against the bright sky, a colossal muscled hero leaning on a huge olive-wood club, a lion's skin worn with the lion's head as a hood, a great bow across his back; beside him a burly broad warrior in a boar's-tusk helmet with a huge body shield; both looking down at the tiny chained figure by the flat sea; their beached war-galley below. Absolutely no text, no lettering anywhere in the image.

### i01-pg23-pn3.png — standard 4:3 — MEDIUM — THE BARGAIN
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/laomedon.png
MATCH LINE: map each: "the lion-hooded hero, arms folded" / "the crowned king, hands spread, desperate."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot on the shore road: the crowned Anatolian king, all silk and desperation, hurries with spread hands toward the mountainous lion-hooded hero who stands unmoved, club grounded like a tree; retainers cowering behind the king; wind rising off the sea. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg24-pn1.png — wide 16:9 — ACTION WIDE — CLUB AGAINST JAWS
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/hesione.png
MATCH LINE: map each: "the lion-hooded hero in the surf" / "the chained princess behind him."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Big action shot: the sea-monster erupting from the shallows over the chained princess, jaws wide — and the lion-hooded hero already planted between them in the surf, his great club meeting the descending jaws in a single colossal impact, spray sheeting in fans, a jagged impact burst at the point of contact. Dynamic ACK action, no gore. Absolutely no text, no lettering anywhere in the image.

### i01-pg24-pn2.png — standard 4:3 — ACTION MEDIUM — THE KILL
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png
MATCH LINE: "the lion-hooded hero astride the monster's neck."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Action medium shot: the hero astride the vast serpent neck of the sea-monster, driving his sword down behind the skull, the huge body thrashing a last white circle of foam; dignified restraint, dark blood minimal and stylized. Absolutely no text, no lettering anywhere in the image.

### i01-pg24-pn3.png — standard 4:3 — QUIET MEDIUM — AFTER
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/hesione.png, refs/telamon.png
MATCH LINE: map each: "the hero snapping the chain" / "the princess steadying herself, regal" / "the boar's-tusk-helmed warrior wading in, unable to look away from her."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet medium shot in the settling surf: the hero snaps the princess's chain between two fingers like thread; she steadies herself on his forearm, regal even now, hair plastered by spray; the burly boar's-tusk-helmed warrior wades in behind, staring at her as if struck. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg25-pn1.png — wide 16:9 — MEDIUM WIDE — CHEATED TWICE
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/telamon.png, refs/laomedon.png
MATCH LINE: map each: "the lion-hooded hero, face darkening" / "the warrior beside him" / "the bland-faced crowned king."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium-wide throne room shot: grooms lead in two ORDINARY bay horses; the crowned king gestures at them with bland generosity from his throne; the lion-hooded hero and his warrior companion stand before him, the hero's face going terribly calm; the court holds its breath. Strictly Bronze Age Anatolian interior. Absolutely no text, no lettering anywhere in the image.

### i01-pg25-pn2.png — close-up 4:3 — THE TERRIBLE CALM
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png
MATCH LINE: "the lion-hooded hero's face."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot of the lion-hooded hero's face: not rage — a terrible quiet certainty, eyes level, jaw set, the lion's teeth framing his brow; faint in the shadowed background behind his head, ghosted, the dim shapes of two cheated laborers from long ago. Absolutely no text, no lettering anywhere in the image.

### i01-pg25-pn3.png — wide 16:9 — WIDE — DEPARTURE
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/telamon.png, refs/hesione.png, refs/laomedon.png
MATCH LINE: map each briefly; the princess watches from the wall, hand at her throat; the king laughs small in the background.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot: the two heroes stride down the shore road toward their beached galley, backs to the city; on the wall above, the young princess watches them go, hand at her throat; small in the background court the crowned king laughs among his courtiers. Strictly Bronze Age architecture only. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg26-pn1.png — wide 16:9 — WIDE — SIX SHIPS
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/telamon.png
MATCH LINE: map each: "at the prow of the lead galley."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide open-sea shot: six Bronze Age war-galleys in line abreast under single square sails, oars beating white, bird-head stem-posts; at the prow of the lead ship the lion-hooded hero stands with his great bow strung, the boar's-tusk-helmed warrior beside him with the huge body shield; spray, speed, purpose. Absolutely no text, no lettering anywhere in the image.

### i01-pg26-pn2.png — wide 16:9 — ACTION WIDE — THE LANDING
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/telamon.png
MATCH LINE: map each.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Action wide shot: keels grinding up a Bronze Age beach, warriors leaping down into the shallows — open-faced conical bronze helmets with cheek-guards and horsehair crests, boar's-tusk helmets, tower shields and round shields, long thrusting spears, absolutely no face-covering Corinthian helmets; horns sounding alarm from massive sloping walls beyond the dunes. Absolutely no text, no lettering anywhere in the image.

### i01-pg26-pn3.png — standard 4:3 — MEDIUM — TOWARD THE SEAM
ATTACH (fetch from repo refs/ and attach to the generation): refs/telamon.png
MATCH LINE: "the boar's-tusk-helmed warrior leading the ram crew."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot in the shadow of the great sloped wall, arrows sleeting down as raiders raise shields overhead: the boar's-tusk-helmed warrior leads a wedge of men carrying a ram-beam at a run toward one particular stretch of smaller, mortal-laid masonry. Strictly Bronze Age architecture only. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg27-pn1.png — tall 2:3 — DRAMATIC LOW ANGLE — THE BREACH
ATTACH (fetch from repo refs/ and attach to the generation): refs/telamon.png
MATCH LINE: "the warrior first through the breach."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tall dramatic low-angle: the mortal-built stretch of wall bursting inward in dust and falling blocks, and through the gap, first of all mankind, the boar's-tusk-helmed warrior — shield up, roaring, lit by the light pouring through the breach. Absolutely no text, no lettering anywhere in the image.

### i01-pg27-pn2.png — standard 4:3 — MEDIUM — THE BLACK MOOD
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png, refs/telamon.png
MATCH LINE: map each: "the lion-hooded hero stopping dead, jealous darkness on his face" / "the warrior ahead in the breach dust."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot just inside the breach: the lion-hooded hero arriving a heartbeat behind — and stopping dead, his face darkening with terrible jealousy at the sight of another man first in glory, his hand tightening white on his sword hilt; the warrior ahead of him half-turned in the dust. Absolutely no text, no lettering anywhere in the image.

### i01-pg27-pn3.png — standard 4:3 — MEDIUM — THE ALTAR OF STONES
ATTACH (fetch from repo refs/ and attach to the generation): refs/telamon.png, refs/heracles.png
MATCH LINE: map each: "the warrior on one knee piling stones" / "the hero above him, the shadow passing into a laugh."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: the quick-thinking warrior drops to one knee and urgently piles loose breach-stones into a rough heap — an altar — palms raised over it in dedication; above him the lion-hooded hero's thunderous face is just breaking, despite itself, into a great laugh. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg28-pn1.png — wide 16:9 — WIDE — THE CITADEL FALLS
ATTACH (fetch from repo refs/ and attach to the generation): refs/laomedon.png
MATCH LINE: "the crowned king at bay on the palace steps, now in armor."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide chaotic shot of the Trojan citadel court: Trojan spearmen falling back through smoke; on the palace steps the crowned king, now in Anatolian scale armor over his robes, at bay with his grown sons around him, spears leveled; raiders pouring in at the edges. Strictly Bronze Age architecture, open-faced helmets only. Dignified restraint, no gore. Absolutely no text, no lettering anywhere in the image.

### i01-pg28-pn2.png — standard 4:3 — MEDIUM — PAYMENT IN FULL
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png
MATCH LINE: "the lion-hooded hero drawing the great bow."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot: the lion-hooded hero draws his great bow at short range, terrible and unhurried, the arrowhead a point of light; beyond his shoulder, out of focus, the armored king frozen mid-shout on the steps. Absolutely no text, no lettering anywhere in the image.

### i01-pg28-pn3.png — standard 4:3 — QUIET MEDIUM — THE LAST SON (births PODARCES: crop refs/podarces.png)
ATTACH (fetch from repo refs/ and attach to the generation): refs/heracles.png
MATCH LINE: "the lion-hooded hero looking down at the boy."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Quiet aftermath shot on the palace steps: fallen armored figures composed and dignified, faces hidden, no blood; smoke drifting; alone alive among them a solemn boy of about ten in a short Anatolian tunic with a small gold pendant stands over his father's body, a child's knife shaking in his fist, facing the mountainous lion-hooded hero who looks down at him. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg29-pn1.png — wide 16:9 — MEDIUM WIDE — THE PRIZE OF HONOR
ATTACH (fetch from repo refs/ and attach to the generation): refs/telamon.png, refs/hesione.png, refs/podarces.png
MATCH LINE: map each: "the warrior with the princess beside him" / "the boy among the captives, looking at her."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium-wide shot in the ordered citadel court: captives assembled with dignity; the boar's-tusk-helmed warrior stands with the young princess given to him as prize of honor beside him; across the court her small brother stands among the captives; brother and sister looking at each other. Absolutely no text, no lettering anywhere in the image.

### i01-pg29-pn2.png — standard 4:3 — MEDIUM — THE VEIL
ATTACH (fetch from repo refs/ and attach to the generation): refs/hesione.png, refs/podarces.png, refs/heracles.png, refs/telamon.png
MATCH LINE: map each: "the princess holding her veil out over the boy's head" / "the hero watching arms folded" / "the warrior nodding."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Medium shot, the formal ransom gesture: the princess draws the veil from her own hair and holds it out at arm's length over the boy's bowed head; the lion-hooded hero watches with arms folded, the boar's-tusk-helmed warrior nods assent; the watching captives and raiders utterly silent. Absolutely no text, no lettering anywhere in the image.

### i01-pg29-pn3.png — close-up 4:3 — THE NAMING
ATTACH (fetch from repo refs/ and attach to the generation): refs/podarces.png
MATCH LINE: "the boy's solemn face beneath the held veil."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Extreme close shot: the solemn face of the boy beneath the held veil, its shadow falling across his eyes, his jaw set, tears refused; the small gold pendant at his throat catching light. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg30-pn1.png — wide 16:9 — WIDE — WEST TO SALAMIS
ATTACH (fetch from repo refs/ and attach to the generation): refs/hesione.png, refs/telamon.png
MATCH LINE: map each: "the princess at the stern rail looking back."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Wide shot at sea: six galleys pulling away from a smoking shoreline; at the stern rail of the last ship the young Anatolian princess stands beside the boar's-tusk-helmed warrior, looking back at the burning city until it is small; on the far beach, tiny, a crowned child alone. Absolutely no text, no lettering anywhere in the image.

### i01-pg30-pn2.png — tall 2:3 — THE BOY KING
ATTACH (fetch from repo refs/ and attach to the generation): refs/podarces.png
MATCH LINE: "the boy crowned on the scorched throne."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Tall shot amid the rubble of the citadel court: the small boy seated on a fire-scorched stone throne far too large for him, a thin gold circlet on his brow, the gold pendant on his chest, elders of the survivors kneeling before him in the ash; through the broken roof one clean shaft of light falls on the child alone. Strictly Bronze Age architecture. Absolutely no text, no lettering anywhere in the image.

### i01-pg30-pn3.png — wide 16:9, letterbox — THE UNAPPEASED
ATTACH (fetch from repo refs/ and attach to the generation): refs/zeus.png (style only, do not depict Zeus)
MATCH LINE: "divine faces in the manner of the attached radiant god style, but one sea-grey and one golden."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Letterbox shot of storm clouds high above a small walled city on a plain: half-formed in the cloud masses, faint and patient, two vast watching divine faces — one wild-bearded and sea-grey, one young and coldly golden — neither angry nor appeased, simply waiting; below, tiny scaffolding on the city wall where men rebuild one stretch of masonry. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg31-pn1.png — wide 16:9 — FRAME, WIDE — [twilight palette]
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png, refs/neleid-prince.png
MATCH LINE: map each.
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Wide shot of the Miletus hall, late: the fire burned to embers, lamps low; the blind bard lowering his phorminx to his knee; the audience silent, some staring into the coals; the young noble on the high seat with his chin on his fist. Absolutely no text, no lettering anywhere in the image.

### i01-pg31-pn2.png — standard 4:3 — FRAME, MEDIUM TWO-SHOT — [twilight palette]
ATTACH (fetch from repo refs/ and attach to the generation): refs/neleid-prince.png, refs/singer.png
MATCH LINE: map each: "the young noble asking quietly" / "the bard answering."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Medium two-shot by ember-light: the young noble leaning forward asking something quietly, palms open; the blind bard's lined face turned toward him, gentle and grave. Absolutely no text, no lettering anywhere in the image.

### i01-pg31-pn3.png — standard 4:3 — FRAME, CLOSE — [twilight palette]
ATTACH (fetch from repo refs/ and attach to the generation): refs/singer.png
MATCH LINE: "the bard's face lifted toward the doorway."
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Close shot: the blind bard's face lifted toward the open doorway of the hall and the white stars over the dark Aegean beyond it, a faint smile, the phorminx silent against his chest. Absolutely no text, no lettering anywhere in the image.

---

### i01-pg32-pn1.png — full page 3:4 — THE GNOME PAGE — [twilight palette]
ATTACH: none
PROMPT: Classic 1970s Amar Chitra Katha comic book art style: bold black ink outlines with rich fine linework and delicate hatching, warm flat-toned color fills, detailed dignified rendering, heroic realistic anatomy, dignified expressive faces, clean composition. Limited twilight palette only: sepia, umber, dusk-blue, lamplight gold. Full-page quiet composition: the Iron Age hall empty of people, the hearth down to red embers, the carved stool with the silent phorminx leaning against it in a pool of lamplight; through the open doorway the star-white night sky over a dark calm sea. Leave the upper third of the image calm and uncluttered for a large ornamented text panel. Absolutely no text, no lettering anywhere in the image.

---
END OF ISSUE 1 PROMPTS. When all art through pg32 exists: send the art+refs zip and say "grand build."
