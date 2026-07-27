# Codex Art Agent

Reusable instructions for generating Trojan Cycle artwork from repository prompts, canonical references, and pull-request branches.

## How to invoke

Give Codex this file as its operating instructions, then provide only the task inputs:

```text
Repository: https://github.com/kartheeque/trojan-cycle
Original PR: <PR number or URL>
Panels:
- <panel filename>
- <panel filename>
```

Example:

```text
Use docs/CODEX_ART_AGENT.md.

Original PR: #17
Panels:
- i02-pg10-pn1.png
- i02-pg10-pn2.png
```

The original PR is required because prompts or references may differ from `main`. Codex must discover the prompt file, output directory, aspect ratio, attachments, match mappings, regeneration notes, and any reference-birth instructions from the repository.

## Mission

For every requested panel:

1. inspect the original PR;
2. use the original PR head commit as the authoritative source;
3. create a new Codex branch from that exact commit;
4. locate and interpret the canonical panel block;
5. load all repository reference images named by the prompt;
6. generate one finished panel at the declared aspect ratio;
7. verify it against every positive and negative prompt clause;
8. create any explicitly declared new references by cropping the accepted panel;
9. commit only intended generated artwork and additive reference files;
10. push the Codex branch;
11. open a separate stacked PR whose base is the original PR head branch.

Never commit directly to another developer's PR branch.

## Non-negotiable invariants

- The original PR head branch and head SHA are the source of truth.
- Never begin from `main` when the task is based on an open PR.
- Never push to the original PR branch, its base branch, or `main`.
- Never rewrite canonical prompts to compensate for a poor generation.
- Never invent, substitute, or web-search a missing repository reference.
- Never modify, replace, rename, copy, or delete an existing file under `refs/`.
- New files under `refs/` are permitted only when the panel explicitly declares a reference birth.
- Stop rather than guess when a prompt, attachment, dependency, or identity mapping is ambiguous.

## Branching and stacked PR workflow

Resolve the original PR metadata, including:

- repository;
- PR number and URL;
- head repository or fork;
- head branch;
- head SHA;
- base branch.

Fetch and check out the exact original PR head commit. Verify the local commit matches the recorded SHA.

Create a new branch from that commit, for example:

```text
codex/generate-i02-pg10-panels
```

For a single panel:

```text
codex/generate-i02-pg10-pn1
```

Verify ancestry before changing files:

```bash
git merge-base --is-ancestor <ORIGINAL_PR_HEAD_SHA> HEAD
```

The final pull request must be stacked as follows:

```text
Codex art branch
    -> original PR head branch
        -> original PR base branch
```

Open the Codex PR against the original PR head branch, not against `main`, unless the original PR head branch itself is `main`.

## Repository discovery

Before generating anything, inspect the repository for:

- `AGENTS.md` or nested agent instructions;
- contribution rules;
- methodology or verification documents;
- issue-specific prompt files;
- `refs/` or equivalent canonical-reference directories;
- artwork output directories;
- naming, commit, and PR conventions.

Instructions nearest the target files take precedence unless they conflict with this specification or the operator's explicit request.

## Canonical panel extraction

Search repository prompt files for a heading containing the exact requested filename.

Read the complete panel block from that heading up to the next panel heading or section boundary. Extract and preserve:

- exact filename;
- title;
- aspect ratio and orientation;
- `ATTACH` paths;
- complete `PROMPT` text, which is the fenced ```text block immediately following the `PROMPT:` label;
- any `MATCH-REVIEW` warning;
- regeneration notes;
- dependency notes;
- `REF-BIRTH` or equivalent instructions.

Do not paraphrase, shorten, improve, normalize, or silently correct the canonical prompt. Submit the complete prompt intact to the image-generation system.

### Block format

Panel blocks are normalized so the fenced block is copy-paste ready with no editing. Inside it, in order:

1. an explicit aspect-ratio directive;
2. the reference-identity instruction, stating positionally which attached image is which subject;
3. the canonical prompt text.

Submit the entire fenced block verbatim. Because the identity mapping now travels inside the prompt, there is no separate `MATCH LINE` to apply — but the attachments must still be supplied in the order given by `ATTACH`, since the identity instruction refers to them positionally as the first, second and third attached image.

`tools/normalize_prompts.py` regenerates this form and is idempotent; a block that already contains a fenced block is left untouched.

If the same filename appears in multiple candidate files and authority cannot be established confidently, stop and report the ambiguity.

## Prompt semantics

Treat the canonical block as follows:

- `PROMPT`: authoritative visual instruction.
- `ATTACH`: mandatory binary image inputs.
- reference-identity line inside the fenced block: authoritative mapping between attachments and depicted subjects, keyed to `ATTACH` order.
- `MATCH-REVIEW`: the mapping could not be derived automatically and the original shorthand is preserved inside the block. This is an ambiguous identity mapping — stop and report rather than guessing the order.
- panel heading: authoritative filename, framing, orientation, and aspect ratio.
- regeneration notes: mandatory defect-avoidance requirements.
- negative clauses: equally binding as positive clauses.
- methodology documents: additional verification requirements.

Do not infer panel content from the filename.

## Reference handling

For every path listed in `ATTACH`:

1. resolve it within the checked-out original PR branch;
2. verify it exists and is a readable image;
3. inspect its format and dimensions;
4. load the actual binary image;
5. pass it to the generation tool;
6. map it to the intended person or object using `MATCH LINE`.

Never substitute:

- a web result;
- a generated approximation;
- a similarly named file;
- a screenshot of a file browser;
- a cached image from another task;
- a version from `main` when the PR branch differs.

Repository references are authoritative for identity and continuity. The written prompt is authoritative for scene, costume, age, pose, action, expression, setting, lighting, and composition unless the repository explicitly says otherwise.

If any mandatory reference is missing or the image-generation system cannot accept it as an image input, stop.

## Dependencies

Some panels depend on references created by earlier panels.

When a required attachment does not yet exist:

- identify the missing dependency;
- locate the earlier reference-birth panel when possible;
- do not fabricate the reference;
- do not generate the dependent panel unless the prerequisite is included in the task and the repository workflow permits using the newly created reference.

Process multi-panel tasks in valid dependency order.

## Image generation

For each panel, submit:

- the canonical prompt verbatim;
- every mandatory attached image;
- explicit identity mappings from `MATCH LINE`;
- the declared aspect ratio;
- repository-required generation settings.

Generate one finished image per requested panel.

Do not produce contact sheets, storyboards, debug composites, prompt previews, multiple alternatives in one file, or visible metadata. Unless explicitly requested by the canonical prompt, the artwork must contain no text, lettering, signatures, logos, captions, watermarks, panel numbers, or speech balloons.

Generate natively at the requested ratio. Do not crop a wrongly shaped generation in a way that removes important content.

## Verification and regeneration

Audit the generated image against the full canonical block before accepting it.

Check at minimum:

### Prompt fidelity

- scene, action, mood, framing, and shot type;
- all important positive details;
- every explicit negative clause;
- all regeneration-specific corrections.

### Character continuity

- each attachment maps to the correct subject;
- faces remain recognizable;
- apparent age, hair, beard, headwear, and distinctive features remain consistent;
- characters are not swapped or duplicated accidentally.

### Counts and anatomy

- required counts of people, infants, animals, ships, props, and objects;
- no accidental duplicates or additions;
- plausible hands, fingers, limbs, and body connections;
- no fused, detached, missing, or duplicated anatomy.

### Historical and environmental accuracy

- requested architecture, clothing, plants, weapons, ships, furniture, and ritual objects;
- no prohibited cultural or chronological intrusions;
- no forbidden modern, classical, medieval, Victorian, or New World elements.

### Composition

- correct orientation and ratio;
- focal action is readable;
- reference characters are large enough to verify;
- no important subject is unintentionally cropped.

### Textlessness

- no accidental words, letters, numbers, signs, logos, signatures, or watermarks.

Regenerate when a material requirement fails. Do not weaken the prompt. If repeated attempts still fail a critical requirement, stop and report the unresolved defect rather than committing known-bad artwork.

## REF-BIRTH: additive reference creation

A panel may explicitly declare that it creates a new canonical reference, for example:

```text
REF-BIRTH: refs/example-character.png
```

When such an instruction exists, Codex may crop the accepted generated panel and save the declared new reference.

### Existing refs are immutable

Before creating a reference, check the destination in the original PR head commit, working tree, and Git index.

If the destination already exists in any form:

- do not overwrite it;
- do not alter it;
- do not rename it;
- do not create a numbered replacement;
- report the collision.

Reference changes are strictly additive.

### Crop source and method

Create the reference only from the accepted panel that explicitly declares the reference birth. Do not redraw or regenerate the face as a separate reference.

Use deterministic local image processing such as Pillow or ImageMagick. Automated face detection may assist, but visual inspection remains mandatory.

Identify the correct subject using the panel prompt, match mappings, reference-birth declaration, and the image itself. If identity is ambiguous, do not create the crop automatically.

### Crop composition

Follow existing `refs/` conventions. The crop should normally contain:

- the entire head and hair;
- all canonical crowns, helmets, veils, diadems, or beards;
- neck and shoulders where visible;
- modest upper clothing;
- a small margin around the subject;
- no unrelated face.

Do not cut through the chin, forehead, hair, beard, crown, helmet, veil, or shoulders.

Preserve source colour and detail. Do not apply beauty filters, facial alteration, generative enhancement, or stylistic repainting. High-quality resizing is allowed.

When no clear repository convention exists, use a portrait crop with at least 512 pixels on its shortest side when practical.

### Reference QA

Open and inspect every saved crop. Verify:

- correct subject;
- recognizable face;
- preserved age and canonical features;
- sufficient sharpness;
- no unrelated person;
- exact declared filename;
- readable image file;
- no text, border, or watermark;
- destination did not previously exist.

### Mechanical diff guard

Before committing, verify that every path under `refs/` is an addition only:

```bash
git diff --name-status <ORIGINAL_PR_HEAD_SHA>...HEAD -- refs/
```

Only status `A` is permitted. Statuses `M`, `D`, `R`, and `C` are forbidden.

Use a mechanical guard when possible:

```bash
git diff --name-status <ORIGINAL_PR_HEAD_SHA>...HEAD -- refs/ |
awk '$1 != "A" { bad=1; print } END { exit bad }'
```

If any existing reference appears changed, restore it before proceeding.

A PR that adds a reference birth should normally remain a draft until a human verifies the crop.

## Output and scope control

Determine output paths from repository conventions and save every accepted panel under its exact requested filename.

Do not silently overwrite accepted artwork. When regeneration is requested, preserve only what repository policy requires and ensure the final diff contains the intended replacement.

Normally modify only:

- requested artwork files;
- explicitly declared new reference files.

Do not modify prompts, existing references, methodology files, scripts, layouts, unrelated art, or issue metadata unless explicitly requested.

Delete or exclude rejected generations, previews, caches, and temporary files before committing.

## Commit and push

Review scope before staging:

```bash
git status --short
git diff --stat
git diff --name-status
```

Stage only intended files. Use a focused commit message such as:

```text
art(issue-02): generate page 10 panels
```

or:

```text
art(issue-02): generate i02-pg10-pn1
```

Never amend or rewrite commits belonging to the original PR. Never force-push.

Push only the new Codex branch.

## Pull request

Open a separate PR with:

- base: original PR head branch;
- head: new Codex branch;
- draft status when human visual review, reference approval, or uncertainty remains.

The PR description must include:

- original PR number and URL;
- original PR head branch and head SHA;
- requested panel filenames;
- canonical prompt files used;
- attached reference paths for each panel;
- generated output paths and pixel dimensions;
- QA summary and regeneration attempts;
- newly created reference paths and source panels;
- confirmation that no existing reference was changed;
- known limitations or unresolved uncertainty;
- confirmation that prompts and methodology files were not modified.

## Final report

Report:

- original PR URL, head branch, and head SHA;
- new Codex branch;
- panels generated;
- prompt files and attachments used;
- output paths and dimensions;
- newly created refs and source panels;
- commit SHA;
- stacked PR URL and base branch;
- draft or ready-for-review status;
- concise QA findings;
- blocked panels or unresolved issues.

Do not report success unless the images were actually generated with their mandatory attachments, committed on the new branch, pushed, and submitted through a separate PR.

## Failure conditions

Stop and report clearly when:

- the original PR or head commit cannot be resolved;
- the requested panel cannot be found;
- the canonical prompt is ambiguous;
- a mandatory reference is missing;
- a dependency has not been created;
- the generation tool cannot accept image references;
- image generation or local image processing is unavailable;
- output cannot be written;
- safe branch or stacked-PR creation is impossible;
- a requested reference path already exists;
- the final diff contains unrelated changes.

Do not fall back to another branch, modify another developer's branch, invent assets, or pretend a plan is a completed generation.
