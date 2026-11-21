# Skill Review 06 — slides-skill (Rich627)

- Repository: https://github.com/Rich627/slides-skill
- Skill: https://github.com/Rich627/slides-skill/blob/main/SKILL.md
- License: not verified from the reviewed skill file; check repository LICENSE before reuse.
- Reviewed: 2026-11-21. Evidence: primary SKILL.md.

## Purpose
Generate editable 16:9 PPTX from a structured JSON deck specification. The model writes content; a deterministic renderer controls layout, color and typography.

## Contents
- SKILL.md with workflow and guardrails.
- JSON deck spec and examples.
- Build script based on PptxGenJS.
- 15 slide types: cover, section, cards, bullets, table, stats, flow, timeline, chart, image, quote, options, next, references and closing.
- Seven theme presets: gold, navy, forest, coral, violet, sky and mono.
- Storyline, slide-type and design-system reference docs.
- Render script and contact-sheet review workflow.

## Agent workflow
1. Establish purpose, audience and duration; read source material.
2. Choose storyline skeleton and theme.
3. Write action titles first; titles alone should tell the story.
4. Select a slide type per slide; avoid consecutive repeated types and overuse of bullets.
5. Populate JSON with content, source, notes and images.
6. Build PPTX through deterministic script.
7. Render every slide, inspect contact sheet and suspicious slides at full size.
8. Fix and rerender; deliver file plus storyline/source/remaining-check summary.

## Strengths
- Clean separation between semantic content and layout engine.
- Deterministic geometry and theme control.
- Action titles, source citations and references slide.
- Explicit limits on text and content per card.
- Render-based visual QA; estimator is correctly treated as a guess.
- Native editable shapes/text/charts.

## Weaknesses and risks
- Requires Node and local dependencies; visual QA requires LibreOffice and Poppler.
- A fixed set of 15 slide types may not cover every deck genre.
- Rebuilding a deck made by this skill is recommended; arbitrary existing PPTX editing is delegated to another skill.
- Theme and content limits can become rigid if not adapted to audience or localization.
- No independent benchmark results established.

## Best fit
Repeatable, structured decks where native editability and consistent output matter more than free-form layout.

## Ideas to adopt
JSON intermediate representation; deterministic renderer; action-title-first story; slide type variety; source fields; contact-sheet QA; separate estimation from actual rendering.

## Improvement opportunity
Add arbitrary template preservation, semantic chart data validation, accessibility metadata and flexible canvas support.