---
id: KDD-022
title: API Centre as separate registry
status: Tentative
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
tags: [api-centre, registry, multi-cloud]
---

## Context

APIM enforces runtime policy but is scoped to its instance. A cross-cloud catalogue of APIs, MCP servers, A2A endpoints, and skills needs a higher-level registry.

## Decision

API Centre (distinct from APIM) is the repository for API / MCP / A2A / skill metadata across multi-cloud deployments. Complements APIM's policy layer.

## Consequences

- API Centre catalogue is the discovery surface; APIM stays as runtime gateway.
- Sync model APIM ↔ API Centre is still TBD ([OQ-007](../open-questions/OQ-007-api-centre-vs-apim-scope.md)).
- Multi-cloud or non-Azure APIs (such as SAP CPI in [KDD-021](KDD-021-cpi-sap-integration-via-mcp.md)) still register here.

## Source

> API Centre...separate product...registry...you don't have to...within APP...can be anywhere

— Jacob Phan and John Blog, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
