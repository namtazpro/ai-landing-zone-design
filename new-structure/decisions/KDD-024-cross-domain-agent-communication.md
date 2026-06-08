---
id: KDD-024
title: Cross-domain agent communication
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
tags: [a2a, cross-domain, registry]
---

## Context

Domains (EFF, HR, Sales) are useful organisational units, but high-value agentic scenarios cut across them (engineering needs HR data; HR needs procurement). Hard boundaries on communication would kill reuse.

## Decision

Agents in one domain (for example EFF) may invoke agents in another (for example HR) through a shared agent registry / orchestration layer. Domain boundaries govern access control, not communication.

## Consequences

- Shared agent registry is a platform deliverable.
- RBAC and per-agent identity ([KDD-009](KDD-009-isolate-sensitive-tools-via-attributes.md), [OQ-014](../open-questions/OQ-014-per-agent-identity-vs-shared-sp.md)) enforce the boundary.
- A2A wiring path stays open ([OQ-013](../open-questions/OQ-013-a2a-through-mcp.md)).

## Source

> share those resources...a multifunctional...useful...in the engineering space...Can they talk...cross boundaries

— Mike, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
