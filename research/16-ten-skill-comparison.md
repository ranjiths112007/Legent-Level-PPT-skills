# Comparative Analysis — Ten Open-Source Presentation and Image Skills

**Reviewed:** 2026-11-21  
**Method:** Qualitative documentation/source review of each repository's README and/or SKILL.md. No controlled execution benchmark has yet been run. Ratings below describe documented design coverage, not measured output quality.

## The ten reviewed projects

1. [PPT Master](15-skill-reviews/01-ppt-master.md) — document conversion, native PPTX, existing-deck editing, template extraction.
2. [PPT Generator (ddpie)](15-skill-reviews/02-ppt-generator.md) — SVG-driven editable shapes, 8 themes, icon/chart library.
3. [AgentBuff Presentation](15-skill-reviews/03-agentbuff-presentation.md) — HTML-first deck, visual style discovery, multi-format export.
4. [slide-maker (Addsum)](15-skill-reviews/04-slide-maker.md) — editable PPTX, ~30 templates, saved generation script and critic review.
5. [Presentation Agent Skills](15-skill-reviews/05-presentation-agent-skills.md) — modular consulting, PPTX, visual direction, restoration and QA skills.
6. [slides-skill (Rich627)](15-skill-reviews/06-slides-skill.md) — JSON spec, deterministic native PPTX renderer, 15 slide types and visual QA.
7. [Knowledge Cat PPT](15-skill-reviews/07-knowledge-cat-ppt.md) — story-first routing, multiple output lanes, validation, editability probes and repair.
8. [Dashi PPT](15-skill-reviews/08-dashi-ppt.md) — HTML deck, multiple variants per page, structured content and media validation.
9. [OpenAI Image Generation Skill](15-skill-reviews/09-openai-imagegen.md) — bitmap generation/editing decision logic and safe asset workflow.
10. [Leonxlnx imagegen-skills](15-skill-reviews/10-imagegen-skills-collection.md) — web/mobile design comps, brand boards and image-to-code.

## Comparison matrix

| Skill | Story planning | Native editable PPTX | HTML/image-first | Image workflow | Existing deck/template | QA/repair | Main limitation |
|---|---|---|---|---|---|---|---|
| PPT Master | Medium | High (shapes; native charts optional) | Preview | Integrated providers/search | Strong | Render checks; verify depth | Dependencies, model dependence |
| PPT Generator | Medium | High for supported SVG primitives | SVG authoring | Icon library; image support | Limited | Optional cross-review | Strict SVG subset; shapes not semantic charts |
| AgentBuff | Medium | Optional/approximate mode | Strong | Style visuals | PPTX conversion | Visual iteration | Default PPTX flattened |
| slide-maker | Strong | Strong by design | Not primary | Some image templates | Reference deck input | Critic + render review | Verify implementation and cross-render |
| Presentation Agent Skills | Modular story role | Generator module | N/A | Dedicated visual director | Screenshot restoration | Dedicated QA | Depends on composition/tools |
| slides-skill | Strong action-title workflow | Strong deterministic renderer | No | Uses supplied/generated images | Limited arbitrary edit | Strong render loop | Fixed slide types; existing deck editing external |
| Knowledge Cat PPT | Very strong | Default professional lane | Multiple lanes | Image-first recipes/style prompts | Template replication | Very strong documented QA | Complexity and many dependencies |
| Dashi PPT | Strong content plan | Export path; verify native editability | Strong | Structured media slots | Style/template variants | Validation and acceptance | Complex workflow; AGPL license |
| OpenAI ImageGen | Not a deck story tool | No | Raster assets | Core capability | Image edit/reference | Inspect and iterate | Raster only; host/model required |
| Leonxlnx imagegen | Design-brief level | No | Image outputs | Core capability | Brand/reference images | Not PPT QA | Not a presentation builder |

Legend: High/Strong means the repository explicitly documents the capability; it is not a measured quality score. "Limited" means the reviewed documentation does not establish a complete workflow.

## Detailed comparative conclusions

