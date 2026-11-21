---
name: legend-ppt-edit
description: >
  Surgically edit existing PowerPoint presentations (.pptx) while preserving 100% of master slides,
  brand themes, fonts, layouts, animations, and non-target slides. Use for monthly business reviews,
  quarterly updates, or template-based data replacement.
license: MIT
user-invocable: true
argument-hint: "<source.pptx> <data.xlsx|data.json> [--mode exact|partial]"
---

# Legend-Level Reference Deck Surgical Editor

You update an existing PowerPoint deck with new data or text while strictly preserving its original design, master layouts, and untouched slides.

## Guiding Rule: In-Place Preservation
Never recreate or regenerate an existing presentation from scratch. Always perform targeted in-place XML/object modifications on a working copy of the original file.

## Operating Modes

| Mode | Purpose | Target Action |
|---|---|---|
| `exact_content_replacement` | Monthly updates / MBRs | Replaces exact metric numbers, dates, and chart values. |
| `same_design_new_content` | Template reuse | Swaps slide topic text while keeping layout geometry. |
| `partial_edit` | Specific slide updates | Modifies specified slide indices (e.g., slides 3, 5, 8). |

## 5-Step Execution Workflow

### Step 1: Clone & Validate Reference Deck
- Create a working copy: `cp source.pptx output_updated.pptx`. Never mutate the original reference file.
- Verify file readability and inspect slide count, layout masters, and embedded media.

### Step 2: Content-to-Object Mapping
- Read the incoming data (CSV, Excel, or JSON).
- Inspect the target slide XML (`ppt/slides/slide{N}.xml` or via `python-pptx`).
- Identify the exact shape IDs, table cell coordinates `(row, col)`, or chart data series that hold the stale values.

### Step 3: Validate Edit Manifest
Ensure changes comply with [reference-edit-manifest.schema.json](file:///d:/legend%20level%20ppt%20skills/schemas/reference-edit-manifest.schema.json):
```json
{
  "manifest_version": "1.0",
  "job_id": "job_001",
  "mode": "exact_content_replacement",
  "source": { "path": "source.pptx" },
  "output": { "path": "output_updated.pptx" },
  "preservation": {
    "keep_masters": true,
    "keep_slide_count": true
  },
  "changes": [
    {
      "slide_index": 3,
      "object_id": "shape_revenue_val",
      "action": "replace_text",
      "target_value": "$4.2M",
      "new_value": "$5.8M"
    }
  ]
}
```

### Step 4: Apply Surgical Mutations
- Mutate only the target text runs inside `<a:t>` tags or update chart series data cached in `ppt/charts/chart{N}.xml`.
- Preserve existing font formatting, character spacing, paragraph leading, and alignment.
- If replacement text is significantly longer, adjust font size conservatively by 1–2 points to prevent box overflow.

### Step 5: Post-Edit Verification
- Open the updated deck to ensure OOXML package integrity.
- Verify that non-target slides remain byte-identical or structurally unchanged.
- Deliver a change audit report detailing old vs new values.
