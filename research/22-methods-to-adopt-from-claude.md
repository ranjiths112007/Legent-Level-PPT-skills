# What Legend-Level PPT Skills Should Learn from Claude

This is the short decision document distilled from [the full Claude presentation workflow research](21-claude-presentation-workflow-research.md).

## 1. The important product distinction

Claude has separate surfaces:
- **Claude for PowerPoint:** template-aware editing inside PowerPoint; supports native charts and diagrams.
- **Claude Slides:** canvas deck creation/export; the PowerPoint export flattens charts, icons and shapes into pictures.
- **Claude Design:** design-system-aware visual canvas for assets, one-pagers, prototypes and layouts.
- **Claude's public PPTX skill:** code-driven generation/editing/inspection with PptxGenJS, OOXML and QA scripts.

We should combine the strongest ideas but not copy the export/editability compromise of Claude Slides when our product claims native PowerPoint editability.

## 2. Adopt these methods

| Claude method | Why it matters | Our implementation |
|---|---|---|
| Audience and purpose before slides | Better storyline and slide count | Structured brief intake |
| Outline before full design | Catches narrative issues early | Storyboard approval stage |
| Reference deck and template awareness | Keeps output on brand | Template inspector and layout mapper |
| Persistent design system | Consistency across decks | Versioned tokens, components, assets and usage notes |
| Selected-object edits | Avoids rebuilding everything | Object-targeted edit manifest |
| Native charts and diagrams | Keeps content editable | Native PowerPoint objects by default |
| Connector context | Brings in reliable data | Explicit source connectors with provenance |
| Skills | Reusable workflow recipes | Small specialist skills/modules |
| Canvas/comments/manual edits | Human-guided iteration | Review UI or targeted revision loop |
| PPTX script + validation | Reproducible output | Deterministic renderer and validator |
| Full-slide rendering | Catches defects invisible in code | Mandatory render/inspect/repair loop |

## 3. Image strategy

Important fact: Anthropic's Help Center says Claude does not generate photos or illustrations like dedicated image-generation tools. Claude can understand images and create diagrams, charts and interactive HTML/SVG visuals.

For our skill:
1. Use native PowerPoint shapes/charts/diagrams for exact data.
2. Use HTML/SVG or vector shapes for technical visuals and icons when appropriate.
3. Use supplied images or an external image-generation provider for photography and illustrations.
4. Use Canva/Adobe connectors only when the provider is actually connected and authorised.
5. Inspect every generated/retrieved asset, maintain consistent art direction and record provenance.
6. Never make an image model responsible for exact text, statistics, labels or data charts.

## 4. The product pipeline we should build

~~~mermaid
flowchart TD
  A[Brief and source files] --> B[Audience and narrative]
  B --> C[Slide storyboard]
  C --> D[Design system]
  D --> E[Layout selection]
  E --> F[Native object builder]
  E --> G[Image asset planner]
  G --> H[External image provider or supplied assets]
  F --> I[PPTX assembly]
  H --> I
  I --> J[Render every slide]
  J --> K[Structural, data and visual QA]
  K -->|Repair| I
  K -->|Pass| L[Editable PPTX and QA report]
~~~

## 5. Minimum implementation priorities

1. Build the brief/storyboard and content-source model.
2. Create a small, strong design-token library and 8–12 reusable slide layouts.
3. Build with editable text, shapes, charts and tables.
4. Add template-aware layout extraction and reference-deck mode.
5. Add an external image-provider interface, not a hard-coded dependency on one image model.
6. Render every slide and automatically detect layout/data errors.
7. Compare our outputs against the same reference briefs and templates in a benchmark.

## 6. What not to copy

- Do not claim private knowledge of Claude's internal algorithms.
- Do not assume every Claude presentation export preserves native chart/shape editability.
- Do not rely on an image model for exact data.
- Do not commit proprietary skill code or assets without checking its licence.
- Do not skip rendering and visual QA.
- Do not claim we are better without a controlled benchmark.

## 7. Primary references

- [Claude for PowerPoint](https://claude.com/docs/office-agents/powerpoint)
- [Claude Slides tutorial](https://academy.claude.com/tutorials/using-claude-design-for-presentations-and-slide-decks)
- [Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)
- [Claude design systems](https://academy.claude.com/tutorials/create-a-design-system-with-claude)
- [Claude image capability FAQ](https://support.claude.com/en/articles/9002504-can-claude-produce-images)
- [Anthropic PPTX skill](https://github.com/anthropics/skills/tree/main/skills/pptx)
- [Anthropic PPT template creator](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator)
