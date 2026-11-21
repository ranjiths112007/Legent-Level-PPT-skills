# 05 — google-labs-code/stitch-skills: Prompt-to-Screen, Design Systems and Code Handoff

## Repository identity

- Repository: https://github.com/google-labs-code/stitch-skills
- Pinned revision: 62fdcd679747aca0792e5dd6591b10ddfad56825
- Root license observed: Apache-2.0.
- Inventory: 91 files, 16 SKILL.md files, split into three plugin groups.
- Core purpose: orchestrate Google Stitch design-generation capabilities, persist design-system context, extract designs from existing code/screenshots, iterate on generated screens and turn them into frontend code.

Sources:
- [Repository README](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/README.md)
- [Generate design skill](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/plugins/stitch-design/skills/generate-design/SKILL.md)
- [Manage design system](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/plugins/stitch-design/skills/manage-design-system/SKILL.md)
- [Extract design MD](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/plugins/stitch-design/skills/extract-design-md/SKILL.md)
- [Prompt enhancement](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/plugins/stitch-utilities/skills/enhance-prompt/SKILL.md)
- [Stitch iteration loop](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/plugins/stitch-utilities/skills/stitch-loop/SKILL.md)

## 1. The overall architecture

The repository separates:
- **design generation** — create or revise screens in Stitch;
- **design-system management** — create, inspect, apply and update persistent visual systems;
- **utility workflows** — improve prompts, extract existing websites, persist project context and iterate;
- **build workflows** — turn generated designs into React, Vite, React Native, shadcn/ui or Remotion outputs.

This is not a PowerPoint generator. Its direct target is screen design and frontend implementation. Its strongest transfer to PPT is the disciplined pipeline from vague brief → structured design prompt → visual system → generated composition → code/build → preview → iteration.

## 2. The three plugin groups and all 16 skills

### A. stitch-design

1. code-to-design — extract a rendered website into a visual/static reference, build a design-system description and upload to Stitch.
2. extract-design-md — derive a reusable DESIGN.md/design profile from project screens or code.
3. extract-static-html — capture an existing website as self-contained HTML, including styles and images where possible.
4. generate-design — call Stitch to create new screen designs or focused edits from a prompt/reference.
5. manage-design-system — create, retrieve, apply and update a project's design system.
6. upload-to-stitch — upload screen/design artefacts to the Stitch project.

### B. stitch-utilities

7. design-md — build or maintain the project design-system description.
8. enhance-prompt — turn vague, underspecified visual requests into actionable screen-generation prompts.
9. site-md — maintain persistent site/project context, information architecture, brand rules and roadmap.
10. stitch-loop — orchestrate repeated design generation and integration.
11. taste-design — guide qualitative design taste and decision-making for generated screens.

### C. stitch-build

12. react-components — turn screen designs into React components.
13. react-native — build React Native implementations using native layout and styles.
14. react-vite-dashboard — build a dashboard project with React/Vite.
15. remotion — create a video composition/animation in Remotion.
16. shadcn-ui — use shadcn/ui components and underlying Radix/Base UI/Tailwind implementation.

The complete source tree is the authority for exact per-skill prompt fields and tool calls.

## 3. The main workflow

### Stage 1 — Enhance the request

A user might say “make a modern dashboard.” The prompt-enhancement skill expands the request with:
- user/audience context;
- product and screen purpose;
- platform and device;
- page hierarchy and information architecture;
- visual direction;
- component and interaction requirements;
- content/data details;
- constraints and exclusions.

The output is a prompt that describes a specific screen or sequence of screens rather than a style adjective.

**PPT transfer:** replace “make a beautiful slide” with a slide specification that names the audience, key message, evidence, visual type, hierarchy, layout, data source and design tokens.

### Stage 2 — Generate with Stitch

The generate-design skill uses Stitch MCP operations to create screens from text and/or reference images. It supports:
- initial screen generation;
- design iteration;
- targeted changes;
- variants;
- retrieving or listing project screens/assets;
- working with selected project/design-system context.

This makes Stitch an external design-generation provider. The skill does not imply that the Stitch model or tool is implemented locally in this repository. A working Stitch MCP configuration/account is required.

