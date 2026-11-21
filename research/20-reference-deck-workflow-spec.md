# Reference-Deck Skill: Operational Workflow and Engineering Contract

> Companion implementation specification for [Reference-Based PowerPoint Recreation](19-reference-based-ppt-recreation.md).  
> Research date: 21 November 2026.  
> Status: proposed operating contract; implementation and benchmarks are still required.

## 1. Goal

Implement a reference-deck capability inside Legend-Level PPT Skills. The user can supply an existing PPTX and replacement content, then ask for a new presentation that retains the original deck's structure and design while changing only the requested information.

The skill is not just a prompt telling an AI to “copy the style.” It is a controlled workflow with:
- Explicit request classification.
- PowerPoint inspection and slide rendering.
- Content extraction and validation.
- Content-to-object mapping.
- A change manifest.
- Minimal edits to a copy of the source deck.
- Visual and structural quality checks.
- A transparent delivery report.

## 2. User-facing behaviour

### Supported request examples

- “Use this PPT as a template and replace the values with the Excel data.”
- “Keep every slide in the same design. Update the month, totals and charts.”
- “Use slides 1–10 as the reference, but update slides 3, 5 and 8 only.”
- “Make another deck with these same layouts and colours but with my new topic.”
- “This PDF is the only reference. Recreate it as an editable PPTX.”

### Initial response rules

1. Identify whether the user supplied an editable PPTX, a template, a PDF or images.
2. Identify the replacement source: direct instructions, Excel/CSV, documents, another deck or mixed sources.
3. Detect the requested fidelity mode.
4. State the default interpretation before high-impact changes.
5. Do not ask the user to repeat information already supplied in files or messages.
6. Ask only for details that materially affect the result, such as ambiguous metric definitions, conflicting data sources or an uncertain slide mapping.
7. For exact replacement, promise preservation as the goal, not as a guarantee before testing.

### Mode selection

| User phrase | Mode |
|---|---|
| “Same exact PPT, only values change” | exact_content_replacement |
| “Same structure and design, new report” | same_design_new_content |
| “Update from this month’s Excel” | same_structure_new_data |
| “Inspired by this PPT” | reference_guided_new_deck |
| “Only update specific slides” | partial_edit |
| “Only PDF/screenshots available” | visual_reference_reconstruction |

If the wording is ambiguous but the supplied PPTX is clearly a source template, default to exact_content_replacement and keep all other elements unchanged.

## 3. Workflow with inputs, operations and outputs

### Step 0 — Create a job record

Inputs:
- User request and explicit constraints.
- Reference file(s).
- Replacement source file(s).
- Output type and any user preferences.

Create:
- Job ID.
- Source-file hashes.
- Mode.
- Requested slide scope.
- Preservation requirements.
- Permission/consent status for external services.
- Output destination.

Never overwrite the source.

### Step 1 — Validate the reference

Required operations:
1. Verify the file type using both extension and content signature.
2. Check whether the package is readable.
3. Check encryption and password status.
4. Record slide count, dimensions and package contents.
5. Identify macro-enabled or embedded content.
6. List external relationships and linked content.
7. Flag features that the chosen editing adapter cannot guarantee to preserve.

Output: intake report with pass/fail/warning states.

Block editing when the package is corrupt, encrypted without a supported credential, or contains a feature that the selected engine is known to destroy. A read-only inspection can still be offered.

### Step 2 — Inspect and render the original

Run the inspector and renderer in parallel where safe.

Inspector output:
- Slide inventory.
- Shape/object inventory.
- Text-run inventory.
- Table inventory.
- Chart inventory.
- Picture/media inventory.
- Relationships and layout/master mapping.
- Notes, hidden slides, transitions and animation flags.
- Package-part hashes.

Renderer output:
- One PNG per slide.
- One contact sheet.
- PDF preview if supported.
- Renderer name and version.
- Any render warnings.

Do not treat a successful PDF export as proof that all PPTX features are retained.

### Step 3 — Build the reference profile

The profile must include:

**Deck identity**
- Slide size and aspect ratio.
- Theme fonts and theme colours.
- Master/layout map.
- Common background and footer rules.
- Brand/logo presence.
- Page-number and title conventions.

**Slide map**
- Slide number and name.
- Section and narrative role.
- Main title object.
- Main body/content objects.
- Main image/chart/table object.
- Fixed design objects.
- Replaceable content slots.
- Uncertain or unsupported objects.

**Visual design**
- Palette with hex values where they can be read reliably.
- Font family and size hierarchy.
- Common margins and gutters.
- Alignment and grid pattern.
- Header/footer positions.
- Chart and table styling.
- Icon/illustration style.
- Image aspect/crop treatment.

