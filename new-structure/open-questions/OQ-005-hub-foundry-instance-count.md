---
id: OQ-005
title: Hub Foundry instance count
status: Open
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [04-solution-overview, 11-management-operations]
blocks_kdds: [KDD-014]
tags: [hub-foundry, environments]
---

## Question

One hub shared across non-prod domains plus a prod hub, or one hub per environment (dev hub + test hub + prod hub)?

## Why it matters

Drives subscription cost, model-deployment count, and blast-radius for hub-side changes.

## Resolution path

- Compare quota footprint and operational cost of one shared non-prod hub vs split dev/test hubs.
- Confirm prod hub is always isolated regardless.

## Source

> one shared...one maybe one shared for dev...one shared for test

— Vincent and Sourabh, 26 May 2026, [Mitie / Microsoft regular technical check-in](../../transcripts/Mitie_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
