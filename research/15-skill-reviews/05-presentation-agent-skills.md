# Skill Review 05 — Presentation Agent Skills

- Repository: https://github.com/hiamberhuang/presentation-agent-skills
- License: MIT (repository README).
- Reviewed: 2026-11-21. Evidence: primary README.

## Purpose
A modular pack for consulting narrative, PPTX creation, slide visuals, screenshot-based restoration and pre-send QA.

## Five included skills
1. consulting-deck-expert — strategy, board, proposal, business-case and consulting storylines.
2. pptx-generator — read/edit/generate editable PPTX using PptxGenJS/XML workflows.
3. slide-visual-director — cover images, section heroes, editorial visuals, conceptual illustrations and slide-safe image prompts.
4. ppt-pixel-restore — rebuild an existing PPT/HTML deck from screenshots using measured visual comparison and regression QA.
5. presentation-qa — pre-send audits for narrative, evidence, layout, rendering, assets and delivery readiness.

## Agent workflow
Compose skills by task: narrative first, generator for implementation, visual director for art direction, pixel restoration for reference matching, QA before delivery. Installer supports Codex/Claude destinations.

## Strengths
Clear responsibility separation; creation and restoration; dedicated image direction; QA as a separate stage; MIT license and installer.

## Weaknesses and risks
Not one monolithic engine; output depends on available tools. Screenshot restoration can reproduce appearance but cannot recover original semantic structure/data. Image provider access is not bundled. README scope is not benchmark evidence. Repository maturity/activity should be monitored.

## Best fit
Agent builders wanting modular narrative, implementation, art-direction, restoration and QA roles.

## Ideas to adopt
Modular skill/references; dedicated visual art director; measured screenshot comparison; separate QA skill; installer and third-party notices.

## Improvement opportunity
Define a shared deck-plan schema and provenance model so separate skills exchange consistent data.