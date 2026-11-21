# 15 — Zara Zhang Rui / Frontend Slides

> Source: [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides/tree/9906a34d640d2111f724544cbc50f7f130569ae1)  
> Snapshot: 21 November 2026 · Branch: `main` · Commit: `9906a34d640d2111f724544cbc50f7f130569ae1` · Root license: MIT

## Executive summary

Frontend Slides is a Claude Code plugin/agent skill for generating **HTML presentations**, not native PowerPoint decks. Its strongest contribution is the visual discovery experience: instead of asking users to describe a style in abstract terms, it generates three preview slides and lets them choose. It also has a progressive-disclosure design library, 34 optional bold template systems, fixed-stage slide geometry, anti-generic style guidance, and a PPTX-to-HTML content extraction script.

The repository explicitly favors zero-dependency, single-file HTML with inline CSS and JavaScript. Its design goal is a stable 1920×1080 stage scaled uniformly to the viewport. It deliberately does not reflow slide content on phones.

## 1. Workflow

### New HTML deck
1. Discover the purpose, length, content readiness and density.
2. Inspect supplied images and incorporate usable assets into the outline.
3. Generate three distinct visual style previews as HTML.
4. Let the user choose a visual direction.
5. Generate the complete HTML presentation in that direction.
6. Open/inspect the result and offer sharing/export.

### Convert PPTX to HTML
1. Run `scripts/extract-pptx.py`.
2. Extract slide text, images and speaker notes to JSON/assets.
3. Show extracted content for user confirmation.
4. Select a visual style.
5. Rebuild a browser-based HTML presentation using the extracted content/assets.

The extraction script uses `python-pptx` and iterates slides/shapes, extracting text frames, image blobs and notes. This is a **content migration path**, not a round-trip PPTX editor: it does not preserve native chart objects, masters/layout inheritance, all geometry, animation, transitions or arbitrary package parts in the generated HTML.

## 2. Architecture

The main `SKILL.md` is a workflow map and loads supporting files only when required:

- `STYLE_PRESETS.md`: curated design directions.
- `bold-template-pack/selection-index.json`: compact template metadata.
- `preview.md`: short previews for shortlisted templates.
- `design.md`: full specification loaded only after the user chooses a template.
- `viewport-base.css`: mandatory fixed-stage CSS.
- `html-template.md`: slide HTML skeleton and features.
- `animation-patterns.md`: CSS/JavaScript animation recipes.
- `scripts/extract-pptx.py`: PowerPoint content extraction.
- `scripts/deploy.sh`: Vercel deployment.
- `scripts/export-pdf.sh`: Playwright-based PDF export.

This is a clear example of **progressive disclosure**: read compact indexes first, shortlist candidates, load previews for candidates, and load the complete design system only after the user chooses. This reduces prompt context and avoids bulk-loading every template.

The skill is also packaged as a Claude Code plugin, but its core Markdown instructions can be used by other coding agents with filesystem and shell access.

## 3. Visual system and presentation model

### Fixed stage
Each slide is authored on a fixed 1920×1080 canvas. JavaScript uniformly scales the stage to fit the browser viewport; letterboxing/pillarboxing is allowed. The slide's internal composition does not rearrange on mobile.

This is a useful approach for consistent visual design and animation timing, but it is fundamentally a web presentation model, not PowerPoint's own object model.

### Content density
The skill asks whether the deck is speaker-led or reading-first:
- Speaker-led: one idea per slide, large type, generous whitespace and few bullets.
- Reading-first: more self-contained detail, structured grids/tables and tighter but still readable spacing.

It prohibits solving excess content by shrinking type until it fits; the deck should gain slides instead.

### Anti-generic design
It actively avoids common generic AI patterns and encourages distinctive type, cohesive palettes, contextual backgrounds and intentional motion. It supports style presets and a bold-template library.

### Style pack architecture
The template index contains 34 optional visual systems. Each entry has mood, tone, formality, density, scheme, best-for/avoid-for guidance, a preview path and a full design path. The system loads only shortlisted previews and one selected full design spec.

This is a valuable machine-readable template-selection pattern: style selection becomes a data lookup informed by the brief, not a vague prompt adjective.

## 4. Tools and dependencies observed

| Tool | Role |
|---|---|
| HTML/CSS/JavaScript | Main output format |
| Inline CSS/JS | Single-file, no build/runtime dependency model |
| Python + `python-pptx` | Extract text, images and notes from existing PPTX |
| Playwright | Screenshot slides and export PDF |
| Vercel CLI | Optional live deployment |
| CSS animations / Intersection Observer | Lightweight slide motion |
| Optional GSAP / ScrollTrigger | More advanced motion recipes |
| Markdown + JSON | Skills, style presets and template metadata |

The README claims no runtime dependencies for the generated HTML. That does not mean the surrounding conversion/deployment tooling has no dependencies.

## 5. Strengths worth adopting

1. **Visual preview selection:** show users three different directions before committing to a whole deck.
2. **Progressive disclosure:** index → shortlist → previews → selected full design specification.
3. **Density as an explicit brief variable:** speaking deck and reading deck require different slide counts and composition.
4. **Fixed-stage geometry:** useful for browser previews and consistent screenshot comparisons.
5. **Anti-generic style rules:** concrete type, colour, texture and layout decisions outperform vague "modern professional" prompts.
6. **Content-aware asset planning:** supplied images can influence the slide outline rather than being appended as decoration.
7. **Simple distribution:** standalone HTML can be opened without a frontend build system.

## 6. Limitations for our PowerPoint project

- Output is HTML; it does not create an editable native PowerPoint file.
- PPTX extraction is one-way and primarily extracts text, images and notes.
- The fixed 1920×1080 browser stage is not equivalent to slide masters/layouts/placeholders.
- CSS/GSAP animations do not transfer automatically to native PowerPoint transitions or object animations.
- A PDF export from browser screenshots is a static rendering and does not preserve HTML interactivity.

**Important:** this repository is a strong visual-design and style-discovery reference, but it should not be used as the native PPTX engine.

## 7. Recommended adoption

| Priority | Pattern | Our implementation |
|---|---|---|
| P1 | Three visual direction previews | Preview three candidate slide styles before generating a new deck |
| P1 | Progressive-disclosure template index | Machine-readable style index and selected template detail |
| P1 | Speaker-led vs reading-first density | Add to deck brief and slide planner |
| P1 | Anti-generic design guardrails | Style-specific rules plus a generic-layout detector |
| P2 | Fixed-stage HTML preview | Optional web preview renderer; keep separate from PPTX geometry |
| P2 | PPTX content extraction | Use as inspiration only; our inspector must preserve full package/object metadata |
| P3 | Vercel/HTML sharing | Optional output path for web presentations |

## Verdict

Adopt its **visual choice UX and progressive-disclosure template library**, not its output engine. It solves the "I don't know what style I want" problem extremely well, but it does not meet the core requirement of editing existing PowerPoint decks while preserving native objects and templates.
