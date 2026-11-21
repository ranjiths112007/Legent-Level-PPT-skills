---
name: legend-ppt-qa
description: >
  Run automated visual quality assurance, linting, and repair on PowerPoint presentations (.pptx).
  Detects text box overflows, element collisions, low contrast ratios, and font fallbacks.
  Applies conservative, minimal in-place repairs.
license: MIT
user-invocable: true
argument-hint: "<presentation.pptx> [--repair] [--out output_repaired.pptx]"
---

# Legend-Level PPT QA & Visual Linter

You perform automated structural and visual quality assurance on PowerPoint files, flagging defect classes and executing conservative, minimal in-place repairs.

## 6 Defect Classes Inspected

1. **Text Overflow & Clipping:** Text exceeding the bounding box of its container shape or running off the slide canvas.
2. **Object Collision:** Unintended overlap between adjacent text boxes, shapes, or chart legends.
3. **Contrast Deficiencies:** Text-to-background contrast ratio below WCAG AA standard (4.5:1 for body, 3:1 for large headers).
4. **Font Inconsistencies & Fallbacks:** Elements using unapproved fonts outside the primary brand typography pair.
5. **Data & Placeholder Orphans:** Untouched template markers (e.g., `Lorem ipsum`, `[Insert Name Here]`, `XX.X%`).
6. **Package & Relationship Integrity:** Broken external hyper-links, corrupt media parts, or invalid OOXML namespaces.

## QA Execution Loop

### Step 1: Headless Slide Rendering
Convert `.pptx` slides to individual PNG images for computer-vision and multimodal agent inspection:
```bash
# LibreOffice headless render command
soffice --headless --convert-to pdf presentation.pptx
pdftoppm -png -r 150 presentation.pdf slide_preview
```

### Step 2: Spatial & Bounding Box Linting
- Extract shape coordinates `(x, y, width, height)` from `ppt/slides/slide{N}.xml`.
- Calculate bounding box intersections to detect overlaps.
- Flag any shape crossing slide boundary margins (< 0.5" from border).

### Step 3: Minimal Conservative Repair
When `--repair` is enabled, apply the smallest possible patch:
- **For Overflow:** Reduce font size by 1–2pt or increase box width into available empty margin. Never delete words.
- **For Collisions:** Shift the lower element downwards along the Y-axis by the minimum delta required to clear whitespace.
- **For Low Contrast:** Adjust text hex color towards pure dark or pure light neutral without altering the background.

### Step 4: Verification & Rerender
Rerender repaired slides to confirm the defect was eliminated without creating secondary collisions. Deliver a QA pass/fail table.
