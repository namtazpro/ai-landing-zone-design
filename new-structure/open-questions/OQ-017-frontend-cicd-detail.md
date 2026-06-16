---
id: OQ-017
title: Frontend CI/CD detail
status: Open
created: 2026-06-05
last_revised: 2026-06-08
hld_sections: [12-platform-automation]
blocks_kdds: []
tags: [cicd, frontend, nextjs]
---

## Question

Confirm the frontend pipeline: `npm ci`, ESLint, Prettier, `tsc`, Jest 70% coverage, and `cosign` image signing.

## Why it matters

Pipeline gates need to be ratified before frontend agents reach Contoso users; today the values come from the deck and have not been re-confirmed by the calls.

## Resolution path

- Validate gate thresholds with the frontend team.
- Land the gates in the shared pipeline templates.

## Source

— Not discussed on the 22 May / 26 May calls; carried from the v0.1 HLD draft.
