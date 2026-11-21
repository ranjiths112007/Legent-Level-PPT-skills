# Repository Deep Dive — Owl Listener / Designer Skills

> Source snapshot: `9a6930cf84a822eb458624bd11c61aac5bbdf224` (21 November 2026). This is a source-tree and instruction analysis, not a run-time benchmark.

## Executive summary

[Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills/tree/9a6930cf84a822eb458624bd11c61aac5bbdf224) is an agent-oriented design-practice toolkit. Its main contribution is not a rendering engine. It packages specialist design knowledge as Markdown skills and composes those skills into task-oriented commands exposed through Claude Code plugins and Gemini CLI extensions.

At the pinned revision, the repository's own README describes the local design-practice collection as **9 plugins, 111 skills and 34 commands**. The marketplace README also advertises four companion collections, producing a larger ecosystem claim of 273 skills and 76 commands across 33 plugins. These figures describe different scopes and must not be mixed. The source tree inventory found 111 local `SKILL.md` files; the 205-file figure in the broader project inventory includes all repository files, not only skills.

**Relevance to Legend-Level PPT Skills:** this repository is especially valuable for audience framing, narrative planning, design rationale, structured critique, token governance, accessibility and QA. It does not itself provide a native PowerPoint generation or editing engine.

## What is in the repository

The local design-practice collection is divided into nine plugin domains:

| Plugin | Skill count (README) | Main responsibility | Transfer to PPT |
|---|---:|---|---|
| `design-research` | 14 | Personas, interviews, journey maps, research synthesis and testing | Research synthesis, audience context, evidence selection |
| `design-systems` | 11 | Tokens, components, accessibility, theming, motion, governance, localization | Slide theme tokens, reusable layouts, brand consistency |
| `ux-strategy` | 12 | Competitive analysis, principles, information architecture, content strategy and service blueprints | Problem framing, strategic narrative, decision logic |
| `ui-design` | 19 | Grid, colour, typography, data visualization and visual perception | Slide layout, chart selection, typography, visual hierarchy |
| `interaction-design` | 22 | State machines, feedback, forms, navigation, onboarding, motion | Useful mainly for interactive presentations and agent interfaces |
| `prototyping-testing` | 10 | Prototyping, usability tests, heuristic evaluation and experiments | Testing a deck with its audience; validating comprehension |
| `design-ops` | 9 | Critique, handoff, sprint planning, workflows, design debt and impact reporting | QA checklists, review workflow, change documentation |
| `designer-toolkit` | 7 | Rationale, presentations, case studies, UX writing and adoption | Directly useful for slide narrative and speaker-facing rationale |
| `visual-critique` | 7 | Hierarchy, brand, composition, typography, colour, affordance and density | Directly useful for rendered-slide inspection |

The top-level README says the suite is for Claude Code and Gemini CLI. It describes skills as reusable domain knowledge (the “nouns”) and commands as orchestrated workflows (the “verbs”). This distinction is important: a skill teaches a model how to reason about one design discipline; a command sequences several skills to complete a task.

## Architecture and implementation

### 1. Skills are small Markdown instruction modules

A typical skill has YAML frontmatter with a `name` and a short `description`, followed by a role, scope, decision criteria, steps, output format and common failure patterns. Examples:

- [presentation-deck/SKILL.md](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/designer-toolkit/skills/presentation-deck/SKILL.md) defines presentation types, a universal story structure and audience-specific guidance.
- [design-token/SKILL.md](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/design-systems/skills/design-token/SKILL.md) defines token categories, token tiers and naming rules.
- [data-visualization/SKILL.md](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/ui-design/skills/data-visualization/SKILL.md) maps analytical tasks to chart families and specifies encoding/accessibility principles.
- [critique-composition/SKILL.md](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/visual-critique/skills/critique-composition/SKILL.md) turns subjective composition feedback into named dimensions and pass/minor/major ratings.

The strongest pattern is **bounded expertise**. Each skill owns a defined problem and explicitly points to related skills for adjacent responsibilities. For example, the data-visualization skill owns chart selection and encodings, while categorical colour ramps belong to the colour-system skill. This reduces duplicated or conflicting guidance.

### 2. Commands orchestrate multiple skills

Commands live in each plugin's `commands/` directory and are Markdown workflow specifications. They have frontmatter describing their purpose and argument hint, then ordered steps and an expected output.

The [build-presentation command](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/designer-toolkit/commands/build-presentation.md) is a compact example:

1. Analyse the audience.
2. Establish a story arc using `presentation-deck`.
3. Distil 3–5 key messages.
4. Plan each slide's purpose, content and visuals.
5. Add decision rationale through `design-rationale`.
6. Refine slide copy through `ux-writing`.

Its output is an outline with slide-by-slide purpose, content, visuals and speaker notes. It does not claim to create a PPTX file. This is a useful narrative-planning front end, not a PowerPoint renderer.

