---
title: "Lesson 2: Modern Data Management"
description: "A 50-minute in-person lecture: the data life cycle, FAIR and CARE, the 2026 NIH and NSF data management and sharing plan formats, repositories and licenses, and a two-site metal-mixture plan exercise, with Superfund examples from Arizona and New Mexico."
type: Lesson
tags:
  - Data Management
  - FAIR
  - CARE
  - Data Management Plans
  - Superfund Research Program
  - Indigenous Data Governance
lesson:
  number: 2
  format: in-person
  duration_minutes: 50
  companion: 02-data-management-self-paced.md
  delivery_modes:
    - lecture
    - tutor
    - interactive
  objectives:
    - "Name the eight stages of the data life cycle and say what data management decision belongs to each"
    - "Apply the FAIR principles to a dataset and explain why FAIR does not mean open"
    - "Explain the CARE principles and what Navajo Nation research review requires before data are collected or shared"
    - "Describe the 2026 NIH data management and sharing plan format and how the NSF Data Management and Sharing Plan differs"
    - "Choose a repository and a license for a dataset, and know when a license is not yours to choose"
  key_terms:
    - data life cycle
    - metadata
    - FAIR principles
    - CARE principles
    - data management and sharing plan (DMS plan)
    - Data Management and Analysis Core (DMAC)
    - persistent identifier
    - repository
    - data rescue
    - CC0 and CC BY
    - Navajo Nation Human Research Review Board (NNHRRB)
  accessibility:
    language: en
    access_mode: [textual]
    access_mode_sufficient: [textual]
    features: [readingOrder, structuralNavigation, tableOfContents, unlocked, annotations]
    hazards: [none]
    media: "Text only: no images, audio, or video. Tables carry header rows. Quiz answers are native details/summary elements."
generated:
  by: "claude/fable-5-1"
  at: "2026-09-12T03:00:00Z"
sources:
  - id: dust-2025
    resource: "https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/lesson2_data_management/index.md"
    title: "DUST 2025: docs/lesson2_data_management/index.md"
    author: "human:tswetnam"
    last_modified: "2025-10-29T20:39:18-07:00"
  - id: unm-carc-foss
    resource: "https://github.com/UNM-CARC/foss/blob/f83c334a6d6a53795631c108aef2f1a477a1b7ef/docs/lessons/02-data-management.md"
    title: "UNM CARC FOSS: Data Management and Documentation"
    author: "team:unm-carc"
    last_modified: "2026-09-11T07:41:50-06:00"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# Lesson 2: Modern Data Management

!!! info "Lesson overview"
    **Format:** 50-minute in-person lecture with one group exercise.

    **Structure:** Introduction (5 min), Core concepts (25 min), Hands-on activity (15 min), Wrap-up (5 min).

    **Homework:** Every section below is a summary. The full material, with the figures, the file-naming examples, the metadata standards, the repository lists, the three self-assessments, and the complete quiz, is in [Lesson 2 homework: Data Management, self-paced](02-data-management-self-paced.md). Complete it before Lesson 3. Learners can also work through either page with an AI tutor: see [Learn with an AI tutor](../about/ai-tutor.md).

!!! abstract "In brief"
    Data management means deciding, before you collect anything, how your data will be named, checked, described, stored, shared, and preserved. The FAIR principles say data should be Findable, Accessible, Interoperable, and Reusable. The CARE principles say that data about Indigenous peoples are governed by those peoples. In 2026, NIH and NSF both changed the plan you must write: NIH now asks for Yes/No commitments, a short justification, and a small table; NSF asks for a two-page Data Management and Sharing Plan. Federal datasets can disappear, so keep and cite your own copy. This lesson gives you the life cycle, the principles, the plan formats, and a two-site exercise.

## Learning objectives

!!! success "After this lecture, you will be able to:"
    1. Name the eight stages of the data life cycle and say what data management decision belongs to each
    2. Apply the FAIR principles to a dataset and explain why FAIR does not mean open
    3. Explain the CARE principles and what Navajo Nation research review requires before data are collected or shared
    4. Describe the 2026 NIH data management and sharing plan format and how the NSF Data Management and Sharing Plan differs
    5. Choose a repository and a license for a dataset, and know when a license is not yours to choose

---

## Introduction (5 minutes)

### Three questions

!!! question "Reflect (1 minute)"
    - If you gave your data to a colleague unfamiliar with your project, could they make sense of it?
    - If you returned to your own data in five years, would you understand it?
    - Which federal dataset does your project depend on, and where is your copy?

### The number one problem

!!! danger "Making it an afterthought"
    Poor data management has no upfront cost. You can do substantial work before realizing you are in trouble, and by then fixing it is exponentially harder. Make data management the **first** thing you decide when a project starts.

### When the data disappear

