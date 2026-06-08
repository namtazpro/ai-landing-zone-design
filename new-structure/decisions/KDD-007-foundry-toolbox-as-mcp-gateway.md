---
id: KDD-007
title: Foundry Toolbox as MCP gateway
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
tags: [foundry, mcp, gateway]
---

## Context

APIM-exposed MCP servers cannot easily filter what an individual agent sees, nor handle agent-specific versioning, without bespoke policy work.

## Decision

Foundry Toolbox sits as a second-layer MCP gateway above APIM-exposed MCP servers, handling versioning, agent-specific filtering, and selective exposure.

## Consequences

- Two-layer MCP topology: APIM (policy/transport) + Foundry Toolbox (agent-facing curation).
- Per-agent tool catalogues become first-class objects in Foundry.
- Toolbox is the place to wire `allow_tools` ([KDD-009](KDD-009-isolate-sensitive-tools-via-allow_tools.md)).

## Source

> Foundry toolbox...additional layer...MCP...gateway...to agent...and that I agree with you...versioning and all that

— Emma Sun, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
