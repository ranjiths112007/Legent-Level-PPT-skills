# 19 — GreenSock / GSAP Agent Skills

> Source: https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760
> Snapshot: 21 November 2026 · Commit: aed9cfd3277740755f6bfc1155c7aa645403b760 · Root license: MIT
> Scope: repository tree, README, eight SKILL.md files and example projects. No runtime benchmark was run.

## Executive summary

GSAP Skills is the official agent-instruction pack for GreenSock Animation Platform. It is a focused technical knowledge base: eight specialist skills teach an agent to use core tweens, timelines, ScrollTrigger, plugins, utilities, React integration, other frameworks and performance practices.

The repository is not an animation renderer or PowerPoint generator. The actual runtime is the GSAP JavaScript package. The skill files reduce API misuse and encode patterns such as timeline sequencing, scoped selectors, cleanup, transform-first animation and reduced-motion handling.

## Inventory and architecture

The checked tree contains 44 files (about 146 KB), including eight SKILL.md files, an agent index, Copilot instructions, Claude/Cursor plugin metadata and small examples for vanilla JavaScript, React, Vue and Nuxt.

| Skill | Responsibility |
|---|---|
| gsap-core | Tweens, easing, stagger, defaults, matchMedia and core CSS/SVG properties |
| gsap-timeline | Sequencing, labels, nested timelines, position parameters and playback |
| gsap-scrolltrigger | Scroll-linked animation, pinning, scrubbing, trigger positions and refresh |
| gsap-plugins | SplitText, Flip, Draggable, Inertia, MotionPath, MorphSVG, DrawSVG and other plugins |
| gsap-utils | Clamp, mapRange, normalize, interpolate, random, snap, wrap, selector and utility functions |
| gsap-react | useGSAP, refs, context scoping, cleanup and SSR boundaries |
| gsap-frameworks | Vue/Svelte lifecycle, mounted/unmounted cleanup and scoped selectors |
| gsap-performance | Transform/opacity preference, batching, stagger, quickTo and bounded concurrent work |

The structure uses small skills with explicit activation conditions and references to related skills. GitHub Copilot needs its own repository/path-specific instructions; it does not automatically load Claude/Cursor skill files.

## Main engineering method

A single tween is appropriate for one action; a timeline is preferred when several actions must be sequenced, overlapped, labelled, reversed or scrubbed. Position parameters and labels make timing intent readable instead of hiding it in chained delays.

Framework integrations address lifecycle safety. React uses the useGSAP hook, a component scope/ref and context-safe callbacks. Vue and Svelte create animations after mount and revert the GSAP context on unmount. Server-rendered frameworks must not execute browser animation code during SSR. Plugins must be registered before use.

The performance skill advises using transforms and opacity instead of animating width, height, top, left, margin or padding when the same result can be achieved without layout changes. It also warns against setting will-change everywhere and creating too many simultaneous tweens.

The core skill addresses prefers-reduced-motion through gsap.matchMedia(), and calls for responsive behavior and cleanup when media-query conditions change.

## Tools and dependencies

| Technology | Role |
|---|---|
| GSAP npm package | Animation runtime |
| @gsap/react | React lifecycle integration |
| JavaScript / TypeScript | Authoring |
| Vite | Example-project dev server |
| Vue / Nuxt | Non-React framework examples |
| SVG | Vector-path animation, morphs and drawing effects |
| Skills CLI and plugin manifests | Agent distribution |
| GitHub Copilot instructions | Copilot-specific guidance |

The repository examples have their own package manifests. The skill repository itself is primarily documentation and examples, not a bundled standalone application. Its README states that GSAP and its plugins are free for commercial use following Webflow's acquisition; verify the current GSAP terms before relying on that for a product release.

## Strengths worth adopting

1. Timeline-based choreography: define the sequence once, with labels, overlaps and reusable timing defaults.
2. Explicit motion API rules: skill activation and related-skill boundaries help agents select the right method.
3. Framework lifecycle discipline: scoped targets and cleanup avoid orphan animations in HTML previews.
4. Performance guidance: transform-first movement, batching and bounded active animations.
5. Accessibility: responsive media-query handling and reduced-motion behavior.
6. Progressive disclosure: load only the GSAP skill needed for the current problem.

## Limitations for Legend-Level PPT Skills

- GSAP targets browser DOM and SVG; it does not write native PowerPoint animation timing trees.
- A GSAP timeline is not the same as PowerPoint PresentationML timing.
- Browser animation can be exported as video or GIF, but that media is not individually editable PowerPoint content.
- ScrollTrigger is meaningful for web pages, not ordinary static slides.
- React/Vue lifecycle guidance belongs to an optional HTML preview/editor, not the core PPTX engine.

## PPT adaptation

Adopt choreography concepts, not GSAP as the primary PowerPoint runtime. Translate a reviewed sequence into a small set of supported PowerPoint entrance, emphasis and exit effects using a dedicated OOXML animation adapter. For complex scenes, offer an explicitly non-native MP4/GIF asset as an optional media fallback. Keep source content and numbers as native PowerPoint objects outside that media.

Useful source files:
- https://github.com/greensock/gsap-skills/blob/aed9cfd3277740755f6bfc1155c7aa645403b760/skills/gsap-core/SKILL.md
- https://github.com/greensock/gsap-skills/blob/aed9cfd3277740755f6bfc1155c7aa645403b760/skills/gsap-timeline/SKILL.md
- https://github.com/greensock/gsap-skills/blob/aed9cfd3277740755f6bfc1155c7aa645403b760/skills/gsap-react/SKILL.md
- https://github.com/greensock/gsap-skills/blob/aed9cfd3277740755f6bfc1155c7aa645403b760/skills/gsap-performance/SKILL.md