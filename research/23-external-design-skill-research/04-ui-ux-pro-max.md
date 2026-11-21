# 04 — nextlevelbuilder/ui-ux-pro-max-skill: Data-Driven Design Intelligence and UI System Routing

## Repository identity

- Repository: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Pinned revision: 2de1134dc4d1cfe112934611ae5803ae17a1bd7e
- Root license: MIT.
- Snapshot: 742 files; 13 SKILL.md paths but 7 unique primary skills (copies are included for CLI packaging).
- Core purpose: provide an AI assistant with structured design knowledge and search/recommendation data, rather than relying only on generic free-form design prompts.

Sources:
- [Repository README](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/2de1134dc4d1cfe112934611ae5803ae17a1bd7e/README.md)
- [Master UI/UX skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/2de1134dc4d1cfe112934611ae5803ae17a1bd7e/.claude/skills/ui-ux-pro-max/SKILL.md)
- [Slide-design skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/2de1134dc4d1cfe112934611ae5803ae17a1bd7e/.claude/skills/slides/SKILL.md)
- [Design-system skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/2de1134dc4d1cfe112934611ae5803ae17a1bd7e/.claude/skills/design-system/SKILL.md)
- [UI styling skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/2de1134dc4d1cfe112934611ae5803ae17a1bd7e/.claude/skills/ui-styling/SKILL.md)

## 1. The core architecture

UI UX Pro Max is not one giant design prompt. It combines:
1. a master router skill;
2. specialist skills (design, slides, design system, branding, banners, UI styling);
3. structured style/palette/typography/icon/chart/stack datasets;
4. a command-line search/retrieval mechanism;
5. a design-system generation step that can be saved and reused.

The most important principle is to retrieve relevant design guidance from structured data rather than make a language model invent every design choice from memory.

## 2. Unique core skills

The seven unique main skills found in the repository are:

### A. ui-ux-pro-max — router and data-backed recommendations

The main skill determines the product context and which specialised data to search. It guides a design system before a page is built. It can search for:
- visual style;
- industry/product context;
- colour palette;
- font pairing;
- icon system;
- chart types;
- UX patterns;
- technology stack.

At the pinned snapshot, the skill references collections such as:
- 80 style choices, 51 marked active;
- 194 product/industry palette or reasoning records;
- 74 font pairings;
- 130 UX guidelines;
- 105 icon options;
- 17 GSAP presets;
- 25 chart types;
- 22 technology stack profiles.

These are source-repository dataset counts, not independently quality-ranked recommendations. Verify the data files directly before relying on an exact count in an implementation.

### B. design — design-task routing and art direction

This skill acts as a higher-level dispatcher. It routes requests to specialised logo design, corporate identity, slides, banners, icon creation and social/visual asset workflows.

It advertises:
- approximately 55 logo styles;
- multiple identity-program deliverables;
- a set of banner styles and format variants;
- icon-family styles;
- HTML/social asset creation.

For image generation, the workflow can route across named providers such as Gemini, Atlas Cloud, MuAPI and UberLLM (provider availability/credentials must be checked at runtime). The skill should not be mistaken for a single fixed generator model.

### C. design-system — reusable visual foundations

This skill establishes a tokenised, component-oriented design system. It separates:
- primitive/raw tokens;
- semantic tokens;
- component tokens.

Typical values include colour, typography, spacing, borders, radii, shadows and component states. It emphasises reusing the saved design system and keeping it consistent rather than scattering one-off hard-coded styles throughout the project.

### D. slides — HTML presentation direction

The slide-specific skill describes strategic HTML presentations. It combines narrative/copy planning with design tokens, charts and slide layout strategies. It is a frontend-oriented presentation workflow, not proof of a complete native PPTX object-editing runtime.

For Legend-Level PPT Skills, its slide content and narrative advice can transfer, but the output engine must remain explicit: HTML deck, PDF, image or native PPTX.

### E. ui-styling — component-level build rules

The UI styling skill advocates:
- React-compatible component implementation;
- Tailwind utility styling;
- Radix UI or Base UI primitives;
- reuse of project frameworks such as Next.js, Vite, Remix or Astro;
- responsive and accessible states.