The [start-here command](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/designer-toolkit/commands/start-here.md) is a router. It places a request on two axes (how decided the work is, and what deliverable is owed), names one stage, selects one command, and identifies two follow-on commands. It deliberately avoids presenting a giant menu. The stages are **understand → frame → explore → make → validate → ship**.

The [critique-screen command](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/visual-critique/commands/critique-screen.md) composes seven critique skills, gathers findings and ranks them P1/P2/P3. Each finding must include the issue, dimension and concrete fix.

### 3. Host integration: Claude Code and Gemini CLI

The repository includes a root Claude marketplace manifest, plugin manifests under each plugin's `.claude-plugin/plugin.json`, and Gemini extension descriptors under `.gemini/extensions/`. The README's Claude Code installation flow adds the marketplace and then installs selected plugins. For Gemini CLI, it documents copying the extension directories into the project's `.gemini/extensions` folder.

The plugin manifest is metadata (name, version, description, author, keywords, homepage and license); the domain instructions live in skill and command Markdown files. The Gemini extension descriptors provide a parallel host entry point. This is an instruction-distribution architecture, not a model-training framework.

**Observed implementation technologies:** Markdown, YAML frontmatter, JSON plugin/extension manifests and small Python repository-maintenance scripts (including README/marketplace checks). The inspected presentation and critique workflows do not depend on a UI framework, charting library or PPTX SDK. Do not infer React, Figma APIs, python-pptx, PptxGenJS or image-generation APIs from this repository.

### 4. Workflow boundaries and routing

The README proposes a natural design-practice sequence:

**design-research → ux-strategy → ui-design / interaction-design → design-systems → design-ops**

This is a useful default, not a mandatory pipeline. The start-here router can skip stages when the task is already well-defined. It also explicitly routes work outside the collection to companion collections rather than pretending the local plugins cover everything.

## Important techniques worth adopting

### A. Narrative before visual styling

The presentation skill distinguishes stakeholder updates, design reviews, final showcases and portfolio narratives. Each has a different audience goal. Its universal structure is:

1. Hook — why the audience should care.
2. Context — what they need to know.
3. Journey — how the work reached this point.
4. Solution — what is proposed and why.
5. Evidence — why the proposal is credible.
6. Ask — what decision, feedback or resource is needed.

It then recommends one idea per slide, progressive disclosure, visual explanation, speaker notes and an audience-specific level of detail. This aligns with our requirement to plan the message and slide sequence before decorating slides.

**Adopt:** require a deck brief containing audience, decision/action, context, 3–5 takeaways, evidence and requested next step. Generate a slide outline before creating any PowerPoint objects.

### B. Design systems through token tiers

The design-token skill separates:
- Global tokens: raw palette, spacing and type values.
- Alias/semantic tokens: roles such as primary action, surface, text and border.
- Component tokens: values scoped to a reusable component.

It covers colour, spacing, typography, elevation, borders and motion, and recommends that components refer to semantic tokens rather than hard-coded raw values.

**Adopt:** create a PPT design-system JSON with theme fonts, colour roles, spacing scale, chart palette, line weights, corner radii, layout margins, reusable component definitions and usage rules. Store the system separately from each deck's content. Map tokens to PowerPoint theme/master values and native shape/chart formatting.

### C. Data visualization as a decision, not decoration

The data-visualization skill links analytical intent to chart families:
- Comparison → bar/grouped bar/bullet.
- Trend → line/area/sparkline.
- Part-to-whole → donut for few categories, stacked bar for many.
- Distribution → histogram/box plot.
- Relationship → scatter/bubble/heat map.

It also emphasizes clear labels, contextual benchmarks, annotation, accessible encoding and avoiding unnecessary decoration.

**Adopt:** add a chart-planning stage that records the question, data grain, dimensions, measures, chart family, encoding, benchmark and takeaway. Generate exact data-driven charts as native PowerPoint charts or editable shapes—not as generated images.

### D. Critique as a structured quality gate

The visual critique collection separates hierarchy, brand consistency, composition, typography, colour, affordance and information density. The composition skill evaluates balance, macro/micro whitespace, rhythm and Gestalt grouping, and requires observation → problem → fix with pass/minor/major status.

The design QA checklist adds implementation checks for visual accuracy, layout/overflow, content, interaction, accessibility and cross-platform behavior. It recommends using real content and data, testing edge cases and comparing against the specification rather than memory.

**Adopt:** after rendering every slide, run separate checks for:
- Message and hierarchy: can the viewer identify the main takeaway quickly?
- Composition: balance, whitespace, alignment and repeated rhythm.
- Typography: size, contrast, readability and consistency.
- Brand: token compliance and consistent imagery.
- Data: labels, units, scales, totals and source fidelity.
- Geometry: bounds, overlap, clipping and overflow.
- Accessibility: contrast, non-colour cues, meaningful reading order and alt text where supported.

