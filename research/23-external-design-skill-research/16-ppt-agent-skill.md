# 16 — Akxan / PPT Agent Skill

> Source: [Akxan/ppt-agent-skill](https://github.com/Akxan/ppt-agent-skill/tree/e2f97f46a2f92633d3f9b95a1a61b0a668c704b3)  
> Snapshot: 21 November 2026 · Branch: `main` · Commit: `e2f97f46a2f92633d3f9b95a1a61b0a668c704b3` · Root license: MIT

## Executive summary

PPT Agent Skill is a Claude Code skill that builds an end-to-end presentation pipeline: requirements interview → research → outline → page planning → HTML design → SVG conversion → editable PPTX. It advertises 26 visual styles, 18 chart types, 10 layout families, reusable visual components, generated imagery, slide-to-slide narrative rhythm, and optional strict validation.

Its most useful contribution is the combination of **content-driven layout planning, visual design rules, a structured resource registry, and a practical HTML → SVG → PowerPoint compiler**. It also exposes a PNG-to-PPTX fallback, but explicitly documents that route as pixel-faithful and non-editable.

## 1. Six-step workflow

1. **Requirements interview:** collect presentation context, audience, intended action, narrative form, content emphasis, evidence needs, visual preferences and animation preference. The skill blocks until the user answers.
2. **Research:** use available search/document tools to gather source material; save a structured collection.
3. **Outline:** use pyramid-principle reasoning and verify slide count, sections and evidence support.
4. **Page planning:** map research material to each slide; define page type, layout hint, cards, data highlights and chart type. The design is driven by the content rather than a repeated template.
5. **Style and HTML design:** choose from 26 presets (or define a custom style), read typography rules, generate relevant image assets, and create page-level HTML.
6. **Post-processing:** package HTML preview, convert HTML to SVG, compile SVG into PPTX, and optionally add transitions/card entrance animations. Run strict validators and smoke tests when enabled.

The skill adapts the research and generation effort to deck size. Small decks use fewer questions and searches; larger decks split production into batches of 3–5 slides.

## 2. Visual planning system

### Layouts
The repository defines 10 layout families such as single-focus, symmetric, asymmetric, three-column, primary-secondary, hero-top, mixed-grid, L-shape, T-shape and waterfall. It describes these as visual "gravity fields" rather than rigid pixel templates. The LLM is expected to choose a layout based on how information should flow, then vary composition while respecting its underlying logic.

### Blocks and components
The component library includes timeline, diagram, quote, comparison, people, image-hero and matrix-chart components. The documentation frames these as narrative carriers, not generic webpage widgets. A composite visual should often be allowed to stand without an extra enclosing card; multiple competing hero components on one slide are discouraged.

### Principles
The principle library covers hierarchy, cognitive load, composition, colour psychology, data visualization and narrative arc. Its rules include one visual anchor per slide, a clear single-sentence takeaway, whitespace hierarchy, restrained accent colours and density rhythm across adjacent slides.

### Style presets
The 26 styles are grouped into five categories: dark professional, light premium, vibrant, cultural/oriental and natural/retro. Style specifications include typography, palettes, backgrounds and signature elements. The README also describes style gallery generation for visual comparison.

## 3. HTML → SVG → PPTX implementation

### Stage 1: HTML design
The LLM generates HTML/CSS slides, using a 1280×720 (16:9) stage, CSS variables, layout definitions and chart/component instructions.

### Stage 2: HTML to SVG
`html2svg.py` uses Node.js, Puppeteer and `dom-to-svg` to render the DOM and convert supported page elements to SVG. It preserves text as SVG `<text>` where possible and marks card groups for PowerPoint grouping/animation.

Some browser effects are not expressible by the SVG converter. The script detects unsupported CSS such as complex gradients, filters, masks, blend modes, clip paths, pseudo-element effects and rotated/clipped elements, then selectively screenshots those elements as image layers. This is a deliberate hybrid strategy: preserve text and common geometry as vectors, rasterize only effects that the vector pipeline cannot represent.

### Stage 3: SVG to PPTX
`svg2pptx.py` uses `python-pptx`, `lxml` and Pillow to map supported SVG elements into native PowerPoint shapes, text boxes, pictures and grouped cards. It handles common SVG geometry and transforms, gradients and image references, and calls `pptx_motion.py` to add transitions and entrance animations by writing PresentationML XML.

### PNG fallback
`html2png.py` + `png2pptx.py` produce a full-slide image for maximum visual fidelity. The repository clearly labels this as non-editable; only slide transitions remain possible. This should never be confused with the editable SVG route.

## 4. Tools and dependencies observed

| Technology | Role |
|---|---|
| Python ≥3.9 | Workflow scripts and converters |
| Node.js ≥18 | Puppeteer and DOM-to-SVG conversion |
| `python-pptx` | PPTX package authoring |
| `lxml` | SVG/OOXML XML processing |
| Pillow | Image conversion and font measurement |
| Puppeteer | Headless browser render |
| `dom-to-svg` | DOM to SVG conversion |
| SVG | Intermediate vector representation |
| HTML/CSS/JavaScript | Design authoring and browser preview |
| PresentationML/OOXML | Native transitions and animations |

The scripts README notes that Puppeteer, `dom-to-svg` and esbuild are installed into the skill's own Node modules on first use. Export dependencies are separate from the prompt-only workflow.

## 5. Strengths worth adopting

1. **A coherent visual grammar:** layouts, card types, chart types and design principles are explicitly enumerated.
2. **Content-driven layout choice:** the planner chooses a visual structure based on the information relationship, not on a random template.
3. **Cross-slide rhythm:** vary density, layout and chapter colour progression while maintaining global identity.
4. **Hybrid vector/raster conversion:** preserve editable text and shapes; rasterize only effects that cannot be represented reliably.
5. **Explicit fallback honesty:** the PNG route is labelled non-editable.
6. **Strict mode and smoke tests:** validate outline, planning, style, slide HTML, screenshots and actual export.

## 6. Limitations for our requirements

- The main authoring path starts from HTML, not from the original PowerPoint package and its native masters/layouts.
- SVG-to-PPTX conversion can produce editable shapes/text, but it does not automatically preserve the source deck's master/layout relationships or original native chart data.
- Rasterized effects are images, not independently editable geometry.
- The PNG fallback is a screenshot deck and fails our editability requirement.
- Font fallback can change typography and require text scaling; the script includes heuristics to mitigate this, but cross-platform rendering still needs tests.
- Its 26 style claims and quality claims are repository-described capabilities; we have not independently benchmarked every style/chart/export combination.

## 7. Recommended adoption

| Priority | Pattern | Our implementation |
|---|---|---|
| P1 | Layout and component registry | Add semantic layout families and reusable slide components |
| P1 | Cross-slide narrative rhythm | Track density, visual motif and chapter transitions in the slide plan |
| P1 | Style gallery | Generate preview contact sheets for new-deck style selection |
| P1 | Strict stage validators | Validate outline, slide plan, HTML/SVG contract and export output |
| P2 | Selective rasterization | Hybrid mode for non-semantic decoration only; keep numbers/text/charts native |
| P2 | Native animation OOXML | After static fidelity is reliable |
| P3 | Full-slide PNG fallback | Offer only as explicitly non-editable visual export, never as default |

## Verdict

A strong reference for a content-first visual grammar and an HTML/SVG-to-editable-shape pipeline. It is less suitable than PPT Master for editing existing decks and preserving masters, but it provides a more approachable six-stage creative workflow and a useful hybrid rendering strategy.
