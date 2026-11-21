# 18 — Comparative Synthesis: Four Presentation Repositories

> This document compares four source-pinned repositories inspected on 21 November 2026. It is a design/architecture comparison, not a benchmark of output quality.

## Executive conclusion

The four repositories solve different layers of the presentation problem:

- **PPT Master** is the strongest reference for native PowerPoint depth, template preservation, source-package awareness and deterministic validation.
- **Frontend Slides** is the strongest reference for visual style discovery, user choice and progressive loading of design systems, but it is HTML-first.
- **PPT Agent Skill** is a strong reference for content-driven layouts, a visual grammar and HTML → SVG → native-shape conversion.
- **Slides AI Plugin** is a compact reference for a shared content plan feeding separate HTML and PPTX renderers, reusable TypeScript helpers and agent-level validation hooks.

Do not choose one repository and copy it wholesale. Combine the best architecture patterns while keeping our product's core requirement fixed: **editable native PowerPoint objects and preservation of existing decks when editing is requested.**

## 1. Side-by-side comparison

| Dimension | PPT Master | Frontend Slides | PPT Agent Skill | Slides AI Plugin |
|---|---|---|---|---|
| Main output | Native PPTX | HTML | HTML preview + PPTX | HTML and PPTX |
| Native PPTX object model | Deep, constrained SVG → DrawingML + OOXML tools | No | SVG → native shapes/text | PptxGenJS native shapes/text |
| Existing PPTX preservation | Explicit import/edit/template routes | One-way content extraction | Not primary workflow | Template/master support claimed; not equivalent to package-aware round trip |
| Visual style selection | Template workspaces and style routes | 3 visual previews + 34 bold templates | 26 style presets/gallery | 12 theme presets, 3 directions |
| Narrative/research planning | Strategist + source conversion + evidence gates | Basic content discovery/outline | Research-first six-step pipeline | Duration-indexed outline |
| Intermediate representation | Restricted project-canonical SVG with metadata | HTML DOM | HTML → SVG | Shared Markdown outline then format-specific implementation |
| Image strategy | Provider adapters, asset layers, strict non-generative chart policy | User-supplied assets; styles and CSS | AI-generated image assets + selective rasterization | Images and SVG helper support |
| Animation | Native OOXML transitions/object animations and narration routes | CSS/JS; optional GSAP | OOXML transitions/card entrances | HTML GSAP; PPTX animation support is not the focus |
| QA | Contract checker, package validation, render/route gates | Fixed-stage and browser checks | Strict validators + smoke tests | Pre-save validator + PostToolUse/Stop hooks |
| Best contribution | Native PowerPoint engineering | Style discovery UX | Content-driven visual grammar | Multi-backend generator architecture |

## 2. Strongest patterns to combine

### A. Separate user intent into modes

Use PPT Master's route separation:
- Create a new deck.
- Fill an existing template.
- Edit an existing deck while preserving its identity.
- Redesign/beautify an existing deck.
- Convert a reference image into editable objects, with limitations disclosed.

This must happen before planning. A user asking "change these three values" must not receive a redesigned deck.

### B. One shared content plan, multiple renderers

Use Slides AI Plugin's orchestration idea:
- Planner produces a format-neutral `SlidePlan`.
- HTML renderer creates web slides if requested.
- PPTX renderer creates native PowerPoint objects.
- Both renderers consume the same approved content and design direction.

Do not force HTML CSS or web animation semantics into the PPTX object model.

### C. A semantic visual grammar

Combine PPT Agent Skill's layout families and narrative components with Designer Skills' research/critique approach:
- Pick a slide structure based on the relationship to communicate.
- Pick charts based on the analytical question.
- Pick a diagram based on semantic relationships.
- Vary visual rhythm while preserving design-system consistency.

### D. Style choice through visual evidence

Use Frontend Slides' three-preview flow:
1. Build a compact candidate style index.
2. Select 2–3 diverse candidates using the brief.
3. Render preview slides.
4. Let the user select or request changes.
5. Load only the selected full style specification.

This is more effective than asking users to choose from a long list of adjectives.

### E. Constrained intermediate representation and compiler

