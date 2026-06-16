---
id: KDD-026
title: No blanket abstraction requirement
status: Decided
supersedes: null
superseded_by: null
created: 2026-05-26
last_revised: 2026-06-08
hld_sections: [05-ai-platform-building-blocks]
tags: [abstraction, mcp, v1]
---

## Context

After agreeing that abstraction matters (KDD-008, KDD-010, KDD-025), there is a risk of over-applying it and forcing every API set through a custom layer.

## Decision

Not every API set needs custom abstraction. Well-designed, small API sets are exposed 1:1 through APIM MCP. Abstract only when pain occurs.

## Consequences

- Per-tool decision: abstract or pass-through, recorded on a checklist.
- Avoids re-introducing the operational toll that [KDD-020](KDD-020-skip-custom-mcp-server-overhead.md) eliminated.
- Consistent with [KDD-012](KDD-012-maximise-work-not-done.md).

## Source

> if we see the abstractions that needed...then we can implementing...got the place for it...feel the pain...performance degradation

— Ha Duong and Mike, 26 May 2026, [Contoso / Microsoft regular technical check-in](../../transcripts/Contoso_Microsoft%20-%20regular%20technical%20check-in%20call%2026%20May%202026.md)
