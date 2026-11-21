# AI Reading Guide — External Design and Presentation Skill Research

> Snapshot date: 21 November 2026. All repository links in this research point to pinned GitHub commits so that an agent can inspect the exact source revision reviewed.

## Purpose

This folder is a technical knowledge base for nine external design / presentation skill repositories supplied by the project owner. Its goal is to let a coding agent understand the repositories' capabilities, operating methods, design principles, tools, dependencies, limits, and relevance to an AI PowerPoint creation system without relying on a superficial repository summary.

This is **not** a claim that every source file in every repository has been copied into this project. The source repositories remain the authorities. The research paraphrases the examined instructions, inventories their skill paths, and links back to exact files. When an AI needs a fine implementation detail, it should retrieve the source file linked in the repository-specific document and verify the current pinned version.

## How to read this knowledge base

Read in this order:

1. README.md — scope, repository list, counts, navigation and evidence limits.
2. 01-taste-skill.md — high-quality art direction, real asset libraries and browser QA.
3. 02-open-design.md — large-scale skills/templates/plugins architecture and HTML-first presentation routes.
4. 03-diagram-design.md — semantic diagram selection and editable SVG construction.
5. 04-ui-ux-pro-max.md — structured design intelligence, style/palette/font datasets and CLI.
6. 05-stitch-skills.md — prompt-to-design-system-to-screen-to-code workflow.
7. 06-awesome-design-skills.md — reusable visual-style preset taxonomy.
8. 07-emilkowalski-skills.md — motion craft, interaction, performance and taste learning.
9. 08-designer-skills.md — research, design systems, strategy, presentation structure and critique.
10. 09-jakubkrehel-skills.md — quality gates for colour, typography, layout, accessibility and interface state.
11. 10-cross-repository-patterns.md — shared principles and conflicts.
12. 11-frameworks-libraries-tools.md — consolidated tool and framework map.
13. 12-what-to-adopt-for-ppt.md — concrete product architecture and adoption priorities.
14. 13-source-and-license-register.md — source provenance, license caution and citation conventions.
15. catalogs/external-skill-path-index.json — machine-readable inventory of skill-document paths in the nine pinned repositories.

## Evidence labels

Each analysis distinguishes:

- **Observed in source:** directly stated or implemented in a checked file/tree at the pinned revision.
- **Repository claim:** a capability described by a README or skill but not independently executed or benchmarked here.
- **Inferred workflow:** a reasoned reconstruction from multiple source files.
- **Recommendation:** a proposed technique for Legend-Level PPT Skills, not a claim about the external repository.
- **Unverified:** a detail requiring execution, license verification or current documentation.

## Critical distinctions an AI must preserve

### A skill is not always an implementation

Some repository entries are full instruction sets with scripts, examples, templates and references. Others are catalogue wrappers that advertise an upstream skill and say to install the original bundle. A catalogue wrapper is not equivalent to the full upstream instruction.

### A design style is not a deck generator

A style preset can specify palette, type, texture, motif and spacing but contain no narrative planner, PPTX writer or data pipeline. It should be used as a style vocabulary, not mistaken for an end-to-end product.

### HTML slides are not native PowerPoint slides

An HTML deck can be beautiful, interactive and excellent for browser presentation. Conversion to PPTX can change fonts, layout, SVGs, chart semantics, notes and animation. Always state the output medium and inspect its editability. OpenDesign's HTML deck modes often use HTML as the source artifact and provide PPTX as a secondary export route; this is not the same as editing native PowerPoint objects.

### Images are not data visualizations

Use image models or stock assets for photographic / illustrative material. Use a deterministic chart library, SVG generator or native PowerPoint chart for exact values, labels, axes and tables. Never entrust factual chart numbers to a text-to-image output.

### UI design knowledge transfers selectively

Many of these repositories focus on websites, app screens and frontend engineering. Their hierarchy, colour, typography, spacing, accessibility, motion and critique methods transfer to slides. Their responsive navigation, hover, app states, React components and phone-specific behaviours do not transfer literally to a static slide.

## Recommended retrieval behavior for an AI agent

When the user asks to create a deck:

1. Resolve the presentation task: audience, decision/action, content sources, slide count, format and constraints.
2. Consult 12-what-to-adopt-for-ppt.md.
3. Resolve design direction using 01, 04, 06, 08 and the source deck/design-system, not by randomly mixing presets.
4. For a diagram, consult 03.
5. For image assets, consult the image-provider and consistency policies in 02, 04 and 11.
6. For motion, consult 07 and the relevant OpenDesign motion/video template only when motion is requested.
7. Build through the existing PPTX architecture/research documents already in the parent repository.
8. Render, inspect, fix, re-render. Use the critique framework from 08/09 and QA rules from the parent repo's rendering research.

When the user asks to reproduce an existing PPT:

1. Follow research/19-reference-based-ppt-recreation.md and research/20-reference-deck-workflow-spec.md in the parent repository.
2. Use external style repositories only to understand design craft; do not allow their styling to overwrite the reference deck in exact mode.
3. Preserve the original objects, geometry, charts, theme and master where possible.
4. Apply only manifest-approved edits and verify final renders.

## What this research does not prove

- It does not execute all 807 skill documents.
- It does not independently benchmark visual quality or claim which repository produces the best design.
- It does not verify every optional API key/provider integration or subscription cost.
- It does not prove that every skill works on every agent host.
- It does not prove every library preserves all PPTX features.
- It does not grant permission to copy code, templates, fonts, images or proprietary skill text.

Treat the pinned source repository and the relevant license as authoritative.