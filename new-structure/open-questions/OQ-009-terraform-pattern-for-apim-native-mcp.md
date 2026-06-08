---
id: OQ-009
title: Terraform pattern for APIM-native MCP
status: Open
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 12-platform-automation, 16-decisions]
blocks_kdds: [KDD-006, KDD-020]
tags: [terraform, apim, mcp, iac]
---

## Question

How is Vincent's working APIM-native MCP demo turned into a repeatable Terraform module the platform team can ship?

## Why it matters

The skip-custom-MCP decision ([KDD-020](../decisions/KDD-020-skip-custom-mcp-server-overhead.md)) relies on this being reproducible; otherwise teams will keep spinning up FastMCP containers by default.

## Resolution path

- Lift the demo into a versioned platform module.
- Define inputs (OpenAPI spec, auth profile, exposure scope).

## Source

> can we do write code to deploy the MCP server in APP...assessment

— Emma, 26 May 2026, [Mitie / Microsoft regular technical check-in](../../transcripts/Mitie_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
