#!/usr/bin/env python3
"""Check internal links, images, and nav coverage in the docs/ bundle.

Errors (exit 1):
  * a relative link or image whose target file does not exist in docs/
  * a site-root-absolute link ("/path") — these break when the site is
    served under a sub-path such as https://<org>.github.io/<repo>/
  * a nav entry in zensical.toml that points at a missing file
  * a Markdown page that is not in the nav (Zensical has no not_in_nav or
    exclude_docs: every page in docs/ is published, so orphans must either
    join the nav or leave the bundle)

Warnings:
  * #anchors that do not match a heading slug or explicit {#id} in the target
  * links to retired hostnames (the old CyVerse domains for these sites)

Usage: python3 scripts/check_links.py [docs]
"""

from __future__ import annotations

import posixpath
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from okf_common import (DOCS, is_external, iter_body_lines,  # noqa: E402
                        iter_link_targets, load_config, nav_pages,
                        split_frontmatter, split_target)

RETIRED_PREFIXES = ("foss.cyverse.org", "cc.cyverse.org", "container-camp.cyverse.org",
                    "learning.cyverse.org", "cyverse-learning-materials.github.io/foss",
                    "cyverse-learning-materials.github.io/container-camp",
                    "cyverse-learning-materials.github.io/learning-materials-home")
# Pages allowed to name the retired hosts (credits and provenance history)
RETIRED_OK = {"about/credits.md", "log.md"}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ATTR_ID_RE = re.compile(r"\{[^}]*#([\w-]+)[^}]*\}")
ICON_RE = re.compile(r":[a-z0-9]+(?:-[a-z0-9]+)+:")
IGNORED = {"llms.txt", "llms-full.txt"}


def slugify(value: str) -> str:
    """Python-Markdown toc default slugify."""
    value = ICON_RE.sub("", value)
    value = re.sub(r"\{[^}]*\}\s*$", "", value)          # trailing attr_list
    value = re.sub(r"<[^>]+>", "", value)                # inline HTML
    value = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", value)  # links -> text
    value = re.sub(r"[`*_~]", "", value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def anchors_for(path: Path, cache: dict) -> set[str]:
    if path in cache:
        return cache[path]
    text = path.read_text(encoding="utf-8")
    try:
        _, body = split_frontmatter(text)
    except ValueError:
        body = text
    found: set[str] = set()
    counts: dict[str, int] = {}
    for _, line, in_code in iter_body_lines(body):
        if in_code:
            continue
        for m in ATTR_ID_RE.finditer(line):
            found.add(m.group(1))
        h = HEADING_RE.match(line)
        if h:
            slug = slugify(h.group(2))
            if slug in counts:
                counts[slug] += 1
                found.add(f"{slug}_{counts[slug]}")
            else:
                counts[slug] = 0
                found.add(slug)
    cache[path] = found
    return found


def main() -> int:
    docs = Path(sys.argv[1]) if len(sys.argv) > 1 else DOCS
    errors: list[str] = []
    warnings: list[str] = []
    cache: dict = {}

    pages = {p.relative_to(docs).as_posix() for p in docs.rglob("*.md")}

    # Nav coverage
    cfg = load_config(docs.parent)
    in_nav: set[str] = set()
    for _, label, target in nav_pages(cfg.get("nav", [])):
        if is_external(target):
            continue
        in_nav.add(target)
        if target not in pages:
            errors.append(f"zensical.toml: nav entry {label or ''!s} -> {target} does not exist")
    for page in sorted(pages - in_nav):
        errors.append(f"{page}: not in the nav (add it to zensical.toml or remove it)")

    # Links
    n_links = 0
    for rel in sorted(pages):
        path = docs / rel
        text = path.read_text(encoding="utf-8")
        try:
            _, body = split_frontmatter(text)
        except ValueError:
            body = text
        offset = text[: len(text) - len(body)].count("\n")
        for lineno, target in iter_link_targets(body):
            n_links += 1
            where = f"{rel}:{lineno + offset}"
            if target.startswith(("http://", "https://")):
                bare = re.sub(r"^https?://", "", target).lower()
                if rel not in RETIRED_OK and any(
                        bare == p or bare.startswith(p + "/") for p in RETIRED_PREFIXES):
                    warnings.append(f"{where}: link to a retired site: {target}")
                continue
            if is_external(target) and not target.startswith("#"):
                continue
            if target.startswith("/"):
                errors.append(f"{where}: site-root-absolute link {target!r} breaks under a sub-path; make it relative")
                continue
            tpath, suffix = split_target(target)
            if not tpath:  # same-page anchor
                frag = suffix[1:] if suffix.startswith("#") else ""
                if frag and frag not in anchors_for(path, cache):
                    warnings.append(f"{where}: anchor #{frag} not found on this page")
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(rel), tpath))
            if resolved.startswith(".."):
                errors.append(f"{where}: {target!r} points outside docs/")
                continue
            dest = docs / resolved
            if tpath.endswith("/") or dest.is_dir():
                if (dest / "index.md").exists():
                    dest = dest / "index.md"
                else:
                    errors.append(f"{where}: {target!r} is a directory without index.md; link the .md file")
                    continue
            if not dest.exists():
                errors.append(f"{where}: broken link {target!r} (no {resolved})")
                continue
            if dest.suffix == ".md" and suffix.startswith("#") and len(suffix) > 1:
                if suffix[1:] not in anchors_for(dest, cache):
                    warnings.append(f"{where}: anchor {suffix} not found in {resolved}")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\nChecked {n_links} links in {len(pages)} pages: "
          f"{len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
