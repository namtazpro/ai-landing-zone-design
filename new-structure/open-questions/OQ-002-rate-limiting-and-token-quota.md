---
id: OQ-002
title: Rate limiting and token quota
status: Open
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [10-governance, 11-management-operations]
blocks_kdds: [KDD-027]
tags: [rate-limit, tpm, rpm, apim]
---

## Question

How to enforce TPM/RPM per domain on a central hub Foundry? Can Microsoft raise limits if required?

## Why it matters

Per-domain throttling is the only way to keep the shared hub fair across consumers without forking per-domain deployments.

## Resolution path

- Draft APIM policy patterns for per-subscription/per-product TPM/RPM enforcement.
- Document quota-uplift escalation path with Microsoft.

## Source

> rate limit...token limit server will impact production...how do we...apply policies

— Sanjay and John Blog, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
