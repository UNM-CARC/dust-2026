#!/usr/bin/env python3
"""Sweep docs/ so every external hyperlink opens in a new browser tab.

Appends {target=_blank} to external [text](http...) links, injects
target=_blank into existing attr blocks, and patches raw HTML anchors.
Internal/relative links, mailto:, images, and fenced code blocks are left
untouched. Frontmatter is preserved byte-for-byte. Idempotent.

Usage: python3 scripts/externalize_links.py [docs]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from okf_common import DOCS, FRONTMATTER_RE, iter_body_lines  # noqa: E402

ATTR_LINK_RE = re.compile(r"((?<!\!)\[[^\]]*\]\((https?://[^)\s]+)\)\{)([^}]*)\}")
BARE_LINK_RE = re.compile(r"((?<!\!)\[[^\]]*\]\((https?://[^)\s]+)\))(?!\{)")
HTML_A_RE = re.compile(r'(<a\s+)(?![^>]*\btarget=)([^>]*href="https?://[^"]*")')
INLINE_CODE_RE = re.compile(r"(`+)(?:.*?)\1")


def _fix(segment: str) -> str:
    def attr_sub(m):
        attrs = m.group(3)
        if "target=" in attrs:
            return m.group(0)
        return f"{m.group(1)}{attrs.rstrip()} target=_blank }}"
    segment = ATTR_LINK_RE.sub(attr_sub, segment)
    segment = BARE_LINK_RE.sub(r"\1{target=_blank}", segment)
    return HTML_A_RE.sub(r'\1target="_blank" \2', segment)


def externalize_links(md: str) -> str:
    out = []
    for _, line, in_code in iter_body_lines(md):
        if in_code:
            out.append(line)
            continue
        parts, pos = [], 0
        for m in INLINE_CODE_RE.finditer(line):
            parts.append(_fix(line[pos:m.start()]))
            parts.append(m.group(0))
            pos = m.end()
        parts.append(_fix(line[pos:]))
        out.append("".join(parts))
    return "\n".join(out) + ("\n" if md.endswith("\n") else "")


def main():
    docs = Path(sys.argv[1]) if len(sys.argv) > 1 else DOCS
    changed = 0
    for path in sorted(docs.rglob("*.md")):
        if "assets" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text) if text.startswith("---") else None
        fm, body = (text[:m.end()], text[m.end():]) if m else ("", text)
        new_body = externalize_links(body)
        if new_body != body:
            path.write_text(fm + new_body, encoding="utf-8")
            changed += 1
            print(f"  updated {path.relative_to(docs)}")
    print(f"{changed} file(s) updated.")


if __name__ == "__main__":
    main()
