# 14 — Hugo He / PPT Master

> Source: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master/tree/63a03673d5c3c928e7f52983a2c8ec65bac30002)  
> Snapshot: 21 November 2026 · Branch: `main` · Commit: `63a03673d5c3c928e7f52983a2c8ec65bac30002` · Root license: MIT  
> Scope: source-tree, documentation, workflow and selected implementation inspection. This is not a full execution benchmark.

## Executive summary

PPT Master is the most directly relevant repository in this batch for our stated goal: an agent-driven system that turns source documents or topics into **natively editable PowerPoint**, while also supporting template extraction, template filling, native deck enhancement, transitions, animations, speaker notes and media workflows.

Its key architectural decision is to use a **project-canonical SVG intermediate representation (IR)** as a design language, then compile supported SVG constructs into PowerPoint DrawingML (OOXML). It does not promise arbitrary SVG compatibility. It defines a restricted contract, validates it, maps supported elements into native PowerPoint objects, and rejects unsupported/ambiguous authoring states. The source contains substantial Python tooling for PPTX intake, OOXML analysis, SVG conversion, package validation, template handling, animation and image workflows.

This is not merely a large prompt. It is a workflow package plus deterministic local engineering tools. The skill routes the request to one top-level runtime, the model authors within a defined contract, and scripts own repeatable conversion and validation.

## 1. Product modes and route architecture

The top-level skill is a router. It requires the host to:
1. Retain the absolute skill directory rather than guessing from the current working directory.
2. Run an attribution/integrity guard.
3. Read the routing authority.
4. Select exactly one route/profile.
5. Load only that route's runtime authority and explicitly triggered supporting references.

The inspected skill lists these top-level modes:

| Route | Job | Main contract |
|---|---|---|
| Generate PPTX | Create a deck from a topic or source material | Research, plan, author SVG IR, validate, export |
| Create Template | Distil a reusable brand/style/layout/deck workspace from references | Template extraction and explicit design-system contracts |
| Edit Native PPTX | Import an existing deck into a source-preserving round-trip workspace | Preserve source topology/objects and apply controlled changes |
| Beautify PPTX | Improve an existing deck under a fidelity-oriented profile | Preserve what the route promises; explicit Quick intent can change the runtime |
| Image to PPTX profile | Reconstruct slides from input images | Rebuild text and independent layers; whole-slide screenshot skin is forbidden |

The route discipline is unusually strict: only one runtime procedure is loaded; blocking gates stop for user confirmation; prerequisites are checked before entering a step; repairs happen at the layer that owns the error; later-phase work is not speculatively prepared.

**Why this matters:** a single "make me a deck" prompt tends to conflate creating, editing, template extraction and image reconstruction. Those tasks have different preservation rules. Route-specific contracts prevent accidental redesign when the user asked for a small edit.

## 2. Main generation workflow

The documented default pipeline is approximately:

1. **Source processing and factual sufficiency** — convert PDF, DOCX, XLSX, PPTX, web pages and other inputs into normalized Markdown; identify research gaps and preserve fact provenance.
2. **Project initialization and source archive** — create a project workspace and archive source files under an explicit ownership boundary.
3. **Template candidate preparation** — prepare candidate brand/style/layout/deck workspaces.
4. **Strategist stage** — establish communication strategy, narrative, design specification and locked constraints.
5. **Image/resource acquisition** — acquire or generate required imagery and supporting assets.
6. **Executor stage** — author slides as SVG IR, with live preview and staged generation.
7. **Quality gates** — early check for the first sample slides, then mandatory final SVG quality check; chart-bearing decks may enter a chart-calibration stage.
8. **Post-processing and export** — finalize SVG, split notes if required, compile PPTX, apply native transitions/animations/narration as selected, and run delivery checks.

The README and technical design explicitly frame the output as a high-quality editable draft for a human to review, not a supposedly perfect sealed final deck.

## 3. The most important technical idea: SVG as a constrained IR

