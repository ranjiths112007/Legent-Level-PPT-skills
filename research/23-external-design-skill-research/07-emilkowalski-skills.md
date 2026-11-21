# 07 — emilkowalski/skills: Motion Craft, Interaction Quality and Design Engineering Taste

## Repository identity

- Repository: https://github.com/emilkowalski/skills
- Pinned revision: 64eb3deb9a5fbfa041faf783e0bc3fd635872e9c
- Root license observed: MIT.
- Snapshot: 36 files, 20 skill documents.
- Core focus: motion design, interaction patterns, frontend polish, animation performance, critique, variants and learning from explicit user taste corrections.

Sources:
- [Repository README](https://github.com/emilkowalski/skills/blob/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/README.md)
- [Skills directory](https://github.com/emilkowalski/skills/tree/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c/skills)

## 1. The 20 skills and their roles

### Motion foundations and review
1. animate — choose the purpose of an animation, element/property, easing, duration, interruptibility and exit behaviour.
2. animation-performance — reason about frame budgets, compositing properties, main-thread work, CSS/JS cost and profiling.
3. animation-vocabulary — shared language for describing motion and motion states.
4. choreograph — coordinate timing and staggering across multiple elements.
5. find-animation-opportunities — inspect an interface and suggest where motion would help.
6. improve-animations — audit an existing animation system and prioritise refinements.
7. remove-animations — identify and remove unnecessary motion.
8. review-animations — strict quality review against animation standards.

### Platform and interaction
9. animate-expo — React Native/Expo animation workflow.
10. apple-design — fluid, interruptible motion and tactile interaction.
11. gestures — drag, swipe, release velocity, spring response and gesture continuity.
12. mobile-native — mobile UI behaviour, safe areas, touch targets, native viewport/font/scroll behaviour.
13. write-swift — native Swift UI/design-engineering practices.

### Taste and product polish
14. emil-design-eng — broader design-engineering quality and visual craft.
15. learn-taste — learn from user corrections, but only save persistent preferences after explicit approval.
16. prototype — create visually distinct variants and let a user select a direction.
17. break-ui — deliberately stress a UI with difficult data to reveal layout failures.
18. pick-ui-library — choose the appropriate UI component library after inspecting the project's dependencies.
19. ask-emil — route a request to the appropriate specialist skill.
20. ask-sonner — focused guidance for the Sonner toast-notification library.

The skill set is broader than presentations. It focuses on product/UI motion and front-end interaction. Its strongest value to PPT is animation craft, variant comparison, visual polish and worst-case layout testing.

## 2. Motion model

The skills encourage motion only when it improves a purpose:
- communicates a state change;
- reveals hierarchy or sequence;
- demonstrates causality;
- provides feedback;
- maintains continuity;
- supports a meaningful user gesture.

Motion should not be added because an animation library is available. The review skills can recommend removing motion when it harms clarity or performance.

### Animation design dimensions

An animation request should describe:
- target element;
- motion property;
- purpose;
- duration;
- easing curve;
- direction/distance/scale;
- delay/stagger;
- entrance and exit;
- interruption behaviour;
- reduced-motion fallback;
- performance requirements.

The important quality goal is coherent motion rather than random easing changes across elements.

### Choreography

The choreograph skill covers sequencing multi-element motion. It supports staggered starts, grouped animation timelines, temporal hierarchy and synchronized sequences.

**PPT transfer:** use transitions sparingly, reveal related points in meaningful order, keep animation timing consistent and avoid making a deck dependent on elaborate motion to be understandable.

## 3. Performance and implementation frameworks

The repository contains front-end and mobile technologies:
- React;
- React Native;
- Expo;
- React Native Reanimated;
- Gesture Handler;
- Expo Router;
- expo-haptics;
- Motion / Framer Motion;
- Vaul for gesture-driven sheets;
- Sonner for toast notifications;
- Swift and native platform UI APIs;
- Swift Testing for test workflows.

These are not dependencies for an ordinary PowerPoint generator. They explain how the skills reason about web/mobile interaction and can inspire motion specifications.

The performance skill focuses on:
- avoiding layout-triggering animation properties when compositor-friendly properties are sufficient;
- keeping frame work within a budget;
- measuring rather than guessing;
- profiling on the actual target device;
- limiting unnecessary animation work;
- respecting reduced-motion preferences.

For PowerPoint, the relevant constraints are slide rendering, exported video, transition support, media size and device playback. Native PowerPoint animation has a different runtime than a React UI, so translate principles rather than libraries.

## 4. Gestures and platform details

The gesture skill values:
- direct 1:1 tracking between finger and object;
- release velocity;
- interruptibility;
- spring physics;
- momentum;
- consistent behaviour when a gesture is interrupted.

The mobile-native skill stresses testing on actual devices and considers:
- safe areas;
- dynamic viewport sizing;
- hover vs tap;
- touch targets;
- scroll/overscroll;
- font and layout behaviour on mobile.

For a presentation, these concepts can transfer to interactive HTML decks or touchscreen kiosks, but they should not silently become requirements for a standard exported PPTX.

## 5. Taste learning and feedback

The learn-taste skill treats user correction as evidence:
1. detect an explicit correction or preference;
2. distinguish a one-off task instruction from a reusable preference;
3. propose a concise rule;
4. request approval before persisting it.

This is an excellent policy for our presentation agent. If the user says “use fewer colours on this deck,” do not necessarily make that a permanent preference. If the user explicitly says “remember that our company decks must use the navy/teal brand system,” then save it to the deck/brand profile.

## 6. Variants and stress testing

The prototype skill generates multiple visibly different design options, then supports selection and refinement. It should not offer fake variants that only change the accent colour; the options should differ in layout, hierarchy or art direction.

The break-ui skill fills a UI with difficult data:
- long names;
- long email strings;
- missing values;
- zero values;
- emoji and mixed Unicode;
- empty collections;
- unusually large numbers.

This exposes wrapping, overflow, alignment and state issues.

**PPT transfer:** create a slide stress-test set with long titles, large metrics, long source notes, unusual currency/units, 0/null values, multi-line labels, CJK/RTL text and maximum chart categories. Render these fixtures before claiming the template is robust.

## 7. A motion QA checklist for PPT

Adapt the motion skills into a presentation-specific test:
- Does the animation express an intentional sequence?
- Can the slide still be understood without motion?
- Do elements appear in reading order?
- Are transitions consistent across the deck?
- Is motion short enough not to slow the speaker?
- Does the output work in PowerPoint's playback environment?
- Is an appropriate no-animation or static export available?
- Are all essential numbers readable before and after animation?

## 8. Limitations

- This is not a PPTX generation engine.
- React Native and web animation dependencies should not be imported into the native PPTX build unless a separate web/video output is requested.
- Some skills are deliberately opinionated, and an AI should not apply all of them to every project.
- User taste should only be made persistent with explicit permission.
- Performance claims need measurement on the target output/runtime.