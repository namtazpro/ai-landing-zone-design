---
id: OQ-014
title: Per-agent identity vs shared service principal
status: Open
created: 2026-06-05
last_revised: 2026-06-08
hld_sections: [06-identity-access, 08-security]
blocks_kdds: []
tags: [identity, rbac, audit]
---

## Question

Is every agent assigned its own Entra ID identity, or are some agents grouped under a shared service principal?

## Why it matters

Per-agent identity gives least privilege and clean audit trails but multiplies identity-lifecycle work; shared SPs invert the trade-off.

## Resolution path

- Default to per-agent identity for production agents.
- Allow shared SP for short-lived prototypes with a documented expiry.

## Source

— Not discussed in the 22 May / 26 May calls; carried from the v0.1 HLD draft.
