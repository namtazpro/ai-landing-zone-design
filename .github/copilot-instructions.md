# OCTA Agentic Platform — working agreement for AI sessions

This repository is the **living architecture workspace** for an Enterprise Architect
office. It is iterated continuously as new assets arrive (Teams call transcripts,
direct architect requests, diagrams). Treat every session as a **continued
conversation**, not a fresh start.

## Start every session here

1. Read the iteration log: [new-structure/docs/CHANGELOG.md](../new-structure/docs/CHANGELOG.md).
   Its **Current state** table and top checkpoint tell you where the last session left off.
2. Confirm the highest `KDD-NNN` and `OQ-NNN` IDs against
   [new-structure/decisions/](../new-structure/decisions/) and
   [new-structure/open-questions/](../new-structure/open-questions/) before assigning new ones.
3. Skim [new-structure/README.md](../new-structure/README.md) and the per-folder READMEs
   for the conventions if anything is unclear.

## Canonical locations

- Working HLD: `new-structure/docs/HLD.md` (ALZ design-area model). **Edit here.**
- KDDs: one file each in `new-structure/decisions/` (`KDD-NNN-<slug>.md`).
- OQs: one file each in `new-structure/open-questions/` (`OQ-NNN-<slug>.md`).
- Direct architect asks: log under `new-structure/requests/`.
- Assets: `new-structure/assets/` with the machine index `assets/index.json`.
- Root `HLD-old.md` is the **deprecated v0.1 baseline — do not use or modify.**

## How to handle each input

- **New transcript** (dropped in `transcripts/`) → ingest decisions, append KDDs and OQs
  continuing the global counters, patch only the affected HLD sections. Use the
  `ailz-ingest-transcript` skill flow.
- **Direct architect request** → treat the request as a decision source. Record a KDD with
  `Source: direct request — <name>, <date>`, and log the ask under `new-structure/requests/`.
- **New diagram / deck** → register via `ailz-ingest-diagram` (update `assets/index.json`)
  and link it into the relevant HLD section.
- **HLD / LLD edits** → incremental via `ailz-author-hld` / `ailz-author-lld`. Never full
  rewrites. Keep diffs reviewable.

## End every iteration here

When a session materially changes the HLD, a KDD, or an OQ:

1. Append a checkpoint entry at the top of the Checkpoints list in
   [new-structure/docs/CHANGELOG.md](../new-structure/docs/CHANGELOG.md), using the template there.
2. Update that file's **Current state** table (HLD version/date, highest KDD/OQ IDs,
   transcripts ingested).
3. Bump `Status` / `Version` / `Last updated` in `new-structure/docs/HLD.md` if the HLD changed.

Do this without being asked — it is what lets the next session resume cleanly.

## Conventions (summary)

- KDD/OQ IDs are zero-padded 3 digits, monotonically increasing across the repo lifetime.
  Always check the current max first.
- A changed decision sentence creates a new **superseding** KDD, not an in-place edit.
  Editorial wording changes edit in place and bump `last_revised`.
- KDD `Source` rows carry: date + speaker/requester + a verbatim quote of 25 words or fewer.
- When an OQ closes, **promote it to a KDD** and update references.
- HLD references to KDDs/OQs link to the per-file artefacts, not to HLD anchor links.
- Tentative decisions stay tagged `Tentative` until ratified by a later call.
- Markdown follows concise prose, ATX headings, no emoji, and workspace-relative links
  (never backtick-wrapped file names).

## Tooling note

`pandoc`, `python-docx`, `python-pptx`, and `markitdown` are not installed and terminal
`pip install` is blocked. Extract `.docx`/`.pptx` with PowerShell
`[System.IO.Compression.ZipFile]` plus a regex XML strip, or install packages via the
`install_python_packages` tool when Python parsing is needed.
