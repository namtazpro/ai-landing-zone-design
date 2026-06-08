# Open questions (OQs)

Per-question records for unresolved design topics. The main HLD §17 carries the complete index.

## File shape

Every OQ lives in one file named `OQ-NNN-<slug>.md` with this frontmatter:

```yaml
---
id: OQ-NNN
title: <human-readable title>
status: Open | Investigating | Resolved | Withdrawn
created: <YYYY-MM-DD>
last_revised: <YYYY-MM-DD>
hld_sections: [<new-section-slug>, ...]
blocks_kdds: [<KDD-NNN>, ...]
tags: [<tag>, ...]
---
```

Body sections, in order:

- `## Question` — the unresolved question, ideally as a single sentence.
- `## Why it matters` — the consequence of leaving it unresolved.
- `## Resolution path` — the steps needed to close it.
- `## Source` — the date, speaker, and ≤25-word quote (or a note that it is not directly attributable to a transcript).

## Lifecycle

- `Open` — captured from a meeting or review, no work in flight.
- `Investigating` — work in flight, owner identified.
- `Resolved` — closed. Add a line referencing the KDD that captures the answer, then move the file to an `archive/` subfolder (or mark and leave in place).
- `Withdrawn` — no longer relevant. Keep the file for audit; explain in a final note.

## Promotion to a KDD

When an OQ closes:

1. Author a KDD with the decision sentence.
2. Set the OQ status to `Resolved` and link to the KDD in the file.
3. Update the HLD section that previously referenced the OQ to point at the KDD instead.
