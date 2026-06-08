# Key Design Decisions (KDDs)

Per-decision records that bind the HLD ([docs/HLD.md](../docs/HLD.md)) to specific call transcripts and decision sentences. The main HLD §16 carries the complete index.

## File shape

Every KDD lives in one file named `KDD-NNN-<slug>.md` with this frontmatter:

```yaml
---
id: KDD-NNN
title: <human-readable title>
status: Proposed | Tentative | Decided | Superseded | Deprecated
supersedes: null | KDD-NNN
superseded_by: null | KDD-NNN
created: <YYYY-MM-DD>
last_revised: <YYYY-MM-DD>
hld_sections: [<new-section-slug>, ...]
tags: [<tag>, ...]
---
```

Body sections, in order:

- `## Context` — the problem the decision addresses.
- `## Decision` — the decision sentence (verbatim from the source whenever possible).
- `## Consequences` — material implications. Brief.
- `## Source` — a ≤25-word verbatim quote, the date, the speaker(s), and a link to the transcript.

## History handling

- **Editorial change** (clarifies wording without changing intent): edit in place, bump `last_revised`, write a normal git commit.
- **Decision change** (the decision sentence flips): create a new KDD with the next ID, set `supersedes: KDD-NNN-old`, and set the old KDD `status: Superseded` with `superseded_by: KDD-NNN-new`. Do not edit the old decision sentence.
- **No revisions section.** Use `git log` / `git blame` for the rest of the history.

## Lifecycle

`Proposed → Tentative → Decided → Superseded → Deprecated`

- `Proposed` — drafted from a meeting note; not yet agreed by stakeholders.
- `Tentative` — agreed in principle, pending one more confirmation or trial.
- `Decided` — agreed and binding.
- `Superseded` — replaced by another KDD (`superseded_by` set).
- `Deprecated` — removed without replacement (rare).

## Optional enforcement frontmatter

A future revision may add an `enforcement:` block per KDD listing how the decision is checked at PR time (PR review agent, CI lint, conftest, etc.). See [../../recommendations/kdd-compliance-in-code-reviews.md](../../recommendations/kdd-compliance-in-code-reviews.md). Not added to the current batch.