### Story and content intelligence
Knowledge Cat is the strongest documented approach: audience shift, outcome, narrative spine, action titles, evidence map and slide plan precede design. slides-skill also has a practical action-title-first process. PPT Generator and PPT Master include planning, but are more production-pipeline oriented. AgentBuff and Dashi emphasize visual production and user taste discovery; their story systems should be supplemented.

### Editable PowerPoint
Best documented options are slide-maker, slides-skill, PPT Master and PPT Generator. Their implementation strategies differ:
- slide-maker advertises native PPTX plus a reproducible generation script.
- slides-skill separates JSON content from deterministic layout.
- PPT Master converts SVG to native shapes and can preserve/edit existing decks.
- PPT Generator converts a controlled subset of SVG primitives to DrawingML.
Knowledge Cat provides a native-PPTX route and explicit editability checks. These claims still need independent tests.

AgentBuff deliberately trades editability for exact visual fidelity in image mode; editable mode is approximate. Do not mistake a screenshot inside a PPTX for an editable slide.

### Visual design and variety
slide-maker's template library is broad; PPT Generator has eight carefully specified themes; Dashi provides multiple per-slide alternatives; AgentBuff lets users choose from previews; Presentation Agent Skills separates art direction into its own module. These are different solutions to the same problem: helping a model avoid repeating generic layouts.

### Image generation
OpenAI ImageGen has the clearest image intent, raster-vs-vector, reference-vs-edit-target and save-path rules. Leonxlnx's collection is valuable for consistent image families and brand boards. Presentation Agent Skills' slide-visual-director is the most directly presentation-specific image art-direction module among these. For our implementation, combine an image prompt planner with image-generation provider adapters and a deck-wide visual consistency brief.

### QA and repair
Knowledge Cat has the broadest documented QA architecture: plan validation, HTML validation, PPTX editability probes, QA rubric and fix/verify loop. Presentation Agent Skills has a dedicated QA module and screenshot restoration. slides-skill makes actual rendering/contact-sheet review mandatory. PPT Master has a production pipeline and checks but its claimed template preservation should be tested. Dashi validates content/media and output variants.

## Conditional winners

| Goal | Best starting point | Why |
|---|---|---|
| Overall workflow architecture | Knowledge Cat PPT | Most complete story-to-build-to-QA routing |
| Native editable PPTX and template editing | PPT Master | Generate/edit/template modes and source conversion |
| Deterministic content-to-native-slide rendering | slides-skill | JSON spec and renderer-owned geometry |
| Broad editable templates and reproducible build | slide-maker | Template breadth plus saved generation script |
| SVG-to-native shape approach | PPT Generator | Controlled SVG subset and conversion |
| Visual taste discovery and pixel-perfect HTML export | AgentBuff | Preview-driven selection and canonical HTML |
| Multiple layout options per slide | Dashi PPT | Three template variants plus custom variant |
| Modular specialist roles | Presentation Agent Skills | Narrative, generator, art direction, restoration and QA |
| Raster image generation/editing | OpenAI ImageGen Skill | Clear tool routing and safe asset workflow |
| Brand boards and coherent design image sets | Leonxlnx imagegen-skills | Narrow image-generation skills for related design assets |

## Free/open-source caveat

"Free skill" and "free execution" are not equivalent:
- A repository may be MIT/Apache/AGPL licensed while image models, LLM tokens, API calls, hosting or deployment cost money.
- Some skills need local Node/Python/browser/rendering dependencies.
- Some require API credentials.
- Some repo license declarations do not cover third-party dependencies, bundled fonts, images or templates.
- AGPL-3.0 is materially different from MIT/Apache; review obligations before combining or distributing code.
- License status is marked unknown where it was not established from the reviewed source. Do not assume an unverified project is permissively licensed.

## What this review does not prove

No skill has been run through the same test corpus in this review. There are no measured claims for deck quality, speed, API cost, editability, overflow rate, factual accuracy or cross-platform fidelity. Star counts are popularity signals, not quality scores. Run the benchmark plan before claiming a winner based on output.