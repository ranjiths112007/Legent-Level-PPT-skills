# 24 — FrankX AI / Awesome Motion Design Agent Skills

> Source: https://github.com/frankxai/awesome-motion-design-agent-skills/tree/e7dc6e2e728c918ffcea5edb2d7c94e2a6f7785d
> Snapshot: 21 November 2026 · Commit: e7dc6e2e728c918ffcea5edb2d7c94e2a6f7785d · Root license: CC0-1.0
> Scope: README, five primary SKILL.md files, quality rubrics and repository verification scripts.

## Executive summary

This repository combines five installable motion-agent workflows with a curated catalogue of external motion technologies and skill packs. It is not one animation engine. Its best contribution is a motion-stack selection and quality-governance layer: decide what the animation is for, choose the lightest suitable runtime, define reduced motion, implement, and prove the result with actual observations.

The checked tree contains 65 files (about 1.15 MB), five SKILL.md files, references, quality rubrics, Python release validators and tests. The repository is licensed CC0-1.0. Third-party tools and linked skill packs retain their own licenses; CC0 on the catalogue does not relicense external projects.

## Five installable skills

| Skill | Responsibility |
|---|---|
| motion-director | Choose a motion stack, define choreography/timing and reduced-motion behavior |
| site-motion-excellence-director | Establish first-read/static-frame quality, motion thesis, beat sequence and acceptance gate |
| web-motion-auditor | Audit keyboard, touch, reduced motion, interruption, resize, failure and performance |
| remotion-video-agent | Plan and render frame-driven videos, social cutdowns and scene sequences |
| generative-media-director | Route image/video generation, specify prompts, preserve provenance and quality-check outputs |

The motion director's runtime selection is practical: CSS for simple interaction; Motion for React UI/layout; GSAP for timelines/scroll/SVG/text; Rive for interactive state machines; Lottie/dotLottie for portable vector loops; Remotion for rendered video/GIF; and Three.js for 3D. This is a conditional decision tree, not a reason to install every library in one project.

## Quality and delivery contracts

The collection has two useful QA models.

### Motion quality rubric

A 0–3 rubric scores purpose, timing, hierarchy, brand fit, accessibility, performance and implementation quality. It requires evidence for scored categories and warns against animating everything, delaying usable content, moving text while the viewer is reading, scroll hijacking and missing reduced-motion support.

### Site motion excellence gate

A stricter 1–5 scorecard checks intent, the still frame, product specificity, hierarchy, choreography, timing, restraint, brand fit, usability, accessibility, runtime fit and evidence. Automatic failures include no reduced-motion route for substantial motion, generated text corruption, hidden controls, layout shifts, scroll traps or no visual proof.

The web auditor also requires interruption and recovery tests: open and close mid-transition, repeat actions rapidly, resize, navigate, switch motion preferences, and check that focus and cleanup remain correct. It distinguishes physical-device checks, emulated input, screenshots, video captures and source review; missing observations must remain unscored.

## Implementation and tooling

The repository does not bundle GSAP, Framer Motion, Remotion, Lottie, Rive or Three.js as one runtime. It curates their use and links to their source documentation and skills. Its own five skills are Markdown instructions; Python scripts validate repository packaging, release payloads, frontmatter and links.

The generative-media director stresses provider availability, terms, cost and authorization. It also preserves exact provenance: prompt, provider/model, source references, rights, date, output hash and review state. It says not to switch silently to paid tools.

## Strengths worth adopting

1. Static-frame gate: if the still frame is weak, animation will not rescue it.
2. Runtime selection: choose the smallest tool that meets the motion requirement.
3. Reduced-motion by design: preserve content, state and reading order.
4. Robust QA: test interruption, keyboard, touch, mobile, failure and actual rendered frames.
5. Evidence-based scoring: unobserved categories remain unscored.
6. Asset provenance: retain source, prompt, provider, model, output hash and rights notes.

## Limitations for Legend-Level PPT Skills

- Most audit instructions target websites and interactive UI, not static PPTX.
- The catalogue's external projects are not all vendored or licensed under CC0.
- The repository does not create native PowerPoint animation objects or edit arbitrary PPTX packages.
- A quality rubric is useful only when supported by actual rendered evidence; it does not replace PowerPoint-specific package and editability checks.

## PPT adaptation

Use motion-director as a runtime-selection policy for a future animation lane. Add a static-first gate, reduced-motion/static alternative, a simple scorecard and an evidence log. Preserve exact PowerPoint content outside generated video/media assets. Keep the native PPTX engine as the source of truth.