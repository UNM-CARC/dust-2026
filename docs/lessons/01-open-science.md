---
title: "Lesson 1: Foundations of Open Science"
description: "A 50-minute in-person lecture: what open science is, its six pillars, the nine Gold Standard Science tenets, and the 2026 public-access and publication-cost rules, with Superfund examples from Arizona and New Mexico."
type: Lesson
tags:
  - Open Science
  - Open Access
  - FAIR
  - CARE
  - Gold Standard Science
  - Public Access Policy
  - Superfund Research Program
lesson:
  number: 1
  format: in-person
  duration_minutes: 50
  companion: 01-open-science-self-paced.md
  delivery_modes:
    - lecture
    - tutor
    - interactive
  objectives:
    - "Define open science and name its six pillars"
    - "List the nine Gold Standard Science tenets and match each to an open-science practice"
    - "State what the NIH Public Access Policy requires at acceptance and why it does not require an article processing charge"
    - "Explain why publication costs now belong in every proposal budget"
    - "Apply 'as open as possible, as closed as necessary' to data collected with tribal and community partners"
  key_terms:
    - open science
    - open access
    - article processing charge (APC)
    - accepted manuscript
    - PubMed Central
    - FAIR principles
    - CARE principles
    - Gold Standard Science
    - pre-registration
    - preprint
    - rights retention
  accessibility:
    language: en
    access_mode: [textual]
    access_mode_sufficient: [textual]
    features: [readingOrder, structuralNavigation, tableOfContents, unlocked, annotations]
    hazards: [none]
    media: "Text only: no images, audio, or video. Tables carry header rows. Quiz answers are native details/summary elements."
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
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# Lesson 1: Foundations of Open Science

!!! info "Lesson overview"
    **Format:** 50-minute in-person lecture with one group activity.

    **Structure:** Introduction (5 min), Core concepts (25 min), Hands-on activity (15 min), Wrap-up (5 min).

    **Homework:** Every section below is a summary. The full material, with all the examples, figures, prices, and policy detail, is in [Lesson 1 homework: Open Science, self-paced](01-open-science-self-paced.md). Complete it before Lesson 2. Learners can also work through either page with an AI tutor: see [Learn with an AI tutor](../about/ai-tutor.md).

!!! abstract "In brief"
    Open science means sharing the papers, data, methods, code, and teaching materials from research so that anyone can check, use, and build on them. In the United States, open science is now a condition of federal funding. Since 1 July 2025, NIH requires every accepted paper to be free to read in PubMed Central on the day it is published. Since May 2025, the federal government also uses a framework called Gold Standard Science, with nine rules for how funded research must be done. This lesson explains the six pillars of open science, the nine Gold Standard Science tenets, and what both mean for Superfund Research Program trainees in Arizona and New Mexico.

## Learning objectives

!!! success "After this lecture, you will be able to:"
    1. Define open science and name its six pillars
    2. List the nine Gold Standard Science tenets and match each to an open-science practice
    3. State what the NIH Public Access Policy requires at acceptance, and why it does not require an article processing charge (APC)
    4. Explain why publication costs now belong in every proposal budget
    5. Apply "as open as possible, as closed as necessary" to data collected with tribal and community partners

---

## Introduction (5 minutes)

### One question

!!! question "Reflect (1 minute)"
    Think of one time you could not get a paper, a dataset, or a protocol that you needed. What did that cost you, and who else did it cost?

### Open science is a condition of funding

Open science is not only an ideal. In 2026 it is a requirement that follows the money:

