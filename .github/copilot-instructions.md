# GitHub Copilot Instructions for Legend-Level PPT Skills

When writing code for presentations (Python with `python-pptx`, TypeScript with `pptxgenjs`, or raw OOXML manipulation):
- Prefer native editable PowerPoint objects over static image replacements.
- Protect master slides, layouts, and theme definitions during in-place edits.
- Use explicit coordinates in EMU or inches to avoid text overlaps and bounding-box clipping.
- Separate numeric data into native PowerPoint charts rather than rendered bitmaps.
- Validate generated packages against the Open XML schema.
