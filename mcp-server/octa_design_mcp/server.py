"""Read-only MCP server exposing the OCTA Agentic Platform design workspace.

Surfaces the living architecture artefacts (KDDs, open questions, the HLD,
transcripts, the asset index, and direct-request logs) to MCP clients as tools
and resources. The server is strictly read-only: it never writes to the
workspace.

Run over stdio (the default for local VS Code / Claude Desktop use)::

    python -m octa_design_mcp

The workspace root is auto-discovered from this file's location, or overridden
with the ``OCTA_WORKSPACE_ROOT`` environment variable.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from mcp.server.fastmcp import FastMCP

# --------------------------------------------------------------------------- #
# Workspace layout
# --------------------------------------------------------------------------- #


def _discover_root() -> Path:
    """Resolve the repository root.

    Honours ``OCTA_WORKSPACE_ROOT`` when set; otherwise assumes this package
    lives in ``<repo>/mcp-server/octa_design_mcp`` and walks two levels up.
    """
    override = os.environ.get("OCTA_WORKSPACE_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[2]


ROOT = _discover_root()
NEW = ROOT / "new-structure"
DECISIONS_DIR = NEW / "decisions"
OPEN_QUESTIONS_DIR = NEW / "open-questions"
REQUESTS_DIR = NEW / "requests"
HLD_PATH = NEW / "docs" / "HLD.md"
ASSETS_INDEX_PATH = NEW / "assets" / "index.json"
TRANSCRIPTS_DIR = ROOT / "transcripts"

ID_PATTERN = re.compile(r"^(KDD|OQ)-(\d{3})", re.IGNORECASE)

mcp = FastMCP(
    "octa-design",
    instructions=(
        "Read-only access to the OCTA Agentic Platform architecture workspace: "
        "key design decisions (KDDs), open questions (OQs), the High-Level "
        "Design (HLD), meeting transcripts, the asset index, and direct-request "
        "logs. Use search_artefacts for free-text discovery, the get_* tools to "
        "fetch a specific artefact by ID, and the list_* tools to browse and "
        "filter. All content is sourced from the live workspace files."
    ),
)


# --------------------------------------------------------------------------- #
# Parsing helpers
# --------------------------------------------------------------------------- #


@dataclass
class Artefact:
    """A markdown file split into frontmatter metadata and body."""

    path: Path
    meta: dict[str, Any]
    body: str

    @property
    def text(self) -> str:
        return self.path.read_text(encoding="utf-8")


def _split_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    """Return ``(metadata, body)`` for a markdown string with YAML frontmatter."""
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) == 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                meta = {}
            if isinstance(meta, dict):
                return meta, parts[2].lstrip("\n")
    return {}, raw


def _load_artefact(path: Path) -> Artefact:
    raw = path.read_text(encoding="utf-8")
    meta, body = _split_frontmatter(raw)
    return Artefact(path=path, meta=meta, body=body)


def _normalise_id(raw_id: str, prefix: str) -> str | None:
    """Normalise loose user input into a canonical ``KDD-001`` / ``OQ-001`` id."""
    raw_id = raw_id.strip()
    match = re.search(r"(\d{1,3})", raw_id)
    if not match:
        return None
    return f"{prefix}-{int(match.group(1)):03d}"


def _find_by_id(directory: Path, canonical_id: str) -> Path | None:
    matches = sorted(directory.glob(f"{canonical_id}-*.md"))
    return matches[0] if matches else None


def _rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _snippet(body: str, query: str, width: int = 160) -> str:
    """Extract a context window around the first case-insensitive match."""
    lower = body.lower()
    idx = lower.find(query.lower())
    if idx == -1:
        return body[:width].strip().replace("\n", " ")
    start = max(0, idx - width // 2)
    end = min(len(body), idx + len(query) + width // 2)
    prefix = "…" if start > 0 else ""
    suffix = "…" if end < len(body) else ""
    return f"{prefix}{body[start:end].strip()}{suffix}".replace("\n", " ")


# --------------------------------------------------------------------------- #
# HLD section parsing
# --------------------------------------------------------------------------- #

_HLD_HEADING = re.compile(r"^##\s+(\d+)\.\s+(.*)$")


def _hld_sections() -> list[dict[str, Any]]:
    """Split the HLD into top-level numbered sections (``## N. Title``)."""
    if not HLD_PATH.exists():
        return []
    lines = HLD_PATH.read_text(encoding="utf-8").splitlines()
    sections: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for line in lines:
        heading = _HLD_HEADING.match(line)
        if heading:
            if current:
                sections.append(current)
            current = {
                "number": int(heading.group(1)),
                "title": heading.group(2).strip(),
                "lines": [line],
            }
        elif current is not None:
            current["lines"].append(line)
    if current:
        sections.append(current)
    for section in sections:
        section["content"] = "\n".join(section.pop("lines")).strip()
    return sections


# --------------------------------------------------------------------------- #
# Collection loaders
# --------------------------------------------------------------------------- #


def _iter_records(directory: Path, id_prefix: str) -> list[Artefact]:
    if not directory.exists():
        return []
    records = []
    for path in sorted(directory.glob(f"{id_prefix}-*.md")):
        records.append(_load_artefact(path))
    return records


def _record_summary(artefact: Artefact) -> dict[str, Any]:
    meta = artefact.meta
    return {
        "id": meta.get("id"),
        "title": meta.get("title"),
        "status": meta.get("status"),
        "tags": meta.get("tags", []),
        "hld_sections": meta.get("hld_sections", []),
        "created": str(meta.get("created")) if meta.get("created") else None,
        "last_revised": (
            str(meta.get("last_revised")) if meta.get("last_revised") else None
        ),
        "path": _rel(artefact.path),
    }


# --------------------------------------------------------------------------- #
# Tools: decisions (KDDs)
# --------------------------------------------------------------------------- #


@mcp.tool()
def list_decisions(
    status: str | None = None,
    tag: str | None = None,
    hld_section: str | None = None,
) -> list[dict[str, Any]]:
    """List key design decisions (KDDs), optionally filtered.

    Args:
        status: Case-insensitive match on the KDD ``status`` (e.g. ``Decided``,
            ``Tentative``, ``Superseded``).
        tag: Case-insensitive match against the KDD ``tags`` list.
        hld_section: Match against the KDD ``hld_sections`` list (substring,
            e.g. ``05`` or ``ai-platform``).

    Returns:
        Frontmatter summaries (id, title, status, tags, sections, dates, path).
    """
    results = []
    for artefact in _iter_records(DECISIONS_DIR, "KDD"):
        meta = artefact.meta
        if status and str(meta.get("status", "")).lower() != status.lower():
            continue
        if tag and tag.lower() not in [str(t).lower() for t in meta.get("tags", [])]:
            continue
        if hld_section and not any(
            hld_section.lower() in str(s).lower()
            for s in meta.get("hld_sections", [])
        ):
            continue
        results.append(_record_summary(artefact))
    return results


@mcp.tool()
def get_decision(kdd_id: str) -> dict[str, Any]:
    """Fetch a single key design decision (KDD) by id.

    Args:
        kdd_id: A KDD identifier in any loose form, e.g. ``KDD-001``, ``kdd1``,
            or ``1``.

    Returns:
        The parsed metadata plus the full markdown body, or an ``error`` field.
    """
    canonical = _normalise_id(kdd_id, "KDD")
    if not canonical:
        return {"error": f"Could not parse a KDD id from {kdd_id!r}."}
    path = _find_by_id(DECISIONS_DIR, canonical)
    if not path:
        return {"error": f"{canonical} not found in {_rel(DECISIONS_DIR)}."}
    artefact = _load_artefact(path)
    return {
        "id": canonical,
        "meta": artefact.meta,
        "path": _rel(path),
        "content": artefact.body,
    }


# --------------------------------------------------------------------------- #
# Tools: open questions (OQs)
# --------------------------------------------------------------------------- #


@mcp.tool()
def list_open_questions(
    status: str | None = None,
    tag: str | None = None,
    hld_section: str | None = None,
) -> list[dict[str, Any]]:
    """List open questions (OQs), optionally filtered.

    Args:
        status: Case-insensitive match on the OQ ``status`` (e.g. ``Open``,
            ``Closed``).
        tag: Case-insensitive match against the OQ ``tags`` list.
        hld_section: Substring match against the OQ ``hld_sections`` list.

    Returns:
        Frontmatter summaries for the matching open questions.
    """
    results = []
    for artefact in _iter_records(OPEN_QUESTIONS_DIR, "OQ"):
        meta = artefact.meta
        if status and str(meta.get("status", "")).lower() != status.lower():
            continue
        if tag and tag.lower() not in [str(t).lower() for t in meta.get("tags", [])]:
            continue
        if hld_section and not any(
            hld_section.lower() in str(s).lower()
            for s in meta.get("hld_sections", [])
        ):
            continue
        summary = _record_summary(artefact)
        summary["blocks_kdds"] = meta.get("blocks_kdds", [])
        results.append(summary)
    return results


@mcp.tool()
def get_open_question(oq_id: str) -> dict[str, Any]:
    """Fetch a single open question (OQ) by id.

    Args:
        oq_id: An OQ identifier in any loose form, e.g. ``OQ-001``, ``oq1``,
            or ``1``.

    Returns:
        The parsed metadata plus the full markdown body, or an ``error`` field.
    """
    canonical = _normalise_id(oq_id, "OQ")
    if not canonical:
        return {"error": f"Could not parse an OQ id from {oq_id!r}."}
    path = _find_by_id(OPEN_QUESTIONS_DIR, canonical)
    if not path:
        return {"error": f"{canonical} not found in {_rel(OPEN_QUESTIONS_DIR)}."}
    artefact = _load_artefact(path)
    return {
        "id": canonical,
        "meta": artefact.meta,
        "path": _rel(path),
        "content": artefact.body,
    }


# --------------------------------------------------------------------------- #
# Tools: HLD
# --------------------------------------------------------------------------- #


@mcp.tool()
def list_hld_sections() -> list[dict[str, Any]]:
    """List the numbered top-level sections of the High-Level Design."""
    return [
        {"number": s["number"], "title": s["title"]} for s in _hld_sections()
    ]


@mcp.tool()
def get_hld_section(section: str) -> dict[str, Any]:
    """Return the content of a single HLD section.

    Args:
        section: Either a section number (e.g. ``5``) or a case-insensitive
            substring of the section title (e.g. ``identity`` or ``building
            blocks``).

    Returns:
        The matched section number, title, and full markdown content.
    """
    sections = _hld_sections()
    if not sections:
        return {"error": f"HLD not found at {_rel(HLD_PATH)}."}
    query = section.strip()
    if query.isdigit():
        target = int(query)
        for s in sections:
            if s["number"] == target:
                return {
                    "number": s["number"],
                    "title": s["title"],
                    "path": _rel(HLD_PATH),
                    "content": s["content"],
                }
        return {"error": f"No HLD section numbered {target}."}
    matches = [s for s in sections if query.lower() in s["title"].lower()]
    if not matches:
        available = ", ".join(f"{s['number']}. {s['title']}" for s in sections)
        return {"error": f"No HLD section matching {query!r}. Available: {available}"}
    s = matches[0]
    return {
        "number": s["number"],
        "title": s["title"],
        "path": _rel(HLD_PATH),
        "content": s["content"],
        "other_matches": [
            {"number": m["number"], "title": m["title"]} for m in matches[1:]
        ],
    }


# --------------------------------------------------------------------------- #
# Tools: transcripts, assets, requests
# --------------------------------------------------------------------------- #


@mcp.tool()
def list_transcripts() -> list[dict[str, Any]]:
    """List ingested meeting transcripts (markdown derivatives)."""
    if not TRANSCRIPTS_DIR.exists():
        return []
    return [
        {"name": p.stem, "file": p.name, "path": _rel(p)}
        for p in sorted(TRANSCRIPTS_DIR.glob("*.md"))
    ]


@mcp.tool()
def get_transcript(name: str, max_chars: int = 40000) -> dict[str, Any]:
    """Fetch a transcript's content by (partial) name.

    Args:
        name: Full or partial transcript file name / stem (case-insensitive).
        max_chars: Truncate the returned content to this many characters
            (default 40000). Set to 0 for the full transcript.

    Returns:
        The transcript content and a ``truncated`` flag, or an ``error`` field.
    """
    if not TRANSCRIPTS_DIR.exists():
        return {"error": f"No transcripts directory at {_rel(TRANSCRIPTS_DIR)}."}
    candidates = sorted(TRANSCRIPTS_DIR.glob("*.md"))
    matches = [p for p in candidates if name.lower() in p.name.lower()]
    if not matches:
        available = ", ".join(p.stem for p in candidates)
        return {"error": f"No transcript matching {name!r}. Available: {available}"}
    path = matches[0]
    content = path.read_text(encoding="utf-8")
    truncated = bool(max_chars) and len(content) > max_chars
    return {
        "name": path.stem,
        "path": _rel(path),
        "truncated": truncated,
        "content": content[:max_chars] if truncated else content,
    }


@mcp.tool()
def list_assets() -> dict[str, Any]:
    """Return the machine-readable asset index (diagrams and decks)."""
    if not ASSETS_INDEX_PATH.exists():
        return {"error": f"No asset index at {_rel(ASSETS_INDEX_PATH)}."}
    try:
        data = json.loads(ASSETS_INDEX_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"error": f"Asset index is not valid JSON: {exc}"}
    data["path"] = _rel(ASSETS_INDEX_PATH)
    return data


@mcp.tool()
def list_requests() -> list[dict[str, Any]]:
    """List direct architect/consultant requests logged in the workspace."""
    if not REQUESTS_DIR.exists():
        return []
    requests = []
    for path in sorted(REQUESTS_DIR.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        artefact = _load_artefact(path)
        requests.append(
            {
                "title": artefact.meta.get("title", path.stem),
                "meta": artefact.meta,
                "path": _rel(path),
            }
        )
    return requests


# --------------------------------------------------------------------------- #
# Tool: cross-artefact search
# --------------------------------------------------------------------------- #

_KIND_SOURCES = {
    "decision": (DECISIONS_DIR, "KDD-*.md"),
    "open-question": (OPEN_QUESTIONS_DIR, "OQ-*.md"),
    "request": (REQUESTS_DIR, "*.md"),
    "transcript": (TRANSCRIPTS_DIR, "*.md"),
}


@mcp.tool()
def search_artefacts(
    query: str,
    kinds: list[str] | None = None,
    limit: int = 20,
) -> list[dict[str, Any]]:
    """Full-text search across all workspace artefacts.

    Searches decisions (KDDs), open questions (OQs), HLD sections, transcripts,
    and request logs for a case-insensitive substring, ranked by match count.

    Args:
        query: The text to search for (case-insensitive substring).
        kinds: Optional subset of artefact kinds to search. Any of
            ``decision``, ``open-question``, ``hld``, ``transcript``,
            ``request``. Defaults to all kinds.
        limit: Maximum number of results to return (default 20).

    Returns:
        Ranked results, each with ``kind``, ``id``/``title``, ``path``,
        ``score`` (match count), and a ``snippet`` around the first hit.
    """
    if not query.strip():
        return []
    needle = query.lower()
    selected = set(kinds) if kinds else {
        "decision",
        "open-question",
        "hld",
        "transcript",
        "request",
    }
    results: list[dict[str, Any]] = []

    # File-backed kinds.
    for kind, (directory, glob) in _KIND_SOURCES.items():
        if kind not in selected or not directory.exists():
            continue
        for path in sorted(directory.glob(glob)):
            if path.name.lower() == "readme.md":
                continue
            artefact = _load_artefact(path)
            haystack = artefact.text.lower()
            score = haystack.count(needle)
            if score == 0:
                continue
            results.append(
                {
                    "kind": kind,
                    "id": artefact.meta.get("id"),
                    "title": artefact.meta.get("title", path.stem),
                    "path": _rel(path),
                    "score": score,
                    "snippet": _snippet(artefact.body or artefact.text, query),
                }
            )

    # HLD sections.
    if "hld" in selected:
        for s in _hld_sections():
            score = s["content"].lower().count(needle)
            if score == 0:
                continue
            results.append(
                {
                    "kind": "hld",
                    "id": f"HLD-{s['number']}",
                    "title": f"{s['number']}. {s['title']}",
                    "path": _rel(HLD_PATH),
                    "score": score,
                    "snippet": _snippet(s["content"], query),
                }
            )

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:limit]


# --------------------------------------------------------------------------- #
# Resources
# --------------------------------------------------------------------------- #


@mcp.resource("octa://hld")
def hld_resource() -> str:
    """The full High-Level Design document."""
    if not HLD_PATH.exists():
        return f"HLD not found at {_rel(HLD_PATH)}."
    return HLD_PATH.read_text(encoding="utf-8")


@mcp.resource("octa://decisions")
def decisions_index_resource() -> str:
    """A compact index of all key design decisions (KDDs)."""
    lines = ["# Key Design Decisions index", ""]
    for artefact in _iter_records(DECISIONS_DIR, "KDD"):
        meta = artefact.meta
        lines.append(
            f"- {meta.get('id')} — {meta.get('title')} "
            f"[{meta.get('status')}] ({_rel(artefact.path)})"
        )
    return "\n".join(lines)


@mcp.resource("octa://open-questions")
def open_questions_index_resource() -> str:
    """A compact index of all open questions (OQs)."""
    lines = ["# Open Questions index", ""]
    for artefact in _iter_records(OPEN_QUESTIONS_DIR, "OQ"):
        meta = artefact.meta
        lines.append(
            f"- {meta.get('id')} — {meta.get('title')} "
            f"[{meta.get('status')}] ({_rel(artefact.path)})"
        )
    return "\n".join(lines)


@mcp.resource("octa://decision/{kdd_id}")
def decision_resource(kdd_id: str) -> str:
    """A single KDD as raw markdown."""
    canonical = _normalise_id(kdd_id, "KDD")
    if not canonical:
        return f"Invalid KDD id: {kdd_id}"
    path = _find_by_id(DECISIONS_DIR, canonical)
    return path.read_text(encoding="utf-8") if path else f"{canonical} not found."


@mcp.resource("octa://open-question/{oq_id}")
def open_question_resource(oq_id: str) -> str:
    """A single OQ as raw markdown."""
    canonical = _normalise_id(oq_id, "OQ")
    if not canonical:
        return f"Invalid OQ id: {oq_id}"
    path = _find_by_id(OPEN_QUESTIONS_DIR, canonical)
    return path.read_text(encoding="utf-8") if path else f"{canonical} not found."


def main() -> None:
    """Entry point for ``python -m octa_design_mcp`` and the console script."""
    mcp.run()


if __name__ == "__main__":
    main()
