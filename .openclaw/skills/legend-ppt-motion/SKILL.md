---
name: legend-ppt-motion
description: >
  Design kinetic presentations, animated slides, and video exports using GSAP, Remotion, and Lottie.
  Translates slide decks into animated timelines, stepping metrics, and frame-accurate video.
license: MIT
user-invocable: true
argument-hint: "<slide-deck.json|outline.md> [--engine gsap|remotion] [--fps 30|60]"
---

# Legend-Level PPT Motion & Animation Engine

You choreograph professional, subtle motion design for presentations, video walkthroughs, and web slide decks.

## Core Motion Philosophy
Motion in presentations must clarify information hierarchy, never serve as decorative distraction.
- **Enter Transitions:** Staggered reveals (top-to-bottom or left-to-right) timed between 200ms–400ms.
- **Data Reveals:** Stepping counters for key metrics (0 → Target value in 800ms with ease-out).
- **Chart Builds:** Bar charts grow vertically from baseline; line charts draw along the path.
- **Transitions Between Slides:** Subtle cross-fades or horizontal pushes (300ms cubic-bezier).

## Engine Selection

| Engine | Best For | Output Deliverable |
|---|---|---|
| **GSAP (GreenSock)** | Web-based interactive presentations | HTML/JS interactive slide decks with timeline controls |
| **Remotion (React)** | Frame-deterministic video rendering | MP4/WebM animated presentation videos |
| **Framer Motion** | React component decks | Interactive web presentations with gesture support |

## Stepping & Pacing Heuristics
- Title reveals: 0ms start, 300ms duration.
- Key takeaway/action line: +150ms delay.
- Content cards/bullets: +100ms stagger between sibling elements.
- Chart series animations: +250ms duration per series.
