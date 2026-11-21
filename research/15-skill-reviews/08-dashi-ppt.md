# Skill Review 08 — Dashi PPT

- Repository: https://github.com/chuspeeism/dashi-ppt-skill
- Skill: https://github.com/chuspeeism/dashi-ppt-skill/tree/main/skills/dashi-ppt
- License: repository reports AGPL-3.0; verify exact current license and obligations.
- Reviewed: 2026-11-21. Evidence: primary SKILL.md and repository metadata.

## Purpose
Generate browser-editable HTML presentations from multiple visual themes, with export to PPTX/PDF.

## Contents
- Main SKILL.md with JSON planning and a detailed production workflow.
- Built-in project/generator, themes and page compositions.
- Theme preview image/grid.
- Three template variants plus one agent-custom composition per logical slide.
- Content packs, layout inspection/query tools, media staging and asset validation.
- Rendering scripts for Windows and macOS/Linux.
- Local preview server and editable browser interface.
- Goal/plan validators and latest-version checker.

## Agent workflow
1. Extract title, goal, audience, owner, page count, focus and output.
2. Confirm theme pack and image intent.
3. Build page-content pack with one main information role per page.
4. Scaffold variants and validate the JSON plan.
5. Render local HTML deck.
6. Validate media paths and content, inspect four variants per logical slide.
7. Repair failing pages, rerender and revalidate.
8. Export editable PPTX or PDF through supported workflow.

## Strengths
- Multiple layout alternatives per slide make visual selection concrete.
- Separates canonical content from layout variants.
- Detailed rules prevent accidental template mutation and stale template text.
- Explicit media staging and asset checks.
- Structured JSON plan and validation.
- Local preview editing and export.
- Has a dedicated acceptance workflow.

## Weaknesses and risks
- Complex workflow and many specialized commands increase onboarding cost.
- Node.js 20+ and dependencies required.
- Browser preview/export requires its local server; static file viewing is not equivalent.
- Media workflow has strict constraints and can be confusing.
- Must be tested carefully on Windows vs macOS/Linux.
- AGPL-3.0 can impose source-sharing obligations when distributing modified covered software; obtain legal review for integration.

## Best fit
Users who want to compare several visual variants for each slide, then edit/export a browser-native deck.

## Ideas to adopt
Separate canonical content from layout projection; preview alternatives; structured media slots; validators for stale template copy; local preview; clear acceptance criteria.

## Improvement opportunity
Offer a simpler default path and a clearly named advanced mode; keep HTML editability and PPTX-native editability as separate claims.