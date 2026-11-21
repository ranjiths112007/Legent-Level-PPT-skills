# Skill Review 09 — OpenAI Image Generation Skill

- Repository: https://github.com/openai/skills
- Skill: https://github.com/openai/skills/tree/main/skills/.system/imagegen
- License: verify the repository's current LICENSE and applicable image/model terms.
- Reviewed: 2026-11-21. Evidence: primary SKILL.md.

## Purpose
Guide an agent to generate or edit raster assets when a bitmap is appropriate: photos, illustrations, textures, sprites, mockups, product visuals, transparent cutouts and infographics.

## Contents
- SKILL.md intent and tool-routing rules.
- Built-in image-tool mode and explicit-only CLI fallback.
- Prompting and sample-prompt references.
- Image use-case taxonomy.
- Asset save-path and non-destructive edit rules.
- CLI-specific references/scripts for users who explicitly choose that route.

## What it makes the agent do
1. Decide whether the request is image generation or editing.
2. Decide whether supplied images are references, edit targets or supporting inputs.
3. Prefer the built-in image tool; do not silently fall back to a CLI requiring an API key.
4. Choose raster generation only when raster output is appropriate; use SVG/HTML/code for deterministic vector/UI work.
5. Structure the prompt by use case, subject, scene, style, composition, lighting and constraints.
6. Generate, inspect, make targeted iterations and validate output.
7. Save project-bound assets into the project rather than leaving them in a temporary/default location.
8. Preserve existing assets non-destructively.

## Strengths
- Excellent decision boundary between bitmap generation and vector/code-native graphics.
- Explicit distinction between generate vs edit and reference vs target images.
- Tool routing is honest and avoids silent API-key fallback.
- Non-destructive edits and project asset path management.
- Prompt taxonomy and specificity policy.
- Inspection and iterative refinement are required.

## Weaknesses and risks
- The skill assumes a host with a built-in image tool; portability depends on runtime.
- CLI fallback is explicit-only and requires API key/network setup.
- Raster images are poor substitutes for editable charts, icons or diagrams.
- Image generation may hallucinate text/data; all labels and facts must be checked.
- Model-specific output quality and rights terms require current provider review.

## Best fit
Creating/editing photographic, illustrative, mockup and conceptual bitmap assets for a presentation or project.

## Ideas to adopt
Intent routing; raster-vs-vector decision; image-role labels; prompt schema; inspect/iterate loop; non-destructive asset versioning; explicit provider/cost/credential handling.

## Critical PPT lesson
Use generated images for visual storytelling, not for charts whose values or labels must be accurate/editable. Generate chart data separately and build the chart as a native object.