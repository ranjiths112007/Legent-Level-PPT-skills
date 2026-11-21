# Skill Review 02 — PPT Generator (ddpie)

- Repository: https://github.com/ddpie/agent-skills
- Skill: https://github.com/ddpie/agent-skills/blob/main/content/ppt-generator/SKILL.md
- License: not established from reviewed skill file; verify before reuse.
- Reviewed: 2026-11-21. Evidence: primary SKILL.md.

## Purpose
Generate professional PPTX by authoring SVG pages and converting SVG primitives into native editable PowerPoint shapes.

## Contents
Eight themes: dark_warm, ai_ops, cloud_orange, consultant, tech_blue, smart_red, exhibit and pixel_retro; SVG design specs and page templates; 640+ SVG icons; 30+ chart/diagram references; SVG compatibility rules; scripts for finalization, icon embedding and conversion; optional cross-review.

## Agent workflow
1. Confirm topic, slide count/duration and style.
2. Propose outline and wait for approval.
3. Read theme design spec and reference SVGs.
4. Author cover, ending, chapter and content SVGs on fixed 1280×720 canvas.
5. Replace icon placeholders with vector paths and finalize SVG.
6. Build charts/diagrams from SVG primitives.
7. Convert text, rectangles, circles, lines and paths into native DrawingML objects.
8. Optionally review narrative, audience fit, domain accuracy, content and visuals; fix and regression-check.

## Strengths
Deterministic theme specs; large icon/chart library; explicit SVG compatibility subset; outline approval; action titles; optional multi-perspective review; editable native shape conversion.

## Weaknesses and risks
Requires Python and shell execution; strict SVG subset; tables manually built from shapes rather than semantic native tables; fixed canvas/fill-page rule can encourage density; installation paths need testing; simulated reviewer roles are not independent domain experts; no benchmark result established.

## Best fit
Consistent decks in a chosen theme, especially technical/business/data presentations.

## Ideas to adopt
Theme-specific specs, SVG compatibility checks, reusable icon/chart catalog, outline approval, native shape conversion, reviewer roles plus regression check.

## Improvement opportunity
Add semantic native charts/tables, source-to-value traceability, renderer QA, accessibility and measurable reviewer reliability.