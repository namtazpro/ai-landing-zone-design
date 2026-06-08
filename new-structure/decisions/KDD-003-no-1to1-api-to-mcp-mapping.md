---
id: KDD-003
title: No 1:1 API-to-MCP mapping
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [mcp, design, context-window]
---

## Context

A 1:1 API-to-MCP mapping multiplies endpoints, inflates the agent's tool list, and ties tool granularity to source-system granularity rather than to user intent.

## Decision

Do not create one MCP server per API. Group APIs by use case or domain; one MCP server exposes multiple grouped operations. Target fewer than ~10 tools per MCP to avoid context-window bloat.

## Consequences

- Tool grouping is an explicit design step, not an emergent property.
- Each MCP server has a curated tool count; new tools must justify their slot.
- Plays into [KDD-008](KDD-008-group-tools-by-intent-not-by-system.md) (intent-driven grouping) and [KDD-010](KDD-010-context-window-optimisation.md).

## Source

> we won't do one-to-one mapping for sure...group the tools...have one MCP...point for a group of tools instead of just one

— Emma Sun and Ha Duong, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
