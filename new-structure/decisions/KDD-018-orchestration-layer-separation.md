---
id: KDD-018
title: Orchestration layer separation
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [orchestration, maf, logic-apps]
---

## Context

Mixing deterministic enterprise workflows and agentic tasks in one engine yields the worst of both: agents stuck in rigid graphs, or workflows pretending to reason.

## Decision

Traditional orchestration (Logic Apps, ADF) owns deterministic, long-running, asynchronous workflows. Agents own autonomous, real-time, agentic tasks. Both coexist.

## Consequences

- Selection criteria (MAF vs Logic Apps) become a documented decision tree ([OQ-011](../open-questions/OQ-011-maf-vs-logic-apps-selection-criteria.md)).
- Deterministic-to-agentic invocation works both ways via MCP / connectors.
- Reduces over-fit of either platform.

## Source

> workflows...orchestration layer...more complex...still need...traditional API calls...connectors...mixed with agents...MCP endpoints

— John Blog, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