PPT Master shows the value of a canonical IR with explicit supported constructs. PPT Agent Skill demonstrates a smaller HTML-to-SVG-to-PPTX pipeline. Our engine should:
- Define a typed, versioned slide/object IR.
- Validate it before export.
- Compile only supported constructs to native PowerPoint.
- Label image/raster fallbacks explicitly.
- Refuse ambiguous or unsupported conversions rather than silently corrupting a deck.

For reference editing, the IR must retain source object identity and package relationships, not merely a fresh SVG page.

### F. Quality gates at multiple layers

Adopt a layered QA model:
1. Content/evidence checks.
2. Narrative and slide-plan checks.
3. Design-token and component checks.
4. IR/schema validation.
5. Geometry/text-fit/overlap checks.
6. PPTX package/relationship integrity.
7. Actual PowerPoint-compatible render inspection.
8. Final re-render after repairs.

A hook that checks whether a validator was called is useful, but it is not proof the output is correct.

## 3. Suggested architecture for Legend-Level PPT Skills

```text
User request + files
      |
      v
Intent router
  create | fill template | edit existing | redesign | image reconstruction
      |
      v
Source intake + evidence ledger
      |
      v
Deck brief + narrative / SlidePlan
      |
      v
Style discovery + design-system resolver
      |
      v
Semantic visual planner
  layout | chart | diagram | image | table
      |
      v
Versioned slide IR
      |
      v
PPTX package inspector / native object engine
      |
      v
Export + deterministic validation
      |
      v
PowerPoint-compatible render + visual critique
      |
      v
Minimal repair + re-render + delivery report
```

The key split is between the model's creative decisions and deterministic engineering. The model decides what the slide should communicate and how it should be composed; code verifies geometry, package integrity, source data and supported mappings.

## 4. Concrete library/tool decision notes

| Capability | Candidate/reference | Decision |
|---|---|---|
| PPTX generation | PptxGenJS (Slides AI Plugin) | Worth prototyping for a TypeScript-native generation backend |
| PPTX package inspection/editing | PPT Master OOXML tooling | Study its package-aware model; implement a narrow safe subset first |
| PPTX generation/editing | python-pptx | Useful for basic construction and extraction; lower-level OOXML needed for unsupported features |
| HTML visual rendering | Puppeteer / Playwright | Useful for HTML previews and screenshots; not a substitute for PowerPoint rendering |
| HTML → SVG | dom-to-svg / custom converter | Useful for an optional vector import lane; must define a strict subset |
| SVG → PPTX | Custom DrawingML compiler | Requires extensive feature mapping and round-trip tests |
| Text measurement | skia-canvas / fontkit | Strong option for measured text placement |
| Visual effects | CSS/GSAP | Keep in HTML renderer; don't promise they transfer to PPTX |
| Motion in PPTX | Direct PresentationML/OOXML | Add after static geometry and package preservation are stable |

## 5. What to build first

1. **PPTX Inspector:** read package parts, masters, layouts, themes, placeholders, text, shapes, charts, tables, notes, media and relationships.
2. **Render harness:** render source and output decks to images using a supported office-compatible renderer.
3. **Safe edit manifest:** address objects by stable source identity and declare exactly what can change.
4. **Text-only edit path:** preserve style, geometry and unrelated package parts.
5. **Native chart/table updates:** maintain values, categories, series and embedded workbook relationships.
6. **New-deck builder:** use a shared SlidePlan and native objects.
7. **Style preview and visual QA:** add the creative system after correctness is measurable.

## 6. Important non-equivalences

- HTML slide output is not an editable PPTX.
- SVG text converted to PowerPoint text is editable text, but SVG pictures or rasterized CSS effects are not individually editable source shapes.
- PptxGenJS can generate native objects, but generating a new deck is not the same as safely editing an arbitrary existing deck.
- A successful `validateDeck()` call does not prove that the PPTX opens, renders correctly, or preserves source masters.
- A screenshot/PDF preview is evidence of appearance, not evidence of object editability.
- "Supports templates" must be tested against actual masters, placeholders, theme inheritance, charts, notes and package relationships.

## 7. Final recommendation

Use **PPT Master as the engineering reference**, **Slides AI Plugin as the clean multi-format orchestration reference**, **PPT Agent Skill as the visual grammar and conversion reference**, and **Frontend Slides as the style-discovery UX reference**.

The next task remains the PPTX Inspector + Renderer. This is the foundation that lets us test the most valuable ideas from all four projects instead of accumulating prompts and style presets without a reliable PowerPoint engine.