The system borrows SVG's XML and 2D graphics model, but defines its own canonical authoring language:
- Allowed elements, attributes, units and metadata are constrained.
- Each supported visual construct has a deterministic DrawingML mapping.
- Canonical authoring syntax is preferred.
- Known legacy spellings may be accepted only with deterministic normalization and a warning.
- Ambiguous or unsupported constructs fail validation/export rather than being silently guessed.

This is an important distinction from generic "HTML/SVG to PPTX" converters. The project controls the subset it accepts so the compiler can produce predictable PowerPoint objects.

The structured route also defines Master/Layout/Slide ownership, stable IDs, slot bounds, placeholder carriers, chart/table markers and layer order. This enables actual slide-master and layout inheritance rather than painting every slide independently.

### Native mapping and editability

The technical design describes mappings for:
- Text and text runs.
- Basic shapes and preset geometry.
- Lines, connectors and paths where supported.
- Images and registered layers.
- Gradients, fills, effects and transforms within the supported contract.
- Tables/charts through explicit structured carriers and native-authority metadata.
- Master/layout background and placeholder inheritance.

The project maintains a PowerPoint ↔ SVG mapping guide so support boundaries are explicit. SmartArt is described as a deliberate omission. This is more honest and maintainable than claiming full compatibility.

### Fail-closed conversion

The workflow separates responsibilities:
- Prompt/templates teach canonical syntax.
- `svg_quality_checker.py` checks the authoring state and blocks on errors.
- `svg_to_pptx.py` performs defensive compiler/package checks and requires the current matching final quality report for formal release.
- Workflow logging records bounded command outcomes without pretending to certify success.

The exporter does not silently fix arbitrary authoring problems or replace the full quality checker.

## 4. Existing PPTX preservation and template architecture

This is the most relevant part for the requirement to preserve an existing design.

The source tree includes PPTX intake and OOXML tooling such as:
- `pptx_intake.py`
- `pptx_template_import.py`
- `pptx_ooxml/analyzer.py`
- `pptx_ooxml/chart_read.py`
- `pptx_ooxml/diagram_read.py`
- `pptx_ooxml/clone.py`
- `pptx_ooxml/edit_safety.py`
- `pptx_ooxml/package.py`
- `pptx_ooxml/slideshow.py`

The template importer analyses an existing PowerPoint package, slide/master/layout relationships, placeholders, native objects and source provenance. The editing route creates a workspace with an immutable source backing and a model-facing authoring representation. The docs describe controlled round-trip behavior, source object references, native restoration proxies and fail-closed rules when a proxy or inherited object is edited in unsupported ways.

A key architectural lesson: **never treat a PPTX as just a set of rendered page images**. It is a package of XML parts, relationships, themes, masters, layouts, notes, charts, diagrams, media and embedded objects. Safe editing requires understanding and preserving package relationships.

## 5. Source research and image generation

PPT Master includes a source-to-Markdown dispatcher and backends for PDF, DOCX/HTML/EPUB/notebooks, Excel, PPTX and web content. Its documented workflow preserves source files and creates normalized content artifacts for planning.

The skill also includes image generation/provider backends and image processing tools. Image generation is a distinct resource-acquisition lane, not a replacement for charts or data graphics. The technical design explicitly says charts, tables and data graphics must be native objects with verifiable values, an exact source asset, or marked for manual work; they must not be reconstructed generatively.

The image-to-PPTX route uses vision/reference-image editing for generated layers and strict visual locks for logos/identity assets. Ordinary text is restored natively over the text-removed base; independent objects are rebuilt as registered layers. A whole-slide screenshot skin is not accepted as editable reconstruction.

## 6. Tools, frameworks and dependencies observed

**Primary implementation language:** Python. The skill also uses structured Markdown/YAML-like instruction metadata, JSON configuration/manifests, SVG, XML/OOXML and local command-line tools.

| Technology | Observed role |
|---|---|
| Python | Workflow tools, conversion, validation, project management, image/audio backends |
| `python-pptx` | PPTX creation/interaction used by scripts; supplemented by lower-level OOXML handling |
| `lxml` | XML/SVG/OOXML parsing and manipulation |
| Pillow | Image handling, measurement and raster support |
| `skia-pathops` | Shape boolean/path operations |
| `uharfbuzz` | OpenType shaping and glyph outlines |
| PyMuPDF | PDF-to-Markdown conversion (AGPL-3.0; optional licensing consideration) |
| `openpyxl` | Excel source conversion |
| `mammoth`, `markdownify`, `ebooklib`, `nbconvert` | Document and source conversion |
| `requests`, BeautifulSoup, optional `curl_cffi` | Web source extraction |
| `google-genai` | Gemini image-generation backend |
| `edge-tts` | Narration backend |
| Flask | Local SVG annotation/editor server |
| SVG + DrawingML/OOXML | Canonical visual IR and native PowerPoint target |

Most tools use the Python standard library; the requirements file labels many integrations as optional. PyMuPDF is explicitly identified as AGPL-3.0, which must be reviewed before redistributing a bundle containing it.

Do not assume every dependency is required for a minimal PPTX editing engine. Select optional modules by route.

## 7. What we should adopt

| Priority | Pattern | Our implementation |
|---|---|---|
| P0 | Route-specific workflows | Separate create, template, fill/edit, enhance and image-reconstruction modes |
| P0 | Canonical intermediate representation | Typed slide/shape IR; evaluate constrained SVG or structured JSON for our first version |
| P0 | Deterministic validation before export | Blocking checker for unsupported nodes, invalid geometry, bounds and missing references |
| P0 | PPTX package and relationship awareness | Inspector for masters/layouts, themes, notes, charts, diagrams, media and relationships |
| P0 | Source-preserving edit workspace | Immutable source plus explicit object map and edit manifest |
| P1 | Template extraction into reusable workspaces | Brand/style/layout/deck template assets with provenance |
| P1 | Separate strategist and executor | Plan narrative and design spec before object construction |
| P1 | Explicit native-vs-raster policy | Per-element representation decision and disclosure |
| P1 | Image provider adapters | Generate visual assets separately; preserve provenance and constraints |
| P2 | Native transitions/animations/narration | Add only after static deck fidelity and validation are stable |
| P2 | Local workflow transcript | Reproducible logs with clear limits; never treat logs as proof of correctness |

## 8. What not to copy blindly

1. **Do not recreate its entire system immediately.** The repository is large and sophisticated. Its scope is much larger than a first working prototype.
2. **Do not use SVG as an unrestricted universal IR.** It works here because the project defines and enforces a strict subset.
3. **Do not mistake source import for lossless support of every PowerPoint feature.** Verify the mapping guide and diagnostics for the exact object types in our target decks.
4. **Do not call the system fully native for every visual.** Complex effects can be represented by raster/image layers; the project distinguishes object editability and has explicit boundaries.
5. **Do not bundle optional dependencies without license review.** In particular, review PyMuPDF's AGPL terms.
6. **Do not accept a successful file write as a successful deck.** The quality checker, package validation and actual render are separate requirements.

## 9. Recommended experiments before adoption

- Create a simple deck with text, lines, shapes and images; inspect the resulting OOXML objects.
- Create a chart/table deck and verify values remain editable and correct.
- Import a deck with a custom master, two layouts, speaker notes and a chart; perform a text-only edit and compare package relationships.
- Round-trip grouped shapes, connectors, SmartArt, SVG and embedded media; document what is preserved, transformed or unsupported.
- Render in PowerPoint/LibreOffice and compare to the SVG preview.
- Deliberately insert unsupported SVG and confirm the checker blocks export.

## Verdict

**Highest-priority reference in this four-repository batch.** PPT Master provides the closest architectural reference for our target: local-first workflows, explicit route contracts, an intermediate representation, native PowerPoint compilation, template preservation, package-aware editing and fail-closed quality gates. Study its concepts and contracts carefully; implement a smaller, testable subset rather than cloning its full codebase.
