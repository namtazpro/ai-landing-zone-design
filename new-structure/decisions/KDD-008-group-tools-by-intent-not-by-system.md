---
id: KDD-008
title: Group tools by intent, not by system
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [mcp, design, intent-driven]
---

## Context

Grouping tools by backend system mirrors the source plumbing instead of the user's job-to-be-done. Agents end up sequencing low-level calls when one intent-shaped operation would do.

## Decision

Group tools by user intent / business operation (for example a "checkout workflow"), not by backend system. Combining `add-to-cart`, `remove-from-cart`, and `checkout` into one abstracted operation reduces agent orchestration burden.

## Consequences

- Tool authors must articulate the intent before defining the schema.
- Intent groupings cross backend boundaries — explicit ownership rules needed.
- Reinforces [KDD-003](KDD-003-no-1to1-api-to-mcp-mapping.md) and [KDD-025](KDD-025-maximo-api-abstraction-example.md).

## Source

> group by...intention rather than actual...how would you use...give it to someone to do something...the intention rather than actual...API call

— Jacob Phan, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
