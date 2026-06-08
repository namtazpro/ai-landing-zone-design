---
id: OQ-015
title: SQL knowledge base access path
status: Open
created: 2026-06-05
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 11-management-operations]
blocks_kdds: []
tags: [knowledge-base, sql, sdk]
---

## Question

Is the SQL knowledge base reached through an MCP-wrapped endpoint or directly via SDK? User convention prefers SDKs where available.

## Why it matters

Direct SDK access skips APIM enforcement; MCP-wrapped access adds a hop but keeps policy and auditing centralised.

## Resolution path

- Default to MCP-wrapped for write paths; allow direct SDK for read-only analytical queries.
- Capture exception path in the per-agent design.

## Source

— Raised in HLD section 12; not resolved on the 22 May / 26 May calls.
