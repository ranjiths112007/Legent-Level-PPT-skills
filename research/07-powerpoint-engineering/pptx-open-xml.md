# PPTX and Office Open XML Structure

**Status:** Technical reference  
**Last reviewed:** 2026-11-21

A .pptx is a ZIP-based Open Packaging Conventions package. It contains XML parts, relationships, media, and other resources. PresentationML defines presentation structures.

Common parts:
- `[Content_Types].xml`
- `ppt/presentation.xml`
- `ppt/_rels/presentation.xml.rels`
- `ppt/slides/slideN.xml`
- `ppt/slides/_rels/slideN.xml.rels`
- `ppt/slideMasters/`
- `ppt/slideLayouts/`
- `ppt/theme/`
- `ppt/media/`
- `ppt/notesSlides/`
- `ppt/charts/`

Actual contents vary. Relationships connect slides to layouts, masters, images, charts, notes and other parts. Do not assume slide numbers map directly to relationship IDs or media filenames.

## Safe inspection

Treat Office files as untrusted. Inspect ZIP entries/XML with limits; do not execute macros or embedded code; validate paths; handle malformed archives; preserve unknown package parts where possible.

Use ECMA-376 / ISO/IEC 29500 and Microsoft's Open XML documentation for authoritative details.
