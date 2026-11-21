# 17 — Proyecto26 / Slides AI Plugin

> Source: [proyecto26/slides-ai-plugin](https://github.com/proyecto26/slides-ai-plugin/tree/1f8505f3a89e6cafd863ebbd0ed8b465db4f3820)  
> Snapshot: 21 November 2026 · Branch: `main` · Commit: `1f8505f3a89e6cafd863ebbd0ed8b465db4f3820` · Root license: MIT

## Executive summary

Slides AI Plugin is a compact Claude Code plugin that orchestrates two distinct presentation backends: animated HTML and editable PPTX. Its architecture is particularly clean: one `slide-design` skill handles content discovery, structure, style and format orchestration; `html-slides` and `pptx-slides` own format-specific generation. A small hook system adds automatic validation prompts after file writes and before the agent stops.

Compared with the previous two repositories, it has a clearer native PPTX code-generation path based on PptxGenJS and TypeScript. It also bundles reusable theme/layout/text/image helpers rather than leaving every slide to be handwritten.

## 1. Orchestrated workflow

The entry-point `slide-design` skill:
1. Discovers topic, purpose, audience, duration, language/tone and existing content.
2. Builds a duration-indexed slide outline and tags each slide with a type.
3. Offers three visual directions, with optional mixed backgrounds across sections.
4. Selects HTML, PPTX or both.
5. Delegates to the format-specific generator.
6. Validates the output.

The slide taxonomy includes title, section divider, content, image-focus, comparison, quote, code, feature-grid, timeline, metrics, meme/GIF, diagram, demo divider, audience question and closing.

The orchestration uses a single `slide-outline.md` as the handoff artifact between planner and backend. This is a useful separation: the HTML and PPTX renderers should receive the same approved content structure, then implement it with format-appropriate primitives.

## 2. HTML backend

The HTML skill creates a single-file deck with inline CSS/JS, viewport fitting, semantic HTML, CSS-first animation and optional GSAP. It includes keyboard/touch navigation, reduced-motion support, Mermaid diagrams, Prism syntax highlighting, and browser editing through `contenteditable`.

The README describes GSAP, SplitText and ScrollTrigger integrations. Some references use CDN-loaded scripts, so "single-file" does not necessarily mean fully offline if those optional remote scripts are used.

## 3. PPTX backend

The PPTX skill uses PptxGenJS through TypeScript scripts executed with Bun. It includes modules for:
- Theme creation and 12 style presets.
- Font-aware text measurement and adaptive font sizing.
- Layout and overlap/bounds helpers.
- Reusable layout builders for feature grids, card rows, timelines, metrics and comparison tables.
- Decorative components.
- Image sizing and SVG sanitization.
- Prism syntax highlighting converted to native text runs.
- Consolidated pre-save validation.

It uses `skia-canvas` for font-aware text measurement; the documented helper stack also includes `fontkit`, `linebreak` and `prismjs`. The package runs without a separate TypeScript build step via Bun.

### Native editability

The PPTX backend creates native text boxes, shapes and grouped elements. Speaker notes are expected on content slides. Architecture diagrams should use PowerPoint shapes rather than screenshot images where possible.

The README says the system supports master layouts for template decks, but the inspected generator path is primarily PptxGenJS construction. This is not equivalent to PPT Master's source-package-aware round-trip editing of arbitrary existing decks. Validate exact template preservation before relying on it.

## 4. Validation hooks

The plugin registers:
- A `PostToolUse` prompt hook for Write/Edit operations. For PPTX generation, it checks whether `validateDeck()` was called and speaker notes are mentioned. For HTML, it checks viewport CSS, reduced-motion support and responsive font sizing.
- A `Stop` hook that checks whether requested files were generated, speaker notes are present and output paths were provided.

The TypeScript `validateDeck()` function checks:
- Text font size below 14pt (blocking issue).
- More than six bullets per slide.
- Object bounds against a 10 × 5.625 inch canvas (currently reported as a warning).
- Missing speaker notes (warning).
- Basic aggregate font statistics.

The inspected validator does not itself perform visual screenshot comparison, exact text-overflow measurement, chart-data verification or full OOXML package integrity checks. The hook prompts also inspect code/process evidence; they are not a substitute for opening and rendering the final deck.

## 5. Tools and dependencies observed

| Technology | Role |
|---|---|
| TypeScript | PPTX helper modules |
| Bun | Executes TypeScript without a separate build step |
| PptxGenJS | Native PPTX generation |
| `skia-canvas` | Font-aware text measurement |
| `fontkit`, `linebreak` | Typography/layout dependencies |
| Prism.js | Syntax-highlighted code runs |
| GSAP / CSS | HTML animation |
| Mermaid | HTML diagrams |
| Claude Code plugin manifests | Skill installation and orchestration |
| Claude hooks | Validation prompting after writes and before stop |

## 6. Strengths worth adopting

1. **Planner/backend separation:** a single slide outline feeds either HTML or PPTX.
2. **Format-aware planning:** choose different visual types depending on the output format.
3. **Reusable TypeScript helpers:** theme, text measurement, layout, charts/components, image and validation modules.
4. **Native shape guidance:** diagram geometry should be editable PowerPoint shapes.
5. **Speaker notes as a delivery requirement:** notes are part of the deliverable, not an afterthought.
6. **Automated agent hooks:** catch common omissions before the task is marked complete.

## 7. Limitations for our requirements

- PptxGenJS generation is not automatically a safe editor for arbitrary existing PPTX files.
- The inspected validator is a useful preflight, but shallow compared with a full rendered-deck QA system.
- Hook prompts can verify that a script appears to call a validator; they cannot prove the final file is visually correct.
- HTML animation capabilities do not translate directly to PowerPoint animations.
- Template/master claims need testing with real customer decks, charts, placeholders, custom fonts and embedded objects.

## 8. Recommended adoption

| Priority | Pattern | Our implementation |
|---|---|---|
| P0 | Shared slide-outline contract | Define a typed `SlidePlan` consumed by every output backend |
| P1 | Format-aware renderers | Keep HTML and PPTX renderers separate but share content/design specs |
| P1 | Typed TypeScript helper modules | Use for our PPTX generation engine if TypeScript/PptxGenJS is selected |
| P1 | Adaptive font sizing | Measure text before placement; never rely on PowerPoint autofit as a magic fix |
| P1 | Layout overlap/bounds validators | Add deterministic geometry tests |
| P1 | Speaker notes | Generate notes from the narrative plan |
| P2 | Agent hooks | Add final-delivery checks, but pair with actual render/package inspection |

## Verdict

A strong lightweight blueprint for a multi-format presentation product. Its orchestration and reusable PPTX helpers are worth adopting, but its validator should be treated as a first-pass lint layer, not a complete quality assurance system.
