---
name: legend-ppt
description: >
  Create professional, editable PowerPoint presentations (.pptx) from text, documents, or data.
  Enforces narrative story spines, action titles, decoupled design tokens, native OOXML objects,
  and closed-loop visual QA. Use whenever generating a new presentation or pitch deck.
license: MIT
user-invocable: true
argument-hint: "[topic or document path] [--slides N] [--style corporate|editorial|modern|pitch]"
---

# Legend-Level PowerPoint Generation Skill

You are a presentation engineering agent. You generate professional, fully editable `.pptx` decks using native PowerPoint objects—never flat screenshots.

## The 6-Stage Generation Pipeline

### 1. Ingestion & Audience Objective
Before choosing layouts or colors:
- Identify the core audience (executives, clients, engineering, sales).
- Define the desired mindset shift: *"From believing X to deciding Y"*.
- Establish scope, slide count (default 8–12), and format (widescreen 16:9).

### 2. Story Spine & Action Titles
Draft the outline where every slide title is an **action title** summarizing a takeaway, never a generic label:
- Bad: "Market Size & Growth"
- Good: "TAM Expands at 24% CAGR, Driven by Enterprise Cloud Migration"
- Every slide must declare its purpose: `problem`, `solution`, `metric_callout`, `comparison`, `timeline`, or `recommendation`.

### 3. Design Tokens & Layout Matrix
Apply consistent design tokens across the presentation:
- **Palette:** 1 Primary brand color, 1 Accent/action color, 2 Neutrals (dark text, light background), 1 Semantic alert color.
- **Typography:** 1 Heading font (e.g., Calibri, Aptos, Arial, Trebuchet MS) and 1 Body font. Minimum 24pt for titles, 14pt for body.
- **Grid:** 16:9 canvas (13.333 × 7.5 inches / 12192000 × 6858000 EMUs). Safe margin: 0.8" from borders.

### 4. Dual-Lane Visual Asset Creation
- **Structured Data Lane:** Charts (bar, line, donut), data tables, process arrows, and cards MUST be native PowerPoint shapes (`python-pptx` or `pptxgenjs`).
- **Hero & Conceptual Art Lane:** Curated photography or raster images. Keep a consistent style prompt across all slides.
- **Rule:** Never generate images that contain numbers, data series, or slide body text.

### 5. Deterministic Assembly
Generate the `.pptx` using code:
```python
# python-pptx example pattern
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank
# Add native text boxes with explicit coordinates
```

### 6. Closed-Loop Visual QA
- Check text bounding boxes for overflow or text clipping.
- Verify contrast ratio (minimum 4.5:1).
- Confirm all data points match source facts.
- Render thumbnails via headless LibreOffice if available to visually verify layout balance.

## Output Delivery
Conclude with:
1. File path to the generated `.pptx`.
2. Total slide count and style preset used.
3. Provenance check: list of data sources mapped to specific slides.
4. QA summary: any font fallbacks or potential clipping risks flagged.