- **Public access is required at acceptance.** The [NIH Public Access Policy](https://grants.nih.gov/policy-and-compliance/policy-topics/public-access/nih-public-access-policy-overview){target=_blank} applies to every manuscript accepted on or after 1 July 2025: the accepted manuscript goes into PubMed Central with no embargo. DOE, EPA, USGS, NSF, and USDA have equivalent zero-embargo policies in force.
- **The federal frame is now Gold Standard Science.** [Executive Order 14303](https://www.whitehouse.gov/presidential-actions/2025/05/restoring-gold-standard-science/){target=_blank} (23 May 2025) sets nine tenets that every agency must build into how it funds, conducts, and manages research. Agencies filed implementation plans in August 2025 and their first annual progress reports on 1 September 2026.
- **Communities expect it.** People living near mine tailings in Arizona-Sonora mining towns, and Navajo Nation and Pueblo of Laguna communities living with abandoned uranium mines, expect research about their exposure to be shared with them, in forms they can use.

!!! example "SRP Example: why it matters here"
    **Arizona:** Findings about arsenic in mine-tailings dust and lung injury protect people only if public health officials and residents can read them promptly, so the DUST Center's papers must be public at acceptance and its protocols reproducible.

    **New Mexico:** The UNM METALS Center's uranium and metal-mixture data are collected with Navajo Nation and Pueblo of Laguna partners under community review. Openness there means sharing on the community's terms, which is what the CARE Principles require.

---

## Core concepts (25 minutes)

### 1. What open science is (5 minutes)

!!! quote "Definition"
    "Open Science is defined as an inclusive construct that combines various movements and practices aiming to make multilingual scientific knowledge openly available, accessible and reusable for everyone."

    — [UNESCO Recommendation on Open Science](https://www.unesco.org/en/natural-sciences/open-science){target=_blank}

Open science touches every stage of a research project:

1. **Planning:** pre-registration and open protocols
2. **Execution:** open notebooks and transparent methods
3. **Analysis:** reproducible workflows and version control
4. **Dissemination:** open-access publishing and data sharing

Homework: [Module 1, definitions and the research life cycle](01-open-science-self-paced.md#module-1-definitions-and-the-research-life-cycle).

### 2. The six pillars (8 minutes)

Open access
:   Publications are free for anyone to read. NIH is satisfied by the free **accepted manuscript** in PubMed Central; a paid "gold" open-access article is optional.

Open data
:   Research data are deposited with a persistent identifier and follow the **FAIR** principles (Findable, Accessible, Interoperable, Reusable), within the limits set by privacy, safety, and the **CARE** principles for Indigenous data.

Open educational resources
:   Teaching and training materials are released under an open license, such as CC BY, so others can reuse and adapt them.

Open methodology
:   Methods are described in enough detail that others can repeat the work: protocols, version-controlled code, and **pre-registration** of hypotheses and analysis plans.

Open peer review
:   Reviews are signed, published, or both, and preprints can be reviewed before journal submission.

Open source software
:   Research software is publicly available under a recognized open license.

??? question "How many pillars are there really?"
    Frameworks count between four and eight. Some combine categories, others split them. Learn the principles, not the number.

!!! example "SRP Example: one pillar in each state"
    **Arizona (open methodology):** Pre-registering the lung-injury endpoints for an arsenic-exposure mouse study fixes the outcomes before the exposures begin, so selective reporting is off the table.

    **New Mexico (open data, as closed as necessary):** A METALS biomonitoring dataset is shared with a DOI and full metadata, but chapter-level exposure values are released only with the community's authority, after Navajo Nation Human Research Review Board approval.

Homework: [Modules 2 to 7](01-open-science-self-paced.md#module-2-open-access), one per pillar.

### 3. Gold Standard Science (8 minutes)

Executive Order 14303 (23 May 2025) directs every federal agency to conduct and manage science according to nine tenets. The [OSTP guidance of 23 June 2025](https://www.whitehouse.gov/releases/2025/06/ostp-issues-agency-guidance-for-gold-standard-science/){target=_blank} applies the tenets to all agency-managed science, intramural and extramural, "from the selection phase throughout closeout": that includes your Superfund grant. Agencies filed implementation plans on 22 August 2025 and their first annual reports on 1 September 2026.

The nine tenets are, for the most part, open-science practices under a new name:

| Gold Standard Science tenet (EO 14303, section 3) | Open-science practice | What you do as a trainee |
| --- | --- | --- |
| Reproducible | Open methodology, open source | Version your code; write protocols another lab can run |
| Transparent | Open data, open access | Deposit data with a DOI; deposit the accepted manuscript in PubMed Central |
| Communicative of error and uncertainty | Open methodology | Report confidence intervals, detection limits, and QA/QC results, not only point estimates |
| Collaborative and interdisciplinary | Open data, open source | Use standard formats so the Arizona and New Mexico centers can compare results directly |
| Skeptical of its findings and assumptions | Open peer review | Post a preprint, invite critique, and answer it in public |
| Structured for falsifiability of hypotheses | Pre-registration | Register hypotheses and endpoints before the exposures begin |
| Subject to unbiased peer review | Open peer review | Review for others, declare your conflicts, prefer venues that publish reviews |
| Accepting of negative results as positive outcomes | Open data, preprints | Publish the null remediation trial and deposit its data |
| Without conflicts of interest | Transparency | Disclose funding and relationships in every output |

**What NIH's plan means for you.** NIH's [implementation plan](https://osp.od.nih.gov/nih-releases-implementation-plan-to-drive-gold-standard-science/){target=_blank} (22 August 2025) commits the agency to expanded rigor and reproducibility training, stronger data-sharing compliance, new support for replication studies, and periodic public reporting on outcomes. In practice, the reviewers of your next proposal and the program officer on your next progress report will be looking for the right-hand column of the table above.

!!! warning "Two things to know before you cite Gold Standard Science"
    1. **Mostly familiar, partly new.** Independent reviews of the agency plans found that they largely restate existing data-management, sharing, and public-access policy ([AIP FYI](https://www.aip.org/fyi/gold-standard-science-plans-emphasize-existing-agency-efforts){target=_blank}; [SPARC brief](https://sparcopen.org/our-work/gss_policy_brief/){target=_blank}). The new elements are the annual reporting, the encouragement to use AI tools to check reproducibility and detect bias in review, and the extension of oversight to all funded research, not only government laboratories.
    2. **It is contested.** The order gives political appointees a role in judging scientific integrity, and [critics in *Science*](https://www.science.org/content/article/what-does-trump-s-call-gold-standard-science-really-mean){target=_blank} and SPARC warn that this could constrain independent inquiry. You can practice the nine tenets on their merits while following that debate.

Homework: [Module 9, Gold Standard Science in depth](01-open-science-self-paced.md#module-9-gold-standard-science-in-depth).

### 4. The 2026 compliance landscape (4 minutes)

Three facts, as of September 2026, that you will act on this year:

1. **Accepted manuscript to PubMed Central, at acceptance, no embargo.** Depositing the free accepted manuscript satisfies NIH. You do not have to pay an APC (Nature's 2026 list price is $12,850) to comply. Publishers steer NIH authors toward paid routes; know the difference before you sign.
2. **Publication costs are moving, so budget them.** NIH floated caps on allowable APCs in July 2025 ([NOT-OD-25-138](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-138.html){target=_blank}); none was final when this page was written. OMB's [proposed revision of 2 CFR 200.461](https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance){target=_blank} (29 May 2026) would make publication costs unallowable unless pre-approved in the award, with a target date of 1 October 2026; it was still a proposal in September 2026. Either way: put publication costs in every proposal budget, explicitly.
3. **As open as possible, as closed as necessary.** Human health data, Indigenous data, and sensitive site locations have limits. Data collected with Navajo Nation partners need [Navajo Nation Human Research Review Board](http://nnhrrb.navajo-nsn.gov/){target=_blank} approval before collection and before release; the Pueblo of Laguna has its own review. The [CARE Principles](https://www.gida-global.org/careprinciples){target=_blank} (Collective benefit, Authority to control, Responsibility, Ethics) govern, and Lesson 2 covers them in depth.

Homework: [Module 10, the 2026 public-access and publication-cost landscape](01-open-science-self-paced.md#module-10-the-2026-public-access-and-publication-cost-landscape).

---

## Hands-on activity (15 minutes)

### Six questions, one per pillar

Work in pairs. Answer yes, partly, or no for your own current project.

!!! question "Where are you now?"
    1. **Open access:** Will the accepted manuscript of your next paper go to PubMed Central at acceptance, and do you know who deposits it?
    2. **Open data:** Could someone reuse your data from the repository record alone, without emailing you?
    3. **Open educational resources:** Have you shared a protocol, slide deck, or training exercise under an open license?
    4. **Open methodology:** Is your analysis code version-controlled, and have you ever pre-registered a study?
    5. **Open peer review:** Have you posted a preprint or reviewed one in public?
    6. **Open source:** Does your research software have a LICENSE file?

### Pick one action for this month

!!! example "Choose one"
    - Create or complete an [ORCID](https://orcid.org/){target=_blank} profile
    - Add publication costs as a budget line in the proposal you are writing
    - Deposit the accepted manuscript of your next paper in PubMed Central yourself
    - Pre-register your next exposure study on [OSF](https://osf.io/){target=_blank}
    - Add a LICENSE file to your analysis code on GitHub
    - Ask whether your data involve tribal partners and need a CARE review

Report out: each pair names its weakest pillar and its one action.

---

## Wrap-up (5 minutes)

### Key takeaways

!!! success "Remember"
    1. Open science is **transparency, accessibility, and collaboration** across six pillars
    2. **Gold Standard Science** renames those practices as nine tenets and now attaches annual agency reporting to them
    3. Public access is **required at acceptance**; the free accepted manuscript is enough
    4. **Publication costs belong in the budget**, because the rules on paying them are changing
    5. **As open as possible, as closed as necessary**: CARE and tribal review set the limits

### Three quick questions

??? question "True or false: every paper in *Nature* and *Science* is open access"
    **False.** These journals sell open access for a fee. NIH compliance is separate: the free accepted manuscript in PubMed Central satisfies the policy without an APC.

??? question "Which Gold Standard Science tenet does pre-registration serve most directly?"
    **Structured for falsifiability of hypotheses.** Registering hypotheses and endpoints before data collection separates confirmatory from exploratory analysis and prevents hypothesizing after results are known.

??? question "Do you need to pay an article processing charge to comply with the NIH Public Access Policy?"
    **No.** Deposit the accepted manuscript in PubMed Central at acceptance. Paying for the version of record to be open is a separate decision, and one that should be in the budget.

### Homework before Lesson 2

Complete [Lesson 1 homework: Open Science, self-paced](01-open-science-self-paced.md) (about 90 to 120 minutes). It holds the full pillar material, the figures, the 2026 prices and policies, the Gold Standard Science deep dive, a 13-question self-assessment, and the full quiz.

**Next:** [Lesson 2: Modern Data Management →](02-data-management.md)

## Key terms

Accepted manuscript
:   The peer-reviewed version of a paper before the publisher typesets it. NIH requires this version in PubMed Central.

Article processing charge (APC)
:   A fee an author or funder pays a journal to make an article open access.

CARE principles
:   Collective benefit, Authority to control, Responsibility, Ethics: rules for Indigenous data governance.

FAIR principles
:   Findable, Accessible, Interoperable, Reusable: rules for data management.

Gold Standard Science
:   The federal science-integrity framework from Executive Order 14303 (2025), with nine tenets.

Pre-registration
:   Recording your hypotheses and analysis plan in a public registry before collecting data.

Preprint
:   A paper shared publicly before peer review.

Rights retention
:   A statement at submission that you keep the right to share your accepted manuscript openly.

<p class="carc-provenance" markdown>Adapted from [DUST 2025](https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/lesson1_open_science/index.md){target=_blank} (last source update 2025-10-14), CC BY 4.0. Spotted a problem? [Open an issue](https://github.com/UNM-CARC/dust-2026/issues){target=_blank}.</p>

*[APC]: Article processing charge
*[NIH]: National Institutes of Health
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
*[QA/QC]: Quality assurance and quality control
*[OSF]: Open Science Framework
*[SRP]: Superfund Research Program
*[UNM]: University of New Mexico
*[METALS]: Metal Exposure and Toxicity Assessment on Tribal Lands in the Southwest
*[SPARC]: Scholarly Publishing and Academic Resources Coalition
*[AIP]: American Institute of Physics
*[ORCID]: Open Researcher and Contributor ID
