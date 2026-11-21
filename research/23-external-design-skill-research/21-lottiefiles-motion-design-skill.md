# 21 — LottieFiles / Motion Design Skill

> Source: https://github.com/LottieFiles/motion-design-skill/tree/d77a9fc8cb371cab1ba5420df5bfd232cd14c9bb
> Snapshot: 21 November 2026 · Commit: d77a9fc8cb371cab1ba5420df5bfd232cd14c9bb · License: MIT
> Scope: README, primary SKILL.md and core director/reference documents. No rendered output was benchmarked.

## Executive summary

LottieFiles' Motion Design Skill is a technology-agnostic motion-director guide. It teaches an agent to decide why something should move, what emotion it should communicate, how the sequence should unfold, and which timing/easing rules fit the context before choosing CSS, Framer Motion, GSAP, Lottie or another implementation.

The repository contains 21 files and one primary SKILL.md, with supporting director, patterns and reference documents. It is not itself an animation engine. For actual MP4, GIF, WebM, dotLottie or Lottie JSON exports, its README directs users to the separate LottieFiles Creator MCP integration.

## Architecture and method

The main skill is organized around three pillars:

1. Emotional intent: define the desired feeling (calm, urgency, delight, confidence or elegance) before selecting motion properties.
2. Visual narrative: structure motion as setup → action → resolution.
3. Motion craft: choose believable timing, easing, path, follow-through and secondary motion.

It suggests three motion layers: primary (the focal action), secondary (supporting details such as a shadow or related icon) and ambient (quiet background movement). It also asks the agent to select one motion personality for a project: playful, premium, corporate or energetic. A small set of timing constants and one signature entrance pattern help establish recognizable motion identity.

## Timing, easing and choreography

The skill provides concrete starting ranges:

| Element | Suggested duration |
|---|---:|
| Micro-feedback | 80–120 ms |
| Button/toggle | 120–180 ms |
| Icon transition | 150–250 ms |
| Card entrance/exit | 200–350 ms |
| Modal/dialog | 300–400 ms |
| Page transition | 400–600 ms |
| Dramatic reveal | 600–1,200 ms |

It recommends easing by direction: ease-out for entrances, ease-in for exits, ease-in-out for on-screen motion and smooth sinusoidal curves for ambient loops. It encourages staggered sequences, consistent direction of travel, one primary focal point and restraint in the number of simultaneously moving elements.

The guide adapts Disney animation principles such as anticipation, staging, follow-through, arcs, slow-in/slow-out, secondary action and appeal. These are useful heuristics, not universal laws. Rigid rules (for example, always using three motion layers) should be treated as context-dependent advice rather than absolute requirements for a professional slide deck.

## Patterns and quality checks

Supporting references include entrance and exit recipes, state feedback, continuous/ambient motion, multi-element choreography, timing/easing tables, property selection, troubleshooting and a motion quality checklist. The checklist checks visual purpose, timing, hierarchy, emotional quality, technical performance and accessibility. It includes reduced-motion alternatives and warns against movement that hides information or overwhelms the viewer.

## Tools and dependencies

| Technology | Role |
|---|---|
| Markdown skill and references | Motion reasoning and reusable recipes |
| CSS / Web Animations | Web animation implementation examples |
| Framer Motion | Declarative React implementation option |
| GSAP | Timeline and high-control web animation option |
| Lottie / dotLottie | Portable vector-animation formats |
| Creator MCP | Optional render/export tool for animation files |

The skill itself is implementation-agnostic. Creator MCP is a separate dependency; availability and permissions must be checked before assuming the agent can export an animation file.

## Strengths worth adopting

1. Design intent before properties: define the motion's job and target emotion first.
2. Motion identity: maintain consistent easing and duration tokens.
3. Choreography: lead with the hero, stagger supporting content and use stillness as contrast.
4. Accessibility: design a reduced-motion experience, not merely a switch that removes all movement.
5. Reusable specification: define a motion brief independently of the implementation engine.

## Limitations for Legend-Level PPT Skills

- The default examples target UI animation and browser-based interactions.
- Lottie JSON/dotLottie and Creator MCP exports are not native editable PowerPoint shape animations.
- The skill does not inspect or edit PPTX files.
- UI duration tables must be adapted to slide pacing and presenter-led delivery; a 300 ms UI response is not a 300 ms slide transition requirement.
- It does not provide a native rendering or PowerPoint QA pipeline.

## PPT adaptation

Create a PowerPoint MotionSpec defining target slide/object IDs, trigger, order, duration, easing, delay, final state and static fallback. Apply motion only when it improves the narrative or progressive disclosure. Use native PowerPoint animations for supported simple effects; reserve Lottie/video assets for explicitly non-native visuals. Every slide must remain understandable when animation is disabled.