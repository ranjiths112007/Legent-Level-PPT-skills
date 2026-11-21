# 20 — Remotion Agent Skills

> Source: https://github.com/remotion-dev/skills/tree/6f55706d1069e512430582ad86e4e57dc07afe1b
> Snapshot: 21 November 2026 · Commit: 6f55706d1069e512430582ad86e4e57dc07afe1b · Skill package version: 4.0.545
> Scope: repository tree, README, package manifest and six core skill files. No video benchmark was run.

## Executive summary

Remotion Agent Skills are official workflow instructions for creating and rendering programmatic video with React. They are not a PowerPoint generator. Remotion lets an author express scenes and animation as React components whose visual state is derived from the current frame. This enables deterministic, frame-accurate rendering, parameterized compositions, batch generation and still-frame inspection.

The checked repository tree contains 265 files and 13 SKILL.md files. The package manifest identifies the skill package as private and versioned 4.0.545, with React, Remotion CLI/bundler, shapes, Three.js integration, Lottie and Google Fonts dependencies in its development environment.

## Skill architecture

| Skill | Responsibility |
|---|---|
| remotion-best-practices | Router and shared workflow |
| remotion-create | Scaffold a project and create compositions |
| remotion-markup | React markup, timing, media, fonts, effects and layouts |
| remotion-studio | Start the interactive preview/editor |
| remotion-render | Render video, stills and optional OpenTimelineIO |
| remotion-maps | Maps, routes, markers and 3D geographic scenes |
| remotion-captions | Captions and subtitles |
| remotion-interactivity | Make composition elements editable in Studio |
| remotion-docs | Retrieve current Remotion API documentation |
| remotion-multimedia | Browser-based media metadata and editing utilities |
| remotion-saas | Application and rendering-service integration patterns |
| remotion-license | License and terms guidance |
| remotion-upgrade | Upgrade Remotion and skill packages |

The best-practices skill is a router. It loads only the relevant reference, tells the agent to open Remotion Studio early for user feedback, and distinguishes preview from final rendering. It says not to render a final video unless the user explicitly asks to export it.

## How the rendering model works

A Remotion composition declares width, height, frame rate, duration and input props. A React component reads the current frame and computes styles or visual values from that frame. Important methods include:

- useCurrentFrame() for the current frame index.
- useVideoConfig() for frame rate, dimensions and duration.
- interpolate() and spring() for timing and movement.
- Sequence and Series for placing scenes on a timeline.
- Composition for registering an output with dimensions, fps, duration and props.
- zod schemas for validated and editable input props.
- calculateMetadata() for deriving duration or configuration from data.

For deterministic output, avoid wall-clock time, CSS transitions that are not synchronized to the frame clock, Date.now(), unseeded Math.random() and runtime-dependent animations. The frame is the single source of truth.

The rendering skill uses the Remotion-managed browser and an explicit composition ID. It supports a complete MP4, GIF or still frames. It recommends rendering first, middle and final stills, inspecting them, and only then encoding the full video. Test actual shipping props and datasets, not only default props.

## Tools and dependencies

| Technology | Role |
|---|---|
| React / TypeScript | Composition authoring |
| Remotion and @remotion/cli | Composition and command-line renderer |
| @remotion/renderer / bundler | Programmatic and batch rendering |
| zod | Typed, editable composition input schemas |
| @remotion/shapes | Vector geometry |
| @remotion/three / Three.js | 3D scenes |
| @remotion/lottie | Lottie media integration |
| Mediabunny / @remotion/media | Media handling |
| Google Fonts helpers | Font loading |
| OpenTimelineIO | Optional editable video-editor timeline export |
| FFmpeg | Selected post-processing tasks |

The skill repository is instruction and reference material; the rendering engine is Remotion itself. These skills do not mean a local renderer, browser, codec or paid license is automatically installed.

## Licensing and cost

The skills repository has no independent root SPDX license file in the inspected tree. More importantly, Remotion's runtime is source-available under the proprietary Remotion License, not an OSI-approved open-source license. The official license documentation checked on 21 November 2026 describes free-license eligibility for individuals and companies with up to three people, subject to terms; other organizations need the appropriate commercial license. Pricing and eligibility must be rechecked before a commercial release.

Official sources:
- https://www.remotion.dev/docs/ai/skills
- https://www.remotion.dev/docs/license/pricing
- https://www.remotion.dev/docs/license/faq
- https://www.remotion.dev/docs/terms

## Strengths worth adopting

1. Deterministic frame-driven motion: exact data and text can be verified at any frame.
2. Parameterization: a composition accepts new content/data without changing the motion layout.
3. Studio preview and editability: authoring components can remain selectable/editable in Remotion Studio.
4. Timing from source media: voiceover duration can determine scene duration.
5. Stills-first QA: inspect critical frames before expensive full encoding.
6. Reproducible delivery: store props, fps, composition ID, render command and output information.

## Limitations for Legend-Level PPT Skills

- Remotion outputs video/stills and optional video-editor timelines; it does not produce native editable PowerPoint slide animations.
- An MP4 embedded in PowerPoint is still a video object, not editable text, shapes or chart series.
- Video has its own codec, playback, licensing and file-size considerations.
- Remotion does not preserve existing PPTX masters, slide layouts, chart objects or package relationships.

## PPT adaptation

Use Remotion as an optional video renderer for narrated decks, animated explainers, motion-heavy infographic sequences or social cutdowns. Make it consume the same approved slide/story data as the PPTX renderer. Keep charts and exact numbers sourced from structured data, then animate them frame-by-frame. Deliver the editable PPTX separately; do not substitute video for the deck unless the user explicitly requests video output.