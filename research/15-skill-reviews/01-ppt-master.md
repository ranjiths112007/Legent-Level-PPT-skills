# Skill Review 01 — PPT Master

- Repository: https://github.com/hugohe3/ppt-master
- Skill source: https://github.com/TerminalSkills/skills/tree/main/skills/ppt-master
- Declared skill license: Apache-2.0; verify bundled dependency licenses before redistribution.
- Reviewed: 2026-11-21. Evidence: primary SKILL.md.

## Purpose
A coding-agent workflow to convert source documents into native/editable PowerPoint, edit existing decks, or derive reusable templates from reference decks.

## Contents
- SKILL.md routing, interaction, generation, edit and template workflows.
- Python project and scripts for source conversion, project setup, image sourcing/generation and export.
- Template library for brands, styles, layouts and decks.
- References for canvas formats, routing and constraints.
- Optional browser preview/editing and annotations.
- Image backends and web-image search adapters.
- Optional transitions, OOXML animations and speaker-note narration.

## Agent workflow
1. Convert PDF/DOCX/HTML/EPUB/notebook/Markdown/URL/text to Markdown.
2. Agree design specification: canvas, page count, template and audience.
3. Select layouts and author each slide as SVG.
4. Convert supported SVG primitives into native PowerPoint shapes/text. Charts/tables may be shape-based by default or native chart/table objects when requested.
5. For existing PPTX, plan pages to select/reorder/repeat/omit and edit planned pages; project claims unchanged pages can be restored byte-for-byte.
6. Create reusable brand/style/layout/deck templates from reference PPTX.
7. Optionally source user images, AI images or web images; add attribution for some licensed sources.
8. Render and quality-check; optionally add animation/narration.

## Strengths
- Three explicit modes: generate, edit native PPTX, create template.
- Clear source conversion and project structure.
- Native shapes avoid default flattened slides.
- Optional image pipeline, live preview and annotations.
- Calls out model/context limits, privacy and licensing.

## Weaknesses and risks
- Model-dependent; first draft still needs polishing.
- Default charts/tables may be shape-based, not data-backed native objects.
- Animation behavior varies across PowerPoint, Keynote, WPS and LibreOffice.
- Dependencies and provider keys increase setup complexity.
- PDF path includes PyMuPDF with AGPL license; dependency license matters.
- Byte-for-byte preservation claim needs independent package comparison.
- Preview/edit workflow needs security and stability tests.

## Best fit
Document-to-deck conversion, branded deck updates and reusable template extraction.

## Ideas to adopt
Explicit generate/edit/template routing; separate source conversion from construction; project artifact folders; template extraction; image provenance; tests for template preservation and chart editability.

Do not copy scripts, assets or templates without reviewing their licenses and dependencies.