# 10 — Cross-Repository Patterns and Design Intelligence Synthesis

> Scope: synthesis of the nine pinned repositories in this folder. These are recurring patterns found in source documentation and code structure, not benchmarked claims about output quality.

## Executive finding

The strongest design systems are not one mega-prompt. They separate **intent, knowledge, style, assets, construction and verification** into explicit stages. The repositories approach this from different angles:

- Taste Skill contributes art direction, curated assets and browser QA.
- OpenDesign contributes a large modular workspace, design-system packages, templates and media workflows.
- Diagram Design contributes semantic diagram selection and vector validation.
- UI/UX Pro Max contributes searchable, data-backed style and implementation recommendations.
- Stitch Skills contributes prompt enhancement → design generation → system extraction → code handoff.
- Awesome Design Skills contributes compact visual-style presets.
- Emil Kowalski Skills contributes motion craft, interaction quality and variant testing.
- Designer Skills contributes research, strategy, narrative, tokens, critique and operational workflows.
- Jakub Krehel Skills contributes strict quality rules for typography, colour, layout, accessibility and review.

## 1. Common architecture patterns

### Pattern A — Small specialist skills, composed by workflows

Several repositories organize domain knowledge as small instruction files and use a router or command to select and combine them. Designer Skills explicitly separates skills (domain knowledge) from commands (workflows). Stitch separates design, utilities and build plugin families. OpenDesign distinguishes functional skills, design templates and plugin/scenario/atom entries.

**Why it matters:** specialist modules can be updated and evaluated independently. A command can orchestrate the right modules without loading every skill into every request.

**PPT adaptation:** define separate skills for deck brief, story planning, slide layout, chart planning, diagram planning, image art direction, native PPTX construction, reference editing and QA. A top-level router should select only the necessary skills.

### Pattern B — Structured design systems instead of repeated style prompts

Taste Skill, OpenDesign, UI/UX Pro Max, Awesome Design Skills, Designer Skills and Jakub Krehel all encode design direction or reusable values outside the one-off task prompt. Their representations differ: asset catalogues, package manifests, token data, style presets, component examples or detailed rules.

**Why it matters:** consistent output requires reusable decisions, not just a fresh adjective list for every slide.

**PPT adaptation:** keep brand identity, slide geometry, typography, colour roles, spacing, chart palettes, component patterns and image rules in a versioned design-system file. Resolve semantic roles to PowerPoint theme and object formatting.

### Pattern C — Plan semantics before drawing

Diagram Design chooses a diagram family from the relationship being explained. UI/UX Pro Max maps task intent to chart and style recommendations. Designer Skills maps audience and deliverable to presentation structure. Stitch enhances vague prompts before generation.

**Why it matters:** a visually polished output can still communicate the wrong relationship or story.

**PPT adaptation:** decide what a slide must prove, then choose chart/diagram/layout. Never choose a chart only because it looks attractive.

### Pattern D — Real assets have a deliberate lifecycle

Taste Skill uses curated photography and asset libraries; OpenDesign and UI/UX Pro Max describe image/video generation and provider routes; style collections specify image treatment and visual motifs.

**Why it matters:** images need relevance, consistency, crop control, provenance and reuse. They should not be improvised at the last moment.

**PPT adaptation:** maintain an asset manifest with source, license/provenance, intended slide, crop, aspect ratio, style notes and alt text. Keep factual text and numeric data as editable objects.

### Pattern E — Render, inspect, repair, repeat

Taste Skill's browser QA, Diagram Design's SVG validation/doctor workflows, Designer Skills' structured critique, Jakub Krehel's interface checks and Emil Kowalski's performance/variant review all treat quality as an iterative gate.

**Why it matters:** model confidence is not evidence that a composition renders correctly.

**PPT adaptation:** render every slide to an image; run deterministic geometry and content checks; inspect visual hierarchy and readability; make minimal repairs; render again. Keep the before/after artifacts and a change log.

## 2. Distinctive capabilities — do not flatten them

| Repository | Distinctive contribution | What it is not |
|---|---|---|
| Taste Skill | Art direction, real asset catalogues, browser screenshot QA | A native PPTX editing engine |
| OpenDesign | Workspace/registry architecture, design-system packages, many deck/media templates | One uniform native-PPTX generator; several routes are HTML-first or upstream wrappers |
| Diagram Design | Semantic diagram choice, SVG structure, import/export/validation | Native PowerPoint shape editing by default |
| UI/UX Pro Max | Searchable data-backed design recommendations and CLI | A single fixed image model or a native PPT engine |
| Stitch Skills | Stitch MCP screen generation and design-to-code workflows | A PowerPoint generator |
| Awesome Design Skills | Reusable visual-style instruction presets | A complete agent or renderer |
| Emil Kowalski Skills | Motion craft, interaction, polish and animation review | Slide narrative or PPTX object engineering |
| Designer Skills | Research-to-strategy workflows, narrative, tokens, critique and QA | A PPTX renderer |
| Jakub Krehel Skills | Strict visual/accessibility rules and review loops | A PPTX writer |

## 3. Shared design quality model

A practical synthesis is a seven-layer model:

1. **Communication layer:** audience, objective, decision, narrative and evidence.
2. **Design intelligence layer:** style direction, semantic hierarchy, layout and chart/diagram choice.
3. **System layer:** theme tokens, components, grids, typography and usage rules.
4. **Asset layer:** generated/curated images, icons, diagrams and provenance.
5. **Construction layer:** deterministic native PowerPoint text, shapes, tables and charts.
6. **Verification layer:** data integrity, geometry, render inspection, accessibility and reference comparison.
7. **Learning layer:** user feedback, evaluation cases, style corrections and versioned improvements.

A failure at an upstream layer should not be hidden with downstream decoration. For example, a weak narrative cannot be fixed by a more attractive colour palette.

## 4. Conflicts and trade-offs to resolve

### HTML-first versus native PPTX

HTML-first systems can be flexible and visually rich, but HTML-to-PPTX conversion may alter fonts, charts, SVGs, animations, notes and object editability. Our default deliverable must be explicit. For an editable PowerPoint requirement, native PPTX objects are the target, not an incidental export.

### SVG versus native shapes

SVG is useful for complex vector art and preserves scalability. Native PowerPoint shapes are preferable when the user must edit each element in PowerPoint. The system should identify which representation it used and why.

### Creative freedom versus template preservation

Art direction presets are useful for new decks. In reference-edit mode, they must not override the source deck's master, theme, layout or geometry. Exact-edit mode must prioritize preservation over redesign.

### Rich motion versus clarity and compatibility

Motion skills improve pacing and choreography, but static exports and accessibility constraints matter. Motion must be optional, purposeful, and non-essential to understanding the slide.

### Data-rich recommendations versus evidence

A searchable design dataset can recommend a chart or palette; it cannot validate the user's underlying data. Data checks must be independent of visual-style recommendations.

## 5. What this synthesis means for our product

Build a modular skill system around one stable contract:

- The planner produces a typed deck brief and slide plan.
- The design-system resolver returns semantic tokens and allowed components.
- The visual planner returns chart/diagram/image specifications.
- The PPTX engine builds native objects wherever practical.
- The renderer produces slide previews.
- QA returns machine-checkable errors and structured visual findings.
- The repair engine applies only approved, minimal changes.
- The evaluator records quality against fixed test decks and user feedback.

The external repositories are sources of design reasoning and workflow patterns. They do not remove the need to implement and test our own native PowerPoint engine.
