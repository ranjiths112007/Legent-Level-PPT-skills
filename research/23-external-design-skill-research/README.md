# External Design Skill Repository Research

**Nine repositories. A cross-referenced engineering handbook for design intelligence, visual systems, image creation, diagrams, motion, presentation craft and agent workflows.**

> Snapshot: 21 November 2026. Research is pinned to exact commit revisions. This is documentation and source-code inspection, not a controlled performance benchmark.

## What is included

This knowledge base studies nine repositories supplied for Legend-Level PPT Skills. It explains each repository's purpose, internal architecture, skill families, actual workflows, frameworks and libraries, tools, assets, limitations, and what can be adapted to a professional AI presentation system.

| Repository | Main area | Snapshot inventory |
|---|---|---:|
| [taste-skill](01-taste-skill.md) | Art direction, real asset libraries, anti-generic design and browser QA | 1,663 files; 1 main skill |
| [open-design](02-open-design.md) | Skills, design templates, design systems, plugin workflows, HTML decks and media generation | 14,308 files; 169 functional skill docs, 115 design-template docs, 272 plugin docs |
| [diagram-design](03-diagram-design.md) | Semantic diagram planning, branded SVG, import/export and validation | 776 files; 1 main skill |
| [ui-ux-pro-max-skill](04-ui-ux-pro-max.md) | Data-driven UI/UX recommendations, style/palette/font/icon/chart/stack datasets | 742 files; 7 unique core skills (13 skill paths including copies) |
| [stitch-skills](05-stitch-skills.md) | Prompt improvement, Stitch generation, design-system extraction, code conversion and build | 91 files; 16 skills |
| [awesome-design-skills](06-awesome-design-skills.md) | Reusable visual-style design instruction presets | 215 files; 67 skills |
| [emilkowalski/skills](07-emilkowalski-skills.md) | Motion design, interaction, performance, animation review and design engineering | 36 files; 20 skills |
| [designer-skills](08-designer-skills.md) | Research, strategy, design systems, interaction, UI, prototyping, operations and critique | 205 files; 111 skill documents |
| [jakubkrehel/skills](09-jakubkrehel-skills.md) | Strict interface quality, typography, colour, layout, accessibility, motion and variants | 90 files; 16 skills |

## Main findings

1. **A strong design agent needs several distinct kinds of intelligence.** It needs communication/story structure, a design system, layout composition, image/diagram planning, deterministic rendering and a quality gate. One giant prompt is not a substitute for those components.
2. **Taste requires constraints and context.** Taste Skill and the visual-style libraries encode deliberate design direction, asset choices, palette/type restrictions, layout rhythm and anti-patterns. Applying a style without understanding audience/content is still bad design.
3. **A design system should be machine-readable and reusable.** Token layers, component inventories, font pairings, semantic colour roles, usage rules, assets and examples should be stored separately from each task's content.
4. **Diagrams need semantic planning.** Diagram Design and the designer skill collections provide a much stronger approach than asking a model to “draw a nice diagram”: determine the semantic relationship first, choose a suitable diagram family, lay out at controlled density, then validate.
5. **Image generation should be a separate asset lane.** Generate images as separate assets, keep them stylistically consistent, and place them in a deliberate composition. Keep exact titles, labels, numbers and charts as editable text/data.
6. **Design quality is iterative.** These repos converge on critique, targeted refinement, browser/render review, worst-case content testing and a measurable quality gate.
7. **Many skills are not PowerPoint generators.** Most of the nine repositories teach frontend UI, brand systems, diagramming or style. We should extract transferable principles and preserve the native PowerPoint output requirements in our own implementation.

## AI reading order

Start with [00-ai-reading-guide.md](00-ai-reading-guide.md), then read the repository deep dives (01–09). The implementation decision documents are [10-cross-repository-patterns.md](10-cross-repository-patterns.md), [11-frameworks-libraries-tools.md](11-frameworks-libraries-tools.md), [12-what-to-adopt-for-ppt.md](12-what-to-adopt-for-ppt.md), and [13-source-and-license-register.md](13-source-and-license-register.md).

For a programmatic inventory of checked SKILL.md files, see catalogs/external-skill-path-index.json.

## The nine pinned source revisions

| Repository | Pinned revision | License at checked revision |
|---|---|---|
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/f6b76575f949707b4e3c37cd86cb44b0b98643e8) | f6b76575f949707b4e3c37cd86cb44b0b98643e8 | MIT |
| [nexu-io/open-design](https://github.com/nexu-io/open-design/tree/e033aad1d15a9d4084316e5223f2c6597fd32619) | e033aad1d15a9d4084316e5223f2c6597fd32619 | Apache-2.0 |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design/tree/d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0) | d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0 | MIT |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/2de1134dc4d1cfe112934611ae5803ae17a1bd7e) | 2de1134dc4d1cfe112934611ae5803ae17a1bd7e | MIT |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills/tree/62fdcd679747aca0792e5dd6591b10ddfad56825) | 62fdcd679747aca0792e5dd6591b10ddfad56825 | Apache-2.0 |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills/tree/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8) | f631a09b4fcc0166f2e2c1a8c81906ef680c57e8 | MIT |
| [emilkowalski/skills](https://github.com/emilkowalski/skills/tree/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c) | 64eb3deb9a5fbfa041faf783e0bc3fd635872e9c | MIT |
| [owl-listener/designer-skills](https://github.com/owl-listener/designer-skills/tree/9a6930cf84a822eb458624bd11c61aac5bbdf224) | 9a6930cf84a822eb458624bd11c61aac5bbdf224 | MIT |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills/tree/672ae44ace6aaed65b86cbb1e2fd6fbea0e79578) | 672ae44ace6aaed65b86cbb1e2fd6fbea0e79578 | MIT |

## Important inventory caveats

- The combined tree scan finds **807 SKILL.md paths** across the nine repositories. This is a path count, not a count of 807 unique independent systems.
- OpenDesign has separate functional-skill, design-template and plugin registries. Many plugin examples are visual templates or route cards; many functional entries only advertise upstream skills. The relevant deep dive describes this difference.
- UI/UX Pro Max has duplicated skill copies for different install/CLI layouts. Its 13 file paths are 7 unique core skills.
- Taste Skill has 1 primary skill but over 1,600 supporting assets, data and implementation files.
- The Designer Skills README advertises a wider skill/command ecosystem than the number of separate SKILL.md files discovered in the pinned tree. Both counts are documented separately rather than conflated.
- The checked source revision can change after this research. Refresh the pinned commits and regenerate the inventory before treating it as current.

## Evidence and reuse rules

- Source skill prose is paraphrased, not copied wholesale.
- Code, visual assets, fonts, image packs, templates and embedded dependencies may carry different licenses from the repository's root license.
- “Open source” does not automatically mean every third-party asset or model output is free for every commercial use.
- No quality ranking is asserted without a controlled, same-input benchmark.