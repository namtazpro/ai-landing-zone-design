---
id: KDD-020
title: Skip custom MCP server overhead
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 12-platform-automation]
tags: [apim, mcp, operations]
---

## Context

Running hand-managed FastMCP containers on Container Apps duplicates capabilities that APIM now exposes natively, and adds operational toil (image lifecycle, autoscale, monitoring).

## Decision

Use APIM's native MCP exposure (Terraform-driven) rather than custom-built FastMCP servers on Container Apps. Reduces operational burden.

## Consequences

- Custom FastMCP becomes the exception, justified by abstraction needs ([KDD-025](KDD-025-maximo-api-abstraction-example.md), [OQ-008](../open-questions/OQ-008-custom-abstraction-trade-offs.md), [OQ-020](../open-questions/OQ-020-functions-vs-container-apps-for-fastmcp.md)).
- Pairs with [KDD-006](KDD-006-apim-native-mcp-conversion.md) and [KDD-017](KDD-017-api-first-tooling-standard.md).
- Terraform module for APIM-native MCP becomes a platform deliverable.

## Source

> why wouldn't we...use APP? If you can tick a box...we don't have...loads of servers...we're managing

— George Smith, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
