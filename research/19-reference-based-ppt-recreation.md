# Reference-Based PowerPoint Recreation and Data Replacement

> Research and engineering specification for the reference-deck mode of Legend-Level PPT Skills.  
> Status: research-backed design proposal; not yet a validated implementation.  
> Research date: 21 November 2026.

## 1. Capability definition

A user uploads an existing PowerPoint and asks:

> “Use this deck as the reference. I will give you new numbers and text. Make me another PPT with the same structure, design, colours, fonts, layout, charts and visual style. Change only the information.”

This is **reference-based presentation recreation**, also called template-preserving editing, deck adaptation or content replacement in an existing presentation. It is different from ordinary slide generation.

The system must understand two independent inputs:

1. **Reference deck:** slide order, layout, visual design, object geometry, typography, theme, masters, charts, tables, images and recurring patterns.
2. **Replacement content:** new text, facts, metrics, tables, charts, images, dates, labels and relationships between values.

It maps the new content to the correct locations in the reference deck and edits the existing PowerPoint using the smallest safe set of changes.

**Product promise:** preserve the original presentation wherever possible; change only what the user asked to change; verify the exported deck visually and structurally.

Do not promise pixel-identical output for every PPTX. Fonts, rendering engines, unsupported features, longer text and embedded content can make exact fidelity impossible. Disclose limitations and offer deliberate fallbacks rather than silently flattening or redesigning the presentation.

## 2. User requests and modes

The skill must infer the intended mode. Do not mix modes silently.

| Mode | User intent | Default behaviour |
|---|---|---|
| A. Exact replacement | “Keep everything the same; replace these values/text.” | Edit the supplied deck in place. Preserve slide count, order, masters, layouts, objects and styling. |
| B. Same design, new content | “Use this deck’s design for my new report.” | Reuse its design system and slide patterns. Slide count may change only where the new story requires it. |
| C. Same structure, new data | “Here is last month’s deck and this month’s Excel.” | Map new data to existing metrics, tables and charts. Validate totals and formulas. |
| D. Reference-inspired deck | “Make a deck that looks like this.” | Extract design tokens and layout patterns; create a new deck. Object-level preservation is not promised. |
| E. Partial edit | “Only update slides 4, 7 and 9.” | Leave all other slides untouched. Produce a changed-slide report. |
| F. PDF/image reconstruction | “I only have a PDF or screenshots.” | Reconstruct from rendered references. Warn that original editability and hidden structure cannot be recovered. |

**Default:** Mode A when an editable PPTX is uploaded and the user asks for the same design/structure with new values. State this interpretation and proceed conservatively. Ask only when an ambiguity affects a material edit.

### Preserve versus improve

Exact-copy mode must not “improve” the deck by changing colours, fonts, moving objects, restyling charts, adding icons, rewriting titles or changing slide order. Design improvements are a separate request. In exact mode, fidelity outranks the agent’s design preferences.

## 3. Why source-deck editing is the right default

A PPTX is not a collection of slide screenshots. It is an Open Packaging Conventions ZIP package containing related XML parts, media and assets. PresentationML defines the presentation, slide list, slide masters, slide layouts, notes and relationships.

A simplified package may include:

- ppt/presentation.xml — presentation definition and slide order.
- ppt/slides/slideN.xml — content and shape tree for each slide.
- ppt/slides/_rels/slideN.xml.rels — relationships to layouts, images, charts, hyperlinks and other parts.
- ppt/slideMasters/ — shared master elements and inherited formatting.
- ppt/slideLayouts/ — reusable placeholder geometry and layout rules.
- ppt/theme/ — theme colours and fonts.
- ppt/media/ — images, audio and video.
- ppt/charts/ — chart definitions and series.
- ppt/embeddings/ — embedded workbooks and other packages.
- ppt/notesSlides/ — speaker notes.
- [Content_Types].xml and relationship files — package declarations and dependency links.

Relationships matter. A chart or picture may not be stored directly inside slide XML. Copying only slide XML or rebuilding from screenshots can break dependencies and lose functionality.