On 5 February 2025 EPA removed EJScreen, its environmental-justice screening tool, from its website; in the same weeks 203 CDC datasets went offline until a court ordered them restored. Community mirrors (the Public Environmental Data Partners copy of [EJScreen](https://screening-tools.com/epa-ejscreen){target=_blank}, the Harvard Library Innovation Lab [data.gov archive](https://lil.law.harvard.edu/blog/2025/02/06/announcing-data-gov-archive/){target=_blank}, the [Data Rescue Project](https://www.datarescueproject.org/){target=_blank}) filled the gap, but EJScreen is still absent from epa.gov as of September 2026. The lesson for your project: **download, DOI, and document what you depend on**, and cite the persistent identifier of the copy you actually analyzed.

!!! example "SRP Example: what a collaborator would need from you"
    **Arizona:** Arsenic concentrations from 50 mine-tailings samples, lung tissue images from an inhalation study, plant biomass from phytoremediation plots. Would they know the units, the detection limits, and which sample came from which site?

    **New Mexico:** Uranium, arsenic, and vanadium water chemistry from abandoned mines on Navajo Nation, household well screening, and a survey collected under Navajo Nation Human Research Review Board (NNHRRB) approval. Would they know which records may never leave the community that owns them?

---

## Core concepts (25 minutes)

### 1. The data life cycle (6 minutes)

Data pass through eight stages, and each stage has a decision you should make on purpose:

Plan
:   Describe the data you will collect or reuse, the formats, the storage, and who has access; write the data management plan.

Collect
:   Set the file-naming convention and folder structure **before** the first sample. Pattern: `YYYY-MM-DD_site_sample-ID_analysis-type_details.ext`. Site codes in filenames, never GPS coordinates or household IDs.

Assure
:   Record quality conditions, distinguish estimated from measured values, flag missing and questionable values, keep an audit trail of checks.

Describe
:   Write the metadata: dataset, people (with ORCID), context, variables and units, quality, and access terms. Use a standard (DataCite, ISO 19115-1 for spatial, MIxS for environmental samples).

Preserve
:   Deposit in a repository with a persistent identifier. Backup is not preservation.

Discover
:   Good metadata lets you, and others, find the data again: repositories, re3data, Google Dataset Search, DataCite Commons.

Integrate
:   Never assume two columns mean the same thing; use standards and ontologies; always cite the data you reuse.

Analyze
:   Reproducible practices: notebooks, version control, recorded software versions, pre-registered plans.

Homework: [Modules 3 to 6](02-data-management-self-paced.md#module-3-what-qualifies-as-data) cover the stages in depth, with the file-naming examples, metadata standards, and repository lists.

### 2. FAIR and CARE (7 minutes)

The [FAIR Guiding Principles](https://www.nature.com/articles/sdata201618){target=_blank} (2016):

Findable
:   A persistent identifier (DOI), rich metadata, and a searchable registry.

Accessible
:   Retrievable by a standard protocol; the metadata stay available even when the data are restricted.

Interoperable
:   Standard formats (CSV, NetCDF, GeoTIFF; cloud-native GeoParquet, COG, Zarr for large data) and shared vocabularies.

Reusable
:   A clear license, documented provenance, and community standards.

!!! warning "FAIR does not mean open"
    Human subjects data can be FAIR and access-controlled. Endangered species locations can be findable in metadata but not accessible. Data collected on Navajo Nation can be FAIR to the Nation and its chapters while access for everyone else is governed by NNHRRB conditions, with a metadata-only record in public repositories.

The [CARE Principles](https://www.gida-global.org/careprinciples){target=_blank} for Indigenous Data Governance answer the question FAIR does not ask: not *can* the data be reused, but *should* they be, by whom, and on whose terms.

- **Collective benefit:** data serve the community's development, governance, and equitable outcomes
- **Authority to control:** Indigenous peoples govern their data
- **Responsibility:** researchers build relationships and capacity
- **Ethics:** minimize harm, maximize benefit, consider future use

!!! warning "Research on Navajo Nation"
    The [NNHRRB](http://nnhrrb.navajo-nsn.gov/){target=_blank} must approve the protocol, and the affected chapter must pass a supporting resolution, **before** collection begins. **The Navajo Nation owns the data.** The NNHRRB approves the Final Report and a Dissemination Plan before results are shared in any form, including preprints, talks, and repository deposits. Pueblo of Laguna partners have their own review, and a university IRB approval is never a substitute. Write these conditions into the plan, the metadata, and the data governance agreement.

!!! example "SRP Example: FAIR and CARE together"
    **Arizona:** Arsenic and phytoremediation data from state land go to Zenodo or the Environmental Data Initiative with a DOI and a CC BY license; the coordinates of remediation plots that could be looted are generalized.

    **New Mexico:** Household well-water and biomonitoring data from Navajo Nation stay in tribally controlled storage or the Native BioData Consortium's Tribal Data Repository, with a metadata-only record and a Local Contexts Notice in the institutional repository so the dataset is findable without leaving the community's control.

Homework: [Module 7, FAIR](02-data-management-self-paced.md#module-7-the-fair-principles) and [Module 8, CARE](02-data-management-self-paced.md#module-8-care-and-research-on-navajo-nation).

### 3. The 2026 plan formats (7 minutes)

Three things changed in the plan you write, as of September 2026:

| Funder or program | What the plan is now | Source |
| --- | --- | --- |
| NIH | For due dates on or after 25 May 2026: **Yes/No sharing commitments**, a **300-word** justification for any limitation on sharing, and a **100-word table** of data types and repositories. No prior approval is needed to change a plan; compliance is reported in RPPR section C.5.c from 1 October 2026. | [NOT-OD-26-046](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html){target=_blank}, [NOT-OD-26-100](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-100.html){target=_blank}, [format page](https://grants.nih.gov/grants-process/write-application/forms-directory/data-management-and-sharing-plan-format-page){target=_blank} |
| NSF | A **two-page Data Management and Sharing Plan** submitted through a Research.gov webform since 27 April 2026; data underlying publications shared at publication; persistent identifiers and minimum metadata required. | [PAPPG 24-1 Supplement 2 (NSF 26-202)](https://www.nsf.gov/policies/document/pappg24-1-supplement-2){target=_blank} |
| Superfund Research Program | A **Data Management and Analysis Core (DMAC)** is mandatory for every P42 center; budget the DMAC's time and repository fees. | [SRP data sharing](https://tools.niehs.nih.gov/srp/data/index.cfm){target=_blank}, [DMAC pages](https://tools.niehs.nih.gov/srp/data/dmac.cfm){target=_blank} |

The 300 words are the only free text in the NIH format. Use them for consent scope, tribal data governance, and site-location sensitivity, and answer the Yes/No commitments honestly: each "No" has to be explained. NIH's Gold Standard Science plan (Lesson 1) adds data-sharing compliance and replication to what reviewers look for.

Homework: [Module 9, data management plans](02-data-management-self-paced.md#module-9-data-management-plans-the-2026-nih-and-nsf-formats).

### 4. Repositories and licenses (5 minutes)

| Data | Where it goes |
| --- | --- |
| Toxicology and biomarker data | [NIEHS CEBS](https://cebs-ext.niehs.nih.gov/datasets/){target=_blank}, [SRP Tox Data Commons](https://toxdatacommons.com/){target=_blank}; [dbGaP](https://dbgap.ncbi.nlm.nih.gov/home){target=_blank} for human subjects (controlled access) |
| Environmental chemistry and geospatial data | [EDI](https://edirepository.org/){target=_blank}, [DataONE](https://www.dataone.org/){target=_blank}, [EPA Science Inventory](https://cfpub.epa.gov/si/){target=_blank}; [Zenodo](https://zenodo.org/){target=_blank} for large spectroscopy files |
| Anything, from your institution | [UA ReDATA](https://redata.arizona.edu/){target=_blank}; [UNM Digital Repository](https://digitalrepository.unm.edu/){target=_blank} and [Dryad](https://datadryad.org/){target=_blank} (UNM member, no fee) |
| Tribal community data | Tribally controlled storage or the [Native BioData Consortium](https://nativebio.org/){target=_blank}; a metadata-only record elsewhere |

Licenses: **CC0** (no restrictions) or **CC BY** (attribution) for research data; avoid non-commercial ("NC") licenses, which block integration and reuse. **Tribal community data are not yours to license.** The research agreement and the community's review board set the terms; publish a metadata record with a Local Contexts Notice instead of a Creative Commons deed.

Homework: [Module 6, preserving and finding data](02-data-management-self-paced.md#module-6-preserve-discover-integrate-analyze) and [Module 10, choosing a license](02-data-management-self-paced.md#module-10-choosing-a-license).

---

## Hands-on activity (15 minutes)

### Draft the NIH 2026 plan for a two-site study

Work in groups of three or four. Your study runs four years, is due after 25 May 2026 (so it uses the NIH 2026 format), and has two sites:

!!! example "The scenario"
    **Site A, Arizona mine tailings (state land):** soil and tailings ICP-MS for arsenic and metals; plant tissue from phytoremediation plots; quarterly hyperspectral drone imagery; a weather station; GPS site characterization. Data must be public no later than publication; some plot locations may need restriction to prevent looting of remediation plants.

    **Site B, abandoned uranium mine on Navajo Nation:** household well and livestock water ICP-MS for uranium, arsenic, and vanadium; dust wipes and soil by gamma spectrometry; urine biomonitoring and a household survey. **NNHRRB conditions:** the Nation owns the data; a chapter resolution precedes collection; the NNHRRB approves the Final Report and Dissemination Plan before any release; household locations are never made public.

    **Team:** two SRP centers, an external analytical lab, a tribal community partner, a DMAC data manager.

Draft, on one page:

1. **Yes/No commitments:** for each data type, will it be shared? Which answers are "No", and why?
2. **The 300-word justification:** in bullet form, what goes in it for Site B, and for the Site A plot locations?
3. **The 100-word table:** data type paired with repository (Zenodo? EDI? Tox Data Commons? tribally controlled storage with a metadata-only record?).

Report out: each group reads its table and its hardest "No".

---

## Wrap-up (5 minutes)

### Key takeaways

!!! success "Remember"
    1. **Plan early:** data management starts before data collection
    2. **FAIR** is a framework that needs interpretation, and FAIR is not the same as open
    3. **CARE** puts authority with the community: on Navajo Nation, the NNHRRB and the chapter decide what is shared
    4. **The 2026 formats are short** and reward honest, specific answers; the DMAC is part of the budget
    5. **Preserve what you depend on:** federal datasets can vanish, so keep and cite your own copy

### Three quick questions

??? question "True or false: FAIR data must be openly available to everyone"
    **False.** FAIR describes how data are identified, described, and made retrievable. Access can be controlled; the metadata must still be findable and persistent.

??? question "Your NIH application is due in October 2026. What does the data management and sharing plan look like?"
    **The 2026 format from NOT-OD-26-046:** Yes/No sharing commitments, a justification of up to 300 words for any limitation, and a 100-word table of data types and repositories.

??? question "Who decides whether household well-water data from Navajo Nation can be deposited in a public repository?"
    **The Navajo Nation**, through the NNHRRB and the affected chapter, under the research agreement. Not the PI, not the university IRB, and not the repository.

### Homework before Lesson 3

Complete [Lesson 2 homework: Data Management, self-paced](02-data-management-self-paced.md) (about 90 to 120 minutes). It holds the data life cycle in full with file-naming and metadata examples, the repository lists, FAIR and CARE in depth, the 2026 plan formats element by element, licenses, three self-assessments, the full two-site scenario, and the complete quiz.

**Previous:** [← Lesson 1: Open Science](01-open-science.md) | **Next:** [Lesson 3: Ethics and Artificial Intelligence →](03-ai-ethics.md)

## Key terms

CARE principles
:   Collective benefit, Authority to control, Responsibility, Ethics: rules for Indigenous data governance.

Data life cycle
:   The eight stages data pass through: plan, collect, assure, describe, preserve, discover, integrate, analyze.

Data Management and Analysis Core (DMAC)
:   The unit every Superfund Research Program center must have to manage and share its data.

Data management and sharing plan
:   The document a funder requires that says how data will be handled during and after a project; NIH and NSF both changed its format in 2026.

Data rescue
:   Copying and preserving public datasets, often government data, before they are withdrawn.

FAIR principles
:   Findable, Accessible, Interoperable, Reusable: rules for data management.

Metadata
:   Structured information about a dataset: who, what, when, where, how, and under what terms.

Persistent identifier
:   A permanent reference to a dataset or person that keeps resolving, such as a DOI or an ORCID.

<p class="carc-provenance" markdown>Adapted from [DUST 2025](https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/lesson2_data_management/index.md){target=_blank} (last source update 2025-10-29), CC BY 4.0. Spotted a problem? [Open an issue](https://github.com/UNM-CARC/dust-2026/issues){target=_blank}.</p>

*[NIH]: National Institutes of Health
*[NSF]: National Science Foundation
*[NIEHS]: National Institute of Environmental Health Sciences
*[EPA]: Environmental Protection Agency
*[CDC]: Centers for Disease Control and Prevention
*[FAIR]: Findable, Accessible, Interoperable, Reusable
*[CARE]: Collective benefit, Authority to control, Responsibility, Ethics
*[DOI]: Digital object identifier
*[DMAC]: Data Management and Analysis Core
*[NNHRRB]: Navajo Nation Human Research Review Board
*[IRB]: Institutional Review Board
*[RPPR]: Research Performance Progress Report
*[PAPPG]: NSF Proposal and Award Policies and Procedures Guide
*[SRP]: Superfund Research Program
*[UNM]: University of New Mexico
*[UA]: University of Arizona
*[ORCID]: Open Researcher and Contributor ID
*[ICP-MS]: Inductively coupled plasma mass spectrometry
*[GPS]: Global Positioning System
*[CEBS]: Chemical Effects in Biological Systems
*[EDI]: Environmental Data Initiative
*[COG]: Cloud-Optimized GeoTIFF
*[MIxS]: Minimum Information about any (x) Sequence
*[PI]: Principal investigator
*[CC]: Creative Commons
