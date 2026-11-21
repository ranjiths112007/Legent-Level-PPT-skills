# Master Source, Documentation, and Repository Register

> **Status:** Authoritative Research Index  
> **Last updated:** 2026-11-21  
> **Scope:** Canonical registry of all 19 primary repositories, 3 supplementary iArt packs, 10 official Claude documentation targets, 5 Anthropic implementation references, 8 technical libraries/engines, and 15 supplementary presentation and image repositories.

---

## 1. Primary Repositories (19 Deep-Dive Repositories)

### Design Systems, UI/UX, and Visual Architecture

| # | Repository | Category / Primary Focus | Core Architecture / Value | License / Terms |
|---|---|---|---|---|
| 1 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Art direction & anti-generic design | Curates visual taste profiles, typography rules, curated assets, and browser-based design QA. | MIT |
| 2 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | Design tokens & design-system catalog | 169 functional skill docs, 115 template specs, component tokens, and CSS/HTML slide foundations. | Apache-2.0 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Semantic diagramming & layout grammar | Semantic diagram planning: determines conceptual relationships before generating vector structures. | MIT |
| 4 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX heuristics & data palettes | Data-driven visual heuristics, chart palettes, font pairing matrix, and contrast guidelines. | MIT |
| 5 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Prompt engineering & code-gen design | Systematic prompt enhancement, design-system extraction, and code-to-design translation. | Apache-2.0 |
| 6 | [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | Reusable visual styling presets | 67 curated design instruction presets for distinct aesthetics (editorial, brutalist, corporate). | MIT |
| 7 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | Motion design & interaction engineering | Micro-interaction rules, spring physics, layout shifts, and choreographic timing constraints. | MIT |
| 8 | [owl-listener/designer-skills](https://github.com/owl-listener/designer-skills) | Design critique & product strategy | Structured design critique rubric, information architecture, and multi-variant design review. | MIT |
| 9 | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | Precision interface craft & accessibility | Strict spacing scales, typography hierarchies, WCAG accessibility, and layout rhythm checks. | MIT |

### PowerPoint Generation & Presentation Engines

| # | Repository | Category / Primary Focus | Core Architecture / Value | License / Terms |
|---|---|---|---|---|
| 10 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Native OOXML & template preservation | Python/OOXML toolchain, constrained SVG intermediate representation, master slide protection. | MIT |
| 11 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | HTML-first slides & style previews | 34 modular template systems, browser visual inspection, and HTML-to-deck pipelines. | MIT |
| 12 | [Akxan/ppt-agent-skill](https://github.com/Akxan/ppt-agent-skill) | Content-driven visual grammar | 18 chart types, 10 layout families, and automated HTML→SVG→PPTX conversion pipeline. | MIT |
| 13 | [proyecto26/slides-ai-plugin](https://github.com/proyecto26/slides-ai-plugin) | Multi-format slide planning | PptxGenJS backend, TypeScript layout abstractions, and automated structural QA hooks. | MIT |

### Motion Design & Programmatic Animation

| # | Repository | Category / Primary Focus | Core Architecture / Value | License / Terms |
|---|---|---|---|---|
| 14 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | High-performance timeline animation | Official GSAP agent guidance for timelines, complex SVG paths, and framework lifecycles. | MIT |
| 15 | [remotion-dev/skills](https://github.com/remotion-dev/skills) | Frame-deterministic React video | React-based video generation; maps programmatic slide layouts directly to frame sequences. | Proprietary Runtime |
| 16 | [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | Vector motion choreography | Technology-agnostic motion direction, easing curves, and vector animation choreography. | MIT |
| 17 | [iart-ai/motion-skills](https://github.com/iart-ai/motion-skills) | Motion skill hub | Umbrella hub coordinating data animation, explainer workflows, and kinetic typography. | MIT |
| 18 | [C-Jeril/framer-motion-skills](https://github.com/C-Jeril/framer-motion-skills) | Declarative layout transitions | Layout animations, enter/exit transitions, and interactive visual deck components. | MIT |
| 19 | [frankxai/awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills) | Motion runtime routing & QA | Runtime selection (CSS vs GSAP vs Remotion), generative media direction, and video QA. | CC0-1.0 |

---

## 2. Additional iArt Specialized Skill Packs

| Repository | Primary Capability | Key Contribution to Presentation Engineering | License |
|---|---|---|---|
| [iart-ai/data-animation-skills](https://github.com/iart-ai/data-animation-skills) | Animated data charts & kinetic stats | Rules for stepping numbers, progressive chart reveals, and metric callouts without visual noise. | MIT |
| [iart-ai/motion-design-skills](https://github.com/iart-ai/motion-design-skills) | Core motion mechanics & transitions | 9 foundational animation skill docs: camera motion, rhythm, hierarchy, and slide transitions. | MIT |
| [iart-ai/explainer-video-skills](https://github.com/iart-ai/explainer-video-skills) | Presentation-to-video narration | Audio-visual synchronization, storyboard sequencing, and voiceover pacing for slide decks. | MIT |

---

## 3. Claude Official Documentation & Workflow References

| Topic / Surface | Canonical URL | Architectural Takeaway for Legend-Level PPT |
|---|---|---|
| Claude for PowerPoint | [Office Agents Docs](https://claude.com/docs/office-agents/powerpoint) | Uses active deck context, edits selected objects in-place, and preserves existing master layouts. |
| Building a PowerPoint with Claude | [Claude Academy Tutorial](https://academy.claude.com/tutorials/building-a-powerpoint-with-claude) | Workflow: inspect template master → outline story → select slide layout → generate editable objects. |
| Claude Slides Tutorial | [Claude Academy Slides](https://academy.claude.com/tutorials/using-claude-design-for-presentations-and-slide-decks) | Shows web-canvas deck authoring; highlights export trade-offs where vector shapes become bitmap pictures. |
| Claude Design — Getting Started | [Support Article 14604416](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) | Visual layout generation via HTML/CSS code components rather than raw diffusion pixels. |
| Claude Design Product Page | [Claude Product Page](https://claude.com/product/design) | Direct-manipulation visual canvas integrated with conversational iteration. |
| Create a Design System with Claude | [Claude Academy Design System](https://academy.claude.com/tutorials/create-a-design-system-with-claude) | Tokenizing brand identity (typography scale, color semantics, component margins) before creating assets. |
| Can Claude Generate Images? | [Support Article 9002504](https://support.claude.com/en/articles/9002504-can-claude-produce-images) | **Critical boundary:** Claude does not natively generate photographic diffusion images; relies on external integrations. |
| Custom Visuals in Claude | [Support Article 13979539](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork) | Rendering dynamic SVG charts, flowcharts, and diagrams through conversational artifacts. |
| Connectors and Skills | [Claude Connectors Docs](https://claude.com/docs/office-agents/connectors-and-skills) | Protocol for agents to read external databases, enterprise files, and tool APIs securely. |
| Create and Edit Files with Claude | [Support Article 12111783](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) | File generation lifecycle in Python/JS sandboxes, package assembly, and user delivery. |
| Claude Artifacts | [Claude Features](https://claude.com/features/artifacts) | Side-by-side interactive viewports for live-rendering code-generated slide decks. |

---

## 4. Anthropic Public PowerPoint Skills & Implementation References

| Repository / File | Path / URL | Implementation Significance |
|---|---|---|
| Anthropic Skills Repository | [anthropics/skills](https://github.com/anthropics/skills) | Canonical collection of production-tested agent skill architectures. |
| Anthropic PPTX Skill Directory | [skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | Core instructions for code-driven PowerPoint authoring. |
| PPTX SKILL.md | [skills/pptx/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) | Enforces PptxGenJS scripts, thumbnail contact sheets, text bounding box rules, and QA checklists. |
| PowerPoint Template Creator | [financial-analysis/ppt-template-creator](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator) | Programmatic creation of branded master decks with enterprise compliance. |
| PPT Template Command | [commands/ppt-template.md](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/commands/ppt-template.md) | Slash-command interaction contract for turning raw user data into structured template-aligned slides. |

---

## 5. Technical Libraries, Standards, and Engines

| Tool / Standard | Canonical URL | Engine Role & Trade-offs |
|---|---|---|
| PptxGenJS | [PptxGenJS Documentation](https://gitbrent.github.io/PptxGenJS/) | Fast, declarative Node/Browser JS library for creating `.pptx` decks from scratch. Weak for editing existing OOXML packages. |
| python-pptx | [python-pptx Docs](https://python-pptx.readthedocs.io/en/latest/) | Mature Python library for creating and reading PowerPoint files. High control over text frames, shapes, and tables; limited chart type customization. |
| Microsoft Open XML SDK | [Microsoft Learn Open XML](https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk) | Authoritative reference for raw OOXML schema (`presentationML`, `drawingML`). Essential for surgical in-place edits without corrupting binary parts. |
| LibreOffice PDF Export | [LibreOffice Docs](https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html) | Headless rendering CLI (`soffice --headless --convert-to pdf`) used to render `.pptx` slides into images for automated visual QA. |
| Remotion Skills Docs | [Remotion AI Docs](https://www.remotion.dev/docs/ai/skills) | Agent instructions for building programmatic, frame-accurate React animations. |
| Remotion Pricing & Licensing | [Remotion License](https://www.remotion.dev/docs/license/pricing) | **Commercial restriction:** Requires paid commercial license for companies with revenue > \$0; dual-licensed (free for individuals/non-profits). |
| Remotion Terms | [Remotion Terms](https://www.remotion.dev/docs/terms) | Distribution and embedding constraints for programmatic video rendering pipelines. |

---

## 6. Supplementary Presentation and Image Repositories

### Presentation Generation References

| Repository | Focus & Architecture |
|---|---|
| [TerminalSkills/skills](https://github.com/TerminalSkills/skills) | Collection of CLI-first agent skills including early PPT Master implementations. |
| [ddpie/agent-skills](https://github.com/ddpie/agent-skills) | Minimalist slide generator producing clean corporate layouts with strict color maps. |
| [nugrahalabib/AgentBuff-Presentation-Skills](https://github.com/nugrahalabib/AgentBuff-Presentation-Skills) | Density modes, visual preview cards, and explicit user-driven fidelity/editability toggles. |
| [addsumtech/slides_maker](https://github.com/addsumtech/slides_maker) | Curated style gallery, self-contained Python project workspace, and independent critic evaluator. |
| [hiamberhuang/presentation-agent-skills](https://github.com/hiamberhuang/presentation-agent-skills) | Specialist agent decomposition: researcher, narrative architect, layout designer, and QA auditor. |
| [Rich627/slides-skill](https://github.com/Rich627/slides-skill) | Validated JSON deck-plan intermediary; deterministic slide-type catalog and contact-sheet QA. |
| [gnipbao/knowledge-cat-ppt-skill](https://github.com/gnipbao/knowledge-cat-ppt-skill) | Story spine, audience shift analysis, action titles, and automated editability probes. |
| [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | Generates multiple distinct layout candidates from a single canonical content object. |
| [SlideSpeak/skills](https://github.com/SlideSpeak/skills) | API-backed commercial slide generator integrating AI models with cloud PPTX compilation. |
| [brycewang-stanford/many-ppt-skills](https://github.com/brycewang-stanford/many-ppt-skills) | Catalog indexing 220+ agent presentation skills across the ecosystem. |

### Image Generation & Visual Prompting References

| Repository | Focus & Architecture |
|---|---|
| [openai/skills - imagegen](https://github.com/openai/skills/tree/main/skills/.system/imagegen) | Separation of raster vs vector paths, prompt structuring, and non-destructive image versioning. |
| [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) | Establishing cohesive image families and brand moodboards before generating individual slide hero assets. |
| [satasuk03/media-gen-skills](https://github.com/satasuk03/media-gen-skills) | Multi-provider image routing (Midjourney, Flux, Stable Diffusion) with strict parameter presets. |
| [NanmiCoder/open-image-prompts](https://github.com/NanmiCoder/open-image-prompts) | High-signal prompt patterns, lighting descriptors, camera angles, and style tokens for presentation imagery. |
| [guanyang/open-agent-hub - baoyu-imagine](https://github.com/guanyang/open-agent-hub/blob/main/skills/baoyu-imagine/SKILL.md) | Structured visual concept translation: turning complex abstract business metaphors into clear, cohesive illustrations. |
