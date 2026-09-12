---
title: "Learn with an AI tutor"
description: "How to load a DUST 2026 lesson into Claude, ChatGPT, Gemini, or NotebookLM and take it as a lecture, a Socratic tutorial, or an interactive quiz, with prompts for screen-reader users, deaf learners, and learners whose first language is not English."
type: Guide
tags:
  - About
  - AI agents
  - Accessibility
  - Tutoring
generated:
  by: "claude/fable-5-1"
  at: "2026-09-12T02:00:00Z"
sources:
  - id: intro-gpt-tutoring
    resource: "https://tyson-swetnam.github.io/intro-gpt/tutoring/"
    title: "GPT 101: AI Tutoring, Student's Guide to Learning with AI"
    author: "human:tswetnam"
    last_modified: "2026-05-09T19:43:45Z"
  - id: dust-ai-agents
    resource: "https://github.com/UNM-CARC/dust-2026/blob/main/docs/about/ai-agents.md"
    title: "DUST 2026: For AI agents"
    author: "human:tswetnam"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# Learn with an AI tutor

The lessons on this site are written so that an AI assistant can teach them. Each lesson page carries a machine-readable `lesson` block (objectives, key terms, duration, delivery modes, accessibility profile), the self-paced pages are divided into modules with checkpoints, and every figure has a text description. Give an assistant the lesson and one of the prompts below, and it can deliver the lesson as a lecture, tutor you through it, or quiz you, in the form that suits how you learn.

!!! abstract "In brief"
    1. Copy the Markdown address of a lesson (the page address plus `index.md`).
    2. Paste it into Claude, ChatGPT, Gemini, or NotebookLM with one of the prompts on this page.
    3. Pick a mode: **lecture**, **tutor**, or **interactive**. Add an accommodation prompt if you use a screen reader, do not hear, or read English as an additional language.
    4. Check any date or dollar figure against the primary source linked in the lesson before you rely on it.

## Step 1: Give the assistant the lesson

Every page on this site has a plain Markdown twin at its address plus `index.md`. That version includes the lesson metadata and the figure descriptions and is what an AI should read.

| Lesson | Markdown address |
| --- | --- |
| Lesson 1 lecture (50 min) | `https://unm-carc.github.io/dust-2026/lessons/01-open-science/index.md` |
| Lesson 1 homework (self-paced) | `https://unm-carc.github.io/dust-2026/lessons/01-open-science-self-paced/index.md` |
| Lesson 2 | `https://unm-carc.github.io/dust-2026/lessons/02-data-management/index.md` |
| Lesson 3 | `https://unm-carc.github.io/dust-2026/lessons/03-ai-ethics/index.md` |
| The whole site in one file | `https://unm-carc.github.io/dust-2026/llms-full.txt` |

How to hand it over:

- **Claude, ChatGPT, Gemini:** paste the address into the chat. If the assistant cannot browse, open the address in your browser, select all, copy, and paste the text into the chat instead.
- **NotebookLM:** add the address as a website source, or upload the copied text. NotebookLM's audio overview is a listening option; it is not a substitute for the text for deaf learners.
- **Claude Projects or ChatGPT custom GPTs:** add `llms-full.txt` as a file so every lesson is available across conversations.

Tell the assistant which page you want if you use the full-site file.

## Step 2: Choose a mode

Each prompt below assumes you have already pasted the lesson address or text. Replace the bracketed parts.

=== "Lecture"

    Use this to hear the lesson delivered in order, the way an instructor would, with a pause for questions after each section.

    ```
    You are teaching me "Lesson 1: Foundations of Open Science" from the DUST 2026
    training. Read the page's lesson block (objectives, key terms, duration) and
    deliver the lesson as a lecture in the order of its headings. For each section:
    state the point in two or three sentences, give the Superfund example from the
    page (Arizona and New Mexico), and then stop and ask whether I have a question
    before moving on. Do not add facts that are not on the page; if I ask about
    something the page does not cover, say so and point me to the primary source
    the page links. When you reach the quiz, ask me each question and wait for my
    answer before revealing the page's answer.
    ```

=== "Tutor"

    Use this for Socratic tutoring: the assistant asks, hints, and checks your understanding, and does not lecture.

    ```
    Act as my tutor for "Lesson 1 homework: Open Science, self-paced" from the
    DUST 2026 training. Work through it one module at a time, in order. For each
    module: ask me what I already know about the topic, then explain only what I
    am missing, using the page's own definitions and examples. At the end of the
    module, give me its checkpoint question and wait for my answer. If I am wrong,
    give a hint, not the answer, and let me try again; reveal the page's answer
    only after my second try. Keep a short list of the key terms I struggled with
    and review them at the end. My field is [your field, e.g. inhalation
    toxicology / environmental chemistry / community-engaged exposure science],
    so choose the example closest to it when the page offers several.
    ```

