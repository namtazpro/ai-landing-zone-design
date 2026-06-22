# Iteration log — OCTA Agentic Platform design

Structured checkpoint trail for the design workspace. Every working session that
materially changes the HLD, KDDs, or OQs appends one entry at the top of the
[Checkpoints](#checkpoints) list. A session **starts** by reading the most recent
checkpoint, so work resumes as a continued conversation instead of being re-inferred.

This log is the human- and agent-readable resume entrypoint. The per-file KDD and OQ
artefacts plus `git log` remain the authoritative history; this file is the fast index.

## Current state

| Field | Value |
| --- | --- |
| Canonical HLD | [HLD.md](HLD.md) |
| HLD version | 0.2 (ALZ-aligned restructure) |
| HLD last updated | 2026-06-08 |
| Highest KDD | KDD-028 → next new decision is **KDD-029** |
| Highest OQ | OQ-020 → next new open question is **OQ-021** |
| Source baseline | [20260514 Agentic platform_vF.pptx](../assets/decks/20260514%20Agentic%20platform_vF.pptx) (14 May 2026) |
| Transcripts ingested | 22 May 2026 (Foundry/MCP support call); 26 May 2026 (Contoso/Microsoft check-in) |
| Customer requirements docs ingested | 2 June 2026 (AI Observability HLR / DR — Mitie / Pankaj Arora) |
| LLD | Not yet authored |

Keep this table in sync with the latest checkpoint below.

## How to use this log

Session start:

1. Read the **Current state** table and the top checkpoint below.
2. Confirm the highest KDD/OQ IDs against [../decisions/](../decisions/) and
   [../open-questions/](../open-questions/) before assigning new ones.

Per iteration (new transcript, direct request, or new asset):

1. Do the work per the workspace conventions (see
   [new-structure/README.md](../README.md) and the per-folder READMEs).
2. Append a new checkpoint entry at the top of the list using the template below.
3. Update the **Current state** table (HLD version/date, highest KDD/OQ IDs,
   transcripts ingested).
4. Bump `Status` / `Version` / `Last updated` in [HLD.md](HLD.md) when the HLD changed.

## Checkpoint entry template

```markdown
### YYYY-MM-DD — <short title>

- Trigger: <transcript name | direct request — name | new asset>
- KDDs: <added KDD-NNN..NNN | none> ; <superseded/closed if any>
- OQs: <added OQ-NNN..NNN | none> ; <closed/promoted if any>
- HLD sections touched: <§ slugs or "none">
- Assets: <registered diagrams/decks or "none">
- Next up: <what the following session should pick up>
```

## Checkpoints

### 2026-06-22 — AI Observability requirements response added

- Trigger: direct request — convert `assets/AI Observability - HLR and Detailed Requirements.docx` into a workable markdown tracker that pairs every requirement and risk with the Microsoft solution proposition.
- KDDs: none added. Highest remains KDD-028.
- OQs: none added. Highest remains OQ-020. Six candidate OQs are listed in section 10 of the new tracker and should be promoted to OQ files when picked up (covering ServiceNow / SLA model, Purview Compliance Manager licensing, vendor list for low-code / external agents, performance / availability / DR targets, bias monitoring approach, schema extension governance).
- HLD sections touched: none. The HLD is not edited by this iteration; the tracker references it as the layered architecture baseline.
- Assets: registered the source `.docx` (legacy binary `.doc` despite the extension) in `assets/index.json` under a new `documents` collection; added `new-structure/responses/` with `README.md` and the working tracker `ai-observability-solution-mapping.md`.
- Microsoft proposition baseline (per direct request): Agent365 (Entra Agent ID), Microsoft Foundry Control Plane, and Azure API Management AI Gateway, supported by Azure Monitor, Microsoft Fabric (lakehouse + Data Agent), Microsoft Purview, Microsoft Sentinel, Defender for Cloud, and Power BI.
- Next up: walk the tracker with the customer, promote the six open items in section 10 to OQ files, and decide whether any Microsoft-side commitments (for example Agent365 as the registration plane) should be ratified as new KDDs.

### 2026-06-16 — GitHub Pages documentation site added

- Trigger: direct request — publish HLD, KDDs, and OQs as a GitHub Pages site for the EA office.
- KDDs: none added. Highest remains KDD-028.
- OQs: none added. Highest remains OQ-020.
- HLD sections touched: none.
- Assets: added MkDocs Material site (`mkdocs.yml`, `new-structure/index.md`),
  generated index pages (`decisions/index.md`, `open-questions/index.md`) via
  `new-structure/scripts/build_indexes.py`, and a Pages deploy workflow
  (`.github/workflows/docs.yml`). Site publishes only `new-structure/`.
- Cleanup: root flat draft renamed to `HLD-old.md` (deprecated, excluded from the
  site); all in-repo links repointed away from it.
- Next up: enable GitHub Pages (Settings → Pages → Source: GitHub Actions) and set
  `site_url` / `repo_url` in `mkdocs.yml` once the repo URL is known.

### 2026-06-16 — Baseline checkpoint established

- Trigger: direct request — set up a structured iteration log so sessions resume cleanly.
- KDDs: none added. Highest remains KDD-028.
- OQs: none added. Highest remains OQ-020.
- HLD sections touched: none.
- Assets: none.
- Next up: ingest the next Teams transcript or process the next architect request;
  start numbering at KDD-029 / OQ-021.

### 2026-06-08 — ALZ-aligned restructure (recorded retrospectively)

- Trigger: workspace restructure into the ALZ design-area model.
- KDDs: 28 decisions split into per-file records under [../decisions/](../decisions/).
- OQs: 20 questions split into per-file records under [../open-questions/](../open-questions/).
- HLD sections touched: full restructure into 19 ALZ sections; HLD moved to
  [HLD.md](HLD.md) at version 0.2. Root flat draft deprecated and renamed `HLD-old.md`.
- Assets: source deck and transcripts referenced from the repository root.
- Next up: continue incremental updates against the new structure.