These are primarily web app implementation technologies. They are not required to make a native PowerPoint deck.

### F. brand — identity and consistency

The branding skill covers identity, brand voice, messaging, design token alignment, brand guideline documentation and asset management. It is useful as a source for brand-aware presentation generation: the design system should align with the brand rather than select an arbitrary attractive palette.

### G. banner-design — asset creation and variants

The banner workflow combines requirements, art direction, variants, screenshot review and iteration. It considers size/crop constraints for different media formats and can use images or generated assets where appropriate.

The important process is not “ask image model to make a banner”; it is requirements → concept → variants → preview → review → refine.

## 3. Retrieval and CLI approach

The repository includes a CLI and searchable data. Its design-system recommendations are intended to be generated from a structured query and then persisted.

A sensible implementation sequence:
1. read the current codebase/product context;
2. infer industry and audience;
3. search relevant style/palette/font/UX guidance;
4. build the recommended system;
5. save the design system to a predictable file;
6. reuse it across pages and later tasks;
7. document deviations rather than silently inventing new token values.

The repo includes package.json/lockfiles for its CLI/gallery/stack parts and Python requirements files for some supporting scripts. It also includes an MCP configuration in its stack area. The exact dependencies should be taken from the relevant package manifest, not guessed from the skill names.

## 4. Frameworks and data families

| Family | Purpose | PPT adaptation |
|---|---|---|
| Style catalogue | Select an appropriate design direction | Deck theme recommender |
| Product/industry profiles | Match visual choices to context | Theme choices by presentation type and audience |
| Colour palette records | Suggest semantic colour systems | Background/text/accent/chart colour roles |
| Font pairings | Choose display/body font combinations | Title/body/label type pairing |
| UX guidelines | Encode good interaction and layout practice | Slide legibility, cognitive load and reader flow |
| Icon catalogue | Consistent visual symbols | One icon family per deck |
| Chart catalogue | Select chart type and chart style | Analytical visual selection |
| GSAP presets | Motion recipes for web animation | Optional slide animation language only |
| Technology stacks | Match implementation with host framework | Mostly not used by native PPTX runtime |

The master skill includes chart selection, style, design and technology as separate decisions. That separation is useful: a font choice should not depend on a chart library, and a theme should not silently decide data semantics.

## 5. Image and asset workflow

The repository's branding and banner skills imply a multi-provider image approach:
- infer brand concept and audience;
- select a visual direction;
- generate/retrieve multiple variants;
- review the actual output image;
- choose the strongest composition;
- crop/scale for each target format;
- preserve reusable brand/asset information.

For presentation creation:
- generate a separate asset for each image region;
- reuse a shared image-family prompt/style guide when a deck needs multiple illustrations;
- store asset ID, source/provider, generation instructions and crop metadata;
- keep chart labels, product names and factual text outside the image.

## 6. Why this is valuable for a presentation agent

The biggest transferable idea is a **retrieval-based design system**:
- the model first searches a database of relevant design options;
- it builds a coherent theme;
- the theme is saved;
- downstream slide/layout components use the same tokens.

This is more reliable than asking the model to reinvent typography, colours, icons and chart styles separately on every slide.

A PPT-specific database should add:
- presentation theme archetypes (editorial, Swiss grid, consulting, investor, academic, technical, financial);
- title/body/footnote/citation type scales;
- PowerPoint-safe fonts;
- chart palettes and chart-specific rules;
- slide archetype/layout catalogue;
- imagery treatment and crop patterns;
- editable shape/diagram recipes;
- accessibility and presentation-distance guidelines.

## 7. Limitations

- Many skill paths are duplicated in package/CLI assets; 13 paths are not 13 different core capabilities.
- Style, palette or font data records are not proof of visual superiority.
- The slides skill is frontend-oriented and should not be confused with native PPTX generation.
- Provider names in a skill do not guarantee a working API key, endpoint or quota.
- A structured retrieval result still requires user-context judgement and rendered QA.
- Do not import every React/Tailwind dependency into the PowerPoint engine. The visual knowledge is transferable; the implementation framework is not automatically transferable.