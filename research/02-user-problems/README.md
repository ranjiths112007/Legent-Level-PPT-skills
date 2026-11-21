# User Problems and Pain-Point Taxonomy

**Status:** Initial taxonomy; systematic collection pending  
**Last reviewed:** 2026-11-21

This is a map of problems to investigate, not a claim that every user experiences every issue.

| ID | Category | Example failure | Impact |
|---|---|---|---|
| UP-01 | Input understanding | Important source content omitted | Incomplete deck |
| UP-02 | Data fidelity | Slide number differs from spreadsheet | Business risk |
| UP-03 | Storytelling | Slides disconnected or lack conclusion | Poor communication |
| UP-04 | Repetitive design | Same layout repeated | Generic appearance |
| UP-05 | Visual hierarchy | Main message unclear | Low comprehension |
| UP-06 | Typography | Overflow or font substitution | Broken layout |
| UP-07 | Color | Poor contrast or inconsistent palette | Readability/brand |
| UP-08 | Image generation | Wrong subject/style/composition | Weak visuals |
| UP-09 | Image placement | Bad crop, low resolution, stretched image | Visual defect |
| UP-10 | Object construction | Uneditable or malformed chart/diagram | Editing friction |
| UP-11 | Layout | Overlap, clipping, uneven alignment | Unprofessional deck |
| UP-12 | Rendering | PPTX differs across renderers | Compatibility |
| UP-13 | Accessibility | Missing alt text/titles/reading order | Exclusion |
| UP-14 | Templates | Existing theme/master not preserved | Rework |
| UP-15 | Automation | Agent stops after saving without inspection | False completion |
| UP-16 | Repair | Fixing one defect breaks another | Regression |
| UP-17 | File handling | Large images, broken links, unsupported media | Delivery failure |
| UP-18 | Licensing | Unlicensed images/fonts | Legal/reuse risk |
| UP-19 | Collaboration | Edits difficult to review/reproduce | Trust/workflow cost |
| UP-20 | Localization | Text expansion/glyph coverage breaks layout | Regional failure |

## Initial user-report leads

Initial research surfaced complaints about generic/repetitive AI layouts; time-consuming assembly from notes, spreadsheets, and work tools; inconsistent fonts, colors, headings, and alignment; and font substitution changing layout. These remain discovery leads only. Add canonical URLs, dates, context, and independent examples to [issue-log.md](issue-log.md).

## Severity model

Score each issue on impact (1–5), observed frequency (1–5), detectability (1–5), and repair cost (1–5). Prioritization can use Impact × Frequency × Detectability; use repair cost to estimate effort. Do not assign frequency without a defined sample.

## Research questions

1. Which failures cause users to abandon AI PPT tools?
2. Which failures are most expensive to fix manually?
3. Which issues can be detected programmatically with high confidence?
4. Which repairs can be automated safely?
5. What matters most: editability, visual quality, accuracy, speed, template fidelity, accessibility?
6. How do needs differ by deck type?
