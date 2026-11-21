# Skill Review 03 — AgentBuff Presentation

- Repository: https://github.com/nugrahalabib/AgentBuff-Presentation-Skills
- Skill: https://github.com/nugrahalabib/AgentBuff-Presentation-Skills/blob/main/SKILL.md
- License: MIT.
- Reviewed: 2026-11-21. Evidence: primary SKILL.md and README.

## Purpose
Create browser-native presentations, then export HTML, PDF, PNG/JPG and PPTX. Can convert existing PPTX into a web deck.

## Contents
Agent-agnostic SKILL.md; fixed 1920×1080 stage and base CSS; HTML template and animation patterns; style presets and optional bold templates; scripts for PPTX extraction, export and deployment; visual-style preview workflow.

## Agent workflow
1. Clarify purpose, length, source readiness, speaker-led vs reading-first density and output formats.
2. Show visual style previews instead of asking users to describe taste.
3. Build a single-file HTML deck as canonical source.
4. Keep each slide fixed at 16:9 / 1920×1080 and scale the stage uniformly.
5. Use CSS typography, backgrounds, motion and contextual styling.
6. Export PDF/PNG/JPG/PPTX from the same render.
7. Offer two PPTX modes: image-first (pixel-perfect, not editable) or editable native text/shapes (approximate fidelity).
8. Convert existing PPTX content to web presentation.

## Strengths
Agent-agnostic; excellent visual style discovery; anti-generic design principles; one canonical source; multiple exports; existing PPTX conversion; reduced-motion and fixed-stage rules.

## Weaknesses and risks
Default PPTX is a full-slide image; editable mode is approximate because fonts and wrapping drift. Fixed 16:9 is not universal. HTML animation may not survive static PDF export. Requires browser/Node/Playwright and Python for conversion. Pixel identity does not imply native editability.

## Best fit
Interactive web talks, style exploration, high-fidelity image-first exports and multi-format publishing when editability is secondary.

## Ideas to adopt
Style preview gallery; explicit fidelity-vs-editability choice; canonical source; speaker-led/reading-first density; reduced-motion support; honest trade-off disclosure.

## Improvement opportunity
Keep native editable PPTX as default for business workflows; retain HTML/image-first as an explicit alternate lane. Test editability and visual fidelity separately.