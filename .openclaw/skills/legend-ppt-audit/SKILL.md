---
name: legend-ppt-audit
description: >
  Deeply audit an existing PowerPoint presentation (.pptx). Inspects slide hierarchy, design tokens,
  typography palettes, accessibility compliance, and structural health. Generates an executive audit report.
license: MIT
user-invocable: true
argument-hint: "<presentation.pptx>"
---

# Legend-Level PPT Audit & Token Extractor

You perform a non-destructive audit of an existing `.pptx` file to assess its visual design quality, structural health, and brand consistency.

## Audit Dimensions

1. **Design System & Token Extraction:**
   - Detects all distinct hex colors used across slides and clusters them into primary, secondary, and neutral roles.
   - Audits all font families and sizes; flags font proliferation (>3 font families across a deck).
   - Measures slide margin and alignment consistency.

2. **Narrative & Structure Audit:**
   - Analyzes title types: flags slides using generic topic titles instead of conclusion-driven action titles.
   - Evaluates slide information density: flags slides with >7 bullet points or >150 words.

3. **Accessibility & WCAG Scoring:**
   - Evaluates text contrast across all slides against WCAG AA standards.
   - Checks presence of alt text on photos and illustrations.

4. **Technical Package Health:**
   - Verifies master slide layout count and detects orphaned layout definitions.
   - Checks total file size and identifies uncompressed images (>2 MB per slide).

## Output Deliverable
Generates a structured markdown audit report with:
- **Presentation Health Score (0–100)**
- **Extracted Design Tokens (Palettes & Fonts)**
- **Prioritized Recommendations (High / Medium / Low)**
