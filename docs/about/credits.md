---
title: "Credits and attribution"
description: "Source materials, contributors, institutional support, license, and how to cite DUST 2026."
type: Reference
tags:
  - About
  - Credits
  - Citation
  - License
generated:
  by: "claude/fable-5-1"
  at: "2026-09-11T00:00:00Z"
sources:
  - id: dust-2025-acknowledgments
    resource: "https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/acknowledgments.md"
    title: "DUST 2025: Acknowledgments"
    author: "human:tswetnam"
    last_modified: "2025-10-14T10:25:44-07:00"
  - id: unm-carc-foss-credits
    resource: "https://github.com/UNM-CARC/foss/blob/d1b13dc37e48b34b294fe21bfbab11b23875b4b1/docs/about/credits.md"
    title: "FOSS (UNM CARC edition): Credits and attribution"
    author: "team:unm-carc"
    last_modified: "2026-09-11T07:53:55-06:00"
  - id: intro-gpt-2026
    resource: "https://github.com/tyson-swetnam/intro-gpt/blob/5fc253b6332d277b21ec965b97648091131c1640/docs/index.md"
    title: "Generative AI & Prompt Engineering (intro-gpt, 2026)"
    author: "human:tswetnam"
    last_modified: "2026-08-31T07:34:27-06:00"
  - id: okf-spec
    resource: "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md"
    title: "Open Knowledge Format (OKF) v0.2 specification"
    author: "team:googlecloudplatform"
status: stable
---

# Credits and attribution

DUST 2026 is a revised edition of DUST 2025 and, like it, synthesizes openly licensed open science materials from several projects. We are grateful to the creators and contributors of everything listed here.

## Primary source materials

### DUST 2025: Open Science Training

The direct predecessor of this site. The three-lesson structure, the 50-minute lesson format, the Arizona Superfund examples, the quizzes, and most of the prose come from the 2025 edition, written for University of Arizona Superfund Research Program trainees.

