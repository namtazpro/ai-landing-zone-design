---
id: OQ-006
title: CPI / SAP endpoint via MCP
status: Open
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
blocks_kdds: [KDD-021]
tags: [sap, cpi, mcp, integration]
---

## Question

What is the concrete integration pattern for non-Azure systems (such as SAP via CPI) routed through APIM and exposed as MCP?

## Why it matters

CPI semantics (async, idempotency, retries) differ from Azure-native APIs and need a settled wrapper pattern before SAP-bound agents go live.

## Resolution path

- Pilot one CPI endpoint via APIM-native MCP.
- Document auth, error mapping, and idempotency conventions.

## Source

— Raised by George Smith, 22 May 2026, [Microsoft Support — Foundry platform and MCP servers](../../transcripts/Microsoft%20Support%20-%20Foundry%20platform%20and%20MCP%20servers%2022%20may%202026.md); no resolution captured in transcript.
