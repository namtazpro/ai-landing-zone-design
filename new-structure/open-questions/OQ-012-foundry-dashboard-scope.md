---
id: OQ-012
title: Foundry dashboard scope
status: Open
created: 2026-06-05
last_revised: 2026-06-08
hld_sections: [11-management-operations]
blocks_kdds: []
tags: [observability, foundry-insights, dashboards]
---

## Question

What metrics belong in Foundry dashboards vs Application Insights, and how do the two integrate?

## Why it matters

Duplicate dashboards lead to inconsistent numbers and unclear ownership during incidents.

## Resolution path

- Catalogue required signals (run count, error rate, token cost, eval score) per agent and per domain.
- Assign each signal a single primary surface (App Insights or Foundry Insights).

## Source

— Not explicitly discussed in the 22 May / 26 May calls; carried from the v0.1 HLD draft.