Every design token must carry provenance: XML/theme value, extracted shape format, render/vision estimate or unknown. Do not describe a guessed visual colour as an exact theme token.

### Step 4 — Ingest and validate replacement content

Supported sources and suggested extractors:

| Input | Extraction | Validation |
|---|---|---|
| XLSX | pandas/openpyxl or Excel API | Sheet/header checks, formula/value distinction, types, totals and units |
| CSV | Python CSV/pandas | Encoding, delimiter, header, duplicate and null checks |
| DOCX | python-docx or document extraction service | Heading/paragraph/table provenance |
| PDF | Text extraction plus page rendering for tables/charts | Page/source coordinates; visually inspect ambiguous tables |
| Another PPTX | Reuse deck inspector | Separate reference material from replacement facts |
| Text or chat | Structured extraction by the model | Preserve source wording and mark inferred fields |
| Cloud workbook | Approved connector/API | Least-privilege access, workbook/table identity and row provenance |

Build a normalized content model. Each value should include source path, source sheet/page, cell/row when available, raw value, normalized value, unit, date range, aggregation, and validation messages.

Do not treat a formatted number string as a number without parsing and validating it. Do not rely only on displayed spreadsheet values if formula recalculation is stale or unavailable.

### Step 5 — Match source content to slide objects

The matching service uses:
- Slide title and section role.
- Nearby text and semantic labels.
- Shape names and placeholder types.
- Object position and dimensions.
- Chart category and series names.
- Table header structure.
- Source spreadsheet field names and data dictionary.
- User's explicit instructions.
- Historical deck mapping, if supplied.

The mapper should output candidate mappings, supporting evidence and confidence. It should separately classify each reference element as:
- fixed,
- replace_text,
- replace_image,
- update_table,
- update_chart,
- derived_callout,
- user_review,
- preserve_unknown.

### Step 6 — Confidence policy

Suggested product thresholds, to be tuned with evaluation:
- 0.95–1.00: eligible for automatic edit only when the mapping is supported by explicit instructions or deterministic structure.
- 0.80–0.94: prepare a mapping preview; require approval for financial, legal, medical, regulatory or client-critical values.
- Below 0.80: do not edit automatically; ask the user or mark the field unresolved.

Confidence is not truth. A model's numeric confidence must not override a data validation failure, missing denominator or contradictory source.

### Step 7 — Create the edit manifest

The manifest must be generated and validated before any write operation.

Every change must include:
- Slide index.
- Stable object identifier and shape name where available.
- Object type.
- Operation.
- New value or source content key.
- Provenance.
- Confidence/evidence.
- Preservation flags.
- Expected change region.
- Whether user approval is required.

Every protected element should be recorded in the preservation plan. The manifest schema is stored at schemas/reference-edit-manifest.schema.json.

Do not execute edits that are not in the validated manifest.

### Step 8 — Apply the edit

Use a format-aware editing adapter.

Preferred operation order:
1. Replace a text run or exact range.
2. Replace placeholder content.
3. Update a cell or table value.
4. Update a native chart using chart-aware APIs.
5. Replace media linked to an existing picture shape.
6. Rebuild a specific object only if a supported targeted edit is impossible.
7. Create a new slide only when the chosen mode allows it.

Always:
- Work on a copy.
- Preserve source package.
- Preserve slide order and slide count in exact mode.
- Preserve shape geometry and formatting unless the manifest explicitly permits a change.
- Keep original object types whenever practical.
- Record all package parts changed.
- Fail safely when object IDs are missing or no longer unique.

### Step 9 — Fit and layout validation

After writing:
- Check all updated text frames.
- Compare text length and line count with source.
- Detect overlap with nearby objects.
- Check minimum font sizes.
- Confirm chart labels and table cells are visible.
- Confirm image crop and aspect.
- Confirm slide title and key metric fit the original hierarchy.

Do not shrink text by default. Request content shortening, a new slide, or an alternate layout when the reference geometry cannot fit the required content legibly.

### Step 10 — Render and run QA

Render the complete deck again.

Run the following tests:

| Test | Pass condition |
|---|---|
| Package opens | PPTX is readable and all required parts resolve |
| Slide count/order | Matches the manifest's policy |
| Object integrity | No unexpected object loss or duplication |
| Preservation | Unchanged package parts/objects remain unchanged where supported |
| Text changes | All approved replacements exist in their target objects |
| Old text scan | No outdated target value remains in targeted scope |
| Data validation | Visible metrics reconcile with normalized data |
| Chart validation | Chart type/style retained and values/categories correct |
| Image validation | Intended asset changed; crop/geometry retained |
| Visual inspection | No unexpected clipping, overlap, font substitution or visual drift |
| Editability | Replaced content remains editable when the manifest requires it |

