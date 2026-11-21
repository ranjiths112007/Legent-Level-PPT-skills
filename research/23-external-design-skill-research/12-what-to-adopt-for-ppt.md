# 12 — What to Adopt for Legend-Level PPT Skills

## Product objective

Build an AI presentation system that can create and edit professional PowerPoint decks while preserving native editability and existing templates. The system must produce more than attractive slide screenshots: it must preserve source data, use real PowerPoint objects, render the deck, validate it and explain any limitations.

## 1. Product modes

Do not mix two different user jobs.

### Mode A — Create a new deck

The system can establish a new narrative and design system, choose layouts, create assets, and build native PowerPoint objects.

### Mode B — Edit an existing deck

The system must inspect the source deck, preserve its theme/master/layout and existing objects, and apply only requested changes. Use the reference-edit manifest and minimal-change workflow already documented in the parent research files. Do not apply a fresh visual style unless the user explicitly asks for redesign.

## 2. Recommended end-to-end pipeline

```text
User request + source material
        |
        v
1. Intake and brief
   audience / purpose / decision / source data / constraints
        |
        v
2. Research and evidence
   extract facts / cite sources / resolve conflicts
        |
        v
3. Narrative planner
   key message / story arc / slide-by-slide purpose
        |
        v
4. Design-system resolver
   template / theme / tokens / layouts / components
        |
        v
5. Visual planner
   chart / diagram / image / table specifications
        |
        v
6. Native PPTX construction
   text / shapes / tables / charts / image assets
        |
        v
7. Render and deterministic QA
   package integrity / bounds / text fit / data / accessibility
        |
        v
8. Visual critique and repair
   hierarchy / composition / typography / brand / density
        |
        v
9. Final verification
   re-render / compare / edit manifest / limitations report
```

## 3. Skills to implement

| Skill | Responsibility | Output contract |
|---|---|---|
| `deck-intake` | Clarify audience, goal, format, source files and constraints | `DeckBrief` |
| `research-synthesis` | Extract evidence and preserve provenance | `EvidenceLedger` |
| `narrative-planner` | Build argument and slide sequence before decoration | `SlidePlan[]` |
| `design-system-resolver` | Inspect template/master and resolve tokens/layouts | `DesignSystem` + `LayoutMap` |
| `slide-composer` | Assign content to layout regions and hierarchy | `SlideComposition[]` |
| `chart-planner` | Select chart and encode data semantics | `ChartSpec[]` |
| `diagram-planner` | Select diagram by relationship and structure | `DiagramSpec[]` |
| `image-art-director` | Generate/select images with crop/style/provenance | `AssetManifest` |
| `pptx-builder` | Create/update native objects | PPTX package + object map |
| `reference-editor` | Apply manifest-approved edits to source deck | Updated PPTX + edit manifest |
| `deck-renderer` | Render all slides to images | Render set + render metadata |
| `deck-qa` | Run deterministic and visual checks | `QAReport` |
| `deck-repair` | Apply minimal repairs and rerender | Repair log + verified render set |

Skills should be small and bounded. Commands should orchestrate them. Keep the deterministic engine separate from the model's instructions.

## 4. Design-system schema

The canonical system should include:

- Canvas: width, height, aspect ratio, safe margins and grid.
- Theme: title/body fonts, theme colour slots and background roles.
- Typography: semantic roles, size, weight, line height and allowed fallbacks.
- Colour: background, surface, text, muted text, border, accent, status and chart series roles.
- Spacing: named scale and layout gaps.
- Components: title block, section header, KPI, chart frame, table, quote, callout, footer, source note.
- Layouts: purpose, zones, placeholders, density limits and allowed components.
- Images: style, aspect ratio, crop, attribution and placement guidance.
- Rules: contrast, minimum readable type, max content density, alignment and prohibited patterns.

Tokens must map to native PowerPoint theme/master values and object formatting. For reference-edit mode, extract and preserve the source deck's values instead of imposing a new system.

## 5. Native object policy

| Content | Default representation | Why |
|---|---|---|
| Titles, body copy, labels, footnotes | Native text boxes/placeholders | Editable and searchable |
| Data charts | Native PowerPoint charts when supported | Data-linked/editable |
| Tables | Native PowerPoint tables | Cell-level editing |
| Simple diagrams | Native shapes and connectors | Element-level editing |
| Complex vector illustration | SVG/image object with explicit representation label | Better fidelity, less granular editing |
| Photography / generated illustration | Image asset | Appropriate media type |
| Exact numbers, chart labels and claims | Native text/data objects | Avoid hallucinated image text |

Never generate a chart as an image when exact values and labels matter.

## 6. Quality gate

A deck is not "verified" merely because a file was exported.

### Deterministic checks
- PPTX package opens and required parts/relationships exist.
- Slide count and intended order match the plan.
- No object exceeds slide bounds.
- No unintended overlaps or clipping.
- Text fits and font fallback is recorded.
- Chart/table data match the source.
- Required source notes and citations are present.
- Theme/master/layout preservation checks pass in edit mode.

### Visual checks
- One clear message per slide.
- Strong hierarchy and readable type at presentation distance.
- Balanced composition and consistent spacing.
- Correct chart/diagram semantics.
- Consistent imagery and brand.
- No accidental visual cliffs, crowded zones or orphaned elements.

### Repair protocol
Every repair must name the slide, object, issue, intended change and reason. Make the smallest change that fixes the issue. Re-render and re-run relevant checks. Preserve a before/after artifact and repair log.

## 7. Evaluation plan

Create a fixed benchmark set:
- Blank deck with an existing corporate theme.
- Existing deck with placeholders and master layouts.
- Data-heavy deck with native charts and tables.
- Deck with grouped shapes and connectors.
- Deck with images, transparency and unusual fonts.
- Reference deck requiring small data/text updates without redesign.
- Long-content and multilingual edge cases.

Measure:
- Content correctness and evidence traceability.
- Native editability by object type.
- Template/style preservation.
- Layout overflow and overlap rates.
- Render fidelity across supported office renderers.
- Accessibility checks.
- Repair count and time.
- User-rated clarity and design quality.

Do not claim that one external repository is "best" without same-brief, same-data, same-output benchmark runs.

## 8. Implementation priority

### P0 — Core correctness
1. PPTX inspector and renderer.
2. Safe native text replacement.
3. Native chart and table update support.
4. Edit manifest validation and reversible changes.
5. Geometry, overflow and data-integrity checks.

### P1 — New-deck quality
1. Narrative planner.
2. Design-system extraction/resolution.
3. Native shape/diagram builder.
4. Image asset workflow.
5. Visual critique and repair.

### P2 — Advanced capabilities
1. Motion/animation support.
2. HTML preview/editor.
3. Interactive presentations.
4. Team workflows and style learning.

**Important sequencing:** the project already has research and a reference-edit manifest schema. The next engineering work should start with the inspector/renderer, then safe text replacement, then native chart/table updates. Do not build a giant prompt-driven generator before the editing and verification foundation exists.
