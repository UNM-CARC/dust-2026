---
title: "Lesson 1 homework: Open Science, self-paced"
description: "The self-paced companion to Lesson 1: twelve modules with checkpoints on the six pillars, Gold Standard Science in depth, the 2026 public-access and publication-cost landscape, a full self-assessment, and the complete quiz."
type: Lesson
tags:
  - Open Science
  - Open Access
  - FAIR
  - CARE
  - Gold Standard Science
  - Public Access Policy
  - Superfund Research Program
  - Self-paced
lesson:
  number: 1
  format: self-paced
  duration_minutes: 100
  companion: 01-open-science.md
  delivery_modes:
    - tutor
    - interactive
    - lecture
  objectives:
    - "Define open science and explain its core components"
    - "Describe each of the six pillars of open science and give a Superfund example of each"
    - "Explain the FAIR and CARE principles and when data must stay closed"
    - "Describe the nine Gold Standard Science tenets, how agencies are implementing them, and the debate about them"
    - "Describe the 2026 US public-access and publication-cost landscape and what it means for SRP trainees"
    - "Evaluate your own research practices against open science principles and choose concrete actions"
  key_terms:
    - open science
    - open access
    - subscription, gold, and diamond open access
    - article processing charge (APC)
    - preprint
    - accepted manuscript
    - version of record
    - rights retention
    - FAIR principles
    - CARE principles
    - open educational resources
    - pre-registration
    - open peer review
    - open source
    - Gold Standard Science
    - Nelson memo
  accessibility:
    language: en
    access_mode: [textual, visual]
    access_mode_sufficient: [textual]
    features: [alternativeText, longDescription, readingOrder, structuralNavigation, tableOfContents, unlocked, annotations]
    hazards: [none]
    media: "No audio or video. Five images, each with alt text and a collapsible text description immediately after it. Tables carry header rows. Checkpoint and quiz answers are native details/summary elements."
generated:
  by: "claude/fable-5-1"
  at: "2026-09-12T02:00:00Z"
sources:
  - id: dust-2025
    resource: "https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/lesson1_open_science/index.md"
    title: "DUST 2025: docs/lesson1_open_science/index.md"
    author: "human:tswetnam"
    last_modified: "2025-10-14T14:51:10-07:00"
  - id: unm-carc-foss
    resource: "https://github.com/UNM-CARC/foss/blob/f83c334a6d6a53795631c108aef2f1a477a1b7ef/docs/lessons/01-open-science.md"
    title: "UNM CARC FOSS: docs/lessons/01-open-science.md"
    author: "team:unm-carc"
    last_modified: "2026-09-11T07:41:50-06:00"
  - id: eo-14303
    resource: "https://www.whitehouse.gov/presidential-actions/2025/05/restoring-gold-standard-science/"
    title: "Executive Order 14303: Restoring Gold Standard Science (23 May 2025)"
    author: "team:white-house"
  - id: ostp-gss-guidance
    resource: "https://www.whitehouse.gov/releases/2025/06/ostp-issues-agency-guidance-for-gold-standard-science/"
    title: "OSTP: Agency Guidance for Implementing Gold Standard Science (23 June 2025)"
    author: "team:ostp"
  - id: nih-gss-plan
    resource: "https://osp.od.nih.gov/nih-releases-implementation-plan-to-drive-gold-standard-science/"
    title: "NIH Releases Implementation Plan to Drive Gold Standard Science (22 August 2025)"
    author: "team:nih-osp"
  - id: sparc-gss-brief
    resource: "https://sparcopen.org/our-work/gss_policy_brief/"
    title: "SPARC: Gold Standard Science, Federal Implementation Strategies and Open Access Policy Intersections"
    author: "team:sparc"
  - id: sparc-2cfr200
    resource: "https://sparcopen.org/our-work/2026-proposed-2cfr200-updates-faqs/"
    title: "SPARC: 2026 OMB Proposed Updates to 2 CFR Part 200, FAQ"
    author: "team:sparc"
  - id: ostp-golden-age
    resource: "https://www.whitehouse.gov/releases/2026/07/45470/"
    title: "OSTP: Science: A New Golden Age (21 July 2026)"
    author: "team:ostp"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# Lesson 1 homework: Open Science, self-paced

!!! info "How to use this page"
    **Time:** about 90 to 120 minutes, in one sitting or several.

    **Structure:** twelve modules. Each ends with a **checkpoint**: answer it in your own words before opening the answer. The in-person lecture, [Lesson 1: Foundations of Open Science](01-open-science.md), is the summary of this page; complete this page before [Lesson 2](02-data-management.md).

    **With an AI tutor:** this page is written so an AI assistant can teach it module by module. See [Learn with an AI tutor](../about/ai-tutor.md) for prompts, including prompts for screen-reader users, deaf and hard-of-hearing learners, and learners whose first language is not English. Every figure has a text description directly below it.

!!! abstract "In brief"
    This page is the full version of Lesson 1. Modules 1 to 8 cover what open science is, its six pillars, and why researchers practice it. Module 9 explains Gold Standard Science, the federal framework that since 2025 has attached nine tenets and annual reporting to funded research. Module 10 explains the 2026 rules on public access and publication costs. Modules 11 and 12 are a self-assessment, discussion questions, an action plan, and the full quiz. Every example pairs an Arizona item with a New Mexico item from the two Superfund Research Program centers.

## Learning objectives

!!! success "After completing this page, you will be able to:"
    - Define open science and explain its core components
    - Describe each of the six pillars of open science and give a Superfund example of each
    - Explain the FAIR and CARE principles and when data must stay closed
    - Describe the nine Gold Standard Science tenets, how agencies are implementing them, and the debate about them
    - Describe the 2026 US public-access and publication-cost landscape and what it means for SRP trainees
    - Evaluate your own research practices against open science principles and choose concrete actions

---

## Module 1: Definitions and the research life cycle

*About 10 minutes.*

### What brings you here?

!!! question "Self-reflection"
    - What does "open" mean to you in the context of your research?
    - Have you encountered barriers to accessing research materials you needed?
    - What concerns do you have about sharing your own work?

### Why open science matters now

