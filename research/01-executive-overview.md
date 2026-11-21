# Executive Overview

**Status:** Research thesis  
**Last reviewed:** 2026-11-21

## Product thesis

Build one reusable AI Agent Skill for presentation engineering. It guides an agent through the full lifecycle:

1. Understand audience, goal, sources, and constraints.
2. Extract and verify content and data.
3. Design a coherent narrative and slide outline.
4. Establish a design system (layout, colors, typography, spacing).
5. Select, create, and prepare visual assets.
6. Construct native, editable PowerPoint objects where practical.
7. Render the deck in a real presentation renderer.
8. Inspect content, visual quality, data integrity, accessibility, and compatibility.
9. Repair defects conservatively and rerender.
10. Deliver the editable deck with a transparent QA report.

## What it is not

- Not merely a prompt to make slides.
- Not a web-based slide editor.
- Not a collection of unrelated skills.
- Not an image-to-PPT converter that flattens every slide.
- Not a guarantee of perfect design or cross-platform rendering.

## Central promise

Help agents produce presentations that are understandable, visually coherent, factually faithful, editable, accessible, and verified to the extent tools permit.

## Differentiation hypotheses

Test these against existing skills:
- Source-to-slide traceability.
- Structured visual defect taxonomy and repeatable QA report.
- Semantic slide planning before object creation.
- Slide-specific layout selection.
- Consistent image direction across a deck.
- Spreadsheet-to-chart/data reconciliation.
- Reversible repairs that preserve the original deck.
- Explicit separation between automated checks and human judgment.

## Primary users

Analysts, business operations teams, consultants, managers, students, educators, startup founders, sales teams, researchers, and AI-agent builders.

## First release recommendation

Start with a measurable loop:

**Inspect existing PPTX → render every slide → detect defined layout defects → produce report → safely fix a narrow defect set → rerender and compare.**

Then add data verification, design intelligence, image workflows, and generation.

## Success metrics

- Reproducible detection precision/recall per defect class.
- Repairs fixing a defect without introducing another.
- Source-data mismatch detection accuracy.
- Editability retention.
- Render compatibility across declared environments.
- Time saved on representative tasks.
- User acceptance/manual correction rate.
- Accessibility detection coverage.