Run both machine checks and visual review. A machine score cannot replace rendering. When a rendering engine differs from the user's PowerPoint version, disclose that as a test-environment limitation.

### Step 11 — Targeted repair

If a check fails:
1. Identify slide/object and failure reason.
2. Make the smallest repair.
3. Re-render.
4. Re-run the failed test and regression checks.
5. Stop after a configurable repair budget.
6. Report unresolved problems rather than repeatedly rebuilding the deck.

Never “fix” a visual mismatch by hiding content or flattening the slide without approval.

### Step 12 — Deliver

Return:
- Editable PPTX.
- PDF preview or slide contact sheet when rendering is available.
- Change report listing slide/object, old value, new value and source.
- QA summary: passed, warnings, failed and not tested.
- Preservation summary.
- Known limitations and user review items.

The final report must distinguish:
- **Verified:** a check actually ran and passed.
- **Warning:** a risk was detected but output may still be usable.
- **Not tested:** no tool/check was available.
- **Failed:** output did not meet a required criterion.

## 4. Editing adapter interface

The model should not generate arbitrary Open XML XML and assume it is valid. The editing runtime should expose a small, testable interface.

Suggested operations:

| Operation | Input | Output |
|---|---|---|
| inspect_deck | File path, safe-inspection options | Deck profile, object inventory, part hashes |
| render_deck | File path, renderer options | PNGs, PDF/contact sheet, render log |
| extract_content | File path(s), source config | Normalized content model |
| validate_content | Content model, rules | Validation result and warnings |
| map_content | Deck profile, content model, user instructions | Candidate mapping with evidence |
| validate_manifest | Manifest, profiles | Validated or rejected manifest |
| replace_text | PPTX copy, slide/object locator, replacement | Updated object result |
| replace_picture | PPTX copy, locator, asset path, crop policy | Updated picture result |
| update_table | PPTX copy, locator, cell map | Updated table result |
| update_chart | PPTX copy, locator, series/categories/values | Updated chart result |
| save_copy | Working package, output path | Output file and changed-part list |
| validate_package | Output file | Integrity and relationship report |
| compare_decks | Source/output, manifest | Object/part changes and visual diff |
| create_report | Manifest, QA, edit log | Human-readable delivery report |

Use typed errors such as:
- UnsupportedFeatureError
- AmbiguousObjectError
- MissingRelationshipError
- ContentValidationError
- TextOverflowError
- RenderingError
- PackageIntegrityError
- PreservationCheckFailed

Do not let a low-level exception silently become an empty output deck.

## 5. Object locator design

An object locator should be more robust than “the 5th object on slide 4.”

Preferred locator fields:
1. Slide part name and slide index.
2. Shape ID.
3. Shape name.
4. Object type.
5. Placeholder type/index.
6. Text fingerprint or chart/table signature.
7. Expected bounding box.
8. Relationship ID for media/chart parts.

Before applying an edit, verify that the locator still matches the expected object. If the shape ID is missing or duplicate, use a combination of shape name, type, text fingerprint and bounds; if the match is still ambiguous, stop.

Never rely solely on object order. PowerPoint object order may change after an edit or copy operation.

## 6. Text replacement contract

Preserve:
- Font face, size, colour, weight and emphasis.
- Paragraph alignment, indentation, bullets and spacing.
- Text-frame margins, vertical alignment and rotation.
- Hyperlinks and fields when not explicitly being replaced.
- Separate formatting runs around the target text.

For a change that spans multiple rich-text runs, determine whether to:
- replace a single run,
- replace a run range and preserve style of the first matched run,
- split or merge runs deliberately,
- or ask for an approval because formatting could change.

Do not rebuild an entire text frame just to change one word.

Keep a record of:
- old text,
- new text,
- target run or range,
- style inherited by new text,
- post-render overflow status.

## 7. Chart update contract

A chart update must validate:
- chart type and subtype,
- series names/count,
- category names/count,
- values and number formats,
- axis minimum/maximum and number display,
- legend and data-label settings,
- source workbook/cache consistency,
- whether chart is native, linked or a picture.

Default policy:
- Keep chart type if the data model still fits.
- Preserve series colours and formatting if supported.
- Never create or delete a series without a source mapping.
- Never silently change from clustered to stacked or from count to percentage.
- When category count differs, check label overlap and axis behaviour.
- Reconcile chart totals with the content model and any slide callouts.
- If the chart's original style cannot be preserved by the chosen library, stop or present an explicit alternative.

