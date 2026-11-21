# 11 — Frameworks, Libraries, Data and Tooling Map

> This map separates observed tools from technologies merely mentioned as examples or supported targets. It is not a recommendation to install every dependency.

## How to read this document

- **Observed:** named in the pinned repository's files or implementation.
- **Integration/target:** a service, host or framework the skill is designed to use.
- **Conditional:** may require credentials, an installed host, or a separate upstream project.
- **Not established:** not proven to be a dependency of the repository or the native PPTX runtime.

## Repository-by-repository map

| Repository | Main implementation surfaces | Named tools / libraries / formats | Evidence boundary |
|---|---|---|---|
| Taste Skill | HTML/CSS/JS design starter, asset catalogues, browser-render QA | Chromium/Chrome/Edge, SVG icons, WebP image sets, Unsplash source, WebGL/shader effects | The checked tree did not establish a single package-manager dependency set; inspect individual scripts before pinning runtime packages |
| OpenDesign | Local-first agent workspace, skills protocol, design-system packages, templates, plugin/scenario registry, media and deck workflows | JSON manifests, CSS tokens, Tailwind v4 mapping, HTML, React/web output, Figma/code migration, PPTX/HTML routes, image/video/audio providers | Some catalog entries are upstream wrappers or template selectors, not locally implemented engines |
| Diagram Design | Semantic diagram planner, HTML wrapper, inline SVG, import/export and validation | SVG, HTML, PNG, Skills CLI; Node/Python CI manifests | CI packages do not prove production rendering dependencies |
| UI/UX Pro Max | Searchable data sets, CLI, skills, style gallery and asset workflows | Style/palette/type/icon/chart/stack datasets, React-compatible code, Tailwind, Next.js, Vite, Remix, Astro, GSAP presets, MCP configuration, provider routes | Web stacks are targets for web work, not requirements for native PPTX |
| Stitch Skills | Three plugin groups: design, utilities and build | Stitch MCP, Puppeteer/browser capture, React 18, TypeScript, React Router, React Native, Remotion, Tailwind, shadcn/ui, Radix/Base UI | Stitch MCP is an external generation service; local skills are orchestration/instructions |
| Awesome Design Skills | Markdown visual-style presets | Markdown instructions, design vocabularies and style rules | No native renderer or PPTX engine |
| Emil Kowalski Skills | Motion and interaction skills for product interfaces | React, React Native, React Native Reanimated; platform animation concepts | UI/motion implementation tools; not slide-generation dependencies |
| Designer Skills | Markdown skills and commands; Claude/Gemini plugin manifests | YAML frontmatter, JSON manifests, Python maintenance scripts, Claude Code plugins, Gemini CLI extensions | Presentation command outputs an outline, not a PPTX file |
| Jakub Krehel Skills | Technology-agnostic design and quality instructions plus design-to-code workflows | Colour/type/layout/accessibility guidance; references to project-specific frontend stacks | No single frontend runtime for the whole repository |

## Tool categories and relevance to our PPT system

### 1. Agent skill packaging

- Markdown skill files with metadata and explicit task boundaries.
- Commands/workflows that sequence specialist skills.
- JSON manifests for plugin/extension registration.
- CLI or MCP integrations for external services.

**Use in our project:** keep skills portable and declarative. Put runtime code in a separate tested package; do not pretend Markdown alone performs deterministic PPTX edits.

### 2. Design-system data

- Semantic design tokens (colour, spacing, typography, borders, elevation, motion).
- Component inventories and examples.
- Style/palette/font/icon/chart datasets.
- Manifest and compiled token formats (for example JSON and CSS).

**Use in our project:** create a canonical JSON token model and a PowerPoint adapter. CSS/Tailwind output is useful for HTML previews but should not become the source of truth for native PPTX.

### 3. Browser and visual QA

- Chromium-based rendering and screenshot capture.
- Browser automation/capture through Puppeteer in the Stitch workflow.
- HTML previews and SVG renderers.

**Use in our project:** browser QA is suitable for HTML previews. For PPTX, also render with a PowerPoint-compatible office renderer and test the actual exported deck. A browser screenshot of a separate HTML deck does not verify PPTX fidelity.

### 4. Vector and diagram tooling

- Inline SVG and SVG/PNG export.
- Semantic diagram selection and structured layout rules.

**Use in our project:** use native PowerPoint shapes/connectors for diagrams users need to edit element-by-element; use SVG for complex vector artwork where whole-object editing is acceptable. Track the representation in metadata.

### 5. Frontend frameworks and animation

- React, React Native, TypeScript, Tailwind, Next.js, Vite, Remix, Astro, Remotion, GSAP and animation libraries appear in selected repositories as web/mobile/video implementation targets.
- These are not all dependencies of every skill and are not required for native PPTX generation.

**Use in our project:** keep an optional HTML preview/editor separate from the core PPTX writer. Select only the stack needed for that product surface.

### 6. Image and media providers

- Some repositories describe external image, video or audio providers and MCP integrations.
- Provider availability, model names, credentials, rate limits and licensing can change.

**Use in our project:** define a provider adapter interface and asset manifest. Do not hard-code a provider into the deck planner. Validate generated media dimensions, provenance, rights and visual consistency before placement.

## Native PowerPoint implementation gap

The nine design repositories do not collectively provide a proven native PowerPoint object engine for our requirements. The PPT project still needs its own tested implementation for:

- Reading PPTX packages and slide masters/layouts.
- Mapping slide placeholders and object geometry.
- Creating/updating editable text, shapes, tables and charts.
- Preserving themes, relationships, notes, embedded media and package parts.
- Rendering PPTX to slide images.
- Checking object bounds, overlaps, text fit and data integrity.
- Producing an edit manifest and reversible repair log.

Potential libraries for that engine must be evaluated separately against test decks and feature requirements. Their presence in an external skill repository must not be assumed.

## Dependency-selection rules

1. Pin versions and record the source commit.
2. Distinguish direct dependencies from optional integrations and example targets.
3. Verify license and transitive dependency terms.
4. Build a minimal proof-of-concept before adopting a library.
5. Test with real decks containing charts, tables, masters, fonts, images, notes and grouped shapes.
6. Keep rendering and editing separate enough that one cannot silently certify the other.
