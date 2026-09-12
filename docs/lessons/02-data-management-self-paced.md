---
title: "Lesson 2 homework: Data Management, self-paced"
description: "The self-paced companion to Lesson 2: twelve modules with checkpoints on the data life cycle, data rescue, metadata, repositories, FAIR and CARE, the 2026 NIH and NSF plan formats, licenses, three self-assessments, a two-site metal-mixture plan scenario, and the complete quiz."
type: Lesson
tags:
  - Data Management
  - FAIR
  - CARE
  - Data Management Plans
  - Superfund Research Program
  - Indigenous Data Governance
  - Self-paced
lesson:
  number: 2
  format: self-paced
  duration_minutes: 100
  companion: 02-data-management.md
  delivery_modes:
    - tutor
    - interactive
    - lecture
  objectives:
    - "Recognize data as the foundation of open science and explain why data management must come first"
    - "Describe the complete life cycle of data and the practices at each stage"
    - "Explain why community mirrors and preservation protect environmental-justice data"
    - "Apply FAIR principles to your research data and CARE principles to data about Indigenous peoples"
    - "Write a data management and sharing plan in the 2026 NIH format and explain how the NSF plan differs"
    - "Choose repositories and licenses for your data, and evaluate your own practices with three self-assessments"
  key_terms:
    - data life cycle
    - observational, experimental, simulation, and derived data
    - file naming convention
    - quality assurance
    - metadata standard
    - repository
    - persistent identifier
    - RO-Crate
    - FAIR principles
    - CARE principles
    - data rescue
    - data management and sharing plan (DMS plan)
    - Data Management and Analysis Core (DMAC)
    - Local Contexts Notice
    - CC0, CC BY, CC BY-SA
  accessibility:
    language: en
    access_mode: [textual, visual]
    access_mode_sufficient: [textual]
    features: [alternativeText, longDescription, readingOrder, structuralNavigation, tableOfContents, unlocked, annotations]
    hazards: [none]
    media: "No audio or video. Three images, each with alt text and a collapsible text description immediately after it. Tables carry header rows. Checkpoint and quiz answers are native details/summary elements."
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

# Lesson 2 homework: Data Management, self-paced

!!! info "How to use this page"
    **Time:** about 90 to 120 minutes, in one sitting or several.

    **Structure:** twelve modules. Each ends with a **checkpoint**: answer it in your own words before opening the answer. The in-person lecture, [Lesson 2: Modern Data Management](02-data-management.md), is the summary of this page; complete this page before [Lesson 3](03-ai-ethics.md).

    **With an AI tutor:** this page is written so an AI assistant can teach it module by module. See [Learn with an AI tutor](../about/ai-tutor.md) for prompts, including prompts for screen-reader users, deaf and hard-of-hearing learners, and learners whose first language is not English. Every figure has a text description directly below it.

!!! abstract "In brief"
    This page is the full version of Lesson 2. Modules 1 and 2 explain why data management comes first and why public data need rescuing. Modules 3 to 6 walk through the data life cycle: types of data, planning and collecting, quality, metadata, preservation, discovery, integration, and analysis. Modules 7 and 8 cover the FAIR principles and the CARE principles, including what research on Navajo Nation requires. Module 9 explains the 2026 NIH and NSF plan formats, Module 10 covers licenses, Module 11 is three self-assessments and a two-site plan scenario, and Module 12 is the quiz. Every example pairs an Arizona item with a New Mexico item.

## Learning objectives

!!! success "After completing this page, you will be able to:"
    - Recognize data as the foundation of open science and explain why data management must come first
    - Describe the complete life cycle of data and the practices at each stage
    - Explain why community mirrors and preservation protect environmental-justice data
    - Apply FAIR principles to your research data and CARE principles to data about Indigenous peoples
    - Write a data management and sharing plan in the 2026 NIH format and explain how the NSF plan differs
    - Choose repositories and licenses for your data, and evaluate your own practices with three self-assessments

---

## Module 1: Why data management comes first

*About 5 minutes.*

### The hidden crisis in research

!!! question "Critical questions"
    - If you gave your data to a colleague unfamiliar with your project, could they make sense of it?
    - If you returned to your own data in five years, would you understand it?
    - When publishing, can you easily find all correct versions of your data?

!!! example "SRP research scenario"
    Imagine a collaborator asks you to share:

    - Arsenic concentration measurements from 50 mine tailings samples
    - Lung tissue images from an inhalation exposure study
    - Plant biomass and metal uptake data from phytoremediation field plots
    - GPS coordinates and soil characterization from multiple Superfund sites
    - Uranium, arsenic, and vanadium (U/As/V) water and soil chemistry from abandoned uranium mines on Navajo Nation
    - Livestock and household well-water screening results from partner communities
    - Community survey data collected under Navajo Nation Human Research Review Board (NNHRRB) approval

    Could they understand your file naming conventions? Would they know which samples came from which sites? Would they understand the units, detection limits, and quality control procedures? Would they know which records may never leave the community that owns them? Environmental health research generates complex, multi-dimensional datasets requiring exceptional organization.

### The biggest challenge

!!! danger "The number one data management problem"
    **Making it an afterthought.**

    Poor data management has no upfront cost. You can do substantial work before realizing you are in trouble. By then, fixing the problem is exponentially harder.

    **The solution?** Make data management the **first** thing you consider when starting research.

### Why data management matters

Well-managed datasets:

- Make life much easier for you and collaborators
- Enable others to reuse and build upon your work
- Are increasingly **required** by funders and journals
- Protect against data loss and irreproducibility
- Save time and prevent costly errors

??? question "Checkpoint 1: Why is the cost of poor data management invisible at the start of a project?"
    Because nothing breaks on day one. Bad file names, missing units, and undocumented QC only hurt when someone (often future you) tries to reuse the data, and by then the people and context that could have explained them are gone.

---

## Module 2: When the data disappear

*About 10 minutes.*