=== "Interactive"

    Use this for practice: quizzes, flashcards, and scenario role-play built from the page.

    ```
    Using "Lesson 1 homework: Open Science, self-paced" from the DUST 2026
    training, build me an interactive session:
    1. Ten multiple-choice questions that cover all six pillars, the nine Gold
       Standard Science tenets, and the 2026 public-access and publication-cost
       rules. Ask one at a time, wait for my answer, then explain using the page.
    2. Flashcards for every term in the page's key_terms list, in random order.
    3. A role-play: you are the program officer reviewing my progress report and
       asking how my project meets Gold Standard Science; I answer; you grade my
       answer against the page's tenet table and tell me what a stronger answer
       would include.
    Keep score, and at the end tell me which modules to reread.
    ```

!!! tip "One page at a time"
    The lecture page is a 50-minute summary; the self-paced page is the full material. Tutor and interactive modes work best on the self-paced page because it has module checkpoints and the complete quiz.

## Step 3: Add an accommodation

Add one of these to any prompt above.

### Screen-reader users and learners who are blind or have low vision

```
I use a screen reader. Read from the Markdown version of the page, not a
screenshot. Start by reading me the heading outline so I know the structure.
Then go one section at a time and stop after each. Whenever the page has a
figure, read its "Text description of this figure" block in full instead of
describing the image yourself. Read tables row by row, naming the column
before each value. Spell out acronyms the first time you use them. Do not use
emoji, bullet symbols, or decorative characters in your replies.
```

If you prefer to listen and speak, the Claude, ChatGPT, and Gemini mobile apps have voice modes; use the same prompt and add "We are in voice mode; keep each turn under a minute of speech."

### Deaf and hard-of-hearing learners

```
I am deaf. Keep everything in text: do not suggest audio overviews, voice
mode, podcasts, or videos. If the page or your knowledge includes a video or
recording, give me its transcript or caption text, or tell me it has none.
Give written feedback on my quiz answers.
```

The DUST 2026 lessons contain no audio or video, so nothing is lost by staying in text. If your instructor records the in-person session, ask for the captioned recording; the lecture page is the script.

### Learners whose first language is not English

```
My first language is [language]. For each section, explain the idea first in
[language], then give the same explanation in plain English with short
sentences. Keep the technical terms in English (for example "accepted
manuscript", "article processing charge", "pre-registration"), because they
are the words I will see in NIH and journal policies, and define each one in
[language] the first time it appears. At the end of each module, give me a
two-column glossary of the module's key terms: English term, definition in
[language]. Ask me the checkpoint questions in English and let me answer in
either language.
```

Your browser can also translate the page directly (in Chrome, right-click and choose "Translate to..."), and the Markdown version translates cleanly.

### Learners who want a slower or a faster pace

```
Set the pace to [slow / fast]. Slow: one idea per message, a comprehension
question after each, and wait for me before continuing. Fast: one message per
module with only the key points and the checkpoint question.
```

## What the assistant is reading

Each lesson page's frontmatter includes a block like this, which an assistant can use to plan a session:

```yaml
lesson:
  number: 1
  format: in-person            # or self-paced
  duration_minutes: 50
  companion: 01-open-science-self-paced.md
  delivery_modes: [lecture, tutor, interactive]
  objectives: [...]
  key_terms: [...]
  accessibility:
    language: en
    access_mode: [textual, visual]
    access_mode_sufficient: [textual]
    features: [alternativeText, longDescription, readingOrder, structuralNavigation, tableOfContents]
    hazards: [none]
    media: "No audio or video. Every figure has alt text and a text description."
```

`access_mode_sufficient: [textual]` means the whole lesson can be understood from text alone; an assistant serving a blind learner can rely on that. The rendered page also carries the same information as a schema.org `LearningResource` record for platforms that read structured data. Instructions for agents are on [For AI agents](ai-agents.md#teaching-a-lesson).

## Use it well

!!! warning "Check the dates and the dollars"
    The lessons state policy facts "as of" a month, with a link to the primary source. An AI tutor may present a pending rule as final, drop a caveat, or invent a date. When a fact would change what you do (a deposit deadline, a budget line, a tribal review step), open the link.

- **Ask for understanding, not answers.** "Explain why the accepted manuscript satisfies NIH" teaches more than "what is the answer to quiz question 1".
- **Struggle first.** Try the checkpoint before asking for the hint.
- **Disclose AI use** in coursework if your program requires it, and never paste unpublished data, participant information, or tribal partners' data into a consumer AI service. [Lesson 3](../lessons/03-ai-ethics.md) covers AI privacy, disclosure, and integrity rules in detail.
- **Prefer an institutional account** (UNM, University of Arizona, and Texas A&M provide enterprise AI access) over a personal one for anything connected to your research.

More prompts and strategies, including study planning and hallucination checks, are in [GPT 101: AI Tutoring](https://tyson-swetnam.github.io/intro-gpt/tutoring/){target=_blank}.

*[NIH]: National Institutes of Health
*[UNM]: University of New Mexico
