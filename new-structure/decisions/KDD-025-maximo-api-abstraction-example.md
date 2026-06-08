---
id: KDD-025
title: Maximo API abstraction example
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
tags: [maximo, mcp, abstraction]
---

## Context

Maximo's REST surface is wide and field-engineer scenarios need only a small, intent-shaped subset. Exposing the raw API would inflate the agent's tool list with low-level operations.

## Decision

Concrete case: collapse ~14 granular Maximo APIs into 7 abstracted operations ("find work order", "create service request with duplicate check"). Reduces agent tool list and improves accuracy.

## Consequences

- Maximo MCP server is hand-crafted (custom abstraction) rather than 1:1 APIM exposure.
- Documents the pattern for when [KDD-010](KDD-010-context-window-optimisation.md) and [KDD-012](KDD-012-maximise-work-not-done.md) trigger abstraction.
- Reinforces [KDD-008](KDD-008-group-tools-by-intent-not-by-system.md).

## Source

> 14...APIs...MCP expose 7...instead of...tree dot...instead of...one dot...duplicate cheque create SR...one endpoint

— Ha Duong and Sourabh, 26 May 2026, [Mitie / Microsoft regular technical check-in](../../transcripts/Mitie_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
