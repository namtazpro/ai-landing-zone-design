---
id: KDD-006
title: APIM-native MCP conversion
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 12-platform-automation]
tags: [apim, mcp, terraform]
---

## Context

Custom FastMCP servers running on Container Apps add operational burden where standard APIs already exist. APIM gained native MCP exposure.

## Decision

Use Azure API Management's native ability to expose OpenAPI specs as MCP servers, deployed via Terraform (working demo confirmed). Avoid custom FastMCP containers wherever standard APIs already cover the use case.

## Consequences

- Fewer hand-managed servers; IaC-driven exposure.
- Custom FastMCP becomes the exception, justified by abstraction needs (see [KDD-008](KDD-008-group-tools-by-intent-not-by-system.md), [OQ-008](../open-questions/OQ-008-custom-abstraction-trade-offs.md)).
- Terraform module pattern needs codifying ([OQ-009](../open-questions/OQ-009-terraform-pattern-for-apim-native-mcp.md)).

## Source

> can do Terraform...native resources...APP...Azure APP...MCP...confirmed that there is a protocol solution

— John Blog and Jane Star, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
