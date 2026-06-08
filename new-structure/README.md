# PRIO Agentic Platform — Design workspace (new structure)

ALZ-aligned restructure of the AI Landing Zone design workspace. The previous flat draft survives at the repository root as [../HLD.md](../HLD.md); this folder is the working artefact going forward.

## Layout

| Folder / file | Purpose |
| --- | --- |
| [docs/HLD.md](docs/HLD.md) | The High-Level Design, restructured around the Azure Landing Zone design areas (19 sections). |
| [docs/](docs/) | Future home of LLD, compliance matrix, and other top-level documents. |
| [sections/hld/](sections/hld/), [sections/lld/](sections/lld/) | Optional per-section split of HLD/LLD content. Empty placeholders for now. |
| [decisions/](decisions/) | One file per KDD (`KDD-NNN-<slug>.md`). See [decisions/README.md](decisions/README.md) for file shape and history handling. |
| [open-questions/](open-questions/) | One file per open question (`OQ-NNN-<slug>.md`). See [open-questions/README.md](open-questions/README.md) for file shape and lifecycle. |
| [requests/](requests/) | Log of direct user asks (empty). |
| [assets/diagrams/hld/](assets/diagrams/hld/), [assets/diagrams/lld/](assets/diagrams/lld/) | Diagram source files (drawio, Mermaid, PNG, SVG). |
| [assets/decks/](assets/decks/) | Slide-deck-derived assets. |
| [assets/index.json](assets/index.json) | Machine-readable asset index consumed by the `ailz-*` skills. |
| [scripts/](scripts/) | Workspace utility scripts (empty). |
| [.ailz/config.json](.ailz/config.json), [.ailz/template-version](.ailz/template-version) | Workspace identity for the `ailz-*` skills. |
| [.copilot-tracking/](.copilot-tracking/) | Reserved for tracking artefacts. |

## Conventions

- **Markdown** — follows the hve-core writing-style and markdown rules. Concise prose, ATX headings, no emoji. File links use workspace-relative paths, never backtick-wrapped names.
- **Transcripts and source deck** stay at the repository root and are referenced via relative paths from this folder.
- **Decision records** follow the shape described in [decisions/README.md](decisions/README.md): frontmatter + Context / Decision / Consequences / Source. No revisions section — `git log` carries history. Decision sentence changes create a new superseding KDD.
- **Open questions** follow the shape in [open-questions/README.md](open-questions/README.md). When an OQ closes, promote it to a KDD and update the references.
- **HLD references** to KDDs and OQs always link to the per-file artefacts under [decisions/](decisions/) and [open-questions/](open-questions/), not to anchor links inside the HLD itself.

## Relationship to root files

- [../HLD.md](../HLD.md) is the previous flat draft (v0.1, single file, 19 sections inline with KDD/OQ tables). Kept as a baseline. Do not modify.
- [../README.md](../README.md), [../20260514 Agentic platform_vF.pptx](../20260514%20Agentic%20platform_vF.pptx), [../transcripts/](../transcripts/), and [../recommendations/](../recommendations/) remain at the repository root. This folder references them via relative paths.