Each finding should include slide number, severity, observed problem and minimal repair. Re-render after repair.

### E. Research and evidence traceability

The research collection includes personas, interview scripts, journey maps, card sorting, behavioural analytics, survey design and qual/quant triangulation. The journey-map skill asks for a persona and scenario, 5–7 stages, goals/actions/touchpoints/thoughts/emotions/pain points/opportunities, an emotional curve and prioritized opportunities.

**Adopt selectively:** for research-heavy decks, preserve source provenance, distinguish observed data from interpretation, and map each key claim to evidence. Do not import UX research artefacts into every business deck when the task does not need them.

## What does not transfer directly to PowerPoint

- Responsive website breakpoints, mobile navigation, hover states and touch-specific interaction patterns are not slide layout rules.
- Frontend component code and web CSS are not native PowerPoint objects.
- Interactive chart tooltips and keyboard navigation may not survive export to a static deck.
- The presentation command creates an outline; it is not a slide-rendering or PPTX-editing engine.
- The README's wider marketplace counts include companion repositories and should not be attributed to this repository alone.

Use the design reasoning, not the wrong output technology.

## Limitations and risks

1. **Instruction quality is not execution proof.** A skill can prescribe a good process without guaranteeing that an agent follows it.
2. **No controlled quality benchmark was found in the inspected material.** The repository should not be ranked above or below other design systems without same-brief testing.
3. **No native PowerPoint object model is implemented here.** We still need our own PPTX parser/writer, renderer, edit manifest, validation and repair logic.
4. **The README has scope-dependent counts.** Use 111 skills / 34 commands / 9 plugins for the local collection; 273 / 76 / 33 describes the broader five-collection marketplace.
5. **Host support and installation are version-sensitive.** Recheck Claude Code and Gemini CLI plugin specifications before implementing compatible loaders.
6. **License scope matters.** The repository declares MIT, but third-party assets or companion repositories may have separate terms. Verify each asset and dependency before reuse.

## Recommended extraction for Legend-Level PPT Skills

| Priority | Extract | Implementation in our project |
|---|---|---|
| P0 | Audience and decision framing | `DeckBrief` schema + one-question clarification |
| P0 | Narrative and slide outline | Story planner with slide purpose, takeaway, evidence and ask |
| P0 | Design tokens | Machine-readable PPT theme/design-system JSON |
| P0 | Seven-dimension critique | Rendered-slide critique report with severity and repair instructions |
| P0 | Visual QA checklist | Deterministic bounds, overlap, text-fit, data and render checks |
| P1 | Chart selection | Chart intent/encoding planner feeding native chart builder |
| P1 | Design rationale | Store why a layout, chart and visual treatment were selected |
| P1 | Research traceability | Evidence ledger linking slide claims to source records |
| P2 | Interaction/state design | Only for interactive decks or companion web presentations |
| P2 | Design sprint and team operations | Optional workflow support, not core PPTX runtime |

## Suggested implementation sequence

1. Build a structured deck brief and narrative planner.
2. Build a reusable token schema and PowerPoint theme adapter.
3. Implement native text, shape, table and chart construction.
4. Add a renderer and deterministic geometry/data checks.
5. Add the seven-dimension critique report and minimal repair loop.
6. Benchmark against a fixed set of reference decks and the same content brief.

## Pinned source files examined

- [Repository README](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/README.md)
- [Presentation Deck skill](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/designer-toolkit/skills/presentation-deck/SKILL.md)
- [Build Presentation command](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/designer-toolkit/commands/build-presentation.md)
- [Start Here router](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/designer-toolkit/commands/start-here.md)
- [Design Token skill](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/design-systems/skills/design-token/SKILL.md)
- [Data Visualization skill](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/ui-design/skills/data-visualization/SKILL.md)
- [Composition Critique skill](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/visual-critique/skills/critique-composition/SKILL.md)
- [Critique Screen command](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/visual-critique/commands/critique-screen.md)
- [Journey Map skill](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/design-research/skills/journey-map/SKILL.md)
- [Design Brief skill](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/ux-strategy/skills/design-brief/SKILL.md)
- [Design QA Checklist skill](https://github.com/Owl-Listener/designer-skills/blob/9a6930cf84a822eb458624bd11c61aac5bbdf224/design-ops/skills/design-qa-checklist/SKILL.md)

## Evidence notes

- **Observed in source:** local plugin structure, Markdown skill/command files, manifests, README-described counts, and the inspected workflows listed above.
- **Repository claim:** installation compatibility and advertised counts/commands not independently executed in this review.
- **Inferred workflow:** the staged pipeline reconstructed from README and command/skill references.
- **Recommendation:** all Legend-Level PPT adoption guidance in this document.
