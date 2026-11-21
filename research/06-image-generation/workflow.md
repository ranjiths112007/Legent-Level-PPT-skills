# Image Generation Workflow

**Status:** Reference  
**Last reviewed:** 2026-11-21

1. Identify the slide's communication goal.
2. Define visual role: hero image, supporting photo, background, illustration, product concept.
3. Choose generation, retrieval, or native objects.
4. Prompt subject, context, composition, style, lighting, palette, crop, and exclusions.
5. Select aspect ratio/resolution for the target region.
6. Generate candidate assets.
7. Inspect correctness, artifacts, unwanted text, style consistency and composition.
8. Edit/regenerate.
9. Crop and position without stretching.
10. Optimize file size and record provenance.
11. Add meaningful alt text.
12. Render the slide and inspect in context.

Provider APIs can expose size, quality, format, compression, transparency/background, and editing controls. These vary by model/version; consult current provider docs.

## Deck-level consistency brief

Define style, palette, realism, lighting, camera angle, backgrounds, motifs and prohibited inconsistencies. Reference images can help but do not guarantee consistency.

## Risks

Wrong subject, embedded text errors, distorted details, inconsistent style, subject under text, wrong crop, low resolution, misleading diagrams, licensing/privacy issues.

Realistic appearance is not proof of factual accuracy. Verify diagrams, maps, products and data visuals independently.