In 2023 the White House declared the Year of Open Science, joined by federal agencies and over 85 universities. In 2025 the federal frame changed to "Gold Standard Science" ([Executive Order 14303](https://www.whitehouse.gov/presidential-actions/2025/05/restoring-gold-standard-science/){target=_blank}), and the policy details are still moving (Module 9). What has not changed, and has in fact tightened, is the requirement itself: zero-embargo public access to accepted manuscripts is now in force at six federal agencies, including NIH (Module 10).

Open science is not just an ideological movement. It is a condition of funding:

- **Federal funders** require data management and sharing plans *and* immediate public access to accepted manuscripts
- **Publishers** increasingly require data and code availability, and increasingly steer authors toward paid open-access routes
- **Universities** are recognizing open practices in promotion and tenure
- **The public** expects access to publicly funded research, and communities near contaminated sites expect it in forms they can use

!!! example "SRP Example: why open science matters for Superfund research"
    **Environmental justice:** Communities in Arizona-Sonora mining towns, and the Navajo communities of Red Water Pond Road, Blue Gap-Tachee and Cameron, and the Pueblo of Laguna near the Jackpile Mine, living with the legacy of abandoned uranium mines, deserve access to research about contamination affecting their health.

    **Reproducibility:** Toxicology studies on arsenic exposure, and on uranium, arsenic and vanadium (U/As/V) mixtures, must be reproducible to inform public health policy.

    **Two centers, one shared problem:** The University of Arizona DUST Center ("Hazardous Dust in Drylands: Exposure, Health Impacts, and Mitigation") and the UNM METALS Center ("Metal Exposure and Toxicity Assessment on Tribal Lands in the Southwest") both study inhaled mine dust. Transparent protocols and data sharing let their results be compared.

    **NIH requirements:** Superfund Research Program grants require data management and sharing plans, and every accepted manuscript must be deposited in PubMed Central at acceptance.

    **Community trust:** Data collected with tribal partners are governed under the CARE Principles and community review. Openness that ignores that authority destroys the trust the research depends on.

    **Public health impact:** Findings about mine-tailings dust exposure and lung disease must be disseminated rapidly to protect vulnerable populations.

### Defining open science

Multiple definitions exist, each emphasizing different aspects:

!!! quote "Key definitions"
    **"Open Science is transparent and accessible knowledge that is shared and developed through collaborative networks"**

    — [Vincente-Saez & Martinez-Fuentes (2018)](https://doi.org/10.1016/j.jbusres.2017.12.043){target=_blank}

    **"Open Science is defined as an inclusive construct that combines various movements and practices aiming to make multilingual scientific knowledge openly available, accessible and reusable for everyone"**

    — [UNESCO](https://www.unesco.org/en/natural-sciences/open-science){target=_blank}

    **"A series of reforms that interrogate every step in the research life cycle to make it more efficient, powerful and accountable in our emerging digital society"**

    — Jeffrey Gillan

### The research life cycle

Open science touches every stage of research, and each stage offers opportunities to embrace openness:

1. **Planning:** pre-registration, open protocols
2. **Execution:** open notebooks, transparent methods
3. **Analysis:** reproducible workflows, version control
4. **Dissemination:** open access publishing, data sharing

### The six pillars at a glance

Open access
:   Publications freely available to all

Open data
:   Research data FAIR and accessible

Open educational resources
:   Educational resources open to everyone

Open methodology
:   Transparent, reproducible methods

Open peer review
:   Review process open and attributed

Open source
:   Software code freely available

??? question "How many pillars are there really?"
    The number varies from [4](https://narratives.insidehighered.com/four-pillars-of-open-science/){target=_blank} to [8](https://www.ucl.ac.uk/library/research-support/open-science/8-pillars-open-science){target=_blank} depending on the framework. Some combine categories, others separate them. What matters is understanding the principles, not memorizing a number.

??? question "Checkpoint 1: In one sentence, what does the UNESCO definition add that the 2018 definition does not?"
    It names **who** open science is for ("everyone") and adds **multilingual**: openness includes language, not only cost and licensing. That matters for research shared with Spanish-speaking border communities and Diné-speaking Navajo communities.

---

## Module 2: Open access

*About 15 minutes.*

<figure markdown>
  [![Open Access logo: an orange open padlock](https://upload.wikimedia.org/wikipedia/commons/f/f3/Open_Access_PLoS.svg){ width="150" }](https://en.wikipedia.org/wiki/Open_access){target=_blank}
  <figcaption>The open-access logo</figcaption>
</figure>

??? note "Text description of this figure"
    The open-access logo, designed by PLOS: an orange padlock drawn in outline with its shackle open, on a white background. It links to the Wikipedia article on open access.

!!! quote "Definition"
    "Open access is a publishing model for scholarly communication that makes research information available to readers at no cost, as opposed to the traditional subscription model"

    — [OpenAccess.nl](https://www.openaccess.nl/en/what-is-open-access){target=_blank}

### Publishing models

1. **Subscription model:** the author pays little or nothing; the publisher charges readers and institutions.
2. **Gold open access model:** the author (or funder) pays an article processing charge (APC); the article is freely available. 2026 list prices ([Nature](https://www.nature.com/nature/for-authors/publishing-options){target=_blank}, [PLOS](https://plos.org/fees/){target=_blank}):

    | Journal | 2026 APC (USD) |
    | --- | --- |
    | Nature | 12,850 |
    | Nature Communications | 7,350 |
    | Scientific Reports | 2,850 |
    | PLOS ONE | 2,477 |

3. **Diamond open access model:** no fees for authors or readers; journals are funded by institutions, societies or consortia. cOAlition S's 2026-2030 strategy [drops hard mandates](https://www.chemistryworld.com/news/what-next-for-open-access-as-coalition-s-scales-back-its-ambitions/4022618.article){target=_blank} and backs Diamond OA, preprints and rights retention instead.

!!! tip "You do not need gold OA to comply with NIH"
    The NIH policy is satisfied by depositing the free **accepted manuscript** in PubMed Central. A $12,850 APC buys the version of record open on the publisher's site; it is not required for compliance. Decide on the merits, and put the cost in the budget.

### Article versions

- **Preprint:** pre-peer-review version, freely available on preprint servers
- **Author accepted manuscript (AAM):** post-peer-review, pre-typesetting; the version NIH requires in PubMed Central
- **Version of record (VOR):** final published version with publisher formatting
- **Rights retention** (applies to the AAM): a statement at submission that you keep the right to share your accepted manuscript openly, so no publisher agreement can block the PubMed Central deposit

!!! example "Preprint repositories"
    - [arXiv](https://arxiv.org/){target=_blank}: physics, math, computer science; an [independent nonprofit since 1 July 2026](https://blog.arxiv.org/2026/06/30/arxivs-next-chapter/){target=_blank}
    - [bioRxiv](https://www.biorxiv.org/){target=_blank}: biology
    - [medRxiv](https://www.medrxiv.org/){target=_blank}: health sciences (a good fit for environmental health research); bioRxiv and medRxiv are run by [openRxiv](https://openrxiv.org/2025-year-in-review/){target=_blank}, an independent nonprofit since 2025
    - [EarthArXiv](https://eartharxiv.org/){target=_blank}: Earth sciences
    - [engrXiv](https://engrxiv.org/){target=_blank}: engineering, including environmental engineering
    - [OSF Preprints](https://osf.io/preprints/){target=_blank}: multi-disciplinary

    **SRP Example (Arizona):** A study on arsenic-induced lung fibrosis mechanisms could be posted to medRxiv immediately after submission to a journal, allowing public health officials to access findings months before formal publication.

    **SRP Example (New Mexico):** A METALS biomonitoring study with Navajo Nation and Pueblo of Laguna partners is shared with the community and cleared under its dissemination approval *before* the preprint is released; the preprint then carries the community-agreed framing rather than the journal's.

??? question "Checkpoint 2: Your paper is accepted at Nature Communications. Name the cheapest fully compliant path under the NIH policy, and what the $7,350 would buy instead."
    Deposit the **accepted manuscript** in PubMed Central at acceptance, with a rights-retention statement if the journal's agreement is restrictive: cost $0. The $7,350 APC buys the **version of record** open on the journal's site, which is a legitimate choice but not a compliance requirement, and must be in the budget.

---

## Module 3: Open data

*About 15 minutes.*

!!! quote "Definition"
    "Open data and content can be freely used, modified, and shared by anyone for any purpose"

    — [The Open Definition](https://opendefinition.org/){target=_blank}

Data are the foundation of science. The **FAIR Principles** guide data management:

Findable
:   Globally unique identifiers, rich metadata, searchable registries

Accessible
:   Retrievable via standard protocols; metadata persists even when data are restricted

Interoperable
:   Standard formats and vocabularies enable data integration

Reusable
:   Clear licenses, detailed provenance, community standards

!!! warning "Public does not mean permanent"
    The [Data Rescue Project](https://www.datarescueproject.org/data-loss-report/){target=_blank} counted 3,000 to 4,000 federal datasets removed from public access since January 2025 (report of 18 August 2026). Deposit your own data in a repository with a persistent identifier; do not assume a government portal will still hold it. The NIEHS [SRP data sharing page](https://tools.niehs.nih.gov/srp/data/index.cfm){target=_blank} lists where SRP-funded datasets are deposited.

!!! warning "As open as possible, as closed as necessary"
    Not all data should be open:

    - Human health data (HIPAA regulations)
    - Endangered species locations
    - Indigenous data (see CARE Principles)
    - Data that could cause harm if misused

    The [**CARE Principles**](https://www.gida-global.org/careprinciples){target=_blank} for Indigenous Data Governance ([Carroll et al. 2020](https://datascience.codata.org/articles/dsj-2020-043){target=_blank}) emphasize:

    - **C**ollective Benefit
    - **A**uthority to Control
    - **R**esponsibility
    - **E**thics

    **SRP Context (Arizona):** Mine site locations near Tribal lands may require consultation with Indigenous communities. Biomarker data from residents near contaminated sites must protect participant privacy while enabling public health research. Precise GPS coordinates of endangered plant species used in phytoremediation studies should be aggregated or restricted.

    **SRP Context (New Mexico):** Research on the Navajo Nation requires approval from the [Navajo Nation Human Research Review Board (NNHRRB)](http://nnhrrb.navajo-nsn.gov/){target=_blank} before collection and before results are shared; data are returned to the community, and chapter-level exposure data are not released without community authority. Pueblo of Laguna partners have their own review. See the [UNM IRB guidance on research with American Indian communities](https://irb.unm.edu/library/documents/guidance/research-with-american-indian-communities.pdf){target=_blank} and the [METALS Center](https://hsc.unm.edu/pharmacy/research/areas/metals/){target=_blank} Community Engagement Core. [Lesson 2](02-data-management.md) covers this in depth.

??? question "Checkpoint 3: A dataset is 'available upon request'. Which FAIR letters does it fail, and why?"
    At least **F** and **A**: without a persistent identifier and a repository record it is not findable, and access depends on one person answering email, which is not a standard protocol and does not survive that person leaving. It usually fails **R** as well, because there is no license or provenance record.

---

## Module 4: Open educational resources

*About 5 minutes.*

<figure markdown>
  [![Global Open Educational Resources logo: an open book whose pages spread outward like raised hands](https://upload.wikimedia.org/wikipedia/commons/2/20/Global_Open_Educational_Resources_Logo.svg){ width="200" }](https://www.unesco.org/en/communication-information/open-solutions/open-educational-resources){target=_blank}
  <figcaption>The Global OER logo (UNESCO)</figcaption>
</figure>

??? note "Text description of this figure"
    The Global Open Educational Resources logo, commissioned by UNESCO: a stylized open book seen from the front, whose pages fan outward and upward like a row of raised hands, suggesting knowledge being shared and received. It links to UNESCO's OER page.

!!! quote "Definition"
    "Open Educational Resources (OER) are learning, teaching and research materials in any format and medium that reside in the public domain or are under copyright that have been released under an open license"

    — [UNESCO](https://www.unesco.org/en/communication-information/open-solutions/open-educational-resources){target=_blank}

**Examples of OER providers:**

- [The Carpentries](https://carpentries.org/){target=_blank}: foundational coding and data science
- [Project Pythia](https://projectpythia.org/){target=_blank}: geoscience Python education
- [OER Commons](https://www.oercommons.org/){target=_blank}: multi-disciplinary resources
- [NIEHS Worker Training Program](https://www.niehs.nih.gov/careers/hazmat){target=_blank}: environmental health and hazardous materials
- [METALS Center](https://hsc.unm.edu/pharmacy/research/areas/metals/){target=_blank} Community Engagement Core: community-facing materials on uranium and metal-mixture exposure, developed with partner communities
- This training: DUST 2026 is itself an OER, licensed CC BY 4.0

!!! example "SRP application"
    **Arizona:** Openly sharing protocols for collecting mine tailings samples, analyzing metalloid concentrations, or conducting plant uptake experiments accelerates research across Superfund sites nationwide. Creating open training materials on working safely with arsenic-contaminated dusts benefits the entire environmental health community.

    **New Mexico:** Materials that explain uranium and metal-mixture exposure in plain language, co-developed with Navajo and Pueblo of Laguna partners, return the research to the communities it came from and can be reused by other tribal communities living near abandoned mines.

??? question "Checkpoint 4: What makes a slide deck an OER rather than just a free download?"
    An **open license** (or public-domain status) that permits reuse and adaptation. A free PDF that is still "all rights reserved" can be read but not legally remixed.

---

## Module 5: Open methodology and pre-registration

*About 10 minutes.*

!!! quote "Definition"
    "An open methodology is one which has been described in sufficient detail to allow other researchers to repeat the work and apply it elsewhere"

    — [Watson (2015)](https://doi.org/10.1186/s13059-015-0669-2){target=_blank}

**Key practices:**

- **Code sharing:** GitHub or GitLab for version-controlled code
- **Protocol publishing:** detailed methods in protocols.io or Nature Protocols
- **Pre-registration:** documenting analysis plans before data collection

<figure markdown>
  ![The Open Science Framework research cycle, a ring of ten stages, with pre-registration marked between designing the study and acquiring materials](../assets/cycle_prereg.png){ width="300" }
  <figcaption>Pre-registration distinguishes hypothesis-generating from hypothesis-testing research (Center for Open Science)</figcaption>
</figure>

??? note "Text description of this figure"
    A circular diagram in shades of blue with the Open Science Framework (OSF) logo at the center. Ten segments run clockwise around the ring, starting at the top right: Search and Discover, Develop Idea, Design Study, Acquire Materials, Collect Data, Store Data, Analyze Data, Interpret Findings, Write Report, and Publish Report, after which the cycle returns to Search and Discover. A callout box labeled "PreRegistration" points at the boundary between Design Study and Acquire Materials: the moment, after the study is designed and before any materials or data are gathered, when hypotheses and the analysis plan are registered.

!!! tip "Why pre-register?"
    - Prevents p-hacking and HARKing (Hypothesizing After Results are Known)
    - Separates exploratory from confirmatory research
    - Increases credibility of findings
    - Directly serves the Gold Standard Science tenet "structured for falsifiability of hypotheses" (Module 9)
    - Platforms: [OSF](https://osf.io/){target=_blank}, [AsPredicted](https://aspredicted.org/){target=_blank}

    **SRP Example (Arizona):** Pre-registering analysis plans for a study comparing lung injury markers between arsenic-exposed and control mice prevents selective reporting of outcomes. Documenting a phytoremediation field trial protocol before planting ensures transparent reporting of both successful and unsuccessful remediation approaches.

    **SRP Example (New Mexico):** Pre-registering the inflammation endpoints for an inhaled mine-dust study fixes the outcomes before the exposures begin. Registering a fungal-mineral bioremediation trial protocol, including the uranium immobilization metrics that count as success, means a null result is still a reportable result.

??? question "Checkpoint 5: At which point in the research cycle does pre-registration happen, and what goes wrong if it happens later?"
    After **Design Study** and before **Acquire Materials** or **Collect Data**. Registered later, the plan can be shaped by the data already seen, which is exactly the hypothesizing-after-results problem pre-registration exists to prevent.

---

## Module 6: Open peer review

*About 5 minutes.*

Traditional peer review has limitations:

- Unreliable and inconsistent
- Delays and expense
- Lack of accountability
- Publication biases
- No incentives for reviewers

**Open peer review options:**

- Signed reviews (the reviewer's identity is known)
- Published reviews (reviews public alongside the paper)
- Reviewer participation (broader community involvement)
- Preprint review (review before journal submission)

!!! example "Open review platforms"
    - [F1000Research](https://f1000research.com/){target=_blank}: post-publication peer review
    - [PREreview](https://prereview.org/){target=_blank}: preprint review, now integrated with bioRxiv and medRxiv so reviews appear alongside the preprint
    - [Sciety](https://sciety.org/){target=_blank}: aggregates public preprint evaluations
    - [PubPeer](https://pubpeer.com/){target=_blank}: post-publication commenting

Gold Standard Science asks for research "subject to unbiased peer review" and "skeptical of its findings and assumptions". Open review is one of the few mechanisms that lets anyone check whether that happened. One of the options NIH floated for capping publication costs would allow a higher APC only at journals that pay reviewers and publish reviewer reports (Module 10).

??? question "Checkpoint 6: Name one benefit and one risk of signed reviews for an early-career reviewer."
    Benefit: credit for the work, and accountability that improves review quality. Risk: retaliation from a senior author whose paper you criticized. Published-but-anonymous reviews and preprint review platforms are middle paths.

---

## Module 7: Open source software

*About 5 minutes.*

!!! quote "Definition"
    "Open source software is code that is designed to be publicly accessible: anyone can see, modify, and distribute the code as they see fit"

    — [Red Hat](https://www.redhat.com/en/topics/open-source/what-is-open-source){target=_blank}

    Learn more: [Open Source Initiative](https://opensource.org/){target=_blank}

Research relies on open source:

- Linux, Python, R, Git
- Scientific libraries: NumPy, SciPy, Pandas, PyTorch
- Data platforms: Jupyter, RStudio, CyVerse
- Environmental tools: QGIS (spatial analysis), OpenAir (air quality), ChemSpider (chemical structures)

<figure markdown>
  <a href="https://xkcd.com/2347/" target="_blank">![xkcd comic 'Dependency': a tall, precarious stack of blocks labeled 'all modern digital infrastructure' rests on one tiny block near the bottom, labeled 'a project some random person in Nebraska has been thanklessly maintaining since 2003'](https://imgs.xkcd.com/comics/dependency.png){ width="400" }</a>
  <figcaption>Modern digital infrastructure relies on open source; handle with care. [XKCD 2347](https://xkcd.com/2347/){target=_blank}, CC BY-NC 2.5</figcaption>
</figure>

??? note "Text description of this figure"
    A black-and-white line drawing of a tall, irregular tower of rectangular blocks of many sizes, stacked so that the whole structure looks about to topple. A label with an arrow at the top reads "All modern digital infrastructure". Near the bottom, a single thin block holds up much of the tower; its label reads "A project some random person in Nebraska has been thanklessly maintaining since 2003". The joke: enormous systems depend on small, unfunded open-source projects.

!!! example "SRP research with open source"
    **X-ray spectroscopy analysis (Arizona):** open-source Python libraries (lmfit, pyFAI) analyze synchrotron data characterizing arsenic speciation in mine-tailings particulate matter.

    **Metal-mixture speciation (New Mexico):** the same pyFAI and lmfit workflows resolve uranium, arsenic and vanadium speciation in nanoparticulate mine waste, so both centers can compare results directly.

    **Spatial modeling:** QGIS and R packages (sf, terra) map contamination dispersal patterns from mine sites across dryland ecosystems.

    **Statistical analysis:** R packages analyze dose-response relationships in toxicology experiments, with complete computational workflows shared on GitHub.

    **Microbiome analysis (New Mexico):** QIIME 2 pipelines for gut immunity studies of metal-mixture exposure, with the full pipeline versioned alongside the sequence data.

    **Image analysis:** open-source tools (CellProfiler, ImageJ) quantify lung tissue damage from inhalation exposure studies.

??? question "Checkpoint 7: An author says their software is open source but will not share it. Is it open source?"
    **No.** Open source requires the code to be publicly available under a recognized license that permits use, modification, and distribution. A claim without the code is not a license.

---

## Module 8: Why do open science?

*About 5 minutes.*

[Bartling & Friesike (2014)](https://doi.org/10.1007/978-3-319-00026-8){target=_blank} identified five schools of thought (motivations):

1. **Democratic:** making scholarship freely available to everyone
2. **Pragmatic:** improving quality through collaboration and critique
3. **Infrastructure:** building better platforms and tools
4. **Public:** engaging society through citizen science and clear communication
5. **Measurement:** developing alternative impact metrics beyond journal publications

We add a sixth:

6. **Compliance:** meeting requirements from funders and institutions, which since 2025 includes Gold Standard Science

<figure markdown>
  ![Diagram of the five schools of open science, each with its assumption, goal, and keywords, arranged around a central box labeled Open Science](../assets/five_schools.png){ width="600" }
  <figcaption>The five schools of thought in open science show its multidisciplinary nature (Fecher & Friesike, openingscience.org, CC BY)</figcaption>
</figure>

??? note "Text description of this figure"
    A grey-scale diagram. A central box reads "Open Science". Five boxes around it each point an arrow at the center and list an assumption, a goal, and keywords:

    - **Infrastructure School** (top): assumption, efficient research depends on the available tools and applications; goal, creating openly available platforms, tools and services for scientists; keywords, collaboration platforms and tools.
    - **Pragmatic School** (left): assumption, knowledge creation could be more efficient if scientists worked together; goal, making the process of knowledge creation more efficient and goal oriented; keywords, wisdom of the crowds, network effects, open data, open code.
    - **Public School** (right): assumption, science needs to be made accessible to the public; goal, making science accessible for citizens; keywords, citizen science, science PR, science blogging.
    - **Democratic School** (bottom left): assumption, the access to knowledge is unequally distributed; goal, making knowledge freely available for everyone; keywords, open access, intellectual property rights, open data, open code.
    - **Measurement School** (bottom right): assumption, scientific contributions today need alternative impact measurements; goal, developing an alternative metric system for scientific impact; keywords, altmetrics, peer review, citation, impact factors.

!!! question "Discussion: your motivation"
    Which school resonates with you? Are there other motivations not captured here?

??? question "Checkpoint 8: Which school does a community-facing plain-language report on uranium exposure belong to, and which does a pre-registration belong to?"
    The community report is the **Public** school (and, if written with the community, also serves the CARE principle of collective benefit). Pre-registration is mostly the **Pragmatic** school, improving quality through transparency and critique.

---

## Module 9: Gold Standard Science in depth

*About 15 minutes.*

### The executive order

[Executive Order 14303, "Restoring Gold Standard Science"](https://www.whitehouse.gov/presidential-actions/2025/05/restoring-gold-standard-science/){target=_blank} (23 May 2025) states that federally funded and conducted science must be:

1. Reproducible
2. Transparent
3. Communicative of error and uncertainty
4. Collaborative and interdisciplinary
5. Skeptical of its findings and assumptions
6. Structured for falsifiability of hypotheses
7. Subject to unbiased peer review
8. Accepting of negative results as positive outcomes
9. Without conflicts of interest

Read the list against Modules 2 to 7. Reproducibility and transparency are open methodology, open data, and open access. Falsifiability is pre-registration. Unbiased peer review and skepticism are what open review is designed to expose. Negative results as positive outcomes is the argument for preprints and data deposit of null findings. In the lecture's table ([Lesson 1, section 3](01-open-science.md#3-gold-standard-science-8-minutes)), each tenet is mapped to the practice and to what you do.

### The OSTP guidance and the reporting cycle

The [OSTP guidance of 23 June 2025](https://www.whitehouse.gov/releases/2025/06/ostp-issues-agency-guidance-for-gold-standard-science/){target=_blank} ([memorandum, PDF](https://www.whitehouse.gov/wp-content/uploads/2025/03/OSTP-Guidance-for-GSS-June-2025.pdf){target=_blank}), signed by OSTP Director Michael Kratsios, sets the mechanics:

- Agencies must apply the tenets to **all** agency-managed science, intramural and extramural, "from the selection phase throughout closeout". Your grant is extramural science; the tenets apply to it.
- Each agency submitted an **implementation plan** by 22 August 2025, and must file an **annual report** to OSTP by 1 September each year, beginning in 2026, describing how it addresses each tenet, its evaluation metrics, training, use of advanced technologies including AI, and challenges.
- Agencies are encouraged to explore **AI and automated tools** for validating reproducible protocols, standardizing transparent data reporting, and detecting bias in peer and merit review. Lesson 3 covers the limits of that idea.

### What the agencies did

- **NIH** released its [implementation plan](https://osp.od.nih.gov/nih-releases-implementation-plan-to-drive-gold-standard-science/){target=_blank} on 22 August 2025 ([plan, PDF](https://www.nih.gov/sites/default/files/2025-08/2025-gss.pdf){target=_blank}). It describes existing initiatives and planned expansions: rigor and reproducibility training for funded researchers, stronger data-sharing compliance, mechanisms to support replication studies, policies to strengthen public trust, and a framework for periodic assessment and public reporting. NIH's parent department published an [HHS Gold Standard Science report for 2025](https://www.hhs.gov/sites/default/files/hhs-gold-standard-science-report-2025.pdf){target=_blank} and its [2026 annual report](https://www.hhs.gov/sites/default/files/gss-at-hhs-annual-report-2026.pdf){target=_blank}.
- **NSF** ([Gold Standard Science page](https://www.nsf.gov/policies/gold-standard-science){target=_blank}) and **EPA** ([Gold Standard Science page](https://www.epa.gov/scientific-leadership/gold-standard-science){target=_blank}) published plans. EPA is the agency whose science governs Superfund cleanups, so its plan bears directly on the sites the DUST and METALS centers study.
- **SPARC's** [policy brief](https://sparcopen.org/our-work/gss_policy_brief/){target=_blank} reviewed the plans and found three common strategies: standardized assessment metrics, automated (AI-based) compliance monitoring, and oversight extended to all federally funded research. It also found agencies **linking Gold Standard Science implementation to their public-access requirements**: persistent identifiers (ORCID for people, DataCite and Crossref for outputs), machine-readable metadata, and transparent reporting of negative results.
- **OSTP's follow-on report**, [*Science: A New Golden Age*](https://www.whitehouse.gov/releases/2026/07/45470/){target=_blank} (21 July 2026), proposes a broad restructuring of federal research funding: rebalancing toward foundational and physical science, national missions such as the Genesis Mission for AI in science, alternative funding models, and metascience units inside agencies to evaluate funding practices. Agencies with large research budgets were asked for action plans within 90 days. The report does not change the public-access or Gold Standard Science requirements described here; it sets the direction for future budgets.

### The debate

Independent reviews ([AIP FYI](https://www.aip.org/fyi/gold-standard-science-plans-emphasize-existing-agency-efforts){target=_blank}) found that the agency plans mostly restate practices agencies already had: data management and sharing plans, public access, rigor training, conflict-of-interest rules. Supporters see the order as giving those practices teeth. Critics ([*Science*](https://www.science.org/content/article/what-does-trump-s-call-gold-standard-science-really-mean){target=_blank}; SPARC) point to the role the order gives political appointees in judging scientific integrity, and warn that "gold standard" can be used to discount inconvenient findings, for example in environmental health, where evidence is often observational and uncertain by nature. Communicating uncertainty honestly (tenet 3) is a scientific virtue; treating uncertainty as a reason to dismiss a finding is not.

For an SRP trainee the practical position is simple. The nine tenets, taken on their merits, are the open-science practices this lesson teaches. Practice them, document them in your proposals and progress reports, and follow the policy debate through the primary sources below.

!!! quote "Primary sources"
    * [Executive Order 14303: Restoring Gold Standard Science, 23 May 2025](https://www.whitehouse.gov/presidential-actions/2025/05/restoring-gold-standard-science/){target=_blank}
    * [Fact sheet: Restoring Gold Standard Science](https://www.whitehouse.gov/fact-sheets/2025/05/fact-sheet-president-donald-j-trump-is-restoring-gold-standard-science-in-america/){target=_blank}
    * [OSTP issues agency guidance for Gold Standard Science, 23 June 2025](https://www.whitehouse.gov/releases/2025/06/ostp-issues-agency-guidance-for-gold-standard-science/){target=_blank} and the [Kratsios memorandum (PDF)](https://www.whitehouse.gov/wp-content/uploads/2025/03/OSTP-Guidance-for-GSS-June-2025.pdf){target=_blank}
    * [NIH implementation plan, 22 August 2025](https://osp.od.nih.gov/nih-releases-implementation-plan-to-drive-gold-standard-science/){target=_blank}; [HHS report 2025 (PDF)](https://www.hhs.gov/sites/default/files/hhs-gold-standard-science-report-2025.pdf){target=_blank}; [HHS annual report 2026 (PDF)](https://www.hhs.gov/sites/default/files/gss-at-hhs-annual-report-2026.pdf){target=_blank}
    * [NSF Gold Standard Science](https://www.nsf.gov/policies/gold-standard-science){target=_blank} and [EPA Gold Standard Science](https://www.epa.gov/scientific-leadership/gold-standard-science){target=_blank}
    * [SPARC: Gold Standard Science, federal implementation strategies and open access policy intersections](https://sparcopen.org/our-work/gss_policy_brief/){target=_blank}
    * [OSTP: Science: A New Golden Age, 21 July 2026](https://www.whitehouse.gov/releases/2026/07/45470/){target=_blank}
    * The 2025-26 federal AI executive orders and policy are covered in [Lesson 3](03-ai-ethics.md)

!!! warning "Verify before you cite"
    This module describes the landscape as of September 2026. Agency annual reports had just been filed and OSTP had not yet responded to them. Check the primary sources and ask your program officer before relying on any of it in a proposal, a budget, or a paper.

??? question "Checkpoint 9: A reviewer asks how your project meets Gold Standard Science. Name three things you can point to that you already do."
    Any three from: a pre-registered analysis plan (falsifiability); version-controlled code and a written protocol (reproducibility); a data management and sharing plan with a repository and DOI (transparency); reported uncertainties and QA/QC (error and uncertainty); a preprint with public review (skepticism, unbiased review); a plan to publish null results (negative results); conflict-of-interest disclosures.

---

## Module 10: The 2026 public-access and publication-cost landscape

*About 10 minutes.* Reference material for proposal writing; skim it now and return to it when you budget a paper.

**1. The 2022 OSTP "Nelson memo" is under repeal, but agency policies stay in force.** Report language attached to the January 2026 appropriations minibus asked OSTP to report on its process of repealing the memo, and the House FY2027 Commerce-Justice-Science report asked NSF to pause new public-access policies until OSTP finishes ([AIP FYI](https://www.aip.org/fyi/scholarly-publishing-costs-under-scrutiny-by-trump-administration){target=_blank}; [STM](https://stm-assoc.org/ostp-to-review-potential-repeal-of-nelson-memo/){target=_blank}). None of that has withdrawn the policies agencies already adopted. Zero-embargo public access to accepted manuscripts began:

| Agency | Zero-embargo public access since |
| --- | --- |
| DOE | 1 October 2024 |
| EPA | 2 January 2025 |
| NIH | 1 July 2025 (NOT-OD-25-047) |
| USGS | 31 December 2025 |
| NSF | 22 January 2026 (NSF 26-202) |
| USDA | 7 April 2026 |

Follow changes on the [SPARC policy tracker](https://sparcopen.org/our-work/2022-updated-ostp-policy-guidance/){target=_blank}.

**2. NIH: accepted manuscript to PubMed Central at acceptance, no embargo.** The [NIH Public Access Policy](https://grants.nih.gov/policy-and-compliance/policy-topics/public-access/nih-public-access-policy-overview){target=_blank} applies to manuscripts accepted on or after 1 July 2025. Depositing the free accepted manuscript satisfies it; you do not have to pay for gold open access. Springer Nature, Wiley and Elsevier nonetheless steer NIH-funded authors toward paid gold-OA routes (see the [Springer Nature federal-compliance page](https://www.springernature.com/gp/open-science/us-federal-agency-compliance){target=_blank}). Know the difference before you sign.

**3. Publication costs: a cap is pending and pre-approval is proposed.** NIH floated caps on allowable article processing charges in a July 2025 request for information ([NOT-OD-25-138](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-138.html){target=_blank}): options ranged from disallowing publication costs entirely, to a $2,000 per-paper cap, to $3,000 only at journals that pay reviewers and publish reviewer reports, to a cap tied to award size. As of June 2026 none had been finalized ([STAT](https://www.statnews.com/2026/06/11/open-access-journal-fees-nature-wiley-elsevier-nih/){target=_blank}), and we found no final policy as of September 2026. Separately, OMB's 29 May 2026 [proposed revision of 2 CFR 200.461](https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance){target=_blank} would make publication costs unallowable unless required by statute or approved in advance by the agency, with a target effective date of 1 October 2026; comments closed 13 July 2026 and the rule was still a proposal in September 2026 ([SPARC FAQ](https://sparcopen.org/our-work/2026-proposed-2cfr200-updates-faqs/){target=_blank}). The proposal states that a general requirement to make results publicly available does not by itself authorize publication costs; the federal-purpose license (2 CFR 200.315(b)) still lets you deposit the accepted manuscript without paying anyone. Practical consequence: **budget publication costs explicitly** in every proposal, and expect to justify them.

**4. Congress kept NIEHS and the SRP.** The FY2026 appropriation [rejected the proposed NIH reorganization and funds all 27 institutes and centers as structured in statute](https://jm-aq.com/congress-rejects-cuts-to-nih-increase-budget-for-fy26/){target=_blank}, so NIEHS and the Superfund Research Program were not folded into a new agency; SRP is funded at $77.1 million for FY2026 (P.L. 119-74).

!!! warning "Verify before you cite"
    This module describes the landscape as of September 2026. The OMB rule, the NIH APC cap and the Nelson memo review were all still moving. Check the primary sources and ask your program officer before relying on any of it in a proposal, a budget or a paper.

??? question "Checkpoint 10: Why does repealing the Nelson memo not, by itself, end the NIH public-access requirement?"
    The memo was guidance to agencies. NIH adopted its own policy (NOT-OD-25-047) under its own authority; that policy stays in force until NIH itself changes it.

---

## Module 11: Self-assessment and action plan

*About 15 minutes.*

### Open science self-assessment

Work individually or in a small group to assess your current practices:

!!! question "Assessment questions"

    **Publications**

    1. Are your published papers freely available?
    2. Do you share preprints before peer review?
    3. Have you retained rights to distribute your work?

    **Data**

    4. Where do you store your research data?
    5. Could someone else understand your data without contacting you?
    6. Have you assigned persistent identifiers (DOIs) to datasets?

    **Methods**

    7. Is your analysis code version controlled and publicly available?
    8. Could someone reproduce your analysis from your documentation?
    9. Have you pre-registered any studies?

    **Education**

    10. Do you share teaching materials under open licenses?
    11. Do you contribute to or use OER in your teaching?

    **Software**

    12. Do you contribute to open source projects?
    13. Is your research software publicly available with a license?

### Group discussion

Share with your group, or write a paragraph if you are working alone:

- Which pillar of open science is strongest in your work?
- Which pillar could you improve most easily?
- What barriers prevent you from being more open?
- What would motivate you to adopt more open practices?

### Action planning

Identify ONE concrete action you can take this month:

!!! example "Example actions"
    - Create an ORCID profile
    - Upload a preprint to medRxiv or bioRxiv
    - Deposit the accepted manuscript of your next paper in PubMed Central at acceptance
    - Add publication costs as a budget line in your next proposal
    - Ask whether your data involve tribal partners and need a CARE review
    - Add a LICENSE file to your analysis code repository on GitHub
    - Create a data management plan for your mine tailings, uranium or toxicology project
    - Share field sampling protocols under a CC BY license
    - Deposit spectroscopy data in a domain repository with a DOI
    - Pre-register your next exposure study on OSF
    - Document your image analysis pipeline in a Jupyter notebook
    - Write one paragraph for your next progress report mapping what you do to the nine Gold Standard Science tenets

??? question "Checkpoint 11: Write your one action here, with a date."
    There is no answer key. If you are working with an AI tutor, ask it to hold you to the date.

---

## Module 12: Quiz and resources

*About 10 minutes.*

### Key takeaways

!!! success "Remember these concepts"
    1. Open science is about **transparency, accessibility, and collaboration**
    2. The **six pillars** provide a framework for openness
    3. **Gold Standard Science** restates those practices as nine tenets, with annual agency reporting since September 2026
    4. Open science benefits **you, your field, and society**
    5. Start with **small, practical steps** rather than perfection
    6. **As open as possible, as closed as necessary**: openness has limits
    7. Public access is now **required at acceptance**, and publication costs belong **in the budget**

### Self-assessment quiz

??? question "True or false: all research papers in Nature and Science are open access"
    **False.** These journals offer open-access options but charge substantial fees (Nature: $12,850 in 2026). Authors must pay extra to make the version of record freely available. Since 1 July 2025, NIH requires the free *accepted manuscript* to be deposited in PubMed Central at acceptance with no embargo; that is public access, not paid open access, and it is satisfied without paying an APC.

??? question "True or false: data 'available upon request' meets the definition of open data"
    **False.** Open data must be freely accessible in a public repository with a persistent identifier. "Available upon request" does not meet FAIR principles: the data are not findable, not accessible without barriers, and not guaranteed to remain available.

??? question "Using GitHub for your analysis code is an example of..."
    **Open methodology.** Version control systems document your computational methods transparently. This enables others to understand, verify, and build upon your work, and it is the first thing a reviewer will look for under the Gold Standard Science tenet "reproducible".

??? question "If an author states their software is open source but refuses to share it, is it open source?"
    **No.** Claiming a license without making the code publicly available does not make it open source. True open source software must be publicly accessible with a recognized license that permits use, modification, and distribution.

??? question "True or false: the 2022 OSTP 'Nelson memo' has been repealed, so federal public-access requirements no longer apply"
    **Partly false.** The memo was placed under review for repeal in January 2026, but the public-access policies that agencies adopted under it remain in force: NIH (1 July 2025), NSF (22 January 2026), USDA (7 April 2026) and the others in the Module 10 table. Repeal of the memo would not by itself withdraw an agency policy.

??? question "Can you charge a $12,850 Nature APC to your NIH award today?"
    **Yes, if it is a reasonable cost of the award, but watch two pending changes.** The latest report we could verify (STAT, June 2026) found no NIH cap in force; the July 2025 RFI (NOT-OD-25-138) floated one that has not been finalized. OMB's proposed 2 CFR 200.461 revision would make publication costs unallowable unless pre-approved in the award (target 1 October 2026). Put publication costs in the budget explicitly, and confirm with your program officer before committing.

??? question "Which Gold Standard Science tenet is served by publishing a remediation trial that did not work?"
    **Accepting of negative results as positive outcomes.** Depositing the data and posting the preprint also serve transparency and reproducibility, and they save the next lab from repeating the trial.

??? question "True or false: Gold Standard Science applies only to research done inside federal laboratories"
    **False.** The June 2025 OSTP guidance applies the tenets to all agency-managed science, intramural and extramural, from selection through closeout. Your Superfund grant is extramural science.

### Looking ahead

In Lesson 2, we will put these principles into practice by learning how to:

- Manage research data throughout its lifecycle
- Create effective documentation
- Implement FAIR principles and honor CARE
- Write a data management and sharing plan

### Additional resources

- [UNESCO Open Science Toolkit](https://www.unesco.org/en/open-science/about){target=_blank}
- [FORRT (Framework for Open and Reproducible Research Training)](https://forrt.org/){target=_blank}: open and reproducible research training materials
- [The Turing Way](https://book.the-turing-way.org/){target=_blank}
- [Center for Open Science](https://www.cos.io/){target=_blank}
- [SPARC federal public-access policy tracker](https://sparcopen.org/our-work/2022-updated-ostp-policy-guidance/){target=_blank}
- [SPARC Gold Standard Science policy brief](https://sparcopen.org/our-work/gss_policy_brief/){target=_blank}
- [Data Rescue Project data-loss report](https://www.datarescueproject.org/data-loss-report/){target=_blank}
- [Barcelona Declaration on Open Research Information](https://barcelona-declaration.org/){target=_blank}
- [openRxiv](https://openrxiv.org/2025-year-in-review/){target=_blank}: home of bioRxiv and medRxiv
- [Retraction Watch data in Crossref](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/){target=_blank}: check whether a paper you cite has been retracted
- More in [Resources](../about/resources.md)

---

**Lecture:** [← Lesson 1: Foundations of Open Science](01-open-science.md) | **Next:** [Lesson 2: Modern Data Management →](02-data-management.md)

<p class="carc-provenance" markdown>Adapted from [DUST 2025](https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/lesson1_open_science/index.md){target=_blank} (last source update 2025-10-14), CC BY 4.0. Spotted a problem? [Open an issue](https://github.com/UNM-CARC/dust-2026/issues){target=_blank}.</p>

*[APC]: Article processing charge
*[APCs]: Article processing charges
*[NIH]: National Institutes of Health
*[NIEHS]: National Institute of Environmental Health Sciences
*[HHS]: Department of Health and Human Services
*[OSTP]: White House Office of Science and Technology Policy
*[OMB]: Office of Management and Budget
*[DOE]: Department of Energy
*[EPA]: Environmental Protection Agency
*[USGS]: United States Geological Survey
*[NSF]: National Science Foundation
*[USDA]: United States Department of Agriculture
*[FAIR]: Findable, Accessible, Interoperable, Reusable
*[CARE]: Collective benefit, Authority to control, Responsibility, Ethics
*[DOI]: Digital object identifier
*[DOIs]: Digital object identifiers
*[QA/QC]: Quality assurance and quality control
*[OSF]: Open Science Framework
*[OER]: Open educational resources
*[SRP]: Superfund Research Program
*[UNM]: University of New Mexico
*[METALS]: Metal Exposure and Toxicity Assessment on Tribal Lands in the Southwest
*[NNHRRB]: Navajo Nation Human Research Review Board
*[IRB]: Institutional Review Board
*[HIPAA]: Health Insurance Portability and Accountability Act
*[SPARC]: Scholarly Publishing and Academic Resources Coalition
*[AIP]: American Institute of Physics
*[ORCID]: Open Researcher and Contributor ID
*[AAM]: Author accepted manuscript
*[VOR]: Version of record
*[OA]: Open access
*[RFI]: Request for information
*[GPS]: Global Positioning System
