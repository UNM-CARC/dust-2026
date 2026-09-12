#!/usr/bin/env python3
"""Generate llms.txt and llms-full.txt from the docs/ OKF bundle.

llms.txt      — linked outline of the site (llmstxt.org convention): every
                concept page with its frontmatter description, grouped by the
                nav sections in zensical.toml, with absolute URLs.
llms-full.txt — the entire corpus concatenated as Markdown, frontmatter
                included, relative links rewritten to absolute URLs, so an
                agent can ingest the whole bundle in one file.

Site name, description, URL, and page order all come from zensical.toml.
Both files are written into docs/ so the static build ships them at the site
root; CI regenerates them and fails if the committed copies drift.

Usage: python3 scripts/gen_llms_txt.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from okf_common import (DOCS, absolutize, frontmatter, is_external,  # noqa: E402
                        load_config, nav_pages, page_url, rewrite_link_targets,
                        site_url, split_frontmatter)


def main() -> int:
    cfg = load_config()
    base = site_url(cfg)
    name = cfg.get("site_name", "Documentation")
    desc = cfg.get("site_description", "").strip()

    example = None
    lines = [
        f"# {name}",
        "",
        f"> {desc} The source repository is an Open Knowledge Format (OKF "
        "v0.2) bundle: every page carries YAML frontmatter with type, "
        "provenance (generated/sources), and lifecycle (status/stale_after) "
        "fields.",
        "",
        f"Full corpus for ingestion: {base}llms-full.txt",
        "",
    ]
    full = [
        f"# {name} — full corpus",
        "",
        "Each page below begins with its canonical URL followed by its "
        "original Markdown, OKF frontmatter included. Relative links have "
        "been rewritten to absolute URLs.",
        "",
    ]

    # section -> subsection -> outline lines, in nav order; empty groups are
    # never rendered. Top-level single pages (other than Home) share a group.
    groups: dict[str, dict[str | None, list[str]]] = {}

    def add(trail: tuple, line: str):
        section = trail[0] if trail else "Other pages"
        sub = " / ".join(trail[1:]) or None
        groups.setdefault(section, {}).setdefault(sub, []).append(line)

    seen: set[str] = set()
    n = 0
    for trail, label, target in nav_pages(cfg.get("nav", [])):
        if is_external(target):
            add(trail, f"- [{label or target}]({target}): External resource.")
            continue
        rel = target.replace("\\", "/")
        if rel in seen or not (DOCS / rel).exists():
            continue
        seen.add(rel)
        if rel.endswith("index.md") or rel == "log.md":
            continue  # OKF §8 listings and the §9 log are not concept pages
        fm = frontmatter(DOCS / rel)
        url = page_url(base, rel)
        example = example or url
        title = fm.get("title") or label or Path(rel).stem.replace("-", " ").title()
        summary = str(fm.get("description", "")).strip()
        suffix = ""
        if fm.get("status") == "deprecated":
            suffix = " (deprecated; kept for history)"
        elif fm.get("status") == "draft":
            suffix = " (draft)"
        add(trail, f"- [{title}]({url}): {summary}{suffix}")
        text = (DOCS / rel).read_text(encoding="utf-8")
        _, body = split_frontmatter(text)
        head = text[: len(text) - len(body)]
        body = rewrite_link_targets(body, lambda t, r=rel: absolutize(t, r, base))
        full += [f"---8<--- {url}", "", (head + body).rstrip(), ""]
        n += 1

    for section, subs in groups.items():
        lines += [f"## {section}", ""]
        for sub, entries in subs.items():
            if sub:
                lines += [f"### {sub}", ""]
            lines += entries + [""]

    lines += ["## Meta", "",
              f"- [Documentation update log]({base}log/): dated history of changes to this bundle.",
              f"- [For AI agents]({base}about/ai-agents/): endpoints and trust signals for agents.",
              ""]
    if example:
        lines[6:6] = [
            "Every page's Markdown source (OKF frontmatter included) is served "
            f"at its URL plus `index.md` — for example {example}index.md.",
            "",
        ]
    log = DOCS / "log.md"
    if log.exists():
        full += [f"---8<--- {base}log/", "", log.read_text(encoding="utf-8").rstrip(), ""]

    (DOCS / "llms.txt").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (DOCS / "llms-full.txt").write_text("\n".join(full).rstrip() + "\n", encoding="utf-8")
    print(f"llms.txt: {n} pages indexed; llms-full.txt: "
          f"{(DOCS / 'llms-full.txt').stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
