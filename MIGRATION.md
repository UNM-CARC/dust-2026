# Migration map

DUST 2026 was built from [DUST 2025](https://github.com/tyson-swetnam/dust-2025) (commit `29027dbda9ca29a123a68d8b4e2ae5dc198f7193`, 2025-10-29) on 2026-09-11, moving from MkDocs Material to Zensical + OKF v0.2. The 2025 site stays online; its pages map to the 2026 site as follows.

| Old source | Old URL | New source | New URL |
| --- | --- | --- | --- |
| `docs/index.md` | https://tyson-swetnam.github.io/dust-2025/ | `docs/index.md` | https://tyson-swetnam.github.io/dust-2026/ |
| `docs/about.md` | https://tyson-swetnam.github.io/dust-2025/about/ | `docs/about/training.md` | https://tyson-swetnam.github.io/dust-2026/about/training/ |
| `docs/lesson1_open_science/index.md` | https://tyson-swetnam.github.io/dust-2025/lesson1_open_science/ | `docs/lessons/01-open-science.md` | https://tyson-swetnam.github.io/dust-2026/lessons/01-open-science/ |
| `docs/lesson2_data_management/index.md` | https://tyson-swetnam.github.io/dust-2025/lesson2_data_management/ | `docs/lessons/02-data-management.md` | https://tyson-swetnam.github.io/dust-2026/lessons/02-data-management/ |
| `docs/lesson3_ai_ethics/index.md` | https://tyson-swetnam.github.io/dust-2025/lesson3_ai_ethics/ | `docs/lessons/03-ai-ethics.md` | https://tyson-swetnam.github.io/dust-2026/lessons/03-ai-ethics/ |
| `docs/resources.md` | https://tyson-swetnam.github.io/dust-2025/resources/ | `docs/about/resources.md` | https://tyson-swetnam.github.io/dust-2026/about/resources/ |
| `docs/acknowledgments.md` | https://tyson-swetnam.github.io/dust-2025/acknowledgments/ | `docs/about/credits.md` | https://tyson-swetnam.github.io/dust-2026/about/credits/ |
| *(new)* | | `docs/about/ai-agents.md` | https://tyson-swetnam.github.io/dust-2026/about/ai-agents/ |
| *(new)* | | `docs/log.md` | https://tyson-swetnam.github.io/dust-2026/log/ |
| `docs/javascripts/extra.js` | | *dropped* (reading-time and print widgets; shortcuts broke under a sub-path) | |
| `mkdocs.yml` | | `zensical.toml` | |
