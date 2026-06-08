---
id: OQ-011
title: MAF vs Logic Apps selection criteria
status: Open
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
blocks_kdds: [KDD-018]
tags: [maf, logic-apps, decision-criteria]
---

## Question

What are the formal criteria for choosing Microsoft Agent Framework vs Logic Apps per workflow?

## Why it matters

The two engines overlap on simple flows; without explicit triggers (statefulness, edge dynamism, connector breadth) teams will default to whichever they already know.

## Resolution path

- Publish a decision tree (deterministic/static → Logic Apps, agentic/dynamic → MAF, mixed → MAF orchestrates Logic Apps step).
- Include a per-pillar trade-off line (cost, observability, retry policy).

## Source

— Touched on by Vincent, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md); no formal criteria captured.
