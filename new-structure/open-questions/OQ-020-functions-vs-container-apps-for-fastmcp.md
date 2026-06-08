---
id: OQ-020
title: Functions vs Container Apps for custom FastMCP
status: Open
created: 2026-05-22
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks, 12-platform-automation]
blocks_kdds: [KDD-020]
tags: [hosting, functions, container-apps]
---

## Question

For any custom FastMCP not handled by APIM-native exposure, do we host on Azure Functions or Azure Container Apps?

## Why it matters

The hosting choice drives cold-start behaviour, cost profile, scaling controls, and per-tool reliability characteristics.

## Resolution path

- Benchmark a representative FastMCP on both platforms.
- Decide a default and document exception path.

## Source

— Discussion on 22 May 2026 referenced both options without consensus; carried from the v0.1 HLD draft.
