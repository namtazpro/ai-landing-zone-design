# OCTA Agentic Platform — Architecture

Welcome to the architecture site for the **OCTA Agentic Platform**, the Azure target
architecture for the Contoso / Microsoft engagement. This site is maintained by the
Enterprise Architecture office and is regenerated from the design workspace on every
change.

## Start here

<div class="grid cards" markdown>

- :material-file-document-outline: **[High-Level Design](docs/HLD.md)**

    The full HLD, structured around the Azure Landing Zone design areas.

- :material-gavel: **[Key Design Decisions](decisions/index.md)**

    Every binding decision (KDD) with context, consequences, and its source call.

- :material-help-circle-outline: **[Open Questions](open-questions/index.md)**

    Outstanding questions (OQs) and the decisions they block.

- :material-history: **[Iteration Log](docs/CHANGELOG.md)**

    Checkpoint trail showing what each working session changed.

</div>

## How this site is maintained

The platform design is a **living artefact**. New Teams call transcripts, direct
architect requests, and diagrams are folded in as iterations. Each iteration:

- appends Key Design Decisions and Open Questions with monotonically increasing IDs,
- patches only the affected High-Level Design sections, and
- records a checkpoint in the [Iteration Log](docs/CHANGELOG.md).

The Decisions and Open Questions index tables on this site are generated from the
per-record source files, so they always reflect the current state of the workspace.
