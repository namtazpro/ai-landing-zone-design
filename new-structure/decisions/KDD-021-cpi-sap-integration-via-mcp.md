---
id: KDD-021
title: CPI/SAP integration via MCP
status: Tentative
supersedes: null
superseded_by: null
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
tags: [sap, cpi, mcp]
---

## Context

SAP and similar non-Azure backends are reached today through point-to-point integrations (for example SAP CPI), which would couple agents directly to backend specifics.

## Decision

Non-APIM systems (for example SAP via CPI) are registered in API Management and exposed as MCP servers so agents can access them without direct system coupling.

## Consequences

- Backend integration retains its existing CPI plumbing; APIM becomes the agent-facing wrapper.
- Discovery of these backends is uniform with native Azure-hosted APIs.
- Pattern still TBD ([OQ-006](../open-questions/OQ-006-cpi-sap-endpoint-via-mcp.md)).

## Source

> might be into...other systems...SAP uses CPI...we want to expose through MCP...discoverable by the AI

— George Smith, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md)
