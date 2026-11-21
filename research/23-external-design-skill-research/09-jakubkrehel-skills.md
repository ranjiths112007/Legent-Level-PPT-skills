# 09 — jakubkrehel/skills: Strict Interface Quality, Layout, Colour and Accessibility

## Repository identity

- Repository: https://github.com/jakubkrehel/skills
- Pinned revision: 672ae44ace6aaed65b86cbb1e2fd6fbea0e79578
- Root license observed: MIT.
- Snapshot: 90 files, 16 main skills plus shared agent guidance/reference material.
- Core focus: inspect, build, improve and explain interfaces through explicit design-quality rules.

Sources:
- [Repository README](https://github.com/jakubkrehel/skills/blob/672ae44ace6aaed65b86cbb1e2fd6fbea0e79578/README.md)
- [Agent guidance](https://github.com/jakubkrehel/skills/blob/672ae44ace6aaed65b86cbb1e2fd6fbea0e79578/AGENTS.md)
- [Skills directory](https://github.com/jakubkrehel/skills/tree/672ae44ace6aaed65b86cbb1e2fd6fbea0e79578/skills)

## 1. Skill inventory

The 16 skills are:

1. afk — create improvements in an autonomous branch/workflow.
2. better-accessibility — keyboard, focus, ARIA, forms, controls, WCAG, screen readers, zoom and motion considerations.
3. better-colors — build palettes, semantic colour tokens, contrast and colour-format guidance.
4. better-interface — general visual interface quality across colour, type, layout, copy, accessibility, finish and motion.
5. better-layout — responsive grouping, alignment, spacing, reading order and RTL-aware layout.
6. better-motion — design motion with intentional timing, easing, distance and state continuity.
7. better-typography — font selection, type scale, hierarchy, OpenType and line wrapping.
8. better-ui — component surface quality, icons, borders, radii, shadows, interaction states and optical alignment.
9. better-writing — concise, appropriate UX/content writing.
10. break — stress-test interfaces with challenging or extreme input data.
11. build-design — convert design references (such as images/Figma) into code.
12. explain-interface — explain a UI from a URL or screenshot.
13. interface-review — review an existing branch/PR for visual regressions and UI problems.
14. state-machine — reason about component states and transitions.
15. upskill — examine previous work and suggest reusable skills/hooks/automation.
16. variant — create differentiated design variants for comparison.

## 2. The shared model: inspect, plan, build, test and explain

The repo's global agent guidance establishes common operating expectations. The specific skills divide responsibilities so an agent doesn't try to solve every design issue with a broad redesign.

Useful conceptual boundaries:
- better-layout creates spatial structure; critique of existing composition should use the relevant review skill.
- better-colors creates and names colour systems; contrast/accessibility is checked separately.
- better-typography defines type hierarchy; wrapping/overflow is checked during rendering.
- better-ui focuses component surfaces and states; better-accessibility evaluates usability and compliance.
- better-motion describes motion; interface QA checks that it remains understandable and performant.
- state-machine models states; break supplies stress cases; interface-review inspects the result.

This division is valuable because the same agent can use focused specialist knowledge and still deliver one coherent output.

## 3. Colour system method

The better-colors skill and reference set cover:
- raw palette generation;
- semantic colour roles;
- light/dark themes;
- contrast measurement;
- accessible colour pairs;
- token naming;
- format conversion (hex, RGB, HSL and related representations);
- reporting and auditing.

Its design-token approach can be represented in three tiers:
1. raw/global palette values;
2. semantic alias tokens;
3. scoped component tokens.

For example, slide text should refer to a semantic foreground role, not directly to a raw hex value sprinkled through every shape. A chart uses semantic series roles so that all charts use a coherent encoding.

**PPT application:** store background, surface, title, body, secondary text, border, accent, success, warning, error and chart-series colours in a theme manifest. Run contrast checks for both text and chart labels.

## 4. Typography method

The better-typography skill deals with:
- font selection and pairing;
- role-based type hierarchy;
- scale and line height;
- weight and emphasis;
- OpenType features;
- wrapping, truncation and text fit.

For PowerPoint, define roles rather than arbitrary per-slide sizes:
- display/cover;
- slide title;
- section heading;
- body;
- chart title/label;
- table;
- caption/source/footnote.

The rendered deck is the final check because font availability and text metrics differ between renderers. A layout that fits in a browser or LibreOffice may overflow in Microsoft PowerPoint.

## 5. Layout and reading order

The better-layout skill covers:
- grouping related content;
- grid and alignment;
- spacing and whitespace;
- responsive adaptation;
- reading order;
- directionality and right-to-left layouts.

PowerPoint has a fixed canvas for each slide, but the same principles still apply:
- create a grid;
- align repeated blocks;
- establish predictable margins;
- group related labels and values;
- keep the reading order consistent;
- design language-specific variants rather than assume Latin text width.

For multilingual decks, RTL must be treated as an intentional layout mode. Simply changing the text alignment to right is not sufficient for all diagram, chart and navigation semantics.

## 6. Better UI and state modelling

The better-ui skill evaluates details such as:
- surface treatment;
- border thickness;
- corner radii;
- shadows/elevation;
- icon family/weights;
- optical alignment;
- focus/hover/disabled/selected states.

The state-machine skill makes interactive state explicit. The break skill then generates difficult state/data situations.

PPT transfer:
- reusable shape components should have explicit variants (normal, selected, warning, negative, muted);
- chart/diagram nodes should have semantic state rules;
- slide controls/presenter views need state coverage;
- tables should test null, long and overflow values.

Most hover/focus state knowledge is for UI rather than static slide output; use it only for interactive HTML deck or presentation tooling.

## 7. Accessibility

The accessibility skill considers:
- keyboard navigation;
- visible focus;
- semantic labels/ARIA where applicable;
- form validation;
- screen-reader behaviour;
- zoom and text resizing;
- reduced motion;
- WCAG 2.2 considerations.

Slide-specific translation:
- maintain sufficient text contrast;
- do not use colour alone to distinguish chart series/status;
- provide meaningful text alternatives for key visuals;
- use readable type sizes from the intended viewing distance;
- maintain logical reading order;
- ensure exported PDF retains searchable/selectable text where possible;
- avoid motion that blocks comprehension;
- include captions/notes where they add access.

## 8. Variant, review and upskill loops

The repository provides three useful learning loops:
- variant: generate multiple distinguishable options to choose from;
- interface-review: inspect a result and give concrete fixes;
- upskill: turn explicit lessons from prior work into reusable guidance.

For our system:
- create design alternatives before a deck theme is locked;
- use slide-level and deck-level reviews after rendering;
- convert only approved repeated user corrections into reusable company rules.

## 9. Frameworks and tools

The main skills are technology-agnostic design guidance. The repo also supports code workflows and design-to-code conversion. Its tree contains root agent instructions, skill files and supporting references; the root license does not imply that external Figma assets or fonts used by a project are licensed with the skill.

Do not infer a single frontend runtime for the whole repo. Inspect the actual user's project and choose the matching build tool/library.

## 10. Limitations and PPT relevance

- It is an interface design/quality suite, not a PowerPoint writer.
- Some recommendations assume responsive web behaviour; PPT is fixed-canvas unless the output is a browser deck.
- Accessibility and contrast rules transfer strongly, but component-specific ARIA/hover guidance does not directly apply to static slides.
- The skill's strictness is useful as a quality bar, but not every stylistic rule should override brand guidelines or a reference template.