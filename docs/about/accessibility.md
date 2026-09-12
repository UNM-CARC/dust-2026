---
title: "Accessibility"
description: "Accessibility statement for DUST 2026: what the site provides for screen-reader users, deaf and hard-of-hearing learners, and learners whose first language is not English, how to use it with AI assistants, known limitations, and how to report a barrier."
type: Guide
tags:
  - About
  - Accessibility
  - AI agents
generated:
  by: "claude/fable-5-1"
  at: "2026-09-12T02:00:00Z"
sources:
  - id: wcag22
    resource: "https://www.w3.org/TR/WCAG22/"
    title: "Web Content Accessibility Guidelines (WCAG) 2.2"
    author: "team:w3c"
  - id: schema-accessibility
    resource: "https://www.w3.org/community/reports/a11y-discov-vocab/CG-FINAL-vocab-20230718/"
    title: "Accessibility Discoverability Vocabulary for Schema.org"
    author: "team:w3c"
  - id: foss-training
    resource: "https://github.com/UNM-CARC/dust-2026/blob/main/docs/about/training.md"
    title: "DUST 2026: About this training (Accessibility First)"
    author: "human:tswetnam"
status: stable
---

# Accessibility

We want every Superfund Research Program trainee to be able to use this training, including people who are blind or have low vision, people who are deaf or hard of hearing, people with cognitive or motor disabilities, and people whose first language is not English. This page says what the site provides, how to use it with assistive technology and with AI assistants, what we know is still missing, and how to tell us about a barrier.

## Our target

We aim to meet [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/){target=_blank} at level AA. The site has not yet been audited by a third party; the author checks pages with keyboard-only navigation, a screen reader, and browser accessibility tools. Pages rewritten by an AI agent are marked unverified until the author reviews them (see [For AI agents](ai-agents.md)).

## What the site provides

**Structure and navigation**

- Every page has one `H1` and a strict heading hierarchy, so a screen reader's headings list is a working outline. The "On this page" table of contents mirrors it.
- A "Skip to content" link is the first focusable element on each page. All navigation, search, the light and dark mode switch, and every quiz or figure description work with the keyboard alone, and focused elements show a visible outline.
- Collapsible content (quiz answers, checkpoints, figure descriptions, reference blocks) uses the native HTML `details` and `summary` elements, which screen readers announce as expandable buttons.
- Tables carry header rows. Layout tables are not used; lists of terms use definition lists.
- The page language is declared as English (`lang="en"`), so screen readers and translation tools pick the right voice and dictionary.

**Images and media**

- Every image has alternative text, and every figure in the lessons is followed by a collapsible **"Text description of this figure"** that states everything the picture shows. The lecture pages contain no images at all. The arrow that marks external links is hidden from screen readers.
- The lessons contain **no audio and no video**. If we add a video, it will carry captions and a transcript.

**Language and reading**

- Each lesson opens with an **"In brief"** plain-language summary in short sentences.
- Acronyms are expanded on first use and defined as abbreviations, so hovering or focusing them shows the full term; a **Key terms** glossary closes each lesson.
- Sufficient color contrast in both light and dark mode, no information conveyed by color alone, and animation disabled when your system asks for reduced motion.
- Print styles produce a clean paper copy with link addresses written out.

**Machine-readable formats**

- Every page is available as plain Markdown by adding `index.md` to its address (for example [`https://unm-carc.github.io/dust-2026/lessons/01-open-science/index.md`](https://unm-carc.github.io/dust-2026/lessons/01-open-science/index.md)), or through the "View this page as Markdown" button beside "View source", and the whole site is one file at [`llms-full.txt`](https://unm-carc.github.io/dust-2026/llms-full.txt). Many screen readers, Braille displays, translation services, and AI assistants handle plain text better than a styled web page.
- Each lesson page declares its accessibility profile in machine-readable form: a `lesson.accessibility` block in its Markdown frontmatter and a [schema.org `LearningResource`](https://schema.org/LearningResource){target=_blank} record in the page head with `accessMode`, `accessModeSufficient`, `accessibilityFeature`, `accessibilityHazard`, and `accessibilitySummary`, following the [W3C accessibility discoverability vocabulary](https://www.w3.org/community/reports/a11y-discov-vocab/CG-FINAL-vocab-20230718/){target=_blank}. Learning platforms, search engines, and AI tutors can read these to choose how to present a lesson.

## Using the site with an AI assistant

AI assistants (Claude, ChatGPT, Gemini, NotebookLM, and the assistants built into screen readers and phones) can adapt these lessons to how you learn. The [Learn with an AI tutor](ai-tutor.md) page has copy-and-paste prompts. In short:

**If you are blind or have low vision**

- Give the assistant the Markdown address of the lesson (page address plus `index.md`) rather than the web page. It gets the same headings, tables, and figure descriptions without the layout.
- Ask it to read the heading outline first, then one section at a time, and to read the "Text description of this figure" block whenever a figure appears rather than describing the image itself.
- Voice modes in the Claude, ChatGPT, and Gemini apps let you take the whole lesson by conversation.

**If you are deaf or hard of hearing**

- Nothing in the lessons requires hearing. If an instructor records the in-person lecture, ask for the captioned recording or the transcript; the lecture page is the written script of that session.
- In an AI tutor, stay in text mode and ask for a written quiz and written feedback.

**If English is not your first language**

- Your browser can translate any page (in Chrome: right-click, "Translate to..."). The Markdown version translates cleanly too.
- Ask an AI tutor to explain each section in your language and in English side by side, to keep the technical terms in English (they are what you will see in NIH and journal policies), and to define each key term in both languages. The [prompt is on the AI tutor page](ai-tutor.md#learners-whose-first-language-is-not-english).
- The UNESCO definition of open science in Lesson 1 includes "multilingual" on purpose: research shared with Spanish-speaking border communities or Diné-speaking Navajo communities is part of what open science means.

!!! warning "AI assistants make mistakes"
    An AI tutor can misread a table, invent a policy date, or drop a caveat. The lessons carry dated facts with primary-source links; when a date or dollar figure matters, check the link. [Lesson 3](../lessons/03-ai-ethics.md) covers how to use AI responsibly in research.

## Known limitations

- Four images load from third-party sites (the open-access and OER logos and the xkcd comic in Lesson 1, the 1956 Dartmouth photograph in Lesson 3); their text descriptions are on our page, but the images themselves may not load if those sites are blocked.
- The file-naming examples in Lesson 2 are code blocks; screen readers read them character by character, so each is preceded by the pattern in prose.
- Linked external sites (publishers, agencies, repositories) are outside our control and vary in accessibility.
- Search results and the light/dark switch come from the site theme ([Zensical](https://zensical.org){target=_blank}); we report theme-level barriers upstream.
- The site is in English. We welcome community translations under the CC BY 4.0 license.

## Report a barrier

If something on this site does not work for you, tell us and we will fix it or provide the content another way:

- Open an [issue on GitHub](https://github.com/UNM-CARC/dust-2026/issues){target=_blank} (say which page and what assistive technology you use)
- Email [tswetnam@unm.edu](mailto:tswetnam@unm.edu)

Trainees can also contact their university's accessibility office: [UNM Accessibility Resource Center](https://arc.unm.edu/){target=_blank}, [University of Arizona Disability Resource Center](https://drc.arizona.edu/){target=_blank}, [Texas A&M Disability Resources](https://disability.tamu.edu/){target=_blank}.

*[WCAG]: Web Content Accessibility Guidelines
*[OER]: Open educational resources
*[NIH]: National Institutes of Health
*[UNM]: University of New Mexico
