---
id: KDD-001
title: Tool registry and categorisation
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [tools, mcp, registry]
---

## Context

Exposing tools individually to agents leaks low-level system details into prompts and bloats the context window. A registry pattern is needed so the platform can govern, version, and surface only what each agent needs.

## Decision

Tools are categorised and grouped by functionality, not assigned individually. Tool groups are wrapped as MCP servers to leverage MCP's input validation, dynamic exposure, and richer descriptions.

## Consequences

- One registration shape across all tools.
- MCP `allow_tools` becomes the in-group sensitivity boundary (see [KDD-009](KDD-009-isolate-sensitive-tools-via-allow_tools.md)).
- Every new tool must be classified into a group before it ships.

## Source

> tools should be categorised...instead of...individual...we will...systemise, categorise those tools...wrap as MCP server so...leverage benefits

— Jane Star, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