- **Site:** [tyson-swetnam.github.io/dust-2025](https://tyson-swetnam.github.io/dust-2025/){target=_blank}
- **Repository:** [github.com/tyson-swetnam/dust-2025](https://github.com/tyson-swetnam/dust-2025){target=_blank}
- **Contributors:** Tyson Swetnam
- **License:** CC BY 4.0

### CyVerse FOSS and the UNM CARC FOSS edition

The CyVerse Foundational Open Science Skills (FOSS) program provided substantial content for Lessons 1 and 2, particularly open science definitions and frameworks, the six pillars of open science, FAIR and CARE data principles, data lifecycle and management practices, and data management plan guidance. The 2026 lessons also draw on the UNM Center for Advanced Research Computing (CARC) edition of FOSS, itself adapted from CyVerse FOSS under CC BY 4.0, for the updated pillars, the CARE and Indigenous data sovereignty section, and the Gold Standard Science material.

- **CyVerse source:** [foss.cyverse.org](https://foss.cyverse.org){target=_blank}
- **CyVerse repository:** [github.com/CyVerse-learning-materials/foss](https://github.com/CyVerse-learning-materials/foss){target=_blank}
- **UNM CARC edition:** [unm-carc.github.io/foss](https://unm-carc.github.io/foss/){target=_blank}
- **Contributors:** CyVerse Science Team, including Jason Williams, Tyson Swetnam, Jeffrey Gillan, and many community contributors
- **License:** CC BY 4.0

### NCEMS Pre-Summit FOSS Training

The NCEMS Pre-Summit training provided refined content on open science motivations and applications, data management best practices, prompt engineering and AI tool usage, and the integration of open science with modern research practices.

- **Source:** [ncems.github.io/pre-summit-foss](https://ncems.github.io/pre-summit-foss){target=_blank}
- **Repository:** [github.com/NCEMS/pre-summit-foss](https://github.com/NCEMS/pre-summit-foss){target=_blank}
- **Contributors:** Tyson Swetnam, Nicole Lazar, and the NCEMS community
- **License:** CC BY 4.0

### Generative AI and Prompt Engineering workshop (intro-gpt, 2026)

Substantial content for Lesson 3 on AI ethics and responsible AI use came from the Introduction to GPT workshop, now titled *Generative AI & Prompt Engineering*. The 2026 lesson uses its 2026 modules on AI ethics frameworks, bias and discrimination in AI systems, transparency and accountability, legal, environmental, and research-integrity considerations, agentic AI and the Model Context Protocol, and prompt engineering fundamentals.

- **Source:** [tyson-swetnam.github.io/intro-gpt](https://tyson-swetnam.github.io/intro-gpt/){target=_blank}
- **Repository:** [github.com/tyson-swetnam/intro-gpt](https://github.com/tyson-swetnam/intro-gpt){target=_blank}
- **Contributors:** Tyson Swetnam
- **License:** CC BY 4.0

### Awesome Open Science

Resources and community connections drew from its curated lists of open science tools, repository and platform recommendations, and community networks and organizations.

- **Source:** [tyson-swetnam.github.io/awesome-open-science](https://tyson-swetnam.github.io/awesome-open-science){target=_blank}
- **Repository:** [github.com/tyson-swetnam/awesome-open-science](https://github.com/tyson-swetnam/awesome-open-science){target=_blank}
- **Contributors:** Tyson Swetnam
- **License:** CC BY 4.0

## Additional influences

### The Turing Way

Inspiration for documentation structure, accessibility, and community-driven open science practices.

- **Source:** [book.the-turing-way.org](https://book.the-turing-way.org/){target=_blank}
- **License:** CC BY 4.0

### The Carpentries

Pedagogical approach emphasizing hands-on learning and practical skills development.

- **Source:** [carpentries.org](https://carpentries.org/){target=_blank}
- **License:** CC BY 4.0

### FORRT

Framework for understanding open science education and training needs. The 2025 edition cited FOSTER Open Science; that link no longer resolves, so we point to FORRT instead.

- **Source:** [forrt.org](https://forrt.org/){target=_blank}

## Technical infrastructure

### Zensical

This site is built with the Zensical static site generator. DUST 2025 was built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/){target=_blank}, whose Markdown syntax (admonitions, content tabs, icons) carries over unchanged.

- **Project:** [zensical.org](https://zensical.org){target=_blank}

### Open Knowledge Format (OKF) v0.2

Every content page carries OKF frontmatter (type, description, tags, provenance, and lifecycle), and the site publishes `llms.txt`, `llms-full.txt`, and a Markdown mirror of each page so that people and AI agents can read the same source. See [For AI agents](ai-agents.md).

- **Specification:** [OKF SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md){target=_blank}

### UNM CARC documentation design

The stylesheet, palette, hero, and card layout follow the UNM Center for Advanced Research Computing documentation, and the build scripts (OKF validation, link checking, llms.txt generation) are shared with the UNM CARC FOSS edition.

- **Design reference:** [carc.unm.edu/docs](https://carc.unm.edu/docs/){target=_blank}

## Content attribution

All content in this training is derived from openly licensed sources and adapted for educational purposes. Specific attributions:

**Lesson 1: Foundations of Open Science**

- Core framework from CyVerse FOSS Lesson 1 and its UNM CARC edition
- Policy context from NCEMS Pre-Summit Training, updated to the 2026 US public-access landscape
- Community resources from Awesome Open Science
- Arizona examples from DUST 2025; New Mexico (UNM METALS) examples created for this edition

**Lesson 2: Modern Data Management**

- Data lifecycle and principles from CyVerse FOSS Lesson 2
- CARE and Indigenous data sovereignty section from the UNM CARC FOSS edition
- Practical examples from NCEMS Pre-Summit Training
- DMP guidance synthesized from multiple sources

**Lesson 3: Ethics and Artificial Intelligence**

- Primary content from the intro-gpt ethics, bias, legal, environment, transparency, and agentic modules (2026)
- Bias framework synthesized from multiple AI ethics sources
- Practical research scenarios created for this training
- Updated policy landscape as of September 2026

## Individual contributors

Special thanks to:

- **Tyson Swetnam** - Original content creation, curation, and instruction across all source materials
- **Jason Williams** - CyVerse FOSS program development and open science leadership
- **Jeffrey Gillan** - CyVerse FOSS content development and geospatial expertise
- **Nicole Lazar** - NCEMS training design and statistical perspectives
- **CyVerse Science Team** - Ongoing development of open science training materials
- **NCEMS Community** - Feedback and refinement of training content
- **UNM CARC** - Zensical and OKF build tooling, stylesheet, and page conventions

## Community acknowledgments

This training benefits from broader open science communities:

- **UNESCO** - Open Science framework and recommendations
- **Center for Open Science** - FAIR principles and research integrity
- **Global Indigenous Data Alliance** - CARE principles for data sovereignty
- **Research Data Alliance** - Data management standards and practices
- **AI ethics researchers** - Frameworks for responsible AI development and use

## Institutional support

DUST 2026 is written for trainees of three NIEHS Superfund Research Program centers:

- **University of New Mexico** - home of the author and of the UNM METALS Superfund Research Center, *Metal Exposure and Toxicity Assessment on Tribal Lands in the Southwest* (NIEHS P42ES025589): [hsc.unm.edu/pharmacy/research/areas/metals](https://hsc.unm.edu/pharmacy/research/areas/metals/){target=_blank}
- **University of Arizona** - home of the UA Superfund Research Center, *Hazardous Dust in Drylands: Exposure, Health Impacts, and Mitigation*: [superfund.arizona.edu](https://superfund.arizona.edu/){target=_blank}
- **Texas A&M University** - home of the Texas A&M Superfund Research Center, *Comprehensive tools and models for addressing exposure to mixtures during environmental emergency-related contamination events*: [superfund.tamu.edu](https://superfund.tamu.edu/){target=_blank}

Development of the source materials was supported by:

- **University of Arizona**
- **CyVerse** (NSF DBI-0735191, DBI-1265383, DBI-1743442)
- **NCEMS**
- **NSF** - Various grants supporting open science infrastructure

Any opinions, findings, and conclusions expressed here are those of the author and do not necessarily reflect the views of NIEHS, NSF, or the participating universities.

## License and reuse

This training is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/){target=_blank}.

**Suggested citation:**

> Swetnam, T.L. (2026). DUST 2026: Open Science Training. https://unm-carc.github.io/dust-2026/

```bibtex
@misc{swetnam2026dust,
  author = {Swetnam, Tyson L.},
  title  = {DUST 2026: Open Science Training},
  year   = {2026},
  url    = {https://unm-carc.github.io/dust-2026/},
  note   = {CC BY 4.0. Revised edition of DUST 2025.}
}
```

To cite the previous edition:

> Swetnam, T.L. (2025). DUST 2025: Open Science Training. https://tyson-swetnam.github.io/dust-2025/

**Attribution requirements:**

When reusing this material you must:

1. Credit this training (DUST 2026) and its predecessor (DUST 2025)
2. Credit the original source materials (CyVerse FOSS, NCEMS, intro-gpt, etc.)
3. Indicate if changes were made
4. Provide a link to the license

**Example attribution:**

> Adapted from "DUST 2026: Open Science Training" by Tyson L. Swetnam (CC BY 4.0), a revised edition of DUST 2025 that synthesizes materials from CyVerse FOSS, the UNM CARC FOSS edition, NCEMS Pre-Summit Training, the intro-gpt workshop, and other open science resources.

## Contributing

We welcome contributions to improve this training:

- **Report issues:** [github.com/UNM-CARC/dust-2026/issues](https://github.com/UNM-CARC/dust-2026/issues){target=_blank}
- **Suggest improvements:** Submit pull requests to [github.com/UNM-CARC/dust-2026](https://github.com/UNM-CARC/dust-2026){target=_blank}
- **Share feedback:** Email tswetnam@unm.edu

All contributors will be acknowledged in future versions.

## Updates and maintenance

This training will be updated to reflect evolving open science practices, new tools and resources, policy changes, community feedback, and emerging AI ethics considerations. Each page records when it was generated in its frontmatter, and the [update log](../log.md) lists every dated change.

## Thank you

Most importantly, thank you to:

- **All open science practitioners** who share their work openly
- **Instructors and educators** who teach these principles
- **Researchers** implementing open practices despite institutional barriers
- **Community partners** in Arizona and New Mexico whose data governance conditions shape how this research is shared
- **You** - for investing time in learning and practicing open science

By working together, we strengthen the foundation of transparent, reproducible, and accessible research for everyone.

<p class="carc-provenance" markdown>Adapted from [DUST 2025](https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/acknowledgments.md){target=_blank} (last source update 2025-10-14), CC BY 4.0. Spotted a problem? [Open an issue](https://github.com/UNM-CARC/dust-2026/issues){target=_blank}.</p>
