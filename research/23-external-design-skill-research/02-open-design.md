# 02 — nexu-io/open-design: Agent Workspace, Design Systems, Deck Templates and Media Pipelines

## Repository identity

- Repository: https://github.com/nexu-io/open-design
- Pinned revision: e033aad1d15a9d4084316e5223f2c6597fd32619
- Root license observed: Apache-2.0. Individual bundled templates and assets can carry separate licenses.
- Snapshot: 14,308 files; 169 SKILL.md paths under the main functional skills registry, 115 design-template SKILL.md files, and 272 plugin SKILL.md files. The full recursive tree contains 562 skill-document paths when all additional locations are included.
- Major feature families: local-first agent workspace, skills, rendering templates, design systems, plugins/scenarios, code/Figma migration, image/video/audio workflows, web/React output and presentation deck templates.

Sources:
- [Repository README](https://github.com/nexu-io/open-design/blob/e033aad1d15a9d4084316e5223f2c6597fd32619/README.md)
- [Skills protocol](https://github.com/nexu-io/open-design/blob/e033aad1d15a9d4084316e5223f2c6597fd32619/docs/skills-protocol.md)
- [Design-system package guide](https://github.com/nexu-io/open-design/blob/e033aad1d15a9d4084316e5223f2c6597fd32619/design-systems/README.md)
- [Plugin specification](https://github.com/nexu-io/open-design/blob/e033aad1d15a9d4084316e5223f2c6597fd32619/plugins/spec/SPEC.md)
- [Guizang presentation template](https://github.com/nexu-io/open-design/tree/e033aad1d15a9d4084316e5223f2c6597fd32619/design-templates/guizang-ppt)
- [HTML PPT master skill](https://github.com/nexu-io/open-design/blob/e033aad1d15a9d4084316e5223f2c6597fd32619/design-templates/html-ppt/SKILL.md)
- [PPTX/HTML fidelity audit](https://github.com/nexu-io/open-design/blob/e033aad1d15a9d4084316e5223f2c6597fd32619/skills/pptx-html-fidelity-audit/SKILL.md)

## 1. Understand the repository's architecture first

OpenDesign is not one presentation skill. It is a local-first AI design workspace that combines several registries and runtimes. The same repository contains:
- portable skills that tell an agent how to perform a task;
- design templates that give the agent an existing artifact or visual system to populate;
- plugins that connect workflows to stages, tool atoms and output contracts;
- design systems that supply brand tokens and components;
- project/runtime tooling to preview, refine, export and hand off artifacts.

The repository explicitly separates functional skills from rendering templates. This distinction is foundational.

### Functional skill

A functional skill describes a capability or workflow, such as designing a UI, analysing a diagram, generating a deck, auditing an export or extracting design tokens.

### Design template

A design template is a prebuilt artifact or visual structure that an agent personalises. It is closer to a seed project/theme/layout catalogue than a universal instruction set.

### Plugin / scenario / atom

- A **plugin** packages a workflow and may define stages, input/output contracts, previews and tools.
- A **scenario** selects or coordinates a default sequence of stages for a task family.
- An **atom** is a small specialised operation called within a stage, such as extracting design tokens, writing a plan, generating media, critiquing or applying a patch.

These should not be collapsed into the same concept. A template can be used inside a plugin; a plugin may call atoms; a skill may be installed independently.

## 2. Registry inventory and interpretation

At the pinned revision:

| Registry | SKILL.md paths | What is inside |
|---|---:|---|
| skills/ | 169 | Functional skill catalogue. Many entries describe an upstream skill and point to its original repo. |
| design-templates/ | 115 | Prebuilt artifact/template instructions, including slide decks, pitch books, reports, landing pages and visual styles. |
| plugins/ | 272 | Official atoms, examples, scenarios, video templates, community plugins and plugin-spec examples. |
| Other locations | 6 | Additional skill documents outside the three primary roots. |
| **Total** | **562** | Paths, not unique standalone capabilities. |

The plugin breakdown is:
- 13 official atoms;
- 200 official examples;
- 14 official scenarios;
- 23 video-template skills;
- 10 community skill documents;
- 12 plugin-spec example skills.

Many HTML PPT theme entries are focused routing cards that select a master template and a visual variant. They should not be counted as 50 completely separate deck engines.

### Important source-quality warning

Many items in the functional skills registry are catalogue stubs. For example:
- the PPTX catalogue entry points to Anthropic's upstream PPTX skill;
- the slides entry points to OpenAI's skills repository;
- the MiniMax PPTX generator entry points to MiniMax's upstream skill;
- frontend-slides points to an external HTML presentation implementation;
- NanoBanana PPT points to an upstream image-led PPT workflow.

The OpenDesign card advertises the task and trigger keywords, but tells the user/agent to install the upstream bundle to get the original assets, scripts and references. Do not treat the stub as a full implementation.

## 3. Skill and plugin protocol

The portable base format is a directory containing a SKILL.md with YAML frontmatter and Markdown instructions. Side folders may hold:
- assets;
- references;
- scripts;
- examples;
- previews;
- evaluation fixtures.

OpenDesign adds optional metadata under od:
- mode;
- surface;
- scenario;
- category;
- preview type/entry point;
- example prompt and localized examples;
- whether a design-system package must be injected;
- which universal craft references are required;
- critique policy.

Modes include:
- prototype;
- deck;
- template;
- design-system;
- image;
- video;
- audio;
- utility mode is used by functional helpers in some cases.

The deck mode is primarily described as a multi-slide HTML presentation with a browser preview. Its primary output is index.html and its secondary output can be slides.json for PPTX export. The bundled Guizang integration is referenced as a deck-mode implementation.

This matters for our product: OpenDesign's deck experience is often **HTML-first**. It should not be assumed to deliver a completely native PowerPoint deck by default.

## 4. Design-system package architecture

OpenDesign's design-system catalogue contains 151 packages at the pinned revision. The current package shape is:

- manifest.json — machine-readable identity, source/provenance and file paths;
- DESIGN.md — canonical agent-readable design prose;
- tokens.css — compiled semantic token stylesheet.

Optional rich package files include:
- USAGE.md — reading order and usage rules;
- components.html — standalone component fixture;
- components.manifest.json — machine-readable component/token index;
- design-tokens.json — structured design token values;
- tailwind-v4.css — Tailwind mapping;
- assets/ and fonts/;
- preview/ pages;
- source/ evidence and extracted snippets.

The runtime can compose this package into the agent's context. The documented order includes package usage guidance, design prose, import mode, CSS tokens, component information, a rich-file index, universal craft references, and then the active skill/template.

### Why this architecture is useful

It prevents every skill from inventing its own palette/type/spacing decisions. The design system is a separate source of truth that multiple skills can read.

For Legend-Level PPT Skills, build an equivalent presentation design-system package:
- theme manifest;
- semantic colour tokens;
- type scale and font roles;
- spacing/grid/margin rules;
- chart palette and chart-specific tokens;
- reusable PowerPoint layout/component definitions;
- icon/asset catalogue;
- logo and attribution rules;
- slide chrome/header/footer rules;
- explicit do/don't guidance.

## 5. OpenDesign deck-making families

OpenDesign contains several different presentation approaches. They are not interchangeable.

### A. Native PPTX generation route

The registry advertises three upstream routes:
- Anthropic PPTX skill;
- OpenAI slides skill;
- MiniMax PptxGenJS generator.

The relevant wrapper entries point to their upstream sources. The implementation advice is to use PptxGenJS for native PPTX creation where the upstream skill supports that route. The actual full logic lives upstream; the OpenDesign cards alone do not give us every script or implementation detail.

**Use this route when:** editable PowerPoint objects, native charts and direct PPTX file output are the priority.

### B. HTML PPT Studio

The master HTML-PPT template identifies:
- 36 visual themes;
- 15 full-deck templates;
- 31 single-page layouts;
- 27 CSS entrance animations;
- 20 Canvas FX animations;
- a keyboard runtime;
- a presenter-mode feature;
- a Chromium rendering script.

The shared design tokens live in assets/base.css. Themes override the same variables, including background/surface/border/text/accent/semantic colours, gradients, radii, shadows, sans font and display font.

The 31 layout types include:
- cover, contents and section divider;
- bullets, two-column, three-column and quote;
- large statistic, KPI grid, table;
- bar, line, pie and radar charts (Chart.js);
- code, diff and terminal;
- flow diagram, architecture diagram, process steps and mind map;
- timeline, roadmap, Gantt, comparison, pros/cons and checklist;
- image hero and image grid;
- CTA and thank-you ending.

The HTML deck uses one section element per slide. The runtime handles navigation, theme cycling, animation selection, fullscreen, presenter mode, overview and deep links.

#### Presenter mode

Pressing S opens a separate presenter window with:
- current-slide preview;
- next-slide preview;
- speaker script;
- timer and slide navigation.

The preview frames load the actual slide HTML, so they share theme and layout rather than approximating it. The windows synchronise with BroadcastChannel/postMessage and keep the same navigation state.

The skill recommends 150–300 words of colloquial speaker notes per slide for a specific presenter-mode deck family. Presenter-only text must stay in hidden notes, not become audience-facing slide content.

### C. Guizang / magazine-web PPT

This route makes a horizontal-swipe HTML deck in an editorial/e-ink visual style. Its workflow is:
1. infer a design direction;
2. clarify audience, duration, source material, image needs, theme and hard constraints;
3. copy the seed HTML template;
4. replace required placeholders;
5. select one of five fixed themes;
6. check that referenced CSS classes exist;
7. plan theme rhythm through the deck;
8. select from a layout catalogue;
9. obey image crop rules;
10. check against the quality checklist;
11. preview in the browser;
12. iterate.

Five theme presets are named in the template README:
- Ink Classic;
- Indigo Porcelain;
- Forest Ink;
- Kraft Paper;
- Dune.

The skill insists on restraint, typographic hierarchy, whitespace, real images and a coherent visual rhythm. It discourages custom palette overrides so the chosen style remains coherent.

### D. Keynote-style HTML deck

The template defines a 1280×720 page. A slide is one HTML section. Each screen is intentionally minimal: a large title, a few supporting lines, a data visual or a quote. It includes current/total slide indicator, keyboard left/right navigation, URL hash and fade entry.

Use it for keynote-style, minimal presentation experiences in a browser, not for dense analytical decks.

### E. Swiss International deck

The Swiss deck has a disciplined, rational grid and fixed theme choices. It is aimed at facts, product analysis and methodology, with restrained decoration. This style is the opposite of the more narrative/e-ink Guizang style. Do not mix the palettes/visual motifs of unrelated theme families.

### F. IBM / investment-banking pitch book

The IB Pitch Book is a specialised decision-deck pattern for strategic alternatives and growth-equity / investment-banking audiences:
- confidentiality ribbon;
- bank/project identity;
- market/sector context;
- trading comparables;
- precedent transactions;
- valuation football field;
- DCF summary and sensitivity matrix;
- strategic alternatives matrix;
- recommendation and process;
- disclaimers and sources.

It requires a provenance log for each figure: source type, source name, freshness/as-of date, licensing and confidence. It distinguishes public filing, licensed vendor data, management-provided input, user-provided figures and assumptions. It warns against presenting untraceable numbers as facts.

This is an excellent example of combining financial-content rules and visual-layout conventions in a single domain template.

### G. PPTX ↔ HTML fidelity audit

This is one of the most technically valuable OpenDesign skills for our PowerPoint system. It explains why HTML layout and PowerPoint export are different rendering worlds.

The audit procedure:
1. Extract actual PPTX shapes, geometry and text-run typography.
2. Inspect HTML source slide-by-slide.
3. Build a severity-ranked audit table.
4. Identify root causes, not just individual slide symptoms.
5. Re-export with geometry constraints.
6. Run an automated verifier.

The skill defines a 16:9 canvas of approximately 13.333 × 7.5 inches. Content elements must end before a reserved footer rail (default content cap around 6.70 inches; footer around 6.85 inches). It uses a vertical cursor to position blocks in reading order and raises an overflow error if the content budget is exceeded. Hero slides compute a vertical centering budget instead of starting from the top margin.

It explicitly preserves italic formatting for rich-text runs and checks the bounding boxes of shapes, not just where the text glyphs end. Its scripts include:
- scripts/extract_pptx.py;
- scripts/verify_layout.py.

Its references include layout discipline, font discipline and an audit-table template. The output is accepted only when all shapes stay inside canvas bounds and no content object intrudes into the footer rail.

**This is a transferable engineering lesson:** layout needs geometric constraints and assertions, not purely visual judgement.

## 6. Media and image-generation architecture

OpenDesign separates generation from final composition. The media-generation scenario selects one atom according to the project kind:
- image → media-image;
- video → media-video;
- audio → media-audio.

The default scenario stages are:
1. discovery;
2. plan;
3. generate;
4. critique loop.

The image/video/audio atom receives a prompt, supported aspect ratio and optional provider. The configured provider can be the user's chosen image/video/audio service. Output media is saved to the project and registered as a live artifact for preview. The critique loop evaluates the result and iterates within a bounded number of attempts.

Additional skill wrappers advertise providers/workflows such as:
- OpenAI image generation;
- Google Imagen;
- Fal image generation/edit/restoration/upscaling and video tools;
- Venice image generation/editing;
- Replicate;
- NanoBanana PPT;
- image-enhancement and ecommerce product-image workflows;
- Sora and Remotion/HyperFrames for video.

Some are catalogue cards pointing to upstream bundles, not complete provider implementations in the current OpenDesign directory.

**PPT principle:** the media provider should create a discrete image asset. The PPT layout engine decides where it goes, how it is cropped and which text/chart remains editable.

## 7. Other skills relevant to design/PPT

Examples of useful functional entries in the 169-skill registry:
- design-brief — turns a brief into design-system/visual requirements;
- design-md — creates a design system context for other tasks;
- design-extract — retrieves design tokens from source;
- design-review — critiques an existing visual artifact;
- theme-factory — applies a theme to an artifact;
- color-expert — extensive colour science and palette reference;
- D3 visualization — structured chart/visual data presentation;
- hand-drawn-diagrams — diagramming in a hand-drawn visual language;
- creative-director — creativity frameworks and concept development;
- imagegen / Imagen / Fal / Venice / Replicate — media provider routes;
- pptx / slides / pptx-generator — upstream PPTX routes;
- ppt-keynote / guizang / Swiss deck / HTML PPT — HTML deck families;
- pptx-html-fidelity-audit — export correctness;
- hyperframes / Remotion / GSAP — motion and video rather than ordinary PPT layout.

The 169 path inventory is in the machine-readable index. Individual skills whose entries are upstream stubs must be followed to their source repository to recover their full implementation.

## 8. Tool and framework map

| Layer | Technologies or mechanisms named in the repository |
|---|---|
| Product application | Node.js, TypeScript/JavaScript, pnpm, Next.js, React, Express, SQLite, Electron/desktop app, local daemon |
| Agent connection | MCP server, runtime adapters, plugin and skill registry, CLI |
| HTML slide authoring | HTML, CSS, JavaScript, static files, design tokens |
| Charts | Chart.js; D3 and other chart tools are advertised in separate skills |
| Motion | CSS animations, Canvas FX, GSAP, HyperFrames, Remotion |
| 3D/effects | WebGL/WebGL2, Three.js, shaders, Canvas |
| PPTX route | PptxGenJS (native object generation), upstream PPTX skills |
| HTML-to-PPTX QA | Python, python-pptx-style extraction and geometry verification |
| Browser QA | Managed Chromium render, PNG captures, visual inspection |
| Design systems | DESIGN.md, tokens.css, manifest.json, optional components.html, Tailwind mapping |
| Media providers | Configured image/video/audio providers and optional provider-specific skills |

The exact app dependency versions should be read from the package manifests at the pinned commit. Do not assume every skill uses every framework listed here.

## 9. Recommended OpenDesign ideas for Legend-Level PPT Skills

Adopt:
- strict separation of skill instructions, design templates and runtime tools;
- packaged design systems with structured tokens and usage rules;
- specialist atoms for inspect, extract, plan, generate, critique and repair;
- provider-agnostic image-generation interface;
- one or more master deck workflows with reusable slide archetypes;
- presenter notes, if desired;
- geometric overflow rails and scripted PPTX extraction/verification;
- critic loop with a bounded iteration budget;
- source/provenance tracking for financial and analytical figures.

Do not copy directly:
- HTML-first output when the user asked for editable PPTX;
- large bundles of theme-only cards as if they were engines;
- browser effects as a default in ordinary business decks;
- provider wrappers without checking whether the upstream skill is actually installed;
- arbitrary template conversion that may flatten native PowerPoint objects.

## 10. Limitations and verification needs

- OpenDesign is a large project with multiple registries; path counts are not a measure of unique working implementations.
- Several entries are catalogue pointers. Read the upstream repository before using its code or dependencies.
- HTML-to-PPTX fidelity must be independently tested across PowerPoint and alternative rendering environments.
- The presence of a style/template file does not prove that it is accessible, responsive, legally reusable or native-PPTX editable.
- The 151 design-system count and other repository catalogue claims are the project's own documentation, not a benchmark.

