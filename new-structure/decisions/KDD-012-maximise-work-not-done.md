---
id: KDD-012
title: Maximise work not done
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [delivery, abstraction, v1]
---

## Context

Planning custom abstractions before they are needed creates speculative work and hides real performance signals behind premature optimisation.

## Decision

Ship v1 as 1:1 API→MCP exposure in APIM. Only introduce abstraction when pain is measured (context-window issues, accuracy drop). Use-case-driven, not anticipatory.

## Consequences

- v1 ships fast; abstraction backlog is data-driven.
- Performance signals must be captured to trigger abstraction work ([KDD-010](KDD-010-context-window-optimisation.md), [KDD-019](KDD-019-per-agent-billing-and-cost-attribution.md)).
- Pairs with [KDD-026](KDD-026-no-blanket-abstraction-requirement.md).

## Source

> maximise work not done...don't make that decision...publish it separately...then you make that decision later...when you see performance

— Jacob Phan and George Smith, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
