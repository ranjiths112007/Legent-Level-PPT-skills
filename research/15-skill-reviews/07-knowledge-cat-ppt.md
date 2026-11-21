# Skill Review 07 — Knowledge Cat PPT Skill

- Repository: https://github.com/gnipbao/knowledge-cat-ppt-skill
- Skill: https://github.com/gnipbao/knowledge-cat-ppt-skill/blob/main/SKILL.md
- License: verify the repository's current LICENSE before reuse.
- Reviewed: 2026-11-21. Evidence: primary SKILL.md and repository README.

## Purpose
A story-first presentation operating system that routes tasks to native PPTX, HTML, image-first PPTX or review-only workflows, then validates and repairs the output.

## Contents
- Main SKILL.md with task triage and modes.
- References for benchmark synthesis/quality gates, engine routing, story architecture, design systems, template replication, HTML production, native PPTX recipes, image-first recipes, QA rubric and open-source productization.
- JSON deck-plan schema and validator.
- HTML starter project and validator.
- Native PPTX builder, text extraction and editability checks/probes.
- Case/evidence verification scripts.

## Agent workflow
1. Triage deck type, stakes, source status, output lane and deadline.
2. Create a deck brief: audience, outcome, promise, scope, format, sources, style and QA level.
3. Build a narrative spine and ghost deck of action titles.
4. Create slide plan with role, message, evidence, visual, notes, sources and asset needs.
5. Route to native PPTX, HTML, image-first or review-only based on user needs.
6. Choose design system and build.
7. Validate plan/HTML/PPTX and inspect rendered slides.
8. Run at least one fix-and-verify loop for production work.
9. Deliver paths, assumptions, risks and next iteration point.

## Strengths
- Most comprehensive lifecycle and mode routing among this sample.
- Story before styling; audience outcome and evidence are central.
- Explicit distinction between native PPTX, HTML and image-first trade-offs.
- Extensive progressive-disclosure references.
- Plan validation, editability probes and QA scripts.
- Template replication and productization are addressed.
- Explicit rules against claiming visual quality from code alone.

## Weaknesses and risks
- Large reference surface and many scripts create complexity.
- Tool dependencies (including artifact-tool where used) vary by host.
- A rich documented workflow does not guarantee every route works in every agent environment.
- Quality-gate claims need independent benchmark replication.
- Need verify license and dependency terms before adopting code/assets.

## Best fit
Complex professional decks, benchmark-oriented generation, deck review/repair, template replication and multi-format workflows.

## Ideas to adopt
Audience-shift brief; story spine and action titles; explicit output-lane routing; source/evidence tracking; plan schema validation; editability probes; visual fix-and-verify; progressive disclosure.

## Improvement opportunity
Keep our own MVP much smaller: one robust workflow, one schema and a few validated scripts. Add advanced lanes only after reproducible tests.