# 25 — Comparative Synthesis: Six Motion-Design Repositories

> Snapshot: 21 November 2026. Compares the six repositories supplied for this research batch, plus selected linked iArt packs. This is source/documentation analysis, not a controlled motion-quality benchmark.

## Executive conclusion

The six repositories cover different layers, not interchangeable solutions:

- GSAP Skills teaches controlled web/SVG animation APIs and timeline choreography.
- Remotion Skills teaches deterministic, frame-driven video compositions and rendering.
- LottieFiles Motion Design Skill teaches motion direction, emotion, timing, easing and visual storytelling independently of runtime.
- iArt Motion Skills is a hub for data animation, motion design and explainer-video workflows, including exact data-driven chart videos.
- Framer Motion Skills teaches declarative React motion, variants, gestures and layout transitions.
- Awesome Motion Design Agent Skills helps choose a runtime and enforce evidence-backed motion QA, accessibility and provenance.

For Legend-Level PPT Skills, the most valuable assets are motion reasoning, named choreography, exact data animation and QA discipline. None of the six is a substitute for a native PowerPoint animation engine.

## 1. Comparison matrix

| Repository | Direct skill docs in submitted repo | Primary output/runtime | Strongest contribution | Main boundary |
|---|---:|---|---|---|
| GSAP Skills | 8 | Browser DOM/SVG via GSAP | Timelines, sequencing, SVG, performance, framework cleanup | Not PowerPoint PresentationML |
| Remotion Skills | 13 | React compositions → MP4/GIF/stills | Frame-deterministic video, parameterized renders, Studio preview | Video is not editable slide objects; runtime has custom licensing |
| LottieFiles Motion Design | 1 + references | Implementation-agnostic motion specs; Creator MCP for exports | Emotion, timing/easing, choreography and motion identity | Skill itself is not an animation engine |
| iArt Motion Skills | 0 in hub; 56 claimed across 19 linked packs | Selected packs use Remotion, SVG, GSAP, Framer, D3, Playwright and FFmpeg | Data-driven charts, narrated deck videos, progressive diagram reveal | Hub is a catalogue; 56 skills are not all in that repo or exhaustively reviewed |
| Framer Motion Skills | 6 | React components via Framer Motion | Variants, springs, gestures and shared layout | React-specific browser runtime |
| Awesome Motion Design Agent Skills | 5 | Router/director/auditor; optional third-party runtimes | Runtime selection, static-first gate, reduced-motion QA and evidence rubric | No bundled animation runtime or PPTX editor |

The five submitted repositories other than iArt contain 33 SKILL.md files in total. The iArt hub contains no SKILL.md of its own. Its README advertises 56 skills across 19 separate packs. Three relevant linked packs were inspected: data-animation (3 skills), motion-design (9 skills) and explainer-video (5 skills). Only selected skill files within those packs were read in depth.

## 2. What transfers to PowerPoint

### A. Motion design as a planning layer

Before creating animation, define the purpose, audience and emotional tone; identify the object that should attract attention; specify the start, action and final state; plan order/overlap; and define a static/reduced-motion version. This is the strongest contribution from LottieFiles and FrankX AI. Motion should clarify progression, explain a relationship or pace a story—not decorate every object.

### B. A portable MotionSpec

Create a versioned, format-neutral specification rather than putting GSAP/Framer/Remotion code inside the SlidePlan. Suggested fields:

- motion_id and slide_id;
- target_object_ids (stable PowerPoint shape IDs or composition element IDs);
- purpose and hierarchy role;
- trigger (on-enter, after-previous, on-click, with-previous or media timeline);
- from/to state or keyframes;
- duration and delay, with units explicitly stated;
- easing/spring profile;
- path/direction and transform origin;
- repeat/yoyo and exit behavior;
- reduced_motion/static fallback;
- selected backend and editability classification;
- required QA frames and expected final state.

The PowerPoint renderer can translate only its supported subset into native PresentationML timing. A video renderer can use frame-based interpolation. An HTML preview can use GSAP or Framer Motion. Keep semantic intent shared but the implementations separate.

### C. Exact data animation

The iArt chart-animation method is useful for KPI storytelling: keep source data/units/metric definitions authoritative; map values to pixels separately from frame progress; make each value a deterministic function of frame; format display values deliberately; use stable identity when ranks reorder; render start/middle/end frames and check every number; reuse a visual template across datasets only after validating one representative output.

This should power an optional animated KPI-video export, not replace the editable PowerPoint chart.

### D. Progressive diagram disclosure

For process and architecture diagrams, reveal in semantic order: nodes → connectors → labels. Highlight the active stage while keeping the rest visible as context. Keep the diagram's colour semantics stable. The same ordering can inform native PowerPoint click/reveal sequences.

