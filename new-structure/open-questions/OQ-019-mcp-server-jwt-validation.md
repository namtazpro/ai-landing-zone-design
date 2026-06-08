---
id: OQ-019
title: MCP server JWT validation
status: Open
created: 2026-06-05
last_revised: 2026-06-08
hld_sections: [08-security]
blocks_kdds: []
tags: [jwt, security, mcp]
---

## Question

What are the canonical issuer, audience, and signature-validation conventions for MCP servers handling incoming Entra ID JWTs?

## Why it matters

Without one validation library/profile, MCP servers will diverge on critical security details such as audience scoping and key rotation.

## Resolution path

- Pick a shared validation library.
- Publish the issuer/audience naming convention per environment.

## Source

— Topic mentioned in HLD section 13; not discussed on the 22 May / 26 May calls.
