---
id: KDD-010
title: Context-window optimisation
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [context-window, performance, abstraction]
---

## Context

Bloated tool lists and granular APIs inflate the agent's context window, slow inference, and drop success rate. Evidence from an internal trial measured the impact directly.

## Decision

Prefer abstracted, intent-driven APIs over granular ones. Evidence from internal trial: ~50% fewer tools, ~30% token savings, lower latency, higher success rate.

## Consequences

- Abstraction is justified by a measured pain signal, not theory.
- Drives [KDD-008](KDD-008-group-tools-by-intent-not-by-system.md) and [KDD-025](KDD-025-maximo-api-abstraction-example.md).
- Tool catalogues must publish their tool-count and per-agent context budget.

## Source

> success rate will be a lot more better...average tokens...less...cost...less...don't bloat the context window

— Ha Duong and Mike, 26 May 2026, [Mitie / Microsoft regular technical check-in](../../transcripts/Mitie_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