### E. Evidence-first QA

Adopt a layered motion QA report:

1. Still-frame quality before motion.
2. Timing, hierarchy and choreography.
3. Text/data fidelity.
4. Start/middle/end frame capture.
5. Reduced-motion/static content completeness.
6. Interruption/reversal checks for HTML previews.
7. Video file probe/playback for MP4 output.
8. Native PPTX package, timing tree and object-editability validation for PowerPoint.

A screenshot cannot prove smooth frame rate; a successful MP4 encode cannot prove the numbers are correct; a PowerPoint save cannot prove the animations remain editable.

## 3. Important technical distinctions

### Native PowerPoint animation versus embedded media

These are separate product modes:

- Native PowerPoint animation: editable slide shapes/text/charts remain PowerPoint objects and are animated through supported PowerPoint timing structures. This is the target when the user needs to adjust objects and animation inside PowerPoint.
- Embedded video/GIF/Lottie asset: an animation is a media object placed on the slide. It may be visually useful, but its internal graphics/text are not separate editable PowerPoint objects.
- HTML presentation animation: works in a browser runtime and is not equivalent to PowerPoint playback.
- Remotion output: renders video/stills from React code; it does not create the original slide object model.

Never describe all four as editable PowerPoint animation.

## 4. Runtime selection

| User goal | Preferred route |
|---|---|
| Simple slide entrance, reveal or emphasis | Native PowerPoint animation adapter |
| Several native objects reveal in order | Native animation timing tree built from MotionSpec |
| Complex animated infographic with exact numbers | Remotion video companion plus editable static/PPTX chart |
| Standalone interactive web presentation | GSAP or Framer Motion, depending on project stack |
| Animated vector logo or visual loop | Lottie/dotLottie or approved media asset |
| Narrated slide-to-video conversion | Remotion presentation-video workflow |
| Reduced-motion or static deck | Keep all content visible in final-state composition |

## 5. Recommended architecture for Legend-Level PPT Skills

```text
Approved SlidePlan + DesignSystem
          |
          v
     Motion planner
          |
          v
     Versioned MotionSpec
          |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
   Native PPTX backend   HTML preview      Video backend
   PresentationML timing GSAP / Motion    Remotion
          |                  |                  |
          v                  v                  v
   Editable slide objects Browser QA       MP4/GIF QA
          |                  |                  |
          +--------- Shared QA / evidence ------+
```

The motion planner should choose no animation unless motion improves clarity or pacing. Native PowerPoint remains the default backend when users request an editable PPTX.

## 6. Implementation priorities

### P0 — Plan motion without rendering it
- Add optional MotionSpec to the SlidePlan schema.
- Define allowed effects: appear, fade, wipe, fly, emphasis, draw, group stagger and exit.
- Define trigger and order semantics.
- Require a static final state and reduced-motion strategy.
- Validate target object IDs and timeline ordering.

### P1 — Native PowerPoint subset
- Implement a small PresentationML timing backend for simple native effects.
- Keep object identity, data editability and layout intact.
- Add tests for on-click, after-previous and with-previous sequencing.
- Round-trip and render in target PowerPoint-compatible environments.
- Do not promise support for all GSAP easing curves or arbitrary physics.

### P2 — Optional video renderer
- Prototype Remotion for narrated presentations and data-driven KPI videos.
- Consume the same EvidenceLedger and validated chart data as the PPTX builder.
- Use frame-driven interpolation and still-first QA.
- Label video media as non-native/editable only as a video object.

### P3 — Optional browser/vector lanes
- Use GSAP for sophisticated SVG/HTML timeline previews.
- Use Framer Motion when the surrounding tool is React and motion follows React state/layout.
- Use Lottie for portable vector animations where target PowerPoint playback compatibility is explicitly tested.
- Keep these dependencies out of the native PPTX core.

## 7. What not to do

- Do not add GSAP, Framer Motion and Remotion as unconditional dependencies of the PPTX generator.
- Do not animate every text line or chart bar by default.
- Do not use generated video/images for exact data without source-data reconciliation.
- Do not confuse browser timeline controls with native PowerPoint triggers.
- Do not claim a complex effect is natively editable when it is a video/GIF/SVG picture.
- Do not make critical information available only during an animation.
- Do not ship meaningful motion without a static/reduced-motion equivalent.
- Do not use Remotion commercially until the proprietary license eligibility and terms are checked.

## 8. Final recommendation

Build the MotionSpec and a small native PowerPoint animation adapter after the PPTX inspector/renderer foundation exists. Adopt LottieFiles for motion vocabulary, GSAP for timeline concepts, iArt for exact data-video patterns, Remotion for a separate video backend, Framer Motion for optional React previews, and FrankX AI for runtime routing and evidence-based QA.