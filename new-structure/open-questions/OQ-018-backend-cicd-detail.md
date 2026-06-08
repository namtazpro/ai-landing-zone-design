---
id: OQ-018
title: Backend CI/CD detail
status: Open
created: 2026-06-05
last_revised: 2026-06-08
hld_sections: [12-platform-automation]
blocks_kdds: []
tags: [cicd, backend, fastapi]
---

## Question

Confirm the backend pipeline: `uv sync`, `ruff`, `mypy`, `pytest ≥ 90%` coverage, and `alembic upgrade head` at startup.

## Why it matters

Backend pipeline gates anchor production deploy quality; today values come from the deck and have not been re-confirmed by the calls.

## Resolution path

- Validate gate thresholds with the backend team.
- Land the gates in the shared pipeline templates.

## Source

— Not discussed on the 22 May / 26 May calls; carried from the v0.1 HLD draft.