!!! danger "EJScreen and data rescue (2025)"
    Environmental-justice data are only as durable as the servers they live on.

    - **21 January to 11 February 2025:** 203 CDC datasets were removed from public sites; a court order in *Doctors for America v. OPM* (11 February 2025) required their restoration ([case record](https://clearinghouse.net/case/46029/){target=_blank})
    - **5 February 2025:** EPA removed EJScreen, its environmental-justice screening tool ([EDGI](https://envirodatagov.org/epa-removes-ejscreen-from-its-website/){target=_blank}; [Harvard EELP tracker](https://eelp.law.harvard.edu/tracker/epa-added-environmental-health-indicators-to-ejscreen/){target=_blank})
    - **7 February 2025:** the Public Environmental Data Partners mirror of [EJScreen](https://screening-tools.com/epa-ejscreen){target=_blank} went live; **14 February 2025** the [EJAM](https://screening-tools.com/epa-ejam){target=_blank} mirror followed (version 3 in 2026)
    - **6 February 2025:** Harvard Library Innovation Lab announced its [data.gov archive](https://lil.law.harvard.edu/blog/2025/02/06/announcing-data-gov-archive/){target=_blank}, now 311,000+ datasets and 16 TB on [Source Cooperative](https://source.coop/repositories/harvard-lil/gov-data/description){target=_blank} (updated July 2026); the [Data Rescue Project](https://www.datarescueproject.org/){target=_blank} launched the same month
    - **13 March 2026:** *Sierra Club v. EPA* was dismissed for lack of standing; EJScreen is still absent from epa.gov

    **The lesson:** download, DOI, and document what you depend on. Keep a dated local copy of every federal dataset your project uses, record its version and source URL, and cite the persistent identifier of the copy you actually analyzed.

    **Ask yourself:** Which federal datasets does your project depend on? Where is your copy?

The rules that require sharing did not disappear; they got more specific. Module 9 covers the 2026 NIH and NSF plan formats in detail. In brief:

- **NSF** ([PAPPG 24-1](https://www.nsf.gov/policies/pappg){target=_blank} with Supplements [26-200](https://www.nsf.gov/policies/document/pappg24-1-supplement-1){target=_blank} and [26-202](https://www.nsf.gov/policies/document/pappg24-1-supplement-2){target=_blank}): data underlying publications shared at publication; a two-page Data Management and Sharing Plan submitted by webform since 27 April 2026
- **NIH** ([NOT-OD-26-046](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html){target=_blank}, [NOT-OD-26-100](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-100.html){target=_blank}): for due dates on or after 25 May 2026, Yes/No commitments, a 300-word justification, and a 100-word table; compliance reported in the RPPR from 1 October 2026
- **Superfund Research Program:** a Data Management and Analysis Core (DMAC) has been mandatory for P42 centers since RFA-ES-23-001, and RFA-ES-27-004 (due 25 September 2026) continues it; 19 DMACs are active ([SRP data sharing](https://tools.niehs.nih.gov/srp/data/index.cfm){target=_blank}, [DMAC pages](https://tools.niehs.nih.gov/srp/data/dmac.cfm){target=_blank}, [NIEHS data policy](https://www.niehs.nih.gov/research/scientific-data/policy){target=_blank})
- **Gold Standard Science:** NIH's implementation plan (22 August 2025) adds data-sharing compliance, replication, and training to its tenets ([NIH OSP](https://osp.od.nih.gov/nih-releases-implementation-plan-to-drive-gold-standard-science/){target=_blank}); the executive order is covered in [Lesson 1](01-open-science-self-paced.md#module-9-gold-standard-science-in-depth)

??? question "Checkpoint 2: Your exposure analysis used EJScreen indicators. What three things should already be in your project folder?"
    A dated local copy of the data, a record of its version and source URL, and the persistent identifier (of your deposited or mirrored copy) that you cite in the paper.

---

## Module 3: What qualifies as data

*About 5 minutes.*

Different data types require different management strategies:

Text
:   Field notes, survey responses, interview transcripts

Numeric
:   Tables, measurements, counts, statistics

Audiovisual
:   Images, videos, sound recordings

Models and code
:   Simulations, algorithms, analysis scripts

Discipline-specific
:   FASTA (biology), FITS (astronomy), CIF (chemistry)

Instrument-specific
:   Raw equipment outputs, sensor readings

!!! example "SRP data types"
    **Environmental chemistry (Arizona):** ICP-MS outputs (arsenic and metalloid concentrations), XRD patterns, synchrotron XAS spectra

    **Metal mixtures (UNM METALS):** ICP-MS and ICP-OES concentrations of U/As/V, gamma spectrometry of soil cores, XANES speciation of uranium and vanadium phases in mine waste

    **Toxicology:** flow cytometry data, histopathology images, gene expression arrays, biomarker measurements

    **Phytoremediation:** plant biomass measurements, metal uptake data, hyperspectral imaging, LiDAR point clouds

    **Epidemiology:** survey responses (with PII protections), biomarker data (HIPAA-compliant), geospatial health data

    **Community exposure:** household well water, dust wipes, urine biomonitoring, collected with partner communities under tribal data-governance conditions

    **Field sampling:** GPS coordinates, soil cores, air quality measurements, meteorological data

### Data sources

Observational
:   Captured in real time, typically outside the lab. **Usually irreplaceable**, so the most important to safeguard. Examples: sensor readings, telescope observations, field surveys.

Experimental
:   Generated under controlled conditions. Often reproducible but expensive and time-consuming. Examples: lab measurements, controlled trials, sequencing.

Simulation
:   Machine-generated from computational models. Reproducible if the model and inputs are preserved. Examples: climate projections, molecular dynamics.

Derived
:   Generated from existing datasets. Reproducible but potentially expensive. Examples: meta-analyses, compiled databases, data mining results.

??? question "Checkpoint 3: Which of your project's data are observational, and why does that class need the strongest backup?"
    Field samples, well-water screening, dust wipes, weather records, and surveys are observational: they record a moment that cannot be re-run. Experimental and derived data can, at a cost, be regenerated; observational data cannot.

---

## Module 4: The data life cycle: plan, collect, assure

*About 10 minutes.*

<figure markdown>
  ![The data life cycle: eight stages arranged in a circle and connected by arrows, from Plan through Collect, Assure, Describe, Preserve, Discover, Integrate, and Analyze, then back to Plan](../assets/data_life_cycle.png){ width="500" }
  <figcaption>Data flow through multiple stages, each with specific management needs (DataONE)</figcaption>
</figure>

??? note "Text description of this figure"
    Eight rounded teal boxes are arranged in a circle and joined by curved arrows that run clockwise. Starting at the top: Plan, then Collect (upper right), Assure (right), Describe (lower right), Preserve (bottom), Discover (lower left), Integrate (left), Analyze (upper left), and an arrow from Analyze back to Plan, showing that the cycle repeats.

Understanding where data are in their life cycle helps plan management strategies.

### Plan

- Describe the data to be collected
- Plan for organization before collection
- Consider all life-cycle stages
- Create the data management plan

!!! tip "Planning questions"
    - What data will you generate or reuse?
    - What file formats will you use?
    - How will you organize and document data?
    - Where will data be stored and backed up?
    - How will you ensure data quality?
    - Who will have access and when?
    - How long must data be preserved?

### Collect

- Implement the organizational system before collecting
- Capture observation metadata simultaneously
- Take advantage of automatic metadata generation
- Use consistent naming conventions
- Document collection conditions

!!! example "File naming best practices"
    ```
    # Good examples
    2026-01-15_site-A_temp-sensor-01_raw.csv
    experiment-03_rep-02_treated_microscopy.tif
    survey_2026_wave-01_demographics.xlsx

    # Bad examples
    data.csv
    final_FINAL_v3_revised_2.xlsx
    New Folder (2)/results!!!.csv
    ```

!!! example "SRP file naming examples"
    ```
    # Mine tailings samples (Arizona)
    2026-04-18_IronKing_MT-014_As-concentration_ICP-MS.csv
    2026-04-18_IronKing_MT-014_XRD-pattern_raw.xy

    # Abandoned uranium mines (Navajo Nation, UNM METALS)
    2026-03-12_RWPR_WELL-07_U-As-V_ICP-MS.csv
    2026-05-02_ClaimTwentyEight_soil-core-03_gamma-spec.csv

    # Lung tissue images
    exp-027_mouse-14_lung-section-03_H&E-stain_40x.tif
    exp-027_mouse-14_lung-section-03_collagen-IF_20x.tif

    # Phytoremediation field data
    2026-03-15_site-B_plot-12_Atriplex-canescens_biomass.csv
    2026-03-15_site-B_hyperspectral_processed_NDVI.tif

    # Keep consistent: YYYY-MM-DD_site_sample-ID_analysis-type_details.ext
    # Rule: site codes in filenames, never GPS coordinates or household IDs
    ```

### Assure

- Record quality conditions during collection
- Distinguish estimated from measured values
- Double-check manually entered data
- Run statistical summaries to find outliers
- Flag questionable or missing values
- Perform validation checks

**Quality assurance checklist:**

- [ ] Define acceptable ranges for measurements
- [ ] Implement automated validation scripts
- [ ] Document calibration procedures
- [ ] Track instrument performance over time
- [ ] Create visualizations to spot anomalies
- [ ] Maintain an audit trail of quality checks

??? question "Checkpoint 4: Rewrite the file name `results_final2.xlsx` for a uranium well-water ICP-MS run at Red Water Pond Road on 3 June 2026."
    Something like `2026-06-03_RWPR_WELL-03_U-As-V_ICP-MS.csv`: date first, a site code rather than coordinates, a sample identifier rather than a household name, the analysis type, and an open format.

---

## Module 5: Describe: metadata and standards

*About 10 minutes.*

!!! quote "Metadata is key"
    "Without thorough description of context, collection methods, measurements, and quality, data are unlikely to be discovered, understood, or effectively used."

**Essential metadata:**

- **Dataset information:** title, dates, version, related datasets
- **People:** authors, affiliations, sponsors, ORCID IDs
- **Scientific context:** research question, hypotheses, methods
- **Data details:** variables, units, formats, missing value codes
- **Quality:** precision, accuracy, uncertainty, QA procedures
- **Access:** license, restrictions, citation instructions

**Metadata standards:**

- [DataCite](https://schema.datacite.org/){target=_blank}: publishing data (schema 4.7, March 2026)
- [Dublin Core](https://www.dublincore.org/){target=_blank}: web-based sharing
- [ISO 19115-1](https://www.iso.org/standard/53798.html){target=_blank}: geospatial data
- [MIxS](https://genomicsstandardsconsortium.github.io/mixs/){target=_blank}: environmental samples (v7: soil, water, sediment)
- [Darwin Core](https://dwc.tdwg.org/){target=_blank}: biodiversity and ecological data
- [Environmental Health Language Collaborative (EHLC)](https://www.niehs.nih.gov/research/programs/ehlc){target=_blank}: harmonized vocabularies for environmental health
- [GA4GH Human Exposome Data Standards](https://www.ga4gh.org/product/human-exposome-data-standards/){target=_blank}: exposure and biomonitoring data
- [Croissant 1.1](https://mlcommons.org/working-groups/data/croissant/){target=_blank} and [Frictionless](https://frictionlessdata.io/){target=_blank}: machine-readable table descriptions (ML-ready datasets)
- Domain-specific standards: check [FAIRsharing.org](https://fairsharing.org/){target=_blank}

!!! example "SRP metadata needs"
    **Mine tailings samples (Arizona):** site GPS coordinates, collection date and time, depth, weather conditions, proximity to mining activity, historical context, chain of custody

    **Abandoned uranium mine samples (UNM METALS):** mine and claim identifier, distance to homes and wells, chapter or pueblo jurisdiction, sampling permit, radiological screening at collection

    **Toxicology experiments:** animal strain and source, exposure protocol (concentration, duration, route), housing conditions, institutional approvals (IACUC), treatment randomization

    **Chemical analysis:** instrument make and model, calibration standards, detection limits, QA/QC procedures, analyst ID, date of analysis, method references

    **Field studies:** plot layout, vegetation surveys, soil characterization, meteorological data, disturbance history, GPS accuracy

    **Community data:** consent scope, NNHRRB protocol number, chapter resolution, Local Contexts TK/BC Notice, embargo and ownership terms, who must approve release

??? question "Checkpoint 5: Which metadata standard would you use for (a) a soil-core dataset, (b) a phytoremediation plant survey, (c) a biomonitoring dataset?"
    (a) MIxS for the environmental sample plus ISO 19115-1 for the spatial layer; (b) Darwin Core; (c) the GA4GH Human Exposome Data Standards, with a DataCite record on top of all three for the DOI.

---

## Module 6: Preserve, discover, integrate, analyze

*About 10 minutes.*

### Preserve

!!! warning "Not just backup: preservation"
    Preservation means ensuring data remain accessible and usable long-term, not just keeping copies on a hard drive.

**Preservation repositories:**

- **Institutional (Arizona):** [UA ReDATA](https://redata.arizona.edu/){target=_blank}
- **Institutional (New Mexico):** [UNM Digital Repository](https://digitalrepository.unm.edu/){target=_blank}; UNM is a [Dryad](https://datadryad.org/){target=_blank} member (up to 300 GB per dataset, no fee); the [UNM Research Data Services guide](https://libguides.unm.edu/data){target=_blank} covers the 2026 NIH and NSF templates
- **Environmental and health:** [NIEHS CEBS](https://cebs-ext.niehs.nih.gov/datasets/){target=_blank}, [SRP Tox Data Commons](https://toxdatacommons.com/){target=_blank}, [NEU Data Dictionaries](https://manati.ece.neu.edu/dictionary/){target=_blank}, [EPA Science Inventory](https://cfpub.epa.gov/si/){target=_blank} and [Environmental Dataset Gateway](https://edg.epa.gov/){target=_blank}
- **Ecological and Earth science:** [EDI](https://edirepository.org/){target=_blank}, [DataONE](https://www.dataone.org/){target=_blank}, [PANGAEA](https://pangaea.de/){target=_blank}, [USGS ScienceBase](https://www.sciencebase.gov/){target=_blank} (USGS authors only)
- **Human subjects:** [dbGaP](https://dbgap.ncbi.nlm.nih.gov/home){target=_blank} (controlled access)
- **General purpose:** [Zenodo](https://zenodo.org/){target=_blank} (50 GB per record), [Figshare](https://figshare.com/){target=_blank} (20 GB free)
- **CyVerse:** [Data Commons](https://datacommons.cyverse.org/){target=_blank} for computational biology

!!! example "SRP repository choices"
    **Toxicology data:** NIEHS CEBS or the SRP Tox Data Commons; dbGaP for human subjects data; Figshare or Zenodo for animal studies

    **Environmental chemistry (Arizona mine tailings):** EPA Science Inventory or Environmental Dataset Gateway for arsenic data from contaminated sites, or Zenodo with appropriate environmental keywords

    **Geospatial data:** DataONE or EDI for mine site characterization and remediation monitoring data; USGS ScienceBase only with a USGS co-author

    **Spectroscopy data:** Zenodo allows large files and assigns DOIs, suited to synchrotron XAS, XANES, or hyperspectral datasets

    **Tribal community data (UNM METALS):** the [Native BioData Consortium](https://nativebio.org/){target=_blank} Tribal Data Repository or tribally controlled storage; a metadata-only record elsewhere (institutional repository, DataCite) so the dataset is findable without leaving the community's control

<figure markdown>
  ![RO-Crate illustration: research outputs on a conveyor belt are packaged by a machine into sealed crates that carry linked metadata](../assets/RO_crate.png){ width="500" }
  <figcaption>RO-Crate 1.3 (June 2026) packages data, code, and metadata as one citable research object (researchobject.org)</figcaption>
</figure>

??? note "Text description of this figure"
    A grey and teal illustration titled "Enabling reproducible, transparent research." A conveyor belt runs from left to right. On the left, loose stacks of documents sit on the belt; a callout labeled "scientific hypothesis" lists the outputs they represent, each with an icon: publications, data, results, workflows, slides, metadata, and logs. The stacks pass through a large box-shaped machine bearing the RO-Crate logo (a flask inside a circular arrow) and come out as sealed transparent crates, each holding a bundle of documents. At the far right one crate is open, and an arrow rises from it to an inset panel labeled RDF that shows the same files linked to one another by arrows, forming a graph. Four labels under the panel give the result: Linked Open Data, Executable, Discoverable, Reproducible.

Package before you deposit: an [RO-Crate](https://www.researchobject.org/ro-crate/){target=_blank} bundles the files, their metadata, and the workflow that produced them, so a reviewer gets the whole research object rather than a bare folder; the same idea applies to software under [FAIR4RS](https://www.nature.com/articles/s41597-022-01710-x){target=_blank}.

**Preservation best practices:**

1. Choose repositories with [TRUST principles](https://www.nature.com/articles/s41597-020-0486-7){target=_blank}
2. Use open, non-proprietary formats when possible
3. Include comprehensive documentation
4. Assign persistent identifiers (DOIs)
5. Apply appropriate licenses
6. Consider embargo periods if needed

### Discover

Good metadata enables discovery by you and others:

- Repository search interfaces, discipline-specific portals, and aggregators such as [re3data](https://www.re3data.org/){target=_blank}
- [Google Dataset Search](https://datasetsearch.research.google.com/){target=_blank}
- [DataONE](https://www.dataone.org/){target=_blank}
- [OpenAlex](https://openalex.org/){target=_blank}: open scholarly index; its November 2025 rewrite ingests DataCite records, so deposited datasets appear next to papers
- [DataCite Commons](https://commons.datacite.org/){target=_blank}: search every DataCite DOI and the people, organizations, and works connected to it

### Integrate

- Data integration requires careful work
- Standards and ontologies are crucial
- Know the data before integrating
- Never assume column headers mean the same thing
- **Always cite data you reuse**
- Use DOIs for citations

### Analyze

- Follow reproducible practices
- Record all software, versions, parameters
- Use computational notebooks (Jupyter, R Markdown, Quarto)
- Version control analysis code
- Pre-register analysis plans when possible
- Document decision points

??? question "Checkpoint 6: Why is 'a copy on the lab server' not preservation, and what would make it preservation?"
    A server copy has no persistent identifier, no guaranteed lifetime, no public metadata, and depends on one lab's IT. Preservation means a trusted repository (TRUST principles), open formats, documentation, a DOI, and a license or access terms.

---

## Module 7: The FAIR principles

*About 10 minutes.*

In 2016, the [FAIR Guiding Principles](https://www.nature.com/articles/sdata201618){target=_blank} changed how we think about data management.

<figure markdown>
  ![FAIR: the words Findable, Accessible, Interoperable, and Reusable with large initial letters, each above an icon: a magnifying glass, a pointing hand, three gears, and a recycling symbol](../assets/fair_principles.png){ width="500" }
  <figcaption>FAIR principles provide a framework for data stewardship</figcaption>
</figure>

??? note "Text description of this figure"
    Four words in a row, black on white, each with an oversized capital letter so that the initials spell FAIR: Findable, Accessible, Interoperable, Reusable. Under each word is a simple black icon: a magnifying glass under Findable, a hand with an extended index finger pressing a button under Accessible, three interlocking gears under Interoperable, and the three-arrow recycling symbol under Reusable.

!!! tip "Why principles, not rules?"
    FAIR is intentionally a set of principles, not rigid rules. Different disciplines must interpret and implement these principles appropriate to their contexts and technologies.

### F: Findable

- (Meta)data assigned a globally unique persistent identifier
- Data described with rich metadata
- Metadata includes the identifier of the described data
- (Meta)data registered in a searchable resource

**Practical implementation:** use DOIs for datasets; create comprehensive README files; register with domain repositories; use descriptive, searchable keywords.

### A: Accessible

- (Meta)data retrievable via a standardized protocol
- The protocol is open, free, universally implementable
- The protocol allows authentication when necessary
- Metadata accessible even when data are unavailable

**Practical implementation:** store in repositories with standard access protocols (HTTPS, S3); provide clear access instructions; maintain metadata permanently; document access restrictions clearly.

### I: Interoperable

- (Meta)data use a formal, shared, broad language
- (Meta)data use vocabularies following FAIR principles
- (Meta)data include qualified references to other data

**Practical implementation:** use standard file formats (CSV, NetCDF, GeoTIFF); prefer cloud-native formats for large data (GeoParquet for vector tables, Cloud-Optimized GeoTIFF for rasters, Zarr for arrays, and DuckDB over Parquet for local analysis); apply community ontologies; link related datasets; document relationships between datasets.

### R: Reusable

- (Meta)data richly described with accurate attributes
- Released with a clear, accessible usage license
- Associated with detailed provenance
- Meet domain-relevant community standards

**Practical implementation:** include comprehensive documentation; apply a recognized license (CC BY, CC0); document data collection and processing; follow discipline-specific standards.

!!! warning "FAIR is not the same as open"
    FAIR does not require data be open. Data can be FAIR but restricted:

    - Human subjects data may be FAIR but require access approval
    - Endangered species locations should be findable in metadata but not accessible
    - Data collected on Navajo Nation may be FAIR to the Nation and its chapters while access for everyone else is governed by NNHRRB conditions, with a metadata-only record in public repositories

??? question "Checkpoint 7: A dataset has a DOI and a rich record but the files can be downloaded only after the data access committee approves a request. Is it FAIR?"
    Yes. Findable (DOI, record), Accessible (a documented, standard protocol that allows authentication), and, if the formats and license are right, Interoperable and Reusable. FAIR describes the mechanism of access, not whether access is unrestricted.

---

## Module 8: CARE and research on Navajo Nation

*About 10 minutes.*

!!! quote "Nothing about us without us"
    The [CARE Principles](https://www.gida-global.org/careprinciples){target=_blank} for Indigenous Data Governance ensure Indigenous Peoples' rights and interests in data are respected. CARE complements FAIR by centering Indigenous rights and interests in data governance: FAIR asks whether data *can* be reused, CARE asks whether they *should* be, by whom, and on whose terms.

Collective benefit
:   Data for inclusive development and innovation, improved governance and citizen engagement, and equitable outcomes

Authority to control
:   Recognize Indigenous rights and interests; empower data for governance; support governance of data

Responsibility
:   Foster positive relationships; expand capability and capacity; support Indigenous languages and worldviews

Ethics
:   Minimize harm and maximize benefit; promote justice; consider future use

!!! warning "Research on Navajo Nation"
    UNM METALS ("Metal Exposure and Toxicity Assessment on Tribal Lands in the Southwest", 2022 to 2027) partners with the Pueblo of Laguna (Jackpile Mine) and the Navajo communities of Red Water Pond Road, Blue Gap-Tachee, and Cameron ([METALS Center](https://hsc.unm.edu/pharmacy/research/areas/metals/){target=_blank}); Arizona mine sites may also lie on or near tribal lands. For work on Navajo Nation:

    - The [Navajo Nation Human Research Review Board](http://nnhrrb.navajo-nsn.gov/){target=_blank} (NNHRRB, established 1996) must approve the protocol, and the affected chapter must pass a supporting resolution, **before** collection begins
    - **The Navajo Nation owns the data.** The NNHRRB must approve the Final Report and a Dissemination Plan before results are shared in any form, including preprints, conference talks, and repository deposits
    - The 2024 Navajo Nation Genetics Research Policy Statement ([Legislation 0241-24](https://www.navajonationcouncil.org/wp-content/uploads/2024/11/0241-24.pdf){target=_blank}) governs genetic and biospecimen research
    - UNM investigators follow the [UNM HRPO](https://hsc.unm.edu/research/compliance/hrpo/){target=_blank} and the [UNM IRB guidance for research with American Indian communities](https://irb.unm.edu/library/documents/guidance/research-with-american-indian-communities.pdf){target=_blank}, which also covers the Southwest Tribal IRB, the IHS IRB, and approval by Pueblo governors (for the Pueblo of Laguna)
    - Tribal nations near Arizona sites each have their own review process; a university IRB approval is never a substitute

    Write these conditions into the DMP, the metadata, and the data governance agreement, not just the IRB file.

!!! tip "Applying CARE in practice"
    When working with data about Indigenous peoples, traditional knowledge, or Indigenous lands:

    1. Engage with communities early
    2. Establish data sovereignty agreements
    3. Respect cultural protocols
    4. Share benefits equitably
    5. Support community capacity building
    6. Label data with [Local Contexts](https://localcontexts.org/){target=_blank} TK and BC Notices (create a Hub account; read their "Data Do's and Don'ts")
    7. Learn from the [Collaboratory for Indigenous Data Governance](https://indigenousdatalab.org/){target=_blank}, the [Native BioData Consortium](https://nativebio.org/){target=_blank}, and the [US Indigenous Data Sovereignty Network](https://usindigenousdatanetwork.org/){target=_blank}

??? question "Checkpoint 8: Your IRB has approved a household survey near an abandoned uranium mine on Navajo Nation. What two approvals are still missing before you collect, and what approval is needed before you present results?"
    Before collection: NNHRRB approval of the protocol and a supporting resolution from the affected chapter. Before any presentation, preprint, or deposit: NNHRRB approval of the Final Report and the Dissemination Plan.

---

## Module 9: Data management plans: the 2026 NIH and NSF formats

*About 10 minutes.*

!!! quote "Failure to plan is planning to fail"
    A data management plan (DMP) is a formal document outlining how data will be handled during and after a research project.

**Why create a DMP?** The stick: you have to; funders require them. The carrot: they make your life easier: they clarify your thinking before starting, anticipate and avoid problems, help you budget, enable collaboration, and facilitate sharing and preservation.

**Essential DMP components** (the traditional narrative; the 2026 formats compress these):

1. **Data description:** types, volumes, formats; existing versus new data; relationship to other data
2. **Metadata and documentation:** standards to be used; tools for documentation; completeness of documentation
3. **Storage and backup:** short-term storage during the project; backup frequency and methods; data security measures
4. **Access and sharing:** who can access data and when; how others can access data; restrictions on sharing
5. **Preservation:** where data will be deposited; how long data will be preserved; costs and responsibilities
6. **Ethics and compliance:** privacy considerations; intellectual property issues; ethical approvals needed

!!! info "NIH: the 2026 format, element by element"
    The [NIH Data Management and Sharing Policy](https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms){target=_blank} itself is unchanged, but the plan you write is not. For due dates on or after 25 May 2026 ([NOT-OD-26-046](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-046.html){target=_blank}), the [format page](https://grants.nih.gov/grants-process/write-application/forms-directory/data-management-and-sharing-plan-format-page){target=_blank} replaces the six-element narrative with three parts:

    1. **Yes/No commitments:** a checklist of sharing commitments; each "No" has to be explained
    2. **Limitation justification (at most 300 words):** the only free text; use it for consent scope, tribal data governance, and site-location sensitivity
    3. **Data and repository table (at most 100 words):** each data type paired with the repository that will hold it

    [NOT-OD-26-100](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-100.html){target=_blank}: no prior approval is needed to change a plan; compliance is reported in RPPR section C.5.c starting 1 October 2026; all awards move to the 2026 format in FY2027. **Budget** for the DMAC's time and any repository fees in the proposal budget. Human subjects protections for community health data and documented restrictions on sensitive data (contaminated-site locations, participant privacy, tribally governed data) still apply.

!!! info "NSF: PAPPG 24-1 with Supplements 26-200 and 26-202"
    The [NSF Proposal and Award Policies and Procedures Guide 24-1](https://www.nsf.gov/policies/pappg){target=_blank} remains in force, with two supplements that change what your plan must promise:

    - **Supplement 1 (NSF 26-200, 8 December 2025):** data underlying publications must be shared at the time of publication ([details](https://www.nsf.gov/policies/document/pappg24-1-supplement-1){target=_blank})
    - **Supplement 2 (NSF 26-202, 22 January 2026):** the DMP is now a **Data Management and Sharing Plan** (2 pages), submitted through a Research.gov webform since 27 April 2026, and must commit to persistent identifiers and minimum metadata ([details](https://www.nsf.gov/policies/document/pappg24-1-supplement-2){target=_blank})
    - A successor guide (GFA 27-1) has been proposed for FY2027; check the [NSF data management plan page](https://www.nsf.gov/funding/data-management-plan){target=_blank} before you submit

!!! tip "DMP tools"
    **[DMPTool](https://dmptool.org/){target=_blank}:** create plans using funder templates; the NIH 2026 template was added 24 April 2026 and the NSF Research.gov webform is mirrored

    **[Data Stewardship Wizard](https://ds-wizard.org/){target=_blank}:** knowledge-based DMP creation

    Both tools provide guidance, templates, and examples to help you write effective plans.

??? question "Checkpoint 9: In the NIH 2026 format, where do you explain that Navajo Nation household data cannot be deposited publicly, and how long can that explanation be?"
    In the limitation justification, the only free-text part, and it can be at most 300 words. The corresponding Yes/No commitment is answered "No", and the 100-word table pairs that data type with tribally controlled storage plus a metadata-only record.

---

## Module 10: Choosing a license

*About 5 minutes.*

By default, creative work is under exclusive copyright. To enable reuse, you must license your work.

CC0 (public domain dedication)
:   Complete surrender of copyright; data freely usable without attribution; the most open option, recommended for maximum reuse.

CC BY (attribution)
:   Requires attribution to the creator; allows any use with credit; balances openness with recognition; the most common license for research data.

CC BY-SA (share-alike)
:   Requires attribution and derivative works must use the same license; ensures openness propagates; less commonly used for data.

!!! warning "Non-commercial restrictions"
    Avoid "NC" (non-commercial) licenses for research data: the definition of "commercial" is ambiguous, it restricts institutional and infrastructure use, it prevents integration with other datasets, and it limits reproducibility.

!!! warning "Tribal community data are not yours to license"
    CC0 and CC BY are inappropriate for data collected with or about tribal communities. Those data are governed by the research agreement and the community's review board (for Navajo Nation, the NNHRRB); access terms, attribution, and future use are set there, not by a Creative Commons deed. Publish a metadata record with a Local Contexts Notice instead.

**Choosing a license:** check funder requirements; consider community norms; more open means more reuse; document the license clearly in the repository; include a LICENSE file with the data.

**Resources:** [Choose a License](https://choosealicense.com/){target=_blank} (software only), [Creative Commons License Chooser](https://creativecommons.org/chooser/){target=_blank}, [Open Data Commons Licenses](https://opendatacommons.org/licenses/){target=_blank}.

??? question "Checkpoint 10: A collaborator proposes CC BY-NC for the arsenic phytoremediation dataset 'so companies cannot profit from it'. What is the problem?"
    "Commercial" is undefined in practice, so the license blocks aggregators, infrastructure providers, and integration with other datasets, and it makes reproduction by anyone at a company legally uncertain. Use CC BY (or CC0) and, if profit is the concern, address it through a data governance agreement, not a license.

---

## Module 11: Self-assessments and the two-site plan scenario

*About 20 minutes.*

### Assessment: the three Vs

!!! question "Volume, velocity, variety"

    **Volume:** size and quantity of data

    - [ ] I know the total size of my active research data
    - [ ] I have enough storage for my data
    - [ ] I have a plan for when data exceed current storage
    - [ ] I have budgeted for data storage costs

    **Velocity:** speed of data generation and analysis

    - [ ] I can keep up with data processing
    - [ ] I have automated workflows for routine tasks
    - [ ] Data are processed in reasonable timeframes
    - [ ] Backlogs are manageable

    **Variety:** diversity of data types

    - [ ] I use standard file formats when possible
    - [ ] Different data types are organized logically
    - [ ] I have appropriate tools for each data type
    - [ ] Data can be integrated when needed

### Assessment: FAIR

!!! question "Findable, accessible, interoperable, reusable"

    **Findable**

    - [ ] Data have unique identifiers
    - [ ] Metadata are comprehensive
    - [ ] Data are registered in searchable repositories
    - [ ] Identifiers are persistent (DOIs)

    **Accessible**

    - [ ] Data are stored in reliable locations
    - [ ] Access methods are documented
    - [ ] Authentication is appropriate
    - [ ] Metadata will persist long-term

    **Interoperable**

    - [ ] Standard formats are used
    - [ ] Community vocabularies are applied
    - [ ] Related datasets are linked
    - [ ] Data work with analysis tools

    **Reusable**

    - [ ] A clear license is applied
    - [ ] Provenance is documented
    - [ ] Quality is described
    - [ ] Usage guidelines are provided

### Assessment: dependency

!!! question "External data my project cannot do without"
    - [ ] I can list every federal or third-party dataset my analysis depends on
    - [ ] I hold a dated local copy of each, with its version and source URL recorded
    - [ ] Each copy is mirrored somewhere my lab controls (institutional storage, a repository deposit)
    - [ ] I cite the persistent identifier of the copy I analyzed, not just the agency home page
    - [ ] I know which community mirror (PEDP, Harvard LIL, DataLumos) to use if the source goes offline

### Scenario: metal-mixture exposure across two Superfund sites

Work in a small group, or alone with an AI tutor playing the DMAC data manager.

!!! example "The scenario"
    You are planning a 4-year NIH Superfund-funded study of metal-mixture exposure, with a plan due after 25 May 2026 (so it uses the NIH 2026 format).

    **Site A, Arizona mine tailings (state land)**

    - Soil and tailings samples (100+ samples per year): ICP-MS for arsenic and metal concentrations
    - Plant tissue samples from phytoremediation plots: biomass, metal uptake, tissue distribution
    - Hyperspectral drone imagery (quarterly): plant stress detection and dust-source mapping
    - Weather station data (15-minute intervals): temperature, humidity, wind, precipitation
    - GPS and GIS data: site characterization, vegetation mapping

    **Site B, abandoned uranium mine on Navajo Nation**

    - Household well water and livestock water: ICP-MS for U/As/V
    - Household dust wipes and outdoor soil: gamma spectrometry, XANES speciation
    - Urine biomonitoring and a household exposure survey
    - **NNHRRB conditions:** the Nation owns the data; a chapter resolution precedes collection; the NNHRRB approves the Final Report and Dissemination Plan before any release; household locations are never made public

    **Project involves:**

    - 2 SRP centers (Arizona and UNM METALS), an external analytical lab, and a tribal community partner
    - 12 team members (PIs, grad students, technicians, a DMAC data manager, community health representatives)
    - NIH Superfund funding requiring a 2026-format DMS Plan
    - Site A data must be public no later than publication
    - Some Site A location data may need restriction to prevent looting of remediation plants

**Your task:** draft key sections of the plan addressing:

1. **Data types and volumes:** estimate sizes, formats (ICP-MS output, drone imagery, gamma spectra, survey responses)
2. **Metadata:** what standards apply? (MIxS for soil and water, Darwin Core for plants, ISO 19115-1 for spatial data, GA4GH exposome standards for biomonitoring)
3. **Storage:** during the project, where will data live? (Institutional storage, field backups, tribally controlled storage for Site B)
4. **Quality:** how do you ensure accuracy? (Calibration standards, duplicate samples, QA/QC protocols)
5. **Sharing:** timeline, repository (EDI? Zenodo? Tox Data Commons? a metadata-only record?), restrictions for sensitive locations
6. **Roles:** who is responsible for what? (DMAC data manager, PI oversight, institutional compliance, community partner)
7. **Ethical considerations:** tribal consultation, community benefit, location data sensitivity
8. **Data governance agreement:** who owns each data type, who approves release, what happens to Site B data when the grant ends

**Discussion points:**

- Site A data can go to Zenodo or EDI; Site B data stay under tribal control. How do you make Site B findable (a metadata-only record?) without making it accessible?
- How do you answer the NIH 2026 Yes/No commitments honestly when part of the data cannot be shared, and what goes in the 300-word justification?
- What metadata is critical for someone to reuse the arsenic phytoremediation data? For the U/As/V well-water data?
- How do you handle data from an external lab with different formats?

### Individual action planning

Choose one improvement to implement this week:

!!! example "Possible actions"
    - [ ] Create a README template for my lab
    - [ ] Set up automated backups
    - [ ] Register for ORCID and start using it
    - [ ] Reorganize one project's file structure
    - [ ] Document one dataset with comprehensive metadata
    - [ ] Choose and apply a license to an existing dataset
    - [ ] Create a data dictionary for the current project
    - [ ] Set up version control for analysis code
    - [ ] Download and DOI-cite the federal datasets my project depends on

??? question "Checkpoint 11: Write your one action here, with a date."
    There is no answer key. If you are working with an AI tutor, ask it to hold you to the date.

---

## Module 12: Quiz and resources

*About 10 minutes.*

### Key takeaways

!!! success "Remember these concepts"
    1. **Plan early:** data management starts before data collection
    2. **FAIR principles** provide a framework but require interpretation
    3. **CARE principles** emphasize ethics and Indigenous data sovereignty; on Navajo Nation the NNHRRB and the community decide what is shared
    4. **Metadata matters:** future you (and others) need excellent documentation
    5. **Preserve what you depend on:** federal datasets can vanish; keep and cite your own copy
    6. **The 2026 formats are short:** NIH Yes/No commitments and the NSF 2-page webform reward honest, specific answers
    7. **Tools exist:** DMPTool, repositories, and standards can help
    8. **Start small:** one improvement at a time compounds over time

### Self-assessment quiz

??? question "What is the biggest challenge in data management?"
    **Making it an afterthought.** Data management problems are not immediately obvious. You can collect substantial data before realizing organization, documentation, or backup is inadequate. By then, fixing problems is exponentially harder. Make data management the first consideration in any project.

??? question "True or false: FAIR and CARE principles are the same"
    **False.** FAIR focuses on making data findable, accessible, interoperable, and reusable, primarily technical concerns. CARE addresses Indigenous data governance, emphasizing collective benefit, authority to control, responsibility, and ethics. Both are important but address different aspects of data stewardship.

??? question "True or false: data available upon request meets open data standards"
    **False.** Open data must be freely accessible in public repositories without requiring individual requests. "Available upon request" creates barriers, does not ensure data persist long-term, and does not meet FAIR findability or accessibility principles.

??? question "Your NIH application is due in October 2026. What does the data management and sharing plan look like?"
    **The 2026 pilot format from NOT-OD-26-046.** For due dates on or after 25 May 2026 the plan is a set of Yes/No commitments, a justification of up to 300 words for any limitation on sharing, and a 100-word table of data types and repositories. You no longer need prior approval to change the plan, but from 1 October 2026 you report compliance in RPPR section C.5.c.

??? question "EPA removed EJScreen in February 2025. Your exposure analysis used its indicators. What should already be in your project folder?"
    **A dated local copy, its version and source URL, and the persistent identifier you cite.** Community mirrors (the PEDP EJScreen and EJAM mirrors, the Harvard LIL data.gov archive, the Data Rescue Project) exist because agencies can withdraw datasets without notice. Download what you depend on, deposit or mirror it where your lab controls it, and cite the identifier of the copy you analyzed.

??? question "Your project needs a license allowing others to use your work with attribution. Which do you choose?"
    **CC BY (Creative Commons Attribution).** CC BY allows anyone to use, modify, and distribute your data as long as they provide appropriate attribution. It balances openness (maximizing reuse) with recognition (ensuring credit to creators) and is the most common license for research data, unless the data are governed by a tribal research agreement, in which case the agreement, not a CC license, sets the terms.

??? question "How does the NSF Data Management and Sharing Plan differ from the NIH 2026 format?"
    NSF's plan is a **two-page narrative** submitted through a Research.gov webform, committing to persistent identifiers, minimum metadata, and sharing data underlying publications at publication. NIH's is **Yes/No commitments, a 300-word justification, and a 100-word table**. Both expect a repository and an identifier for every shared data type.

### Looking ahead

In Lesson 3, we will address ethical considerations in modern research by exploring:

- Bias and discrimination in AI systems
- Responsible use of AI tools and agents in research
- Transparency and accountability
- Best practices for ethical AI integration

### Additional resources

- [DataONE Best Practices](https://dataoneorg.github.io/Education/bestpractices/){target=_blank}
- [FAIR Principles](https://www.gofair.foundation/fair-principles){target=_blank} and [TRUST Principles](https://www.nature.com/articles/s41597-020-0486-7){target=_blank}
- [CARE Principles](https://www.gida-global.org/careprinciples){target=_blank}
- [DMPTool](https://dmptool.org/){target=_blank}
- [Registry of Research Data Repositories](https://www.re3data.org/){target=_blank}
- More in [Additional resources](../about/resources.md)

---

**Lecture:** [← Lesson 2: Modern Data Management](02-data-management.md) | **Next:** [Lesson 3: Ethics and Artificial Intelligence →](03-ai-ethics.md)

<p class="carc-provenance" markdown>Adapted from [DUST 2025](https://github.com/tyson-swetnam/dust-2025/blob/29027dbda9ca29a123a68d8b4e2ae5dc198f7193/docs/lesson2_data_management/index.md){target=_blank} (last source update 2025-10-29), CC BY 4.0. Spotted a problem? [Open an issue](https://github.com/UNM-CARC/dust-2026/issues){target=_blank}.</p>

*[NIH]: National Institutes of Health
*[NSF]: National Science Foundation
*[NIEHS]: National Institute of Environmental Health Sciences
*[EPA]: Environmental Protection Agency
*[CDC]: Centers for Disease Control and Prevention
*[USGS]: United States Geological Survey
*[FAIR]: Findable, Accessible, Interoperable, Reusable
*[CARE]: Collective benefit, Authority to control, Responsibility, Ethics
*[DOI]: Digital object identifier
*[DOIs]: Digital object identifiers
*[DMP]: Data management plan
*[DMS]: Data management and sharing
*[DMAC]: Data Management and Analysis Core
*[DMACs]: Data Management and Analysis Cores
*[NNHRRB]: Navajo Nation Human Research Review Board
*[IRB]: Institutional Review Board
*[HRPO]: Human Research Protections Office
*[IHS]: Indian Health Service
*[IACUC]: Institutional Animal Care and Use Committee
*[HIPAA]: Health Insurance Portability and Accountability Act
*[PII]: Personally identifiable information
*[RPPR]: Research Performance Progress Report
*[PAPPG]: NSF Proposal and Award Policies and Procedures Guide
*[SRP]: Superfund Research Program
*[UNM]: University of New Mexico
*[UA]: University of Arizona
*[ORCID]: Open Researcher and Contributor ID
*[ICP-MS]: Inductively coupled plasma mass spectrometry
*[ICP-OES]: Inductively coupled plasma optical emission spectrometry
*[XRD]: X-ray diffraction
*[XAS]: X-ray absorption spectroscopy
*[XANES]: X-ray absorption near-edge structure spectroscopy
*[GPS]: Global Positioning System
*[GIS]: Geographic information system
*[LiDAR]: Light detection and ranging
*[NDVI]: Normalized difference vegetation index
*[CEBS]: Chemical Effects in Biological Systems
*[EDI]: Environmental Data Initiative
*[COG]: Cloud-Optimized GeoTIFF
*[MIxS]: Minimum Information about any (x) Sequence
*[GA4GH]: Global Alliance for Genomics and Health
*[EHLC]: Environmental Health Language Collaborative
*[RDF]: Resource Description Framework
*[TK]: Traditional Knowledge
*[BC]: Biocultural
*[PI]: Principal investigator
*[PIs]: Principal investigators
*[PEDP]: Public Environmental Data Partners
*[LIL]: Library Innovation Lab
*[EDGI]: Environmental Data and Governance Initiative
*[EELP]: Environmental and Energy Law Program
*[QA/QC]: Quality assurance and quality control
*[QA]: Quality assurance
*[CC]: Creative Commons
*[OPM]: Office of Personnel Management
*[RFA]: Request for applications
*[OSP]: Office of Science Policy