## 8. Picture update contract

The picture object has both an asset and a frame. Replacing the asset must not accidentally reset the frame.

Preserve where supported:
- x/y/width/height,
- crop rectangle,
- rotation and flip,
- z-order,
- shape mask/geometry,
- transparency and effects,
- alt text policy.

If new image aspect ratio differs, preserve crop or ask whether fit/fill is preferred. Do not silently stretch a person, logo or product.

## 9. Preservation and risk policy by feature

| Feature | Exact mode policy |
|---|---|
| Simple text, shapes, images | Edit in place after tests |
| Placeholders, masters and layouts | Preserve; update placeholder text without changing master by default |
| Tables | Cell-level updates where supported |
| Native charts | Update data via chart-aware adapter; validate workbook and caches |
| Grouped shapes | Preserve group and edit child only if supported |
| SmartArt/diagrams | Treat as high risk; inspect and preserve or use a verified engine |
| Audio/video | Preserve untouched; never execute/play automatically |
| OLE/embedded packages | Preserve untouched; do not execute |
| Animations/transitions | Preserve and test; do not rewrite without explicit request |
| Notes/comments | Preserve unless explicitly requested |
| Linked media/data | Preserve link; warn if source unavailable or stale |
| Digital signatures | Warn that editing may invalidate signature assurances |
| Password-protected file | Require supported password flow or stop |
| PDF/screenshot reference | Rebuild from visuals; clearly state editability limitations |

## 10. Plugin and connector plan

The skill should expose adapters, not hard-coded dependence on one vendor.

**Minimum local stack**
- File access.
- Python runtime.
- PPTX inspection/editing library.
- Spreadsheet parsing library.
- Rendering engine.
- Vision model for layout understanding.
- Output file delivery.

**Optional connector adapters**
- OneDrive/SharePoint: storage and retrieval through Microsoft Graph or a connected file provider.
- Google Drive: storage/retrieval; Google Slides API for documents converted to Google Slides.
- Excel/Sheets: spreadsheet tables/ranges as replacement content.
- Canva: optional design import/export, never assumed to maintain all PowerPoint object fidelity.
- Image generation: optional visual asset creation.
- GitHub: version code, schemas, examples and test fixtures, not confidential source presentations.

A Google Slides API action operates on a Google Slides presentation. It is not a direct, lossless edit API for a local PPTX. Microsoft Graph file APIs can manage OneDrive/SharePoint files, but do not treat DriveItem file operations as structured slide-object editing. For actual in-app PowerPoint experiences, investigate the Office Add-in JavaScript API separately.

## 11. Suggested skill instruction block

The following should become the core policy section of the eventual reference-deck skill:

~~~text
When a user supplies an existing editable PowerPoint and asks for the same design, layout, structure or style with new content:

1. Treat the existing deck as the source of truth.
2. Determine whether the user wants exact replacement, same-design adaptation, partial edit or reference-guided generation.
3. Preserve the original file and create a separate output copy.
4. Inspect the PPTX structure and render every source slide before editing.
5. Build a reference profile containing slides, objects, geometry, themes, masters, layouts, typography, colours, images, tables and charts.
6. Extract and validate all new content, with source lineage for every important value.
7. Map content to slide objects using explicit instructions, placeholders, labels, shape metadata and visual context.
8. Create and validate an edit manifest before any file write.
9. Change only objects in that manifest. Preserve object type, coordinates, run styling, chart style, image crop and master/layout inheritance whenever possible.
10. Never invent values or change a metric definition. Stop when data is missing or ambiguous.
11. Never flatten a native chart/table/object into an image unless the user accepts that trade-off.
12. Never silently shrink text to an unreadable size or hide overflow.
13. Save a new PPTX, render all slides, and run package, content, data, preservation and visual QA.
14. Repair only failed objects and repeat the tests.
15. Deliver the PPTX, preview, change report, QA result and all warnings. Distinguish verified checks from untested items.
~~~

## 12. Definition of done

An exact replacement task is complete only when:
- The output PPTX opens and passes package validation.
- All requested changes are applied to the intended objects.
- No unintended slide or object was changed, within the tested capabilities of the chosen engine.
- Data and calculations reconcile with their source.
- Every slide was rendered and visually checked.
- Text overflow, chart collisions, broken images and unexpected layout drift are absent or explicitly disclosed.
- The final file is a new editable PPTX where editability was required.
- A change report and QA report are delivered.

A deck that merely looks similar in a generated PDF is not a completed editable-PPTX task.