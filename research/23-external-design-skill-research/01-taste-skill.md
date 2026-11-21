# 01 — Leonxlnx/taste-skill: Art Direction, Visual Assets and Design Quality Gates

## Repository identity

- Repository: https://github.com/Leonxlnx/taste-skill
- Pinned source revision: f6b76575f949707b4e3c37cd86cb44b0b98643e8
- Root license observed at this revision: MIT. Check the licenses of bundled fonts, photographs, textures, shaders, third-party code and each asset group separately.
- Tree inventory: 1,663 files, one primary SKILL.md. This is a very asset-heavy repository, not a collection of 1,663 independent agent skills.
- Primary skill: skills/taste-skill/SKILL.md.
- Core scope: high-quality frontend page design and redesign, especially landing pages, portfolios and product pages. It explicitly warns that it is not intended as a generic dashboard, data-table or multi-step product UI generator.

Pinned source:
- [Repository README](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/README.md)
- [Primary skill instructions](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/SKILL.md)
- [Effects library guide](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/assets/effects/README.md)
- [Scene library guide](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/assets/objects/_scenes/README.md)
- [Print core assets](https://github.com/Leonxlnx/taste-skill/blob/f6b76575f949707b4e3c37cd86cb44b0b98643e8/skills/taste-skill/assets/objects/_print-core/README.md)

## 1. The core philosophy

The skill's core idea is that design quality is not achieved by sprinkling gradients, rounded cards and generic UI elements onto a page. It begins by reading the intent, industry, audience and aesthetic signals, then committing to a coherent visual direction.

It treats design rules contextually. Not every pattern should fire on every brief. The model is expected to:
1. infer what sort of product, service or brand the user is describing;
2. identify relevant aesthetic direction and avoid mismatched visual language;
3. state a concise design interpretation;
4. avoid asking unnecessary questions when the brief is already clear;
5. select only the assets, layouts and effects that support the selected direction.

The skill is deliberately narrow. Its rules are written for landing pages, portfolios and redesigns, rather than dense enterprise dashboards. This scope restriction is valuable: an agent that applies editorial landing-page rules to a KPI dashboard will create the wrong density, information architecture and interaction model.

## 2. Brief inference and category routing

The source skill distinguishes business/product kinds such as:
- software;
- gaming;
- technology;
- product;
- service;
- place.

The category affects visual choices, image selection, hero composition and available effects. For example, a technology product may justify terminal imagery, precise grids or procedural objects; a place or hospitality brand may need photography and spatial storytelling rather than shader-driven decoration.

The practical idea for our PPT system is to infer a visual context before choosing a style. A presentation about an industrial incident, a luxury product, a university research topic and a financial performance report should not all receive the same visual vocabulary.

### Taste signals

The skill encourages the agent to read signals from:
- the nouns and verbs in the brief;
- product category and audience;
- the emotional tone and price/quality position;
- user-provided reference images or sites;
- assets already present in the project;
- the intended conversion or communication goal.

The source skill is not a universal taste model. It is a specific art-direction policy for a web page domain. Reuse the method, not its exact styling defaults.

## 3. Architecture and asset libraries

The repository is large because it packages an opinionated frontend starter and a catalogue of assets/effects. The following modules are visible in the skill and source tree.

### A. Starter and style foundation

- assets/starter.html: a starting HTML composition.
- assets/system.css: common design rules and structural styles.
- assets/layout/layout.css: shared layout patterns.
- assets/layout/deal.mjs: layout decision/selection logic.

These files turn the written style rules into a reusable base, rather than asking the model to re-create CSS conventions from zero each time.

### B. Layout system

The layout chooser contains 11 hero patterns:
- split;
- centred;
- product;
- photo;
- place;
- collage;
- editorial;
- word;
- film;
- statement;
- triptych.

These are not merely decorative labels. They describe different ways to allocate the initial viewport to a headline, subject image, product interface, location, typography or a multi-panel composition.

**PPT transfer:** create a layout resolver based on message type and available evidence. A slide's job (statistic, comparison, recommendation, process, product story, timeline) should determine its geometry. Do not randomly select a layout for visual variety.

### C. Photography and real assets

The skill has a curated photography catalogue in assets/photos/photos.json, bundled Commons imagery in WebP sets and support for retrieving new photographs from Unsplash.

The instructions emphasise using real, relevant imagery rather than generic placeholder visuals. Photo credits and attribution should be preserved. Images should be chosen for subject, crop, lighting and the visual role they play in the composition.

Important distinction:
- A real photograph is a separate asset.
- A generated image is a separate asset with its own provenance.
- A slide itself should remain composed of editable PowerPoint text and data objects around that image.

For our deck generator, asset selection should be an explicit stage with an asset manifest, not an incidental result of asking the model to “add some images”.

### D. Effects and scenes

The repository provides effect modules and scene/3D-object collections:
- scripts/effects.mjs;
- assets/scenes/;
- assets/objects/;
- assets/objects/_scenes/;
- assets/objects/_print-core/;
- product-render/photo-kit groups.

Procedural 3D, scenes and WebGL effects are meant to support selected tech/software/gaming visual directions. They are not intended to be inserted everywhere.

A key constraint documented in the source is limiting the number of simultaneous WebGL contexts (maximum four) and providing static or reduced-motion fallbacks. This is a useful example of treating visual ambition and runtime cost as a trade-off.

**PPT transfer:** complex 3D or WebGL effects can be converted into a rendered still or short video asset, but should remain optional. Do not make every slide depend on a live browser shader.

## 4. Runtime, libraries and tools

The repository is primarily a local frontend generation environment:
- Node.js 22 or newer;
- HTML, CSS and JavaScript;
- ES modules and small Node scripts;
- Chromium/Chrome/Edge for browser rendering and screenshot QA;
- WebGL / WebGL2 for effects and procedural visuals;
- optional FFmpeg for media-related processing;
- network access for fetching new fonts, photography and selected assets;
- bundled assets can provide an offline fallback.

The repository tree did not expose a root package.json in the inspected snapshot. Do not invent a package manager or dependency list from the repository's appearance. Read the individual scripts and asset README files before claiming an exact external package dependency.

## 5. The quality-assurance pipeline

The strongest reusable idea is its multi-layer browser QA gate.

Scripts visible in the source include:
- scripts/start.mjs — prepares a design direction, palette and font selection;
- scripts/icons.mjs — loads/handles local SVG icon assets;
- scripts/effects.mjs — applies visual effects;
- scripts/moments.mjs — manages visual moments;
- scripts/consistency.mjs — checks consistency;
- scripts/perf.mjs — performance-oriented checks;
- scripts/shoot.mjs — browser capture;
- scripts/gate.mjs — completion gate;
- scripts/copy-lint.mjs — wording/copy validation;
- assets/layout/check.mjs — layout-related checks.

The browser check is run at multiple viewport widths, including desktop, tablet and mobile sizes (1440, 1024, 820, 768 and 390 are listed in the skill). It checks for problems such as:
- empty or missing visual assets;
- failed shaders or WebGL contexts;
- contrast reductions;
- misalignment and section-height drift;
- placeholder copy;
- invented addresses or ungrounded content;
- slow-network image failures.

The gate is designed to block fixable failures. The skill describes a limited number of repair cycles (up to three) before completion.

### Why this is important

A design agent cannot evaluate its output solely from the HTML/CSS it wrote. It must render the result in the actual presentation environment and inspect what the viewer sees.

For PPT:
- use the actual target slide dimensions;
- render every slide;
- compare against the design system or reference deck;
- detect overflow/overlap and visual drift;
- check font availability and chart labels;
- require the final rendered deck to pass a checklist.

## 6. How a request is processed

A practical reconstruction of the skill workflow is:

1. **Read the brief.** Identify product type, audience, purpose, tone and hard constraints.
2. **Choose an art direction.** Select a coherent visual world appropriate to the category.
3. **Choose a hero/layout pattern.** Use the layout resolver rather than inventing an arbitrary structure.
4. **Select typography and palette.** The start script chooses from curated palette and type data.
5. **Select assets.** Use bundled or user-approved assets and preserve credits.
6. **Compose the page.** Use starter, system CSS, layout CSS and components.
7. **Add only justified effects.** Avoid overuse and respect performance/reduced-motion constraints.
8. **Render and inspect.** Use a real Chromium browser at multiple widths.
9. **Run consistency/performance/copy gates.**
10. **Repair and rerun.** Complete only after the quality gate passes or limitations are reported.

This is a reconstruction from the public skill and its files, not a claim that all internal orchestration is exposed.

## 7. What we should adopt for PPT

| Taste Skill method | PPT adaptation |
|---|---|
| Brief inference before style | Presentation audience, decision and visual direction classifier |
| Category-specific layouts | Slide archetype selection based on communication purpose |
| Curated typography/palette data | Versioned theme and typography token library |
| Real asset catalogue | Asset retrieval/generation with source, rights and crop metadata |
| Coherent art direction | One visual system per deck; no random style mixing |
| Controlled WebGL/effect budget | Optional motion/3D budget; static fallback |
| Multi-viewport browser QA | Slide-size render QA and target PowerPoint renderer tests |
| Copy and consistency lint | Fact, terminology, title, footnote and visual consistency checks |
| Finish gate | Pass/fail QA report before delivery |

## 8. What not to copy literally

- Do not use the 11 web hero layouts as the complete PPT layout catalogue.
- Do not make WebGL/live browser effects a mandatory PowerPoint feature.
- Do not apply landing-page section/scroll logic to slide navigation.
- Do not use unsplash retrieval as a substitute for a controlled licensed image library.
- Do not transfer the software/gaming preference for terminal aesthetics to financial, academic or public-sector presentations by default.
- Do not claim a fully working PowerPoint is produced by this repo; its main skill is a frontend design skill.

## 9. Evaluation questions for our own implementation

1. Does the selected art direction fit the brief, audience and content?
2. Are image subjects relevant and compositionally useful?
3. Do repeated image assets have coherent colour and style?
4. Does the layout support the message rather than decorate it?
5. Does every rendered slide/page pass visual and structural checks?
6. Are assets licensed/attributed and all generated images separately recorded?
7. Can the output be opened and edited in the target format?

The last question is specific to our PPT system and must be measured independently.