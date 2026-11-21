# 23 — C-Jeril / Framer Motion Agent Skills

> Source: https://github.com/C-Jeril/framer-motion-skills/tree/837d7268fc4a3cf5b1f8904616ec97c7485e3eda
> Snapshot: 21 November 2026 · Commit: 837d7268fc4a3cf5b1f8904616ec97c7485e3eda · License: MIT
> Scope: README, all six SKILL.md files and React example project. No execution benchmark was run.

## Executive summary

Framer Motion Skills is a compact set of six agent skills for the Framer Motion React animation library. It teaches models to use motion components, animation props, motion values, springs, reusable variants, scroll-linked motion, gestures, layout animation and React lifecycle behavior.

The repository contains 24 files (about 47 KB), six SKILL.md files, a skills index, Copilot instructions and a small React/Vite example. It is instruction plus reference code, not a PowerPoint or general-purpose animation renderer.

## The six skills

| Skill | Main APIs and patterns |
|---|---|
| framer-motion-core | motion components, initial/animate/transition, useMotionValue, useTransform, useSpring |
| framer-motion-react | AnimatePresence, exit transitions, layoutId, Next.js/SSR and LazyMotion |
| framer-motion-variants | Reusable variant states, state machines, staggerChildren, repeat, keyframes and parent/child orchestration |
| framer-motion-scroll | useScroll, useTransform, useInView, parallax and progress indicators |
| framer-motion-gestures | Drag, pan, tap, hover, focus, constraints and spring momentum |
| framer-motion-layout | Shared layout transitions, layoutId, reorderable lists and AnimatePresence |

## How it works

Framer Motion is declarative and React-native. The agent describes the desired state on a motion component, and the library animates between states. Variants define reusable named states and allow the parent to orchestrate child animation order. AnimatePresence keeps exit animations available as React components mount and unmount. Motion values can be transformed or spring-smoothed without forcing a full application-state update on every frame.

The skill set contains explicit guardrails: use keys with AnimatePresence, avoid conflicting layout animations, constrain draggable items where appropriate, use CSS-property camelCase, and avoid layout-heavy animations where a transform can express the motion. SSR guidance keeps browser-only behavior on the client.

## Tools and dependencies

| Technology | Role |
|---|---|
| framer-motion npm package | React animation runtime |
| React | Component model |
| Vite | Runnable example app |
| JavaScript / JSX | Animation authoring |
| Skills CLI / plugin marketplace | Agent-skill installation |
| ClawHub | Optional skill distribution path |

The main runtime dependency is Framer Motion in a React project. The six SKILL.md files do not implement the animation engine. This library is React-specific; it should not be selected as the core animation runtime for a non-React PPTX generator.

## Strengths worth adopting

1. Variants as semantic states: model reveal, emphasis, exit and focus states with named variants.
2. Parent/child choreography: stagger multiple items while keeping the timing definition reusable.
3. Gesture and layout concepts: valuable for an optional interactive HTML slide preview/editor.
4. Declarative authoring: the same approved state can be implemented consistently across components.
5. Scoped responsibilities: six skills avoid a single unstructured animation instruction file.

## Limitations for Legend-Level PPT Skills

- Framer Motion requires React and animates browser-rendered elements.
- It does not emit PowerPoint PresentationML animation timing.
- Browser layout transitions do not preserve PowerPoint shape IDs or object geometry.
- A rendered GIF/MP4 is media, not individually editable slide content.
- Scroll and gesture features apply primarily to interactive web presentations or authoring interfaces.

## PPT adaptation

Use Framer-style named animation states as a format-neutral MotionSpec vocabulary: hidden, entering, visible, emphasizing, exiting and reduced-motion/static. Map only supported effects to native PowerPoint animation primitives; use Framer Motion for an optional React-based HTML viewer or editor.