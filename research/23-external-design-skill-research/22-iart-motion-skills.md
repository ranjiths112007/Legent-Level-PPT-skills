# 22 — iArt / Motion Graphics Skills Collection

> Hub: https://github.com/iart-ai/motion-skills/tree/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f
> Snapshot: 21 November 2026 · Hub commit: e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f · Hub license: MIT
> Additional inspected packs: data-animation-skills, motion-design-skills and explainer-video-skills (all MIT at checked commits).
> Scope: hub README/tree, selected SKILL.md files in three linked packs, and verification scripts. The full advertised 56-skill collection was not exhaustively inspected.

## Executive summary

The submitted repository is a hub and discovery index, not a single repository containing 56 complete skills. Its README advertises 56 skills across 19 independently installable packs. The hub tree itself contains only 10 files, no SKILL.md files and a small set of utilities for showcasing and verifying rendered media.

The real value is in linked packs. Three relevant packs were inspected:

| Pack | Pinned commit | Files | Skill docs |
|---|---|---:|---:|
| data-animation-skills | 6570c0c4fbc9daa8d7ac1f1163a890352344206b | 21 | 3 |
| motion-design-skills | b85e50c4cef5ff17aa2187a10d49d2dae9226c74 | 47 | 9 |
| explainer-video-skills | 3c13a1bc360c08503f24f9c9a99fda6d3d35de56 | 28 | 5 |

These three packs contain 17 skill documents, although only selected individual skill files were read in depth for this review.

## Most useful presentation-adjacent workflows

### A. Chart animation from data

The chart-animation skill treats every frame as a pure function of current frame and source data. It separates data-to-pixel scales from time interpolation, keeps numeric labels exact, rounds and formats display values, uses stable identity when ranks reorder, and requires start/middle/end still inspections before MP4 encoding.

It supports one template rendered against many CSV/JSON datasets. This is directly useful for repeated monthly KPI storytelling, but its output is a rendered video, not an editable PowerPoint chart animation.

### B. Convert slide decks into narrated video

The presentation-video skill rebuilds slide content as motion graphics rather than screen-recording someone presenting in PowerPoint. It first establishes one throughline, one message per slide, a logical pitch spine and a hook/CTA. Voiceover duration determines each scene's exact length; on-screen reveals are timed to narration. The result is a new video artifact, not a replacement editable PPTX.

### C. Progressive diagram and chart reveals

The diagram-animation skill recommends revealing nodes, then edges, then labels; highlighting the active step while keeping the rest visible as context; and holding each stage long enough to read. It supports SVG, GSAP, CSS, Framer Motion, D3 and Remotion. Its output contract includes an exact-time freeze mechanism, screenshots at start/middle/end, exact-number checks and a reduced-motion final-state fallback.

### D. Motion design and visual direction

The motion-design pack separates animation principles, colour motion, shot composition, motion art direction, Remotion video, logo animation and backgrounds. This separates content, visual direction and motion mechanics instead of blending them into one prompt.

## Tools and architecture observed

| Tool | Role |
|---|---|
| Remotion / React | Frame-driven video composition and rendering |
| D3 scales | Map numerical data to graphical dimensions |
| GSAP | Browser/SVG timelines and detailed choreography |
| Framer Motion | Declarative React motion and stagger patterns |
| SVG / HTML / CSS | Vector scenes and animated diagrams |
| Playwright | Freeze/capture exact states for web-animation checks |
| FFmpeg / MP4 probes | Encoded video inspection and media checks |
| Contact-sheet scripts | Review multiple output frames together |

The three inspected child packs contain small shell verification tools for contact sheets, frame seeking and MP4 probing. The hub itself is not the runtime. The README also advertises a hosted iArt MCP/API route that needs an account/API key; the presence of a skill pack does not make that hosted rendering service free or automatically available.

## Strengths worth adopting

1. Exact data in motion: numbers and charts remain tied to structured source data, not image-model output.
2. Frame-deterministic animation: any important frame can be reproduced and inspected.
3. One template, many datasets: useful for recurring reports and monthly KPI video variants.
4. Narrative timing: voiceover owns the timeline in narrated presentations.
5. Progressive diagram disclosure: reveal relationships in a readable order.
6. Render evidence: output stills/contact sheets and probe the final encoded file.

## Limitations for Legend-Level PPT Skills

- The hub is not the implementation; it points to 19 separately installable packs.
- The 56-skill count is a README claim, not a count of unique implementations independently executed.
- Remotion outputs MP4/GIF/WebM or still frames, not native PowerPoint animation objects.
- D3/GSAP/Framer examples are web/video approaches and do not preserve PPTX masters, editable chart series or shape identity.
- A video can be inserted into PowerPoint as media, but its internal text and graphics are not separate editable PowerPoint objects.

## PPT adaptation

Add an optional data-to-motion-video lane that consumes the same validated content model as the PPTX renderer. Use it for animated monthly KPI summaries, narrated board-deck recaps and animated diagrams. Keep the PPTX deck as the editable source of truth and generate MP4 as a separate deliverable. Use deterministic chart data and frame-by-frame still validation.

Sources:
- https://github.com/iart-ai/data-animation-skills/tree/6570c0c4fbc9daa8d7ac1f1163a890352344206b
- https://github.com/iart-ai/motion-design-skills/tree/b85e50c4cef5ff17aa2187a10d49d2dae9226c74
- https://github.com/iart-ai/explainer-video-skills/tree/3c13a1bc360c08503f24f9c9a99fda6d3d35de56