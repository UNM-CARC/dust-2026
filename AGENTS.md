# Agent guide — DUST 2026: Open Science Training

This repository is DUST 2026, three 50-minute lessons on open science,
research data management, and the ethics of artificial intelligence for NIEHS
Superfund Research Program trainees at the University of Arizona DUST Center
and the UNM METALS Center. It is built with [Zensical](https://zensical.org),
styled after the [UNM CARC documentation](https://carc.unm.edu/docs/), and
published at <https://tyson-swetnam.github.io/dust-2026/>. The `docs/` tree
is an **Open Knowledge Format (OKF) v0.2 knowledge bundle**
([spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)):
every content page carries YAML frontmatter with `type`, `title`,
`description`, `tags`, provenance (`generated`, `sources` with per-file
`last_modified`), and lifecycle (`status`, `stale_after`) fields. Section
`index.md` files are OKF §8 directory listings (no frontmatter);
`docs/log.md` is the OKF §9 dated change log.

## Reading the corpus

- `docs/llms.txt` — linked outline of every page with descriptions.
- `docs/llms-full.txt` — the entire corpus in one file, frontmatter included.
- Trust: pages without a `verified:` key are **unverified** (OKF §5.3).
  Lessons carry `stale_after` because the policy, pricing, and AI facts they
  cite change quickly; a page past that date needs a fact refresh.

## Commands

```bash
uv venv --python 3.12 .venv && source .venv/bin/activate
uv pip install -r requirements.txt          # zensical + pyyaml (Python 3.11+)
zensical serve                              # live preview at localhost:8000
zensical build --clean                      # static site -> site/
python3 scripts/okf_validate.py docs        # OKF conformance (CI-enforced)
python3 scripts/check_links.py docs         # links, images, nav coverage (CI-enforced)
python3 scripts/gen_llms_txt.py             # regenerate llms.txt indexes (CI checks drift)
python3 scripts/postbuild_agent_surface.py  # after build: md mirror + meta + robots.txt
python3 scripts/externalize_links.py        # add {target=_blank} to external links
```

## Editing rules

1. Every content page needs OKF frontmatter with a non-empty `type`
   (Lesson, Guide, or Reference). Run `okf_validate.py` before committing;
   CI fails otherwise.
2. Every `.md` file under `docs/` must be in the `nav` of `zensical.toml`.
   Zensical has no `not_in_nav`/`exclude_docs`: anything in `docs/` is
   published, so drafts do not belong in the tree.
3. Section `index.md` files carry **no frontmatter**: an `# H1`, one
   sentence, then `* [Title](page.md) - description` bullets (OKF §8). Keep
   their descriptions identical to the pages' `description` fields.
4. Links between pages are relative (`../about/resources.md`), never
   site-root-absolute (`/about/...`): the site is served under
   `/dust-2026/`. External links get `{target=_blank}`. No `{{ }}` template
   lines (Zensical has no macros plugin).
5. Every "SRP Example" callout pairs an Arizona (arsenic, mine tailings,
   phytoremediation, lung injury) item with a New Mexico (UNM METALS:
   uranium and metal mixtures, Navajo Nation and Pueblo of Laguna partners)
   item. Name centers, partner communities, and project topics, not
   individual investigators.
6. Dated facts (funder policy, article-processing charges, AI regulation,
   energy figures) must cite a primary source and say "as of <month year>".
   When you refresh them, update `generated.at` and `stale_after`.
7. Meaningful changes get a dated entry in `docs/log.md` (newest first,
   `## YYYY-MM-DD` headings).
8. After content changes: `gen_llms_txt.py`, `check_links.py`, build, then
   commit with a descriptive message.
9. Never mark a page `verified:`; only the author does that, as
   `verified: { by: "human:tswetnam", at: <ISO 8601> }`.
10. Keep the CC BY 4.0 attribution intact: the `sources` frontmatter, the
    `.carc-provenance` footer on adapted pages, and `docs/about/credits.md`.
