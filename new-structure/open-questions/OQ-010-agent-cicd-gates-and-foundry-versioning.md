---
id: OQ-010
title: Agent CI/CD gates and Foundry versioning
status: Open
created: 2026-06-05
last_revised: 2026-06-08
hld_sections: [12-platform-automation]
blocks_kdds: []
tags: [cicd, foundry, versioning]
---

## Question

What are the formal PR gates, Foundry version registry semantics, and rollback strategy for agent deployments?

## Why it matters

The HLD describes the shape of PR validation and deployment but leaves gating thresholds, version naming, and rollback procedure unstated.

## Resolution path

- Pin gate thresholds (eval pass rate, secret scan severity, lint failures).
- Define semver and Foundry-tag conventions per environment.
- Document one-click rollback procedure end-to-end.

## Source

— Not discussed directly in the 22 May / 26 May calls; carried from the v0.1 HLD draft.