### Stage 3 — Establish and manage a design system

The design-system skills can:
- create a design-system document from existing screens;
- retrieve current project design context;
- extract design tokens from source code;
- apply a design system to new screens;
- update a system when a project evolves.

The intended result is a reusable design profile rather than a one-off set of colours. A design profile should include palette, typography, component styling, spacing, layout and visual rules.

### Stage 4 — Extract existing designs

There are two different extraction routes.

**From source code:** inspect a project and extract CSS variables, Tailwind configuration, theme files, component styles and typography into a structured design-system description.

**From an existing web page:** use Puppeteer/browser capture to obtain screenshots and inspect the page. The extraction workflow can inline CSS and images to produce a self-contained static HTML reference. Some steps use a browser subagent and may ask the user which extraction strategy to use.

The code-to-design skill combines static HTML extraction, design-system extraction and Stitch upload.

### Stage 5 — Build code from designs

The build skills convert generated screen designs into an implementation:
- React components;
- Vite dashboard;
- React Native screens;
- shadcn/ui components;
- Remotion video.

The repository's React component examples use React 18 and TypeScript with common client-side architecture such as TanStack Query and React Router. React Native uses platform-native style definitions. shadcn/UI is treated as a copy-in component system built on Radix UI or Base UI and Tailwind CSS.

### Stage 6 — Iterate and preserve project context

The stitch-loop skill uses a persistent prompt handoff file such as .stitch/next-prompt.md. It supports a repeated cycle:
1. write the next design request;
2. generate in Stitch;
3. retrieve the result;
4. integrate it into the project;
5. visually verify the output;
6. update project context.

The site/project context document (SITE.md) records:
- product identity;
- design rules;
- architecture;
- sitemap;
- roadmap;
- implementation state.

This prevents an agent from treating every future turn as a blank design request.

## 4. Stitch integration and external dependencies

Key dependency: Stitch MCP. The skills describe MCP interactions and Stitch project/screen management; the local repository itself is not a replacement for the Stitch generation service.

Other named tools:
- Puppeteer for static site/browser capture;
- browser subagent for some extraction paths;
- Stitch upload utilities, including scripts to avoid file-size limitations of base64 tool arguments;
- React 18 and TypeScript;
- Vite;
- TanStack Query;
- React Router;
- React Native;
- Remotion;
- shadcn/ui;
- Radix UI or Base UI;
- Tailwind CSS.

An upload route may require a Stitch API key. Tool configuration and current provider access should be checked before execution. A skill file is an instruction layer, not proof that its external credentials are available.

## 5. Why this is relevant to a PPT skill

| Stitch method | Presentation equivalent |
|---|---|
| Improve vague prompt | Convert broad PPT request into structured deck/slide brief |
| Generate screens from image/text reference | Generate slide composition options from brief/reference |
| Extract DESIGN.md | Extract design profile from previous PPT or brand guide |
| Manage persistent design system | Reuse deck theme and brand tokens over time |
| Save SITE.md project context | Save deck brief, content model, storyboard and style guide |
| Generate variants | Offer multiple cover/layout/theme options before committing |
| Visual verification | Render every slide and compare |
| Code handoff | Export design to native editable PPTX objects |

### A Stitch-like PPT workflow

1. Create a structured brief.
2. Extract a source deck/theme profile where available.
3. Produce a slide storyboard.
4. Generate a consistent design-system description.
5. Generate 1–3 layout candidates for important slides.
6. User or critic chooses the best direction.
7. Build the complete deck with a deterministic PPTX renderer.
8. Render and inspect.
9. Iterate on only the failed or requested slides.
10. Persist the deck's reusable style and mappings for later updates.

## 6. What not to assume

- Stitch screen generation is not native PowerPoint object generation.
- A screen converted to React is not a PPT slide.
- A project design system may capture web components and responsive rules that do not map literally to slide components.
- The MCP service and credentials must actually be available.
- A screen that looks correct in Stitch can change when rebuilt in React or PowerPoint; the exported target must be rendered and tested separately.