Microsoft explains this format:
- [Open XML SDK: package structure](https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk)
- [PresentationML overview](https://learn.microsoft.com/en-us/office/open-xml/presentation/overview)
- [PresentationML structure](https://learn.microsoft.com/en-us/office/open-xml/presentation/structure-of-a-presentationml-document)
- [Working with presentation slides](https://learn.microsoft.com/en-us/office/open-xml/presentation/working-with-presentation-slides)
- [Working with slide masters](https://learn.microsoft.com/en-us/office/open-xml/presentation/working-with-slide-masters)

### High-fidelity principle

If the source deck contains a title box, edit that title box. If it contains a native chart, update its data. If it contains a table, update its cells. If it contains a picture with a crop and mask, replace the picture while retaining its crop and geometry. Do not delete the slide and recreate it unless editing cannot be done safely.

This approach can preserve:
- Exact object coordinates, sizes, z-order and alignment.
- Native shape types, grouped objects and connectors.
- Theme, master and layout inheritance.
- Table dimensions and cell styles.
- Chart type, axes, legends and formatting.
- Image crop, rotation and masks.
- Hyperlinks, notes and presentation metadata.

But package preservation depends on the editing library. A library may rewrite package parts even when only one shape is edited. “The file opened and saved” does not mean “lossless round trip.”

## 4. End-to-end workflow

~~~mermaid
flowchart TD
  A[Upload reference PPTX] --> B[Validate and inspect package]
  B --> C[Extract object inventory and relationships]
  B --> D[Render all slides to images]
  C --> E[Build structural reference profile]
  D --> F[Build visual reference profile]
  E --> G[Join visual and structural understanding]
  F --> G
  H[New text, Excel, CSV, PDF or instructions] --> I[Extract and normalize content]
  I --> J[Validate values, units, dates and sources]
  G --> K[Identify editable slots and slide roles]
  J --> L[Map content to slots]
  K --> L
  L --> M[Confidence checks and ambiguity review]
  M --> N[Create edit manifest]
  N --> O[Apply minimal edits to a copy]
  O --> P[Render edited deck]
  P --> Q[Visual, structural, data and text-fit QA]
  Q -->|Fail| R[Targeted repair]
  R --> P
  Q -->|Pass or disclosed exception| S[Deliver PPTX, preview and edit report]
~~~

### Stage 1 — Intake and validation

Accept:
- PPTX as the preferred editable reference.
- POTX as a template source where supported.
- Legacy PPT only through an explicit conversion step; conversion may alter features.
- PDF or slide images as visual-only references.
- XLSX, CSV, DOCX, PDF, text, URLs or instructions as replacement content.

Before processing:
1. Preserve the uploaded source as read-only.
2. Work on a separate copy and write output under a new filename.
3. Check extension, MIME type, file signature, package integrity, size and slide count.
4. Reject or quarantine malformed and encrypted/password-protected files unless a supported password workflow exists.
5. Detect macro-enabled formats and embedded OLE/package content. Never execute macros, scripts or embedded files.
6. Inventory external links, linked media and data connections. Do not fetch external resources without permission.
7. Record hashes and processing metadata where reproducibility is required.

PPTX is ZIP-based. Use safe archive inspection and protect against path traversal, oversized decompression, excessive entry counts and malformed XML. Do not extract arbitrary archive paths into a shared working directory.

### Stage 2 — Structural extraction

Create a machine-readable inventory for every slide and object.

**Slide-level fields**
- Slide index and stable slide-part name.
- Width and height in EMUs; orientation and aspect ratio.
- Layout and master references.
- Background and theme references.
- Notes presence, transition and animation flags.
- Slide relationships and hidden state where detectable.

**Object-level fields**
- Slide index, object ID, shape name and object type.
- Type: text box, placeholder, auto-shape, picture, table, chart, group, connector, SmartArt/diagram, media or unknown.
- Bounding box: x, y, width and height in EMUs.
- Rotation, flip, crop, z-order and grouping ancestry.
- Fill, line, transparency, shadow, effects and geometry.
- Text paragraphs and runs, including font family, point size, bold, italic, underline, colour, hyperlinks, bullets, alignment, margins, spacing and line breaks.
- Table dimensions, cell text and cell styling.
- Chart type, title, categories, series, values, axes, legend, number formats, data labels, source workbook and relationship IDs.
- Picture relationship, media type, source asset, crop rectangle and alt text.
- Placeholder type/index and inherited-style references.

Do not flatten rich text into one string during extraction. A text frame can contain separately formatted runs; rebuilding it may destroy emphasis, hyperlinks, fields or numbering.

### Stage 3 — Rendering and reference profile

Structural metadata cannot fully explain how a deck looks. Render every slide to PNG or another stable image format. Create:
- Full-resolution slide images.
- A contact sheet for deck-wide review.
- Per-slide image dimensions.
- Optional overlays showing object bounds and object IDs.
- A visual comparison baseline for QA.

Use a vision-capable model to interpret:
- Slide purpose and narrative role.
- Visual hierarchy and reading order.
- Fixed branding versus content-dependent elements.
- Alignment, whitespace and grouping.
- Main evidence chart/table and data callouts.
- Repeated layout patterns across slides.
- Decorative versus semantic objects.

Pair vision analysis with structural extraction. Vision-only analysis can misread small labels, data and exact geometry. XML-only analysis can miss perceived hierarchy, whitespace and visual balance.

Create a **Reference Deck Profile** containing:
- Slide sequence and section boundaries.
- Repeated archetypes: cover, agenda, KPI dashboard, comparison, chart, table, process, case study, conclusion and appendix.
- Theme palette and observed non-theme colours.
- Heading/body/label fonts and sizes.
- Backgrounds, margins, grid, recurring shapes and accent rules.
- Chart and table styles.
- Image treatment, aspect ratio, crop style and icon family.
- Logo position, footer, page number and confidentiality treatment.
- Per-slide content regions and object relationships.

Distinguish direct formatting from inherited formatting. A slide can look styled because it inherits properties from a layout or master rather than storing those properties on the slide.

### Stage 4 — Replacement content extraction

Input may be an Excel workbook, CSV, Word report, PDF, raw text, another presentation or a combination.

Build a normalized **Content Model** before editing:
- Source file and sheet/page references.
- Metric or content key.
- Raw and normalized values.
- Unit, currency, date range, denominator and aggregation rule.
- Label, category, group and period.
- Source row/column or document location.
- Data type, null status and validation status.
- Whether the value is user-supplied or derived.

Never invent missing numbers or silently infer an aggregation method. If a metric is On-time %, the system needs the numerator, denominator and definition. A visually matching chart with incorrect data is a failed presentation.

Validation examples:
- Reconcile totals and subtotals.
- Check percentages and verify numerator/denominator.
- Ensure date periods are consistent.
- Confirm units (₹, $, minutes, kilometres, %, counts).
- Detect duplicate rows and inconsistent client/district labels.
- Compare new values with text callouts and chart totals.
- Flag empty cells, formula errors, unexpected negatives and missing categories.

### Stage 5 — Content-to-slot mapping

For each reference object or region, determine whether it is:
- Fixed label, brand element or decoration.
- A content slot to replace.
- A calculation derived from other values.
- A chart/table whose data should be updated.
- A visual asset to retain or replace.
- An element that must remain untouched.

Use multiple signals:
1. User's explicit instructions.
2. Placeholder tokens or recurring labels.
3. Slide title and nearby text.
4. Object name, placeholder type and layout.
5. Chart series and category labels.
6. Spatial context and visual analysis.
7. Similarity to previous-period decks, if supplied.
8. Data dictionary and source column names.

A semantic model may suggest likely matches, but it must not be the only authority for high-impact fields. For recurring reports, use an explicit mapping table or reviewed manifest. If confidence is low, ask the user or present a mapping preview.

**Example:** The old title says “September 2026 Performance” and the new data contains October values. The title slot probably maps to “October 2026 Performance.” A KPI labelled “Total Orders” may map to the orders_total key; a nearby “+12% MoM” callout should be recalculated only if comparison period and formula are known.

### Stage 6 — Edit manifest

Before editing, create an explicit manifest. It is the source of truth for intended changes.

~~~json
{
  "mode": "exact_content_replacement",
  "source": "reference.pptx",
  "output": "updated_report.pptx",
  "preserve_slide_count": true,
  "preserve_slide_order": true,
  "changes": [
    {
      "slide": 3,
      "object_id": "8",
      "object_name": "ReportTitle",
      "operation": "replace_text",
      "target": "October 2026 Performance",
      "source_key": "report_month",
      "confidence": 0.99,
      "preserve_run_formatting": true
    },
    {
      "slide": 5,
      "object_id": "12",
      "object_name": "OrdersChart",
      "operation": "replace_chart_data",
      "source_key": "orders_by_state",
      "preserve_chart_style": true,
      "preserve_chart_type": true,
      "confidence": 0.94
    }
  ],
  "untouched": ["logo", "footer", "master", "slide_backgrounds"]
}
~~~

The full machine-readable contract is in schemas/reference-edit-manifest.schema.json.

### Stage 7 — Minimal edit strategy

Apply the narrowest edit operation that satisfies the request.

| Object | Preferred operation | Preserve |
|---|---|---|
| Text run | Replace intended run/range | Run and paragraph formatting, hyperlinks and fields where possible |
| Text box | Update text frame only when run-level mapping is unsafe | Geometry, fill, line, margins and text style |
| Title placeholder | Update placeholder text | Layout/master inheritance |
| Picture | Replace asset in existing picture shape | Crop, transform, geometry, z-order and effects |
| Table | Update individual cells | Dimensions, cell formatting, merges and position |
| Native chart | Update data and embedded workbook/cache through chart-aware API | Chart type, axes, colours, labels, layout and position |
| Shape/diagram | Change identified text/property only | Grouping, connectors, ordering and geometry |
| Slide | Duplicate/reuse reference layout only when adding a slide is allowed | Master/layout/theme relationships |
| Background/master | Do not touch unless asked | Global deck identity |

Avoid global find-and-replace unless mapping has been checked. The same word may occur in a title, footer, notes, source citation and chart label with different meanings.

For run-level replacements, do not concatenate all frame text and write it back unless the system accepts loss of rich formatting. Text may be split into runs for styling, hyperlinks or field values.

### Stage 8 — Native charts and tables

A chart is more than its visible image. It can have chart XML, a relationship to an embedded workbook, cached values, series formulas, number formats and formatting rules.

For a native editable chart:
1. Identify the chart part and its relationships.
2. Extract chart type, series names, categories and values.
3. Validate incoming data shape against current series and categories.
4. Replace data through a chart-aware library where supported.
5. Confirm workbook source and chart cache reflect new values.
6. Preserve axes, legend, data labels, colours and number formats.
7. Render and confirm visual output matches the data.

If category count changes, axis labels and rotation may become unsuitable. Do not claim exact preservation without visual verification.

A chart pasted as a picture is not a native chart. It requires image replacement or recreation and has no editable series data.

PowerPoint's guidance distinguishes linked/embedded Excel data and picture pastes:
- [Insert and update Excel data in PowerPoint](https://support.microsoft.com/en-us/powerpoint/insert-and-update-excel-data-in-powerpoint)
- [Change data in an existing chart](https://support.microsoft.com/en-gb/powerpoint/change-the-data-in-an-existing-chart)

A PowerPoint table is different from an embedded Excel worksheet. Detect object type before editing.

### Stage 9 — Text fit and overflow

Old text may fit while new text does not. This is a common template-replication failure.

Use this order:
1. Preserve original font size and line spacing if the text fits.
2. Apply normal wrapping when consistent with the source.
3. Shorten wording without changing meaning only if the user permits editorial compression.
4. Reflow inside the same region while preserving hierarchy and alignment.
5. Ask whether adding a slide or using another layout is acceptable.
6. Reduce font size only within a declared minimum size and only if allowed.

Never silently shrink to unreadable sizes, stretch boxes over nearby objects or hide content. Keep a text-fit report.

Check text frame dimensions, line count, estimated rendered height, clipping, overlap with neighbours, minimum font size and actual rendered output. Text measurement alone is not enough.

### Stage 10 — Images and visual assets

For exact replacement:
- Retain the original image if its meaning remains valid.
- Replace only the intended picture asset when the user supplies a new image.
- Preserve crop, aspect ratio, clipping, transparency, effects, rotation and position.
- Keep logos and brand artwork unchanged unless asked.

For a new visual asset:
1. Determine its role: hero, product, background, illustration or evidence.
2. Infer style, composition, subject placement, aspect ratio and colour treatment from reference.
3. Generate or retrieve an asset consistent with the deck.
4. Inspect the result against the slide and reference.
5. Place it in the existing image region, preserving geometry.
6. Record source and usage assumptions.

Do not generate factual charts, numeric labels, tables, logos or exact text. Use native PowerPoint objects or source assets. Generated images are not automatically brand-safe or factually accurate.

## 5. Tool and library assessment

No single library should be assumed to preserve every PowerPoint feature. Use an adapter layer so the editing engine can change without rewriting the reasoning workflow.

| Tool / integration | Best use | Strengths | Cautions |
|---|---|---|---|
| Open XML SDK (.NET) | Low-level PPTX inspection and editing | Official Microsoft tooling; strongly typed PresentationML parts; control over relationships, slides, layouts and masters | More engineering; requires package/schema knowledge |
| python-pptx | Python extraction and common text/shape/table/chart edits | Mature ecosystem; supports existing files, text, images, tables, shapes and common charts | Broad round-trip support is not a guarantee of lossless preservation for every advanced feature; test SmartArt, media, timing, OLE and extensions |
| Aspose.Slides for Python/.NET | Higher-level existing deck edits, text replacement, chart updates and rendering | Broad presentation object model; targeted text and chart APIs; preserve-content features documented | Commercial licensing for the commercial product; verify API/platform/version and terms. Aspose.Slides FOSS for Python is a separate project |
| WolfPPT | Candidate for conservative edits to existing PPTX | New Python package with python-pptx-like API; claims untouched package parts remain byte-identical; MIT community version | Very new in November 2026; project claims are not independent benchmarks. Test before production adoption |
| LibreOffice Impress CLI | Render and convert PPTX for QA | Headless PDF conversion and local rendering; useful in Linux CI | Fonts and rendering may differ from PowerPoint; some features render differently |
| PowerPoint desktop / Office add-in API | In-app editing and user-side rendering | Actual PowerPoint environment; documented add-in object model | Client licensing/deployment; API coverage varies; avoid server-side unattended COM automation |
| PptxGenJS | Generate new slides or fallback rebuilds | JS authoring, charts, shapes and slide master definitions | Primarily a new-deck authoring engine, not the default editor for arbitrary existing decks |
| Google Slides API | Edit after conversion to Google Slides | batchUpdate supports slides, shapes, page elements and tables | Operates on Google Slides documents; conversion can alter fidelity |
| Vision-capable LLM | Interpret layouts and match content to regions | Understands hierarchy, slide purpose, visual patterns and ambiguous references | Approximate; must not determine exact data values, coordinates or final fit alone |
| Image generation model | Create/edit visual assets | Useful for illustrative and photographic assets | Not a native slide editor; never use for authoritative charts or exact text |

### Library recommendation

**MVP:** Python orchestration and extraction, conservative PPTX editing adapter, deterministic renderer and visual QA. Benchmark python-pptx and WolfPPT on the same corpus before choosing. Keep Open XML SDK as a low-level path. Evaluate Aspose if the required feature set/fidelity justifies commercial licensing.

Do not hard-wire the skill to one editor. Define adapter operations such as inspect_deck, replace_text, replace_picture, update_table, update_chart, save_copy, validate_package and render_deck.

### Library evidence and references

- [python-pptx documentation](https://python-pptx.readthedocs.io/en/latest/) lists reading/writing, text, images, tables, shapes and chart capabilities. Its [chart guide](https://python-pptx.readthedocs.io/en/stable/user/charts.html) documents replacing existing chart data.
- [Microsoft Open XML SDK](https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk) explains package parts and relationships.
- [Aspose.Slides: edit presentations](https://docs.aspose.com/slides/features/edit-presentations/), [preserve content](https://docs.aspose.com/slides/features/preserve-content/), [replace text in Python](https://docs.aspose.com/slides/python-net/search-and-replace-text/) and [update charts](https://docs.aspose.com/slides/python-net/create-chart/).
- [WolfPPT PyPI](https://pypi.org/project/wolfppt/) and [source repository](https://github.com/wolfiesch/wolfppt-oss) describe package-preservation claims that must be independently tested.
- [PptxGenJS masters](https://gitbrent.github.io/PptxGenJS/docs/masters) documents authoring masters and placeholders.
- [Google Slides API overview](https://developers.google.com/workspace/slides/api/guides/overview) documents batch updates.
- [LibreOffice PDF export](https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html) documents command-line PDF export options.

## 6. Rendering, QA and repair

A saved file is not necessarily a correct deck. Render the edited presentation and inspect it.

### QA layers

**A. Package integrity**
- PPTX is a valid ZIP/OPC package.
- Required parts and relationships resolve.
- XML parses.
- Slide count, order and list match the manifest.
- No missing media or broken chart relationships.
- No unexpected object deletion.

**B. Structural preservation**
- Untouched slide XML and package parts remain unchanged where the engine supports this.
- Untouched object IDs and shape types remain.
- Master, layout, theme and dimensions remain stable.
- Only intended objects changed.
- Output is separate from source.

**C. Content and data integrity**
- Requested replacement content appears.
- No old values remain in targeted fields.
- Fixed labels, footers and legal text remain.
- Totals, formulas, percentages and chart series reconcile with source.
- Text is not clipped or truncated.
- Dates, units and currencies are consistent.

**D. Visual fidelity**
- Render every slide after editing.
- Compare the new deck with the source.
- Ignore expected differences only in approved change regions.
- Review contact sheet for order, rhythm and theme consistency.
- Inspect changed slides at full resolution.
- Check alignment, font substitution, whitespace, crop, chart labels and overflow.
- Use overlays/difference maps as diagnostics, not the only decision method.

**E. Human review**
- Show uncertain mappings and low-confidence edits.
- Provide preview and changelog.
- Allow rollback to the original.
- Require review for sensitive board, financial, regulatory or client decks.

### Visual comparison

For every slide, keep the original raster, edited raster, alpha overlay, pixel-difference image, optional perceptual score and object-bound comparison.

Pixel differences are noisy when antialiasing or fonts differ. Use them to find likely changed regions, then inspect those regions. An exact-edit result should show differences mainly where approved replacements occurred. Do not optimize a similarity score by hiding meaningful content changes.

### Repair loop

1. Identify failed slide and object.
2. Classify failure: overflow, missing object, wrong data, broken image, font substitution, chart collision, relationship problem or visual drift.
3. Repair only the affected object.
4. Re-render affected slide and complete deck.
5. Re-run relevant checks.
6. Record repair and remaining limitation.

Do not regenerate the full deck to fix one text box. Prefer minimal, reversible edits.

## 7. Plugins, APIs and integrations

The skill must be useful without a specific plugin marketplace. Capabilities come from instructions, file permissions, the editing engine, renderer and model/API calls. Connectors are optional sources and destinations.

| Integration | Role | Required? | Notes |
|---|---|---|---|
| File upload / conversation files | Receive reference deck and new content | Yes | Preferred MVP intake; process in isolated working directory |
| Python runtime | ZIP inspection, parsing, data validation, editing and QA | Strongly recommended | Deterministic operations belong in code |
| PPTX editing library | Read/modify native PowerPoint objects | Yes | Use adapter; benchmark features and fidelity |
| LibreOffice or PowerPoint renderer | Render slide images/PDF | Yes | Record renderer and version |
| Vision model API | Understand slide screenshots and ambiguous regions | Recommended | Send minimal sensitive content |
| Image generation API | Create replacement visuals when requested | Optional | Preserve region geometry and record assets |
| Excel/CSV reader | Extract metrics, tables and data | Required when supplied | Use pandas/openpyxl or equivalent; validate values |
| Google Drive/Docs/Slides APIs | Fetch files or edit Google Slides-native output | Optional | Google Slides batchUpdate edits Google Slides documents, not original PPTX |
| Microsoft Graph / OneDrive / SharePoint | Retrieve/store decks and source files | Optional | Graph DriveItem APIs manage files; do not assume full structured slide editing |
| PowerPoint Office Add-in API | In-app PowerPoint interaction | Optional advanced path | Use documented JavaScript APIs and test supported platforms |
| Canva integration | Optional import/export or design workflow | Optional | Not the core edit engine; verify imports/exports for flattening and element changes |
| GitHub | Store skill code, schemas, tests and docs | Useful for development | Never commit confidential user decks or datasets to public repository |

### Plugin design

Expose capability-focused adapters:
- **File input:** upload/download PPTX and supporting files.
- **Cloud drive:** read/write one approved OneDrive, SharePoint or Google Drive location.
- **Spreadsheet:** retrieve workbook ranges/files and provide structured tables.
- **Vision/image:** analyze slide images and optionally create visual assets.
- **Presentation engine:** local/hosted deterministic inspect/edit/render operations.
- **Delivery:** save finished PPTX, preview PDF and change report to an approved destination.

A connector does not itself preserve slide fidelity; it only provides access. Never request broad access to a drive when one file is sufficient. Ask authorization and use least privilege.

### PowerPoint automation warning

Microsoft documents risks of unattended server-side Office automation, including instability, deadlocks, interactivity assumptions and security concerns. For server-side processing, prefer Open XML-based libraries or components designed for unattended use. A desktop add-in or explicit user-operated PowerPoint session is a different deployment model.

Sources:
- [Microsoft: server-side Office automation](https://support.microsoft.com/en-us/visio/considerations-for-server-side-automation-of-office)
- [Microsoft: unattended Office automation in Microsoft 365 RPA](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
- [Microsoft Graph: OneDrive file operations](https://learn.microsoft.com/graph/api/resources/onedrive?view=graph-rest-1.0)
- [Google Slides API overview](https://developers.google.com/workspace/slides/api/guides/overview)

## 8. Failure cases and defensive behaviour

| Failure | Cause | Required response |
|---|---|---|
| New text does not fit | Different length/language | Wrap/reflow; keep legible; ask before reducing font or adding slides |
| Wrong value maps to chart | Similar labels or ambiguous source | Explicit mapping, data lineage and reconciliation; block low-confidence edits |
| Chart shows old values | Embedded workbook/cache not both updated | Validate both and render |
| Image crop changes | Different aspect ratio or fill semantics | Preserve crop/transform or ask for crop decision |
| Font changes | Missing font on renderer/target machine | Detect substitution; record it; use approved fonts |
| Master change affects all slides | Inherited styles propagate | Do not edit masters by default; inspect dependent slides |
| Object becomes uneditable | Screenshot/flattened replacement | Disclose flattening; require approval when editability matters |
| SmartArt/media breaks | Incomplete library support | Detect high-risk feature; preserve/skip or use tested engine |
| Unsupported feature lost on save | Editor rewrites package | Compare package parts; use preservation-oriented engine or block |
| External data stale | Linked workbook/media unavailable | Warn; do not silently refresh or fetch |
| Different language changes layout | Text expansion and font metrics | Reflow only in permitted mode; inspect every slide |
| Notes/hidden slides altered | Inventory ignores non-visible content | Inventory and preserve by default |
| Signature invalidated | Package edited and re-saved | Warn that signature assurances may be invalidated |

## 9. Security, privacy and licensing

- Treat every uploaded file as untrusted.
- Do not execute VBA, OLE objects, embedded scripts, links or macros.
- Never dereference arbitrary external links automatically.
- Isolate file processing; enforce file-size, decompression and XML limits.
- Keep originals read-only; save a separate output copy.
- Do not send confidential decks to external vision/image APIs without authorization.
- Minimize data sent to vision models; crop or redact where possible.
- Never commit user decks, datasets, API tokens, credentials or sensitive logs to GitHub.
- Retain only data needed to perform the task and follow deployment retention policies.
- Review licenses for libraries, fonts, icons, images and generated assets. Free skill code does not imply every dependency or asset is free for commercial use.
- Do not copy competitor code because its behaviour is documented; implement independently unless its license permits reuse.

## 10. Recommended architecture

Separate the **reasoning skill** from the **deterministic editing runtime**.

~~~mermaid
flowchart TB
  U[User request and files] --> A[Reference-deck skill / orchestrator]
  A --> I[Intake and security]
  I --> X[Deck inspector]
  I --> C[Content extractor]
  X --> P[Reference profile]
  C --> D[Normalized content model]
  P --> M[Mapping planner]
  D --> M
  M --> V[Confidence checks and edit manifest]
  V --> E[Editing adapter]
  E --> R[Renderer]
  R --> Q[QA engine]
  Q -->|Repair| E
  Q -->|Pass| O[PPTX + PDF preview + edit report]
~~~

### Components

1. **Reference-deck skill (SKILL.md):** intent detection, required inputs, mode selection, preservation rules and orchestration.
2. **Intake validator:** extensions, archives, encryption, macros and relationships.
3. **Deck inspector:** package parts, slide/object inventory, text runs, tables, charts, assets and layout.
4. **Renderer:** slide images, PDF and contact sheet.
5. **Vision interpreter:** design intent, slide roles and hierarchy.
6. **Content extractor:** structured content from spreadsheets and documents.
7. **Content validator:** numeric integrity, dates, units and lineage.
8. **Mapping planner:** content keys to objects with confidence and evidence.
9. **Edit manifest:** all planned edits, untouched elements and preservation rules.
10. **Editing adapter:** minimal object-level edits.
11. **QA engine:** package validity, preservation, text fit, data correctness and visual similarity.
12. **Repair agent:** repairs only failed objects and repeats tests.
13. **Delivery reporter:** PPTX, preview, changed-slide list, warnings and provenance.

### Suggested repository layout

~~~text
reference-ppt-skill/
├── SKILL.md
├── README.md
├── schemas/
│   ├── deck-profile.schema.json
│   ├── content-model.schema.json
│   └── reference-edit-manifest.schema.json
├── src/
│   ├── intake/
│   ├── inspect/
│   ├── render/
│   ├── content/
│   ├── mapping/
│   ├── edit_adapters/
│   ├── qa/
│   └── reporting/
├── prompts/
│   ├── slide-visual-analysis.md
│   ├── content-mapping.md
│   └── repair-planner.md
├── tests/
│   ├── fixtures/
│   ├── expected/
│   ├── test_package_integrity.py
│   ├── test_text_preservation.py
│   ├── test_chart_data.py
│   └── test_visual_regression.py
└── examples/
    ├── exact-text-replacement/
    ├── monthly-data-update/
    └── reference-guided-new-deck/
~~~

## 11. Specialist sub-skills

Recommended focused modules:
- reference-deck-inspector — package and object inventory.
- slide-render-and-vision-audit — render and visually describe slides.
- design-system-extractor — typography, colours, spacing and components.
- content-source-extractor — parse new files into structured data.
- content-slot-mapper — match information to existing regions.
- native-pptx-editor — change text, picture, table, chart and shape objects.
- chart-data-updater — series, categories, formulas, cache and appearance.
- text-fit-checker — detect overflow and maintain legibility.
- pptx-preservation-checker — compare package parts and relationships.
- visual-regression-reviewer — detect unexpected visual drift.
- change-report-generator — report changes, unchanged items and warnings.

These are modules with narrow responsibilities, not 11 independent agents that all rewrite the same deck. The orchestrator calls deterministic tools; model reasoning is used only for semantic and visual interpretation.

## 12. Implementation roadmap

### Phase 1 — Inspect safely
- Accept PPTX, validate and copy source.
- Extract slide count, size, object inventory, text and image references.
- Render slides and create contact sheet/deck profile.
- Do not edit yet.
- Test decks with text, pictures, tables, charts, groups, notes and multiple masters.

**Exit criterion:** inspect a representative corpus without changing the source.

### Phase 2 — Safe text replacement
- Explicit object-ID or placeholder mapping.
- Preserve run-level styling.
- Support placeholders, shapes, tables and notes only when requested.
- Output copy, change report, overflow detection and render-after-edit.

**Exit criterion:** text updates preserve unmodified elements in tested decks.

### Phase 3 — Tables and native charts
- Update table cells without rebuilding table.
- Update chart series and embedded data using chart-aware library.
- Validate totals/categories/caches.
- Add chart render QA.

**Exit criterion:** charts/tables show correct data and retain tested styling.

### Phase 4 — Images and design reuse
- Replace image assets while preserving crop and geometry.
- Extract slide archetypes and design tokens.
- Add reference-driven new-slide fallback.
- Record flattened versus editable objects.

**Exit criterion:** asset replacement and new-slide reuse do not cause unexpected theme drift.

### Phase 5 — Integrated report updating
- Add Excel/CSV/document ingestion.
- Confidence-based mapping.
- Optional cloud drive adapters and approval UI.
- Full visual regression and repair.
- Build benchmark fixtures with permission.

**Exit criterion:** update a recurring report from new source data and return a verified edit report.

## 13. Test strategy and success metrics

Build a consented benchmark corpus:
- Corporate template with master/layout inheritance.
- Monthly operations report with KPIs and charts.
- Financial deck with tables and percentage calculations.
- Multiple masters and section dividers.
- Custom fonts and image crops.
- Hidden slides and speaker notes.
- SmartArt, audio/video, OLE and animations.
- Deck converted from Google Slides or Keynote.
- Native charts mixed with chart screenshots.
- Long replacement text.

Score these dimensions separately:

| Metric | Measures |
|---|---|
| Mapping accuracy | Correct content reaches the intended object |
| Data correctness | Numbers, formulas, units and chart series are correct |
| Preservation rate | Untouched objects and package parts survive |
| Visual fidelity | Unchanged regions remain visually consistent |
| Text-fit rate | Text renders without clipping or illegible shrinking |
| Editability rate | Replaced objects remain native where expected |
| Relationship integrity | No broken image/chart/media/layout links |
| Repair rate | Failures fixed by targeted repair |
| Transparency | Warnings and non-editable objects disclosed |

Do not claim “95% accurate” without a reproducible corpus, scoring rubric and measured results.

## 14. Product rules — non-negotiable

1. Preserve the original deck whenever an editable PPTX is provided.
2. Never rebuild from scratch in exact mode unless the user approves.
3. Keep slide count, order, aspect ratio, master and theme stable in exact mode.
4. Edit only objects listed in the manifest.
5. Never fabricate missing values, categories, sources or chart data.
6. Never replace a native chart with an image without approval.
7. Never silently shrink fonts below the approved legibility threshold.
8. Do not run macros, embedded packages or external links.
9. Save a separate output copy; keep the source untouched.
10. Render and inspect every slide after modification.
11. Reconcile visible numbers with supplied data.
12. Report edits, untouched elements, warnings and validation results.
13. Distinguish confirmed preservation from best-effort preservation.
14. Never claim pixel-perfect fidelity or full editability unless checked.

## 15. Research sources

1. [Microsoft Open XML SDK — package structure](https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk)
2. [Microsoft PresentationML overview](https://learn.microsoft.com/en-us/office/open-xml/presentation/overview)
3. [Microsoft PresentationML structure](https://learn.microsoft.com/en-us/office/open-xml/presentation/structure-of-a-presentationml-document)
4. [Microsoft working with presentation slides](https://learn.microsoft.com/en-us/office/open-xml/presentation/working-with-presentation-slides)
5. [Microsoft working with slide masters](https://learn.microsoft.com/en-us/office/open-xml/presentation/working-with-slide-masters)
6. [python-pptx documentation](https://python-pptx.readthedocs.io/en/latest/)
7. [python-pptx chart updates](https://python-pptx.readthedocs.io/en/stable/user/charts.html)
8. [Aspose.Slides — edit presentations](https://docs.aspose.com/slides/features/edit-presentations/)
9. [Aspose.Slides — preserve existing content](https://docs.aspose.com/slides/features/preserve-content/)
10. [Aspose.Slides Python — replace text](https://docs.aspose.com/slides/python-net/search-and-replace-text/)
11. [Aspose.Slides Python — update charts](https://docs.aspose.com/slides/python-net/create-chart/)
12. [WolfPPT PyPI](https://pypi.org/project/wolfppt/)
13. [WolfPPT source repository](https://github.com/wolfiesch/wolfppt-oss)
14. [PptxGenJS slide masters](https://gitbrent.github.io/PptxGenJS/docs/masters)
15. [Google Slides API overview](https://developers.google.com/workspace/slides/api/guides/overview)
16. [Google Slides API request reference](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations/request)
17. [OpenAI image and vision docs](https://developers.openai.com/api/docs/guides/images-vision)
18. [Microsoft insert/update Excel data in PowerPoint](https://support.microsoft.com/en-us/powerpoint/insert-and-update-excel-data-in-powerpoint)
19. [Microsoft change data in an existing chart](https://support.microsoft.com/en-gb/powerpoint/change-the-data-in-an-existing-chart)
20. [LibreOffice PDF export parameters](https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html)
21. [Microsoft server-side Office automation considerations](https://support.microsoft.com/en-us/visio/considerations-for-server-side-automation-of-office)
22. [Microsoft unattended Office automation considerations](https://learn.microsoft.com/en-us/office/client-developer/integration/considerations-unattended-automation-office-microsoft-365-for-unattended-rpa)
23. [Microsoft Graph OneDrive file API](https://learn.microsoft.com/graph/api/resources/onedrive?view=graph-rest-1.0)

### Evidence limitations

This is a research-backed engineering proposal, not proof that every listed library preserves every PPTX feature. WolfPPT is a very recent project as of this research date; its package-preservation claims require independent tests. Licensing and API support can change. Pin versions, verify licenses and run the proposed benchmark corpus before implementation.