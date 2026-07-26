# Releases

Finished, reader-facing PDF builds of The Trojan Cycle, one file per issue.

## Naming convention
- Final builds: `Issue-NN-<Title>.pdf` — fully lettered per the house pipeline (caption bands, in-art face-safe balloons, gnome plates).
- Incremental builds: `Issue-NN-<Title>-INCREMENTAL-pgAA-BB.pdf` — draft assemblies of the pages whose art exists so far. Draft mode renders dialogue as attributed boxes rather than in-art balloons, and every page carries a draft footer. Each incremental file is REPLACED in place as more art lands, and finally replaced by the final build (the `-INCREMENTAL-` file is then deleted in the same commit).

## Current contents
| File | Status |
|---|---|
| Issue-01-The-Burden-of-the-Earth.pdf | FINAL — 32 pages, fully lettered |
| Issue-02-The-Swan-and-the-Egg-INCREMENTAL-pg01-09.pdf | INCREMENTAL — pages 1–9 (art through pg09); pg07 panels are the verified regenerations |

Large finished issues may additionally be attached to GitHub Releases to keep clone size manageable; this folder always holds the current canonical build.
