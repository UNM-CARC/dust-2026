# DUST 2026: Open Science Training

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Built with Zensical](https://img.shields.io/badge/built%20with-Zensical-ba0c2f)](https://zensical.org)

Three 50-minute lessons, each with a self-paced homework page, for NIEHS
Superfund Research Program trainees at the
[University of Arizona DUST Center](https://superfund.arizona.edu/), the
[UNM METALS Center](https://hsc.unm.edu/pharmacy/research/areas/metals/), and the
[Texas A&M Superfund Research Center](https://superfund.tamu.edu/):

1. **Foundations of Open Science** — principles, the six pillars, Gold
   Standard Science, and the 2026 US public-access and publication-cost
   landscape
2. **Modern Data Management** — the data life cycle, FAIR and CARE, the 2026
   NIH and NSF plan formats, data rescue
3. **Ethics and Artificial Intelligence** — bias, responsible and agentic AI
   use, NIH and journal AI rules, energy and water costs, regulation

Each lesson is a 50-minute lecture page plus a twelve-module self-paced
homework page with checkpoints, written so an AI tutor can deliver it.

**Website:** <https://unm-carc.github.io/dust-2026/>

This is the 2026 edition of [DUST 2025](https://tyson-swetnam.github.io/dust-2025/).
It is built with [Zensical](https://zensical.org), styled after the
[UNM CARC documentation](https://carc.unm.edu/docs/), and structured as an
[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
knowledge bundle so the content is first-class for both humans and AI agents.

## Quick start

```bash
uv venv --python 3.12 .venv && source .venv/bin/activate   # or: python3.12 -m venv .venv
uv pip install -r requirements.txt   # zensical + pyyaml (Python 3.11+)
zensical serve                       # live preview at http://localhost:8000
zensical build --clean               # static site in ./site
```

## Repository layout

```
├── zensical.toml              # Site configuration (theme, nav, extensions)
├── docs/                      # The OKF knowledge bundle + site content
│   ├── index.md               # Landing page (declares okf_version: "0.2")
│   ├── log.md                 # OKF update log (reserved filename)
│   ├── lessons/               # Three lecture pages + three self-paced pages + listing
│   ├── about/                 # Overview, resources, credits, AI tutor, accessibility, AI-agent guide
│   ├── assets/                # Images and logos
│   ├── stylesheets/extra.css  # UNM cherry + turquoise theme, DUST additions
│   └── llms.txt, llms-full.txt  # Generated agent indexes (do not edit)
├── scripts/
│   ├── okf_validate.py            # OKF v0.2 conformance checker (CI)
│   ├── check_links.py             # Links, images, and nav coverage (CI)
│   ├── gen_llms_txt.py            # Builds docs/llms.txt + docs/llms-full.txt
│   ├── postbuild_agent_surface.py # Markdown mirror, OKF meta tags, robots.txt
│   └── externalize_links.py       # Adds {target=_blank} to external links
├── MIGRATION.md               # 2025 URLs -> 2026 URLs
├── AGENTS.md / CLAUDE.md      # Rules for coding agents working in this repo
└── .github/workflows/docs.yml # Validation + GitHub Pages deployment
```

## Machine readability (OKF)

Every content page carries YAML frontmatter with:

- `type` — `Lesson`, `Guide`, or `Reference` (required by OKF)
- `title`, `description`, `tags` — used by search, indexes, and agents
- `generated: { by, at }` — who or what produced the current content
- `sources` — provenance links to the exact upstream DUST 2025, FOSS, or
  GPT 101 file, with `last_modified` from git history
- `status` / `stale_after` — lifecycle markers; the lessons carry a
  `stale_after` date because the policy and AI facts they cite move quickly
- `lesson` (Lesson pages) — objectives, key terms, duration, delivery modes,
  and an accessibility profile; the build turns it into a schema.org
  `LearningResource` record so AI tutors and learning platforms can pick a
  delivery mode (see `docs/about/ai-tutor.md` and `docs/about/accessibility.md`)

Pages rewritten by an agent are intentionally **unverified** (no `verified`
key). When the author reviews a page, they add:

```yaml
verified: { by: "human:tswetnam", at: "2026-XX-XXT00:00:00Z" }
```

The deployed site is directly consumable by AI agents:

- `/llms.txt` ([convention](https://llmstxt.org)) — linked outline;
  `/llms-full.txt` — the full corpus with frontmatter in one file.
- **Markdown mirror**: any page URL + `index.md` returns that page's source
  with OKF frontmatter (e.g. `/lessons/01-open-science/index.md`).
- Rendered pages carry `<link rel="alternate" type="text/markdown">` and
  `okf:*` meta tags; `robots.txt` advertises all of the above.
  `docs/about/ai-agents.md` is the human- and agent-readable guide.

After content changes, regenerate the indexes (CI fails on drift) and check
the bundle:

```bash
python scripts/okf_validate.py docs
python scripts/check_links.py docs
python scripts/gen_llms_txt.py
zensical build --clean && python scripts/postbuild_agent_surface.py site
```

## Using these materials

All content is licensed [CC BY 4.0](LICENSE): use it in workshops and
courses, adapt it to your discipline, remix it, with attribution. Suggested
attribution:

> Adapted from "DUST 2026: Open Science Training" by Tyson L. Swetnam
> (<https://unm-carc.github.io/dust-2026/>), CC BY 4.0, which builds on
> DUST 2025, CyVerse FOSS, and the GPT 101 workshop.

**Citation (BibTeX):**

```bibtex
@misc{swetnam2026dust,
  title        = {DUST 2026: Open Science Training},
  author       = {Swetnam, Tyson L.},
  year         = {2026},
  howpublished = {\url{https://unm-carc.github.io/dust-2026/}},
  note         = {Licensed under CC BY 4.0}
}
```

See [docs/about/credits.md](docs/about/credits.md) for source materials,
contributors, and funding.

## Deployment

Pushing to `main` runs OKF validation and the link check, verifies the
llms.txt indexes are current, builds the site, adds the agent surface, and
deploys to GitHub Pages via `.github/workflows/docs.yml`. The workflow enables
Pages automatically (`configure-pages` with `enablement: true`); if the first
deploy fails on permissions, set Settings → Pages → Source to "GitHub Actions"
once.

## Contact

- **Author:** Tyson L. Swetnam, UNM Center for Advanced Research Computing
- **Email:** <tswetnam@unm.edu>
- **ORCID:** [0000-0002-6639-7181](https://orcid.org/0000-0002-6639-7181)
- **Issues and suggestions:** <https://github.com/UNM-CARC/dust-2026/issues>
