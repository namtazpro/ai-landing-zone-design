---
id: OQ-008
title: Custom abstraction trade-offs
status: Open
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 12-platform-automation]
blocks_kdds: [KDD-020, KDD-025, KDD-026]
tags: [abstraction, mcp, decision-criteria]
---

## Question

What decision criteria determine when to build custom FastMCP abstraction (for example duplicate-check + create-SR) vs rely on APIM + standard APIs?

## Why it matters

Without explicit criteria, abstraction becomes either a vanity habit or a thing nobody dares to introduce; both miss the cost-window-vs-toil sweet spot.

## Resolution path

- Capture pain signals (token bloat, latency, accuracy drop, repeated agent retries).
- Define thresholds that move a tool group from "1:1 in APIM" to "custom MCP".

## Source

> this is very use case specific...don't think that we can give clear guidance without knowing actual use cases

— Ha Duong, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
