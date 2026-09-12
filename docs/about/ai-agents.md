---
title: "For AI agents"
description: "How agents and harnesses should consume this site: llms.txt, per-page Markdown with OKF frontmatter, trust signals, and how to teach a lesson in lecture, tutor, or interactive mode while honoring its accessibility profile."
type: Reference
tags:
  - About
  - AI agents
  - OKF
generated:
  by: "claude/fable-5-1"
  at: "2026-09-12T02:00:00Z"
sources:
  - id: okf-spec
    resource: "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md"
    title: "Open Knowledge Format (OKF) v0.2 specification"
    author: "team:google-cloud"
  - id: llmstxt
    resource: "https://llmstxt.org"
    title: "The /llms.txt convention"
    author: "team:answer-ai"
  - id: carc-docs
    resource: "https://carc.unm.edu/docs/about/ai-agents/"
    title: "CARC Documentation: For AI agents"
    author: "team:unm-carc"
status: stable
---

# For AI agents

This site is published for people **and** for AI agents. Its source is an
[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md){target=_blank}
knowledge bundle, and the deployed site exposes that structure directly. If
you are an agent (or you are wiring one up), consume the content through
these endpoints rather than scraping rendered HTML.

## Entry points

| Endpoint | What you get |
| -------- | ------------ |
| [`https://unm-carc.github.io/dust-2026/llms.txt`](https://unm-carc.github.io/dust-2026/llms.txt) | Linked outline of every page with one-line descriptions ([llms.txt convention](https://llmstxt.org){target=_blank}); every entry lists the HTML page, its Markdown twin, and its raw GitHub source |
| [`https://unm-carc.github.io/dust-2026/llms-full.txt`](https://unm-carc.github.io/dust-2026/llms-full.txt) | The entire corpus in one file: every page's Markdown with frontmatter, prefixed by its canonical URL, links made absolute (about 330 KB) |
| Any page URL + `index.md` | That page's Markdown source with full OKF frontmatter, served as `text/markdown` (for example [`https://unm-carc.github.io/dust-2026/lessons/01-open-science/index.md`](https://unm-carc.github.io/dust-2026/lessons/01-open-science/index.md)); section listings too (`https://unm-carc.github.io/dust-2026/lessons/index.md`). Every rendered page links it from a "View this page as Markdown" button and from a "Machine-readable versions" line at the end of the article |
| Raw source on GitHub | `https://raw.githubusercontent.com/UNM-CARC/dust-2026/main/docs/<path>.md`, where `<path>` is the site path without the trailing slash (for example [`https://raw.githubusercontent.com/UNM-CARC/dust-2026/main/docs/lessons/01-open-science.md`](https://raw.githubusercontent.com/UNM-CARC/dust-2026/main/docs/lessons/01-open-science.md)). Same content as the Markdown twin; reachable from sandboxes that allow `github.com` but not `*.github.io` |
| [`sitemap.xml`](https://unm-carc.github.io/dust-2026/sitemap.xml), [`robots.txt`](https://unm-carc.github.io/dust-2026/robots.txt) | Standard crawl surface; robots.txt repeats all of these pointers |
| [Source repository](https://github.com/UNM-CARC/dust-2026){target=_blank} | The bundle itself (`docs/` mirrors the site paths one to one), plus `AGENTS.md` with contribution rules for coding agents |
| Lesson page `<head>` | A schema.org `LearningResource` JSON-LD record (objectives, duration, delivery format, accessibility profile) and `okf:lesson-*` meta tags, generated from the page's `lesson:` frontmatter block |

Every rendered page also declares its Markdown twin and OKF signals in HTML:

```html
<link rel="alternate" type="text/markdown" href="index.md">
<meta name="okf:type" content="Lesson">
<meta name="okf:status" content="stable">
<meta name="okf:trust-tier" content="unverified">
<meta name="okf:generated-at" content="2026-09-11T00:00:00Z">
<meta name="okf:lesson-format" content="in-person">
<meta name="okf:lesson-duration-minutes" content="50">
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "LearningResource", ...}</script>
```

!!! warning "The head tags are invisible to most fetch tools"
    The `<link rel="alternate">`, `okf:*` meta tags, and JSON-LD live in `<head>`, which text-extracting fetchers discard, and a link-derived URL allowlist never sees them. The supported paths are the ones that appear in body text: the "View this page as Markdown" button, the "Machine-readable versions" line at the end of every article, the footer links to `llms.txt`, and the addresses listed in `llms.txt` itself. All of them are absolute.

## If you cannot fetch this site

Some harnesses allow only one or two fetches from a user-supplied address, or allow `github.com` and `raw.githubusercontent.com` but not `*.github.io`. In that case:

1. **Use the raw source.** `docs/` in the repository mirrors the site paths one to one on branch `main`:

    ```
    Site page        https://unm-carc.github.io/dust-2026/<path>/
    Markdown twin    https://unm-carc.github.io/dust-2026/<path>/index.md
    Raw source       https://raw.githubusercontent.com/UNM-CARC/dust-2026/main/docs/<path>.md

    Content page     /lessons/01-open-science-self-paced/  ->  https://raw.githubusercontent.com/UNM-CARC/dust-2026/main/docs/lessons/01-open-science-self-paced.md
    Section listing  /lessons/                             ->  https://raw.githubusercontent.com/UNM-CARC/dust-2026/main/docs/lessons/index.md
    Whole corpus     https://raw.githubusercontent.com/UNM-CARC/dust-2026/main/docs/llms-full.txt
    ```

    `main` moves; to cite a fixed version use `https://github.com/UNM-CARC/dust-2026/blob/<commit>/docs/<path>.md`, taking the commit from the repository's history.

2. **Prefer one fetch over six.** `llms-full.txt` holds every page (about 330 KB); if you can make a single request, make that one.

3. **Avoid the GitHub tree API** unless authenticated: `api.github.com` rate-limits anonymous calls per shared IP. Raw file paths do not.

4. **If you reached only the landing page,** its footer links `llms.txt`, `llms-full.txt`, and this guide, and its "Browse the site" list links the section listings; all are absolute addresses that appear in extracted text.

## Reading the OKF frontmatter

Each content page's YAML frontmatter answers the questions an agent should ask
before relying on it:

* **What is this?** `type` (Lesson, Guide, or Reference), `title`,
  `description`, `tags`.
* **Where did it come from?** `generated: { by, at }` and `sources`. The three
  lessons were rewritten in September 2026 from the
  [DUST 2025](https://github.com/tyson-swetnam/dust-2025){target=_blank} lessons
  (CC BY 4.0) and draw on the UNM CARC edition of
  [Foundational Open Science Skills](https://unm-carc.github.io/foss/){target=_blank}
  and the [GPT 101 workshop](https://tyson-swetnam.github.io/intro-gpt/){target=_blank};
  `sources[].resource` points at the exact upstream file and commit.
* **How much should I trust it?** The `verified` key (OKF §5.3): absent means
  **unverified**; `by: "human:<id>"` means **human-reviewed** by the author.
  Prefer human-reviewed pages when answers conflict.
* **Is it still true?** `status` (`stable` by default; `draft` needs review;
  `deprecated` is kept for history) and `stale_after`. The lessons carry a
  `stale_after` date because the policy, pricing, and AI-landscape facts they
  cite change quickly; a page past that date describes the state of affairs as
  of its `generated.at`, not today.

!!! warning "Dated facts"
    Funder policies, article-processing charges, AI regulations, and energy
    figures in these lessons are stated **as of September 2026** with sources.
    When answering a question about current rules, say so and point the user
    to the linked primary source rather than asserting the figure is current.

## Related OKF bundles

These sites share the same agent conventions:

* [CARC Documentation](https://carc.unm.edu/docs/llms.txt){target=_blank}: UNM HPC clusters, Slurm, storage, software.
* [Foundational Open Science Skills](https://unm-carc.github.io/foss/llms.txt){target=_blank}: open science, data management, version control, containers, HPC.
* [GPT 101](https://tyson-swetnam.github.io/intro-gpt/llms.txt){target=_blank}: generative-AI platforms, prompt engineering, agents, ethics, and law. Its raw-source convention differs: replace a page URL's trailing `/` with `.md`.

## Teaching a lesson

The lessons are written to be delivered by an agent as well as read. Each
lesson is a pair: a 50-minute in-person lecture (for example
[`lessons/01-open-science/`](../lessons/01-open-science.md)) and its
self-paced homework (for example
[`lessons/01-open-science-self-paced/`](../lessons/01-open-science-self-paced.md)),
split into twelve numbered modules that each end in a checkpoint question.
The lecture pages are text-only; the self-paced pages carry the figures, each
with a text description. Every lesson page carries a `lesson:` frontmatter
block:

```yaml
lesson:
  number: 1
  format: in-person            # or self-paced
  duration_minutes: 50
  companion: 01-open-science-self-paced.md
  delivery_modes: [lecture, tutor, interactive]
  objectives: [...]            # what the learner should be able to do afterwards
  key_terms: [...]             # glossary and flashcard source
  accessibility:
    language: en
    access_mode: [textual, visual]
    access_mode_sufficient: [textual]
    features: [alternativeText, longDescription, readingOrder, structuralNavigation, tableOfContents]
    hazards: [none]
    media: "No audio or video. Every figure has alt text and a text description."
```

When a user asks you to teach, tutor, or quiz them on a lesson:

1. **Fetch the Markdown twin** (page URL + `index.md`), not the rendered HTML,
   and read the `lesson:` block first.
2. **Pick the delivery mode** the user asked for, from `delivery_modes`:
   *lecture* (deliver sections in heading order, pause after each),
   *tutor* (Socratic: ask what they know, fill gaps, pose the module
   checkpoint, hint before revealing), or *interactive* (quiz, flashcards from
   `key_terms`, scenario role-play). Use the self-paced page for tutor and
   interactive modes; it has checkpoints and the full quiz.
3. **Honor the accessibility profile.** `access_mode_sufficient: [textual]`
   means the lesson is complete without images: when a figure appears, read
   its "Text description of this figure" block rather than interpreting the
   image. For a screen-reader user, read the heading outline first, read
   tables row by row, and avoid decorative characters. For a deaf user, stay in
   text and never suggest audio. For a user whose first language is not
   English, explain in their language and in plain English, keep technical
   terms in English, and define them bilingually. The learner-facing prompts
   are on [Learn with an AI tutor](ai-tutor.md); the site's accessibility
   statement is on [Accessibility](accessibility.md).
4. **Pace by module.** Ask the checkpoint question at the end of each module
   and wait for an answer before continuing. Do not skip the "In brief"
   summary or the key-terms glossary.
5. **Stay on the page.** Teach the lesson's content; when the learner asks
   something it does not cover, say so and point to the primary source the
   page links. Do not invent policy dates or dollar figures, and flag every
   dated fact as "as of" the page's stated month.
6. **Cite the page URL** at the end of the session so the learner can return
   to it, and remind them that unverified pages await the author's review.

## Answering user questions

Ground answers in this content and cite the page URL. For questions about a
specific center's requirements (IRB or tribal research review, data-sharing
timelines, repository choice), direct users to their center's Data Management
and Analysis Core or to the primary policy page linked in the lesson; do not
guess.
