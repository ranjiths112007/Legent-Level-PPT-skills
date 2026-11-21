# How Claude Creates Presentations: Product, Design, Image, and PowerPoint Workflow Research

> **Research date:** 21 November 2026  
> **Purpose:** Understand Claude's publicly documented presentation workflow and extract engineering/design methods for Legend-Level PPT Skills.  
> **Evidence policy:** Product documentation and public source code are treated as primary evidence. Where Anthropic does not disclose internal implementation, this document says so rather than guessing.

## Executive summary

Claude has more than one route for creating presentation work. They are related, but they are not the same system and they do not produce the same kind of PowerPoint output.

1. **Claude for PowerPoint** is an add-in inside Microsoft PowerPoint. It can use the open deck and selected slide/object as working context, read the template's slide master, layouts, fonts and colours, create slides, edit targeted elements, and create native editable charts and diagrams. This is the most relevant reference for our goal of making high-fidelity, editable PPTX files.
2. **Claude Slides** is a deck editor/canvas inside Claude. It can build, edit, present and export decks. Its PowerPoint export has an important editability trade-off: text, tables, pictures, slide backgrounds and speaker notes stay editable, while charts, icons and shapes become pictures. Transitions and skipped slides are omitted.
3. **Claude Design** is a visual canvas for designs, one-pagers, mockups and prototypes. It can use design systems, reference screenshots and code components; users can iterate by conversation, comments and direct manipulation. It is not a conventional photographic image-generation model.
4. **Claude file creation / the public PPTX Skill** is a code-driven route. The public Anthropic PPTX skill describes using PptxGenJS for new decks, XML/package editing for existing decks, extraction scripts, thumbnail grids, validation and rendered-slide QA.
5. **External connectors and tools** extend Claude with source data and specialist design capabilities. Officially documented integrations include Microsoft 365 connectors and Claude Design destinations such as Canva, Adobe, Gamma and others. A connector is a route to another tool; it does not mean Claude's own model has become an image-generation model.

**Most important finding:** Claude does not publicly claim to generate photographs or illustrations with its own image model. Anthropic's Help Center explicitly says Claude does not generate photos or illustrations like image-generation tools. Claude can interpret uploaded images and build diagrams, charts and interactive visuals with HTML/SVG. For photographic or illustrative slide assets, the product workflow uses supplied assets or connected design tools such as Canva/Adobe, or a separate image-generation service. See [Can Claude produce images?](https://support.claude.com/en/articles/9002504-can-claude-produce-images) and [Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design).

This is a public-behaviour and workflow analysis. Anthropic has not published the complete internal prompt chain, model routing, layout-ranking algorithm, image-pipeline internals or exact implementation details of the PowerPoint add-in. Any such details below are identified as inference or our proposed design, not fact.

---

## 1. Claude presentation products: do not confuse them

| Claude surface | What it is | What it is good at | Important limitation / distinction |
|---|---|---|---|
| Claude for PowerPoint | Microsoft PowerPoint add-in with Claude in a side pane | Building in an existing corporate template, editing selected slides, native charts and diagrams, iterative changes | Requires a supported PowerPoint version and a Claude plan/account or supported enterprise model route. Human review remains necessary. |
| Claude Slides | Presentation artifact inside Claude | Create a deck from notes/files/data, edit on canvas, comments, speaker notes, present and export | PPTX export converts charts, icons and shapes into pictures; some presentation features are omitted. |
| Claude Design | Visual canvas/artifact for designs, one-pagers, mockups and prototypes | Brand-aware visual composition, design-system reuse, iterations and handoff to tools | Not a built-in photo/illustration generator. Best understood as a design canvas and composition workflow. |
| Claude Code + skills | Coding agent with reusable skill instructions and scripts | Generate PPTX with code, inspect files, create reproducible workflows and integrate validation | Requires scripts/dependencies and technical execution. A skill describes a workflow; it is not a magical presentation renderer by itself. |
| Claude file creation | Code execution/file creation in Claude conversations | Generate PPTX, XLSX, DOCX, PDF and data visualizations | The generated file still needs inspection, refinement and QA. |

### 1.1 Claude for PowerPoint — the most relevant reference

Anthropic's official product documentation describes the add-in as being able to:

- Build slides using an existing client/corporate template.
- Make pinpoint edits to selected slides instead of regenerating the entire deck.
- Generate a complete deck structure from a natural-language request.
- Convert bullets into diagrams and native PowerPoint charts.
- Retrieve external context through connectors.
- Iterate on feedback while preserving formatting and template compliance.
- Read the slide master, layouts, fonts and colour scheme.
- Use the currently selected slide/object as specific context for the requested edit.
- Use Skills and persistent PowerPoint-only instructions.
- Share relevant context across Claude for PowerPoint, Excel, Word and Outlook.

The official tutorial describes a typical example: a branded template is already open; Claude reads its master, layouts and theme; chooses a title slide, section-header and content layout; generates the slide sequence; then the user asks for targeted edits such as simplifying the executive summary, combining overlapping market slides or reordering the storyline. Claude asks before making changes in the described workflow and can identify where it obtained data.

**What is confirmed:** these behaviours are documented by Anthropic.

**What is not publicly disclosed:** the exact sequence of internal model calls, private prompts, object-selection algorithm, ranking model for layouts, or low-level Office API calls used by the commercial add-in. We should not pretend to know them.

