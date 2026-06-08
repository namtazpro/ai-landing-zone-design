---
id: KDD-023
title: Skill vs MCP tool framework
status: Tentative
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 19-glossary-and-references]
tags: [skill, mcp, primitives]
---

## Context

"Skill" and "MCP tool" both surface in design conversations and sometimes get used interchangeably, which dilutes both primitives and confuses tool authors.

## Decision

Skills encode deterministic workflows/instructions an agent should follow. MCP exposes external systems an agent can invoke. Do not replicate one as the other.

## Consequences

- Glossary fixes the split; reviewers reject duplicates.
- Skill authors target the agent's reasoning loop; MCP authors target external systems.
- Pairs with [KDD-018](KDD-018-orchestration-layer-separation.md).

## Source

> skill...workflow...agent...MCP server...interact with other system...make that system available...multiple agents

— Ha Duong, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