Primary sources:
- [Use Claude for PowerPoint — Anthropic documentation](https://claude.com/docs/office-agents/powerpoint)
- [Building a PowerPoint with Claude — Claude Academy](https://academy.claude.com/tutorials/building-a-powerpoint-with-claude)

### 1.2 Supported PowerPoint environment and account access

At the research date, the Claude for PowerPoint documentation lists:
- PowerPoint on the web.
- PowerPoint for Windows with a Microsoft 365 subscription, build 16.0.13127.20296 or later.
- PowerPoint for Mac, version 16.46 or later.

The documentation lists Pro, Max, Team and Enterprise plans for general availability. It does not support PowerPoint 2016/2019 perpetual or volume editions, iPad or Android PowerPoint, or older Microsoft 365 builds below the required shared-runtime threshold.

Install flow described by Anthropic:
1. Open the Claude for Microsoft 365 listing in Microsoft AppSource.
2. Install the add-in.
3. Open PowerPoint, activate it and sign in with the Claude account.
4. For organizations, an administrator can deploy the add-in through the Microsoft 365 Admin Center or a custom manifest.

These details may change; verify the live product documentation before writing installation instructions into our own README.

### 1.3 Claude Slides — the export editability trap

Claude Slides lives inside Claude. A user can:
- Ask for a deck from notes, uploaded files, data or a connected source.
- Attach a prior presentation or name a design system as the design reference.
- Receive an outline or answer clarifying questions before generation.
- Edit slide text and elements directly on the canvas.
- Leave comments on individual slide elements and ask Claude to change them.
- Ask for multi-slide restructuring in the adjacent conversation.
- Add charts by describing the data or naming the source.
- Write speaker notes and present the deck.
- Export PDF, HTML, PNG and PowerPoint; send it to Google Slides when Google Drive is connected.

The documented export behaviour matters:

| Element | Claude Slides PowerPoint export |
|---|---|
| Text boxes | Editable |
| Tables | Editable |
| Pictures | Editable as picture objects |
| Slide backgrounds | Editable |
| Speaker notes | Editable |
| Charts | Become pictures |
| Icons | Become pictures |
| Shapes | Become pictures |
| Slide transitions | Not included |
| Skipped slides | Not included |

This means the deck can look correct but be less editable than a deck whose charts and shapes are true PowerPoint objects. Do not describe the Claude Slides PPTX export as fully native/editable in every object category.

Primary source: [Making slides and presentations with Claude](https://academy.claude.com/tutorials/using-claude-design-for-presentations-and-slide-decks).

### 1.4 Claude Design — the visual-design canvas

Claude Design pairs a conversation with a canvas. Its documented workflow is:

1. Start a design from chat or the Artifacts tab.
2. Attach/import the design system.
3. Add contextual references (screenshots, existing assets, codebase or slide deck).
4. Describe what is needed and who the output is for.
5. Review the generated canvas/artboards.
6. Refine through chat, inline comments and direct editing.
7. Export or hand off to another tool.

The canvas uses artboards and layers. Layers may contain text, shapes, images and nested elements. Users can drag, resize, align, edit text and use properties/adjustment controls. Claude can be asked for alternative layouts and for accessibility/design reviews.

Claude Design can import references including screenshots, existing assets, codebases, PPTX, DOCX and XLSX. It can export PPTX, PDF, Google Slides and HTML, and can send work to connected apps such as Adobe, Canva, Gamma, HubSpot, Miro, Lovable, Replit, Vercel, Wix and others as documented in the current product pages.

Primary sources:
- [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)
- [Claude Design product page](https://claude.com/product/design)

---

## 2. How Claude's presentation workflow works (observable stages)

Anthropic does not publish the private internal chain of thought or every internal step. The following is a practical workflow reconstruction based on public product documentation, official tutorials and public skills.

### Stage 1 — Understand the job

Claude is prompted with:
- Purpose of the presentation.
- Audience and decision-makers.
- The message or decision the audience should leave with.
- Source documents and data.
- Desired length or presentation time.
- Style reference or design-system name.
- Output target (Claude Slides, PowerPoint, PDF, Google Slides, etc.).

When there is enough context, it can start creating. When the prompt is underspecified, the documented Slides workflow may ask questions or share an outline first. Missing figures should be requested or left as visible placeholders instead of being fabricated.

**Why this matters:** slide design quality starts with a clear communication objective. A visually impressive deck with no argument is still a bad presentation.

### Stage 2 — Build the narrative / slide plan

A sensible presentation structure usually includes:
- Cover and context.
- Executive summary or key message.
- Problem/opportunity.
- Evidence and analysis.
- Comparison or alternatives.
- Recommendation.
- Risks, next steps or decision requested.
- Appendix and sources when necessary.

Claude's PowerPoint tutorial demonstrates restructuring a deck after generating it: reduce six executive-summary bullets to three takeaways, merge two overlapping market slides, and move the regulatory slide earlier because it explains the growth drivers.

The lesson for our skill is to validate storyline separately from visual design:
- Does each slide have one job?
- Does the slide title state the takeaway, not just the topic?
- Is there evidence for the takeaway?
- Is the sequence logical?
- Are repeated ideas removed?
- Is the requested decision/action clear?

### Stage 3 — Read the visual system or existing template

There are three common routes:

**Route A: existing PowerPoint template.** Claude for PowerPoint reads the slide master, layouts, fonts and colour scheme. The public PPTX template-creator skill shows how to inspect dimensions, available layouts and exact placeholder positions.

**Route B: prior deck as visual reference.** Claude Slides/Claude Design can use an attached deck or screenshot as the pattern. The user can also ask to rebuild a new reporting period using the old deck and new spreadsheet.

**Route C: reusable design system.** Claude can read a saved design system containing brand identity, design tokens, component definitions, assets and usage notes.

### Stage 4 — Select slide layout and compose visual hierarchy

A design system and master/layout selection constrain the design, but content still needs composition. The official public PPTX skill gives concrete layout recommendations:
- Two-column text + illustration.
- Icon-and-text rows.
- 2×2 or 2×3 content grids.
- Half-bleed image with content overlay.
- Large statistic callouts.
- Before/after or pros/cons comparison columns.
- Timelines and process flows.
- Charts with readable labels and controlled grid lines.
- A repeated visual motif, used consistently rather than a different decoration on every slide.

It recommends varying the layout instead of putting every section on the same title-and-bullets slide. It also describes one reusable layout per slide frame (for example: title, section divider, title-only, chart-and-commentary and table) with logo, footer and slide number on the layout/master rather than duplicated manually on every slide.

**Important distinction:** a PowerPoint slide layout/master is not the same as an individual content composition. The layout is the frame; cards, charts, images, icons and callouts are composed inside the safe content region for the slide.

### Stage 5 — Create native PowerPoint content

When editability matters, build content as native PowerPoint objects:
- Text boxes and rich-text runs.
- Native shapes and connectors.
- Editable diagrams built from grouped shapes/connectors.
- Native charts for supported chart types.
- Native tables.
- Images only for actual image assets or for visual forms that cannot reasonably be represented as native objects.

Claude for PowerPoint specifically documents native editable charts and diagrams. The public PPTX generation skill recommends PptxGenJS for new decks and native charts via addChart() for chart types PowerPoint supports. It says to use a visual image only for chart forms that have no native PowerPoint equivalent, such as Sankey/network/chord examples in that skill.

### Stage 6 — Add image assets and supporting visuals

The important distinction is between:
- **Photos/illustrations:** use user-provided assets, a connected design tool or a separate image-generation model/service.
- **Diagrams/process flows/charts:** create with native PowerPoint shapes or charts wherever possible.
- **Decorative vector compositions:** generate as SVG/HTML or shape layers if they remain crisp and appropriately editable.
- **Logos and brand assets:** use the actual supplied/approved brand files. Do not ask a text-to-image model to invent or redraw a brand logo.
- **Icons:** use a consistent licensed icon set or native symbols; avoid mixing styles.

For every image, define a clear visual brief:
- Purpose on that slide.
- Subject and action.
- Camera/framing or composition.
- Subject position (for example, right side with negative space on left for slide text).
- Aspect ratio and target pixel dimensions.
- Palette and lighting.
- Art direction (photographic, editorial illustration, technical 3D, flat vector, etc.).
- Consistency with the rest of the image family.
- What must not appear (unwanted text, watermark, fake UI, extra logos, incorrect hands, or extra objects).

Generate images as separate assets and then place them into the existing slide frame. Do not generate a complete slide screenshot when the user expects editable headings, charts and captions.

### Stage 7 — Iterate and refine

Claude exposes several edit loops:
- Edit manually on the slide/canvas.
- Comment on one visual or text element.
- Ask for a targeted change to a selected slide.
- Ask for a broader storyline or theme change.
- Duplicate before a major redesign to preserve a fallback.

The lesson for our own agent is to apply targeted changes rather than regenerating an entire deck after every comment. Keep a changelog and rerun QA after each meaningful revision.

### Stage 8 — Export, render and verify

The generation process is not complete when the file saves. Anthropic's public PPTX skill recommends:
- Extract text/content from the output and check for missing content, ordering and leftover placeholders.
- Run a PPTX validator for schema, relationships, content types, charts and slide structure.
- Render the deck to PDF and individual slide images.
- Inspect every slide for clipping, overlap, alignment, spacing, low contrast, bad margins, footer/citation collisions and misplaced decorations.
- Fix the generator rather than manually patching a broken output repeatedly.
- Re-render after changes.

It explicitly warns that the first render commonly contains real visual defects. This supports a mandatory render–inspect–repair loop.

---

## 3. Claude's design-system model

A design system is the repeatable definition of a brand's visual language. Anthropic's public design-system guide describes brand colours, typography, components and usage rules. It is not merely a list of hex colours.

### 3.1 Design system contents

| Area | Stored information | Used for |
|---|---|---|
| Brand identity | Brand summary, tone, logo references and asset library | Keeps visual language consistent |
| Colour tokens | Primary, secondary, accent, surface, text, border, semantic colours per theme | Consistent backgrounds, text, emphasis and states |
| Typography tokens | Font families, weights, sizes, line heights and roles | Title/body/caption/label hierarchy |
| Spacing | Spacing scale, margins, gaps, padding | Consistent alignment and rhythm |
| Shape tokens | Corner radius, line width, shadows and effects | Reusable cards, frames and dividers |
| Components | Buttons/cards/badges/tables/charts/diagram components and their variants | Repeatable visual building blocks |
| Icons and assets | Named logos, icon families, photos, illustrations and files | Approved and consistent visual assets |
| Usage notes | Where to use or avoid a colour, style or component | Prevents incorrect application |
| Theme variants | Light/dark or presentation-specific alternatives | Keeps the system coherent across contexts |

### 3.2 How Claude builds a design system

Anthropic documents these routes:
1. Start a blank design system and describe the brand.
2. Upload brand files: brand guidelines, logos, fonts, token files, finished slides, product screenshots or design files.
3. Sync from GitHub or a local codebase, where tokens and components already exist.
4. Build from connected tools, drives or wikis.

The first draft is deliberately small. The product asks the user to review it, and is designed to ask before filling a value the source files do not show.

A key documented behaviour: a finished deck or product screenshot can convey more about the brand than a written brand-guidelines PDF alone, because it shows the rules as they are actually used.

### 3.3 How the design system is represented

Anthropic documents the saved design system as a package with an overview and supporting files. The documented file pattern includes:

- README.md — short overview and index, read first.
- api/tokens.md — token values and their usage notes.
- api/components/<component>.md — component variants, sizes and how to use them.
- api/icons.md and api/assets/<group>.md — named icon and asset references.
- tokens.json — structured token data used by tools.
- components/bundle.js — reusable component definitions.

Claude reads the overview first and then only the pieces needed for the current request. Usage notes can tell Claude when a specific colour/component should and should not be used.

This is valuable for our product: **store design rules once, then reuse them across every deck**, rather than asking the model to invent a new palette and type scale for every presentation.

Primary source: [Setting up a design system in Claude](https://academy.claude.com/tutorials/create-a-design-system-with-claude).

---

## 4. How the design is applied to each slide

The public documentation does not publish Anthropic's internal layout-ranking algorithm. The following describes the observable template mechanisms and the engineering rules visible in the official PPTX skills.

### 4.1 Read the template geometry

The public template-creator skill uses python-pptx to inspect:
- Slide width and height.
- Number and names of layouts.
- Placeholder indices and types.
- Placeholder x/y coordinates, width and height.
- Title, subtitle, footer and content regions.
- The true content start position, which may be lower than the subtitle because templates reserve space for a separator or decoration.

This is important. If our agent places a chart directly after a subtitle without detecting the reserved separator area, it can collide with the template design.

### 4.2 Choose a layout by content role

Use the right visual structure for the content:

| Content type | Good slide patterns |
|---|---|
| Executive recommendation | Large takeaway headline + 2–3 supporting proofs |
| KPI summary | 3–5 large metrics + small labels + short interpretation |
| Trend | Native line/column chart + one insight |
| Market segmentation | Bar chart, treemap or grouped comparison |
| Before/after | Two aligned panels with metric delta |
| Process | Numbered flow or connected diagram |
| Timeline | Chronological line with milestones and short notes |
| Comparison | Matrix or side-by-side columns |
| Geography | Map or location-based chart with data legend |
| Case study | Problem → action → result, supported by one visual |
| Risks | Severity/likelihood matrix or grouped risk cards |
| Conclusion | Decision, owner, next action and deadline |

Do not select a complex visual just to make a slide look busy. Choose the visual that makes the point easiest to understand.

### 4.3 Maintain visual hierarchy

A strong slide needs:
1. Primary takeaway (what to notice).
2. Supporting evidence (why it is true).
3. Context/source (what to trust, how to interpret).
4. Optional secondary detail.

The main headline should usually communicate the conclusion, not only name the subject. For example, “On-time performance improved in 8 of 10 regions” is more useful than “On-time performance.”

### 4.4 Use a consistent visual motif

The public PPTX skill advises choosing one distinctive motif and repeating it across the deck—examples include rounded image frames or icons in coloured circles. Don't use a random new decoration on every slide, and don't rely on an accent bar/stripe as the only sign of design.

Other practical design rules:
- Use dark title/conclusion slides and light content slides, or commit to a dark theme throughout.
- Align columns and repeated cards to the same grid.
- Keep sufficient margins and whitespace.
- Use a limited palette with semantic colour roles.
- Avoid low-contrast text and overly dense footers.
- Use consistent chart axes, labels, number formats and legend positioning.
- Use consistent crop ratios and image treatment.
- Give every slide a reason for its visual element.

These are design recommendations from public skill instructions and general slide-engineering practice, not claims about Claude's undisclosed internals.

### 4.5 Typography and rendering gotchas

The public PPTX skill warns that the font named in the PPTX is rendered by the recipient's PowerPoint, while local QA may use LibreOffice and substitute fonts. Different font metrics can make a text box appear to fit in one renderer but overflow in another.

The skill identifies a safe font list for its QA environment and recommends extra space when using fonts with unreliable substitutes. The exact list depends on the test environment. Our implementation should:
- Detect fonts in the source theme and in all text runs.
- Prefer installed and licensed fonts where choosing a new design.
- Preserve user fonts in reference-based mode.
- Leave extra fit margin where the rendering engine may substitute a font.
- Inspect the actual rendered result and disclose render-engine mismatch.
- Never shrink text until it becomes unreadable just to pass a layout test.

---

## 5. How Claude handles diagrams, charts, icons and images

### 5.1 Charts

Claude for PowerPoint documents creating native PowerPoint charts from user data or instructions. The public PPTX generation skill recommends keeping charts native for chart types supported by PowerPoint.

A robust chart workflow is:

1. Identify the analytical question (comparison, trend, composition, distribution, relationship, ranking).
2. Validate the dataset and definitions.
3. Choose a chart type that fits the analytical purpose.
4. Use a native PowerPoint chart when possible.
5. Set series names, categories and values from the source.
6. Format axes, labels, number formats, legend, palette and gridlines.
7. Add a takeaway title and source note.
8. Validate that chart values match the source data.
9. Render and inspect labels, overlap, axis ranges and readability.

**Never ask an image model to draw a chart with exact values.** Image models can misspell labels or change numbers. Native charts or deterministic SVG generated from data are safer.

### 5.2 Diagrams and process flows

Use native shapes/connectors for:
- Flowcharts.
- Timelines.
- Operating models.
- Org structures.
- Decision trees.
- System architecture.
- Before/after diagrams.
- Funnel and lifecycle stages.

The official Claude for PowerPoint documentation states that it can convert bullets into diagrams and editable native charts/diagrams. That is stronger than a screenshot-only approach.

### 5.3 Icons

The public PPTX skill provides a concrete icon pipeline: render an icon component/library to SVG, optionally rasterize at sufficient resolution and embed the result. This demonstrates that an icon need not be generated from a text prompt.

Recommended policy:
- Select a single icon family.
- Match stroke/fill weight.
- Use icons to reinforce meaning, not decorate every bullet.
- Prefer native/editable vector shapes or SVG where supported.
- Rasterize only where required by the target library and use a sufficiently high resolution.
- Verify icon licensing and avoid copying logos.

### 5.4 Photography and illustrations: Claude's actual image capability

Anthropic's official Help Center states that Claude does not generate photos or illustrations the way dedicated image-generation tools do. Claude can analyse uploaded images and can create custom diagrams, charts and interactive visuals using HTML/SVG.

Claude Design can build visual compositions on a canvas and can work with supplied assets and design connectors. Anthropic's product examples show Claude Design orchestrating a branded campaign asset workflow in Canva and handing visual work off to tools such as Adobe and Gamma. That is different from claiming that the Claude language model itself generated a new photographic image.

So we must separate the following capabilities:

| Task | Claude itself | Other service/tool |
|---|---|---|
| Understand uploaded slide/photo | Yes, vision/image understanding | — |
| Extract visual style from reference | Yes, with image/slide analysis | Renderer/PPTX parser provides exact geometry |
| Draw a process diagram | Yes, HTML/SVG or native PowerPoint diagram workflow | PowerPoint runtime for native editable result |
| Create chart from numbers | Yes, via chart/data tools | PowerPoint chart APIs or deterministic renderer |
| Generate interactive SVG/HTML visual | Yes, documented custom visual workflow | — |
| Generate a new realistic photo/illustration with its own image model | No, not according to current Help Center | Dedicated image-generation service |
| Use supplied photo/logo/product image | Yes | File attachment or connected asset store |
| Create/modify branded campaign assets through a connected design app | Claude can orchestrate documented connected workflows | Canva, Adobe and other connected providers |
| Generate every slide as a raster image | Possible through separate external image model, but poor default | Not recommended for editable decks |

### 5.5 Recommended asset creation pipeline for our skill

For any slide that genuinely needs a photo or illustration:

1. **Define the asset brief** from the slide's message, not from a vague instruction such as “make it beautiful.”
2. **Extract the reference art direction:** crop, lighting, perspective, colour family, subject scale, whitespace and illustration/photographic style.
3. **Plan the slide frame first:** target aspect ratio, image bounds, safe text zone and crop behaviour.
4. **Choose an asset route:** user-supplied asset, approved stock/source, Canva/Adobe connector or external image-generation API.
5. **Generate or retrieve the asset separately** from the slide text and chart.
6. **Inspect it:** subject correctness, visual consistency, text artefacts, watermark, false logos, extra objects, weird geometry and rights/usage constraints.
7. **Create a family of assets** using a shared style brief and reference image where consistency across slides matters.
8. **Place it into the slide** as a picture object, preserving crop, size and position.
9. **Render the entire slide** and verify contrast, negative space and composition.
10. **Record its provenance** in an asset manifest.

Never generate numeric labels, exact wording, company logos, product specifications or analytical charts inside an image model. Put exact information in editable PowerPoint text, shapes or chart data.

---

## 6. Claude's publicly documented PowerPoint engineering skill

Anthropic publishes a pptx skill in its anthropics/skills repository. Its SKILL.md is marked as proprietary in the repository metadata/license. We can study the workflow concepts, but must not copy its proprietary text or scripts into this MIT-licensed project without explicit permission.

### 6.1 Task routing in the skill

The public skill routes different jobs to different methods:

| Task | Public skill approach |
|---|---|
| New presentation | Generate a PptxGenJS script; use a structured deck for non-throwaway work |
| Edit existing PPTX or build from a template | Unpack the PPTX, edit slide XML/package parts, then repackage |
| Read presentation content | Extract slide text, tables, chart data, alt text and notes |
| Understand the visual template | Generate a labelled thumbnail/contact sheet |
| Validate output | Run schema, relationship, content-type, chart and slide checks |
| Visual QA | Convert deck to PDF/images and inspect every slide |

### 6.2 Useful supporting scripts described by the skill

- Slide text extraction to Markdown.
- Thumbnail/contact-sheet generation with labelled slide numbers.
- Slide duplication with package relationship bookkeeping.
- Cleaning unused slides, media and relationships after structural changes.
- Applying a theme to a generated deck.
- Validating schema, relationships, content types, charts and slides.
- Converting a PPTX to PDF via a headless LibreOffice wrapper.

These are the kinds of deterministic utilities our skill should implement independently.

### 6.3 Creating from scratch with PptxGenJS

The official skill tells the model to create a JS script and generate the PPTX. It includes important implementation warnings:
- Set the slide layout/dimensions before adding slides.
- Use valid colour syntax expected by the library.
- Avoid shared mutable option objects that the library changes in place.
- Use proper bullet paragraph properties rather than literal bullet characters.
- Put speaker notes into the notes API, not slide body text.
- Use native charts for supported chart types.
- Set chart titles, data labels, palette and axes intentionally instead of relying on default chart formatting.
- Validate the result after generation.
- Avoid invalid or unsupported OOXML structures.

**Lesson:** a good deck skill needs code-level implementation knowledge, not only a long prompt describing design.

### 6.4 Existing deck/template editing

The public skill describes unpacking a PPTX and editing the XML parts rather than blindly rebuilding the entire deck. It stresses:
- Inspect the template first.
- Generate a contact sheet with a unique filename.
- Use slide text extraction plus thumbnails to understand content and layouts.
- Select layouts appropriate to the content.
- Duplicate slides using a helper that maintains package bookkeeping; do not just copy one slide XML part manually.
- Perform structural operations before content edits when that avoids cloning modified content.
- Clean orphaned relationships/media after deletions.
- Run package checks against the source template to distinguish template-inherited issues from new regressions.

This is a low-level package-editing workflow. It is not proof that every PPTX feature is always preserved. We must test any implementation against real files containing charts, SmartArt, groups, embedded objects, fonts, animations and media.

### 6.5 Template-to-skill creator

Anthropic also publishes a separate ppt-template-creator skill in its financial-services repository. Its purpose is to convert a user-supplied PPTX/POTX into a reusable skill that contains:
- A copy of the template as an asset.
- A self-contained SKILL.md.
- Layout and placeholder documentation.
- Exact dimensions and content boundaries.
- Example slide generation to validate the extracted template.

Its analysis procedure extracts placeholder x/y/width/height, not just the layout name. It warns that the actual body content start may be lower than the subtitle due to a divider, border or reserved space. It uses the object placeholder position to find the safe start of body content.

**Lesson for our project:** template analysis must recover exact usable geometry and placeholder mappings. “Use the title layout” is not enough.

### Public source files

- [Anthropic PPTX skill](https://github.com/anthropics/skills/tree/main/skills/pptx)
- [Anthropic PPTX skill source file](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md)
- [Anthropic PPT template creator](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator)
- [Template creator command](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/commands/ppt-template.md)

---

## 7. Connectors, skills, integrations and external providers

### 7.1 Difference between the two extension types

Anthropic documents these as separate concepts:

- **Connector:** gives Claude context or actions in an external system. Examples include data providers, connected files or organizational MCP servers.
- **Skill:** a reusable set of instructions/resources for a type of task. Skills can be automatically selected when relevant or invoked explicitly in the PowerPoint add-in.

The official Claude for M365 documentation lists financial connectors such as S&P Global, LSEG and Daloopa as examples, as well as custom connectors. It says skills available in Claude settings can be applied automatically, and users can invoke a skill in the PowerPoint side panel with /.

### 7.2 Relevant integration categories for presentation creation

| Integration category | Examples from the documented ecosystem | What it contributes | Caveat |
|---|---|---|---|
| PowerPoint host | Microsoft PowerPoint add-in / AppSource | Native slide editing context | Requires supported PowerPoint builds and plan |
| Office data sources | Claude for Excel, Word and Outlook | Spreadsheet values, reports, email context | Validate source ranges and permissions |
| External data connectors | S&P Global, LSEG, Daloopa and custom MCP connectors | Market/financial context | Check licence and permission to use data |
| Cloud files | Google Drive and connected enterprise file stores | Reference decks, spreadsheets, brand files | Storage access is not the same as PowerPoint object editing |
| Brand/design systems | GitHub, codebase, design files and brand uploads | Tokens, components, fonts and assets | Require versioning and human review |
| Design applications | Canva, Adobe and Gamma among documented Claude Design destinations | Create/continue branded visual asset and deck work in specialist tools | Connector availability and action scope vary |
| Image-generation provider | Separate image-generation API or an image service exposed via a connector | Creates raster photos/illustrations | Not Claude's native image-generation capability |
| Rendering/QA | LibreOffice, PowerPoint or a controlled renderer | Exports slides to PDF/images for QA | Different renderers may substitute fonts or render features differently |
| GitHub | Source skill, code, schemas, benchmarks and version control | Reproducible skill development | Never store confidential customer decks in a public repository |

### 7.3 Image/design integrations

Claude Design's current product documentation lists destinations including Adobe, Canva, Gamma, Lovable, Miro, Replit, Vercel, Wix and others. The product page also describes a workflow that analyses business data, plans a campaign and generates campaign assets in Canva.

For our skill, make this an **optional asset-provider interface**. The core system should work with user-uploaded images and native PowerPoint objects without requiring Canva/Adobe. When a provider is connected, pass the user-approved visual brief and receive an asset with provenance and file metadata.

Do not market an integration as “free” just because the connector itself is available. The destination may require its own subscription, API quota, model credits or licensing.

### 7.4 Recommended plugin architecture

Use adapters with clear boundaries:

- presentation_host: PowerPoint or local PPTX editing.
- file_provider: uploaded files, Drive, OneDrive or SharePoint.
- spreadsheet_reader: workbook data and formulas.
- research_connector: web/CRM/market data source.
- design_system_provider: GitHub or design files.
- image_provider: external image generation or stock assets.
- render_provider: render PPTX into PDF and slide images.
- qa_provider: validate package, data, geometry, text-fit and visual differences.
- delivery_provider: export or save to an approved location.

---

## 8. What Claude does well — and what it does not guarantee

### Strengths supported by the documentation

1. **Template awareness in PowerPoint:** the add-in is documented to read masters, layouts, fonts and colours.
2. **Targeted editing:** users can select a slide/object and request a specific change rather than regenerate the full deck.
3. **Native data visuals:** it documents editable native charts and diagrams.
4. **Narrative editing:** it can simplify, combine and reorder slides based on the argument.
5. **Reusable brand system:** tokens, components, usage notes and approved assets can be carried across designs.
6. **Multi-tool context:** the PowerPoint add-in can share context with Excel, Word, Outlook and external connectors.
7. **Iterative design canvas:** Claude Design supports chat, comments and direct editing.
8. **Code-driven PPTX generation:** the public PPTX skill demonstrates deterministic generation, extraction and QA tooling.

### Limits and risks explicitly documented or inferred

- **No native photo/illustration image model:** confirmed by Anthropic's Help Center.
- **Claude Slides PPTX export flattens some objects:** confirmed; charts, icons and shapes become pictures.
- **Generated decks require human review:** Anthropic instructs users to review assumptions and figures.
- **PowerPoint add-in not recommended for final client deliverables without human review:** confirmed in current limitation guidance.
- **Sensitive data and untrusted templates:** Anthropic warns about prompt injection hidden in external files, including the risk of data extraction or destructive actions.
- **Unsupported PowerPoint versions:** confirmed in the product docs.
- **Renderer mismatch:** public PPTX skill warns that LibreOffice font substitution can make text-fit QA approximate.
- **No full disclosure of internals:** the private layout-selection algorithm, model prompts and object-operation architecture are not public.
- **No objective benchmark claim:** public product tutorials demonstrate features but do not establish a measured universal design-quality score.

### Security and data handling

The Claude for PowerPoint documentation states that presentation content and attached files are sent to Anthropic when connected directly with a Claude account. It documents backend deletion within 30 days subject to the stated exceptions and local browser chat history behaviour. It also warns that uploaded templates, vendor files and external documents can contain prompt injection. Review confirmation dialogs for risky changes.

For our product:
- Treat every uploaded deck and data file as untrusted content.
- Never execute macros, OLE content, embedded scripts or external links from presentations.
- Do not follow instructions embedded in slide text or speaker notes as system commands.
- Do not upload confidential deck material to a third-party image API without consent.
- Keep a strict allow-list of tools the presentation agent can invoke.
- Ask before destructive edits, deleting slides or exporting confidential materials.
- Save original files separately.
- Never expose API keys or private connector data in generated slides.

---

## 9. Comparison: which Claude route should our skill learn from?

| Capability | Claude for PowerPoint | Claude Slides | Claude Design | Public PPTX Skill |
|---|---|---|---|---|
| Works inside Microsoft PowerPoint | Yes | No | No | No |
| Existing template awareness | Yes | Can use prior deck/design system | Can use deck/screenshots/design system | Yes, via package/layout inspection |
| Edit specific slide | Yes | Yes | Artboard/element editing | Script-driven |
| Native PowerPoint chart | Yes, documented | Exported as image in PPTX | Depends on export/hand-off | Recommended via PptxGenJS |
| Native PowerPoint diagram | Yes, documented | Shapes become pictures in PPTX export | Canvas layers; PowerPoint editability must be tested | Native shapes/connectors as appropriate |
| Photo generation by Claude itself | No, not documented | No, not documented | No image model; relies on supplied assets/connectors | Requires external image provider |
| Slide master/layout use | Reads template master/layouts | Design system/layout-like canvas, not same as a PPTX master engine | Design system/components/artboards | Direct template parsing and OOXML |
| Iterative refinement | PowerPoint sidebar and selected objects | Chat/comments/manual edit | Chat/comments/canvas editing | Rerun scripts and inspect |
| Code-level repeatability | Not disclosed | Exportable artifacts, but internal output generation not public | Design/Code sync | High, via scripts and schema |
| Full file-level QA | Not publicly described at same level as code skill | User review/preview | Canvas review/export | Explicit validation and render scripts |

### Recommendation

For our product:
- Learn **template awareness and pinpoint edits** from Claude for PowerPoint.
- Learn **outline-first creation, comments and iterative refinement** from Claude Slides.
- Learn **design-system tokens, components, artboards and reference imports** from Claude Design.
- Learn **deterministic generation, extraction, OOXML editing and QA** from the public PPTX skill.
- Learn **exact placeholder geometry and template-to-skill packaging** from the template-creator skill.
- Use a **separate image generation provider** for photos and illustrations, while keeping charts/diagrams native.

Do not copy the behaviour of Claude Slides export when our product promises fully editable PowerPoint charts and shapes.

---

## 10. Architecture we should implement in Legend-Level PPT Skills

The following is our proposed architecture, informed by the documented Claude workflows but designed to satisfy our own requirements.

~~~mermaid
flowchart TD
  A[User brief, files and constraints] --> B[Intent and output router]
  B --> C[Research and content extraction]
  C --> D[Evidence and fact validation]
  D --> E[Storyline planner]
  E --> F[Slide plan / storyboard]
  F --> G[Design system resolver]
  G --> H[Slide layout planner]
  H --> I[Native PPTX object builder]
  H --> J[Image brief and asset planner]
  J --> K[Image provider or supplied assets]
  I --> L[PPTX assembler]
  K --> L
  L --> M[Render every slide]
  M --> N[Visual, data, structural and accessibility QA]
  N -->|Failure| O[Targeted repair]
  O --> M
  N -->|Pass or disclosed warning| P[Editable deck + preview + QA report]
~~~

### 10.1 Required internal data structures

**Deck brief**
- Audience, purpose, key message, duration, slide-count range, tone, output type, source files, reference decks and explicit constraints.

**Storyline**
- Slide number, section, message/action title, evidence, intended audience takeaway, source citations and recommended visual type.

**Design system**
- Palette tokens, semantic roles, typography, spacing, grid, margins, components, chart styles, logo/assets, icon family and usage notes.

**Slide specification**
- Chosen layout, object positions, hierarchy, text content, chart/table data, image asset IDs, sources, and expected editable object types.

**Asset manifest**
- Asset ID, target slide, purpose, source/provider, prompt or retrieval query, dimensions, aspect ratio, crop, licence/rights notes and validation status.

**QA report**
- Text overflow, overlaps, bounds violations, missing assets, package validity, chart-data checks, sources, editability checks and visual issues.

### 10.2 Specialist modules

- brief-and-audience-analyser
- source-researcher
- content-and-data-validator
- storyline-planner
- design-system-extractor
- slide-layout-planner
- native-chart-and-diagram-builder
- image-brief-generator
- image-provider-adapter
- pptx-object-builder
- template-preservation-editor
- slide-renderer
- visual-qa-reviewer
- accessibility-checker
- repair-planner
- delivery-reporter

Keep the orchestrator simple. Use deterministic code for coordinates, data, chart values, file changes and validation. Use the model for narrative, semantic matching, design interpretation and qualitative critique.

---

## 11. Practical design and content rules for our future skill

### Narrative rules
- One core message per slide.
- Use takeaway/action titles where appropriate.
- One main proof visual per analytical slide.
- Avoid repeating the same content on multiple slides.
- End with a recommendation, decision, or explicit next step when the audience needs to act.
- Keep claims linked to source material.

### Layout rules
- Select layout based on message type, not random variety.
- Use the slide master/layout where a template exists.
- Respect content region boundaries and footer space.
- Use a consistent grid for columns/cards.
- Avoid placing text across busy imagery unless contrast is controlled.
- Keep intentional negative space.
- Do not default every slide to a title with bullet list.

### Visual rules
- Use a restrained palette with semantic roles.
- Use a small set of font roles and sizes.
- Maintain contrast and legibility.
- Repeat a recognizable motif instead of mixing visual styles.
- Keep icon family consistent.
- Use images with enough whitespace for text when text overlays are needed.
- Use dark/light section transitions deliberately, not randomly.

### Data rules
- Use native charts for factual numbers.
- Select chart type based on analytical question.
- Use consistent axes and number formats across comparisons.
- Never infer denominators or definitions silently.
- Check every chart against its source values.
- Label units and periods.
- Distinguish estimates, forecasts and actuals.

### Image rules
- Images should add meaning, not merely fill empty space.
- Do not generate slide screenshots.
- Use real brand logos.
- Generate a coherent image family rather than unrelated one-offs.
- Avoid text inside generated images.
- Record source, rights and generation provider.
- Preserve native text and chart elements outside the image region.

### QA rules
- Extract text and scan for missing/placeholder content.
- Validate package and relationships.
- Render every slide and inspect the images.
- Check overflow first; then overlap, spacing, margins, contrast and alignment.
- Re-render after every repair.
- Do not declare success based only on code or a successful file save.

---

## 12. Prompt patterns we can adapt

These are original prompt patterns based on the documented workflows, not copied internal Claude prompts.

### A. New deck from source material

~~~text
Create an editable PowerPoint for [audience] to achieve [decision/action].
Use the attached sources as the only factual basis.
First provide a slide-by-slide storyline with one takeaway title per slide.
For every slide, specify the evidence, visual type, and source.
Use the selected design system and vary layouts based on the message.
Use native PowerPoint text, shapes, tables, charts and diagrams wherever possible.
Use image generation only for photographic or illustrative assets.
Do not invent numbers or missing facts. Mark unresolved information clearly.
After generation, render all slides and return a QA report.
~~~

### B. Existing template adaptation

~~~text
Use the attached PPTX as the template.
Inspect the slide masters, layouts, theme, typography, colours, placeholders, object positions and safe content areas.
Map each planned slide to the most suitable existing layout.
Preserve logos, footer, master, colour system, typography and existing design motifs.
Do not redraw the template or replace native editable elements with screenshots.
Create the deck and validate it against the original template.
~~~

### C. Visual style replication from a reference deck

~~~text
Analyse the attached reference presentation.
Extract a design profile: palette, type scale, grid, margins, title treatment,
chart styles, table styles, image treatment, icon family, shapes and repeated motifs.
Separate fixed brand elements from replaceable content.
Create a new presentation using this visual system.
Do not copy reference facts unless requested; use only the new source content.
Render and compare the deck against the reference style.
~~~

### D. Image brief for a slide

~~~text
Create one asset for slide [N].
Purpose: [what the image must communicate].
Subject/action: [what is shown].
Composition: [camera/framing and subject position].
Keep [left/right] area clean for slide text.
Aspect ratio: [ratio].
Art direction: [photographic/editorial/illustrated/3D].
Palette: use the approved design-system colours.
This is an image asset only, not a slide or infographic.
Do not include text, numbers, logos, watermarks or extra UI.
~~~

### E. Iterative slide critique

~~~text
Review the rendered slide as a communication designer.
Identify the 3 most important problems in hierarchy, density, contrast,
alignment, whitespace, data clarity and audience comprehension.
Propose the smallest changes that fix those problems.
Keep the approved content and design system unchanged unless I authorise it.
~~~

---

## 13. Implementation plan for Legend-Level PPT Skills

### Phase 1 — Design and narrative engine
- Audience/goal/constraints intake.
- Content extraction and source map.
- Storyline and slide plan.
- Design system schema and a first theme library.
- Layout catalogue and selection rules.

### Phase 2 — Deterministic editable PPTX builder
- PptxGenJS or another proven builder for new decks.
- Native text, shapes, tables and charts.
- Reusable layout/master definitions.
- Theme token application.
- Speaker notes and source lines.

### Phase 3 — Template-aware generation
- Read existing PPTX/POTX.
- Extract layout and placeholder dimensions.
- Build contact sheet.
- Map slides to existing layouts.
- Add a template reference mode and object preservation tests.

### Phase 4 — Visual asset provider
- Separate image brief planner.
- Supplied asset support.
- One image-provider adapter (select after testing quality/cost).
- Asset manifest and licensing metadata.
- Consistent image family and crop behaviour.

### Phase 5 — Rendering and quality loop
- PPTX validator.
- Headless renderer.
- Contact sheet and per-slide images.
- Visual QA checklist.
- Data/chart and text-fit checks.
- Targeted repair and re-render.

### Phase 6 — Integrations and reuse
- Connectors to approved files and spreadsheet providers.
- Optional Canva/Adobe or other creative provider.
- Skill packages for recurring templates and brand rules.
- GitHub CI with synthetic test decks.
- Benchmark corpus and independent scoring.

### MVP sequence

Do not implement every feature at once. The first usable version should produce a small but reliable deck:
1. Read a brief and source files.
2. Draft and validate the story.
3. Select one of a small set of slide layouts.
4. Build native PowerPoint slides/charts/tables from a design system.
5. Render and run QA.
6. Deliver PPTX plus a QA report.

Only then add advanced image providers, template editing, animation, collaboration and multi-agent workflows.

---

## 14. What we should measure before claiming we are better

Build a benchmark deck set with permission and varied content. Compare our generated output with:
- Claude for PowerPoint (where accessible).
- Claude Slides export.
- Claude public PPTX skill workflow.
- Our own renderer/editor.

Score separately:
- Storyline quality and factual correctness.
- Brand/design consistency.
- Layout variety and hierarchy.
- Native object editability.
- Visual fidelity after rendering.
- Image usefulness and consistency.
- Chart/data accuracy.
- Text fit/overflow.
- File validity and rendering compatibility.
- Human editing time required.

Use the same source materials, brief, template and evaluation rubric for each system. A subjective “looks better” screenshot is not a reproducible benchmark. Do not make a numerical quality claim without measured results.

---

## 15. Sources and evidence register

### Anthropic product and Help Center sources

1. [Use Claude for PowerPoint](https://claude.com/docs/office-agents/powerpoint) — supported versions, template awareness, targeted editing, native charts/diagrams, connectors, skills, persistent instructions, M365 context, limitations and security.
2. [Building a PowerPoint with Claude](https://academy.claude.com/tutorials/building-a-powerpoint-with-claude) — practical demonstration of template reading, deck generation, executive summary revision, slide merge and reorder.
3. [Making slides and presentations with Claude](https://academy.claude.com/tutorials/using-claude-design-for-presentations-and-slide-decks) — Claude Slides workflow, story input, design-system use, manual/comment/chat edits, chart/image behaviour, speaker notes and PPTX export trade-offs.
4. [Claude Artifacts](https://claude.com/features/artifacts) — Claude Slides, Design, Docs and related artifact capabilities.
5. [Can Claude produce images?](https://support.claude.com/en/articles/9002504-can-claude-produce-images) — confirms no built-in photo/illustration generation; describes image understanding and HTML/SVG visuals.
6. [Custom visuals in chat and Cowork](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork) — custom diagrams/charts/interactive visuals built inline.
7. [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) — canvas workflow, artboards/layers, references, iterations, design/code handoff and export.
8. [Claude Design product page](https://claude.com/product/design) — product positioning and connected destinations.
9. [Setting up a design system in Claude](https://academy.claude.com/tutorials/create-a-design-system-with-claude) — brand tokens, components, design-system import routes, usage notes and file representation.
10. [Connectors and Skills for Claude for M365](https://claude.com/docs/office-agents/connectors-and-skills) — difference between external context connectors and reusable task skills.
11. [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) — file creation, code execution and PowerPoint/spreadsheet/document workflow.

### Public Anthropic GitHub source references

12. [Anthropic PPTX skill directory](https://github.com/anthropics/skills/tree/main/skills/pptx) — source skill for PPTX creation/editing/analysis.
13. [Anthropic PPTX SKILL.md](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) — task routing, PptxGenJS, package editing, content extraction, layout, charts, typography and QA. Repository metadata marks this skill as proprietary; study its concepts and check licence terms before reuse.
14. [Anthropic financial-services PPT template creator](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator) — reusable template-skill generation from PPTX/POTX.
15. [PPT template creator command](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/commands/ppt-template.md) — command route to template analysis and package validation.

### Technical standards and tools

16. [PptxGenJS documentation](https://gitbrent.github.io/PptxGenJS/) — JavaScript PowerPoint generation.
17. [python-pptx documentation](https://python-pptx.readthedocs.io/en/latest/) — Python object model for reading/writing common PowerPoint content.
18. [Microsoft Open XML SDK](https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk) — PPTX package/OOXML concepts.
19. [LibreOffice PDF export](https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html) — rendering/preview export options.

### Evidence limits

- This research describes public product behaviour and public skill instructions. It does not expose Anthropic's private prompts, internal orchestration, full PowerPoint add-in source code or internal visual-ranking algorithms.
- Official tutorials are product demonstrations, not independent controlled benchmarks.
- The public PPTX skill's license is proprietary as shown in its repository metadata. Do not copy code/instructions into this project's MIT-licensed materials without checking permissions.
- Claude's file types, supported PowerPoint builds, model access, integrations and plan availability can change. Re-check the official pages before implementation and release.
- Our suggested architecture and evaluation criteria are original recommendations for Legend-Level PPT Skills, not features Anthropic has promised.
