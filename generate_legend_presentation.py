import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.oxml import parse_xml

# -------------------------------------------------------------
# Color Palette (Dark Theme / High-Contrast Modern Corporate)
# -------------------------------------------------------------
BG_COLOR = RGBColor(15, 23, 42)          # Slate-900 (Canvas)
CARD_BG = RGBColor(30, 41, 59)          # Slate-800 (Cards)
CARD_BORDER = RGBColor(51, 65, 85)      # Slate-700 (Card Outline)
TEXT_WHITE = RGBColor(255, 255, 255)    # Primary Headings
TEXT_MUTED = RGBColor(148, 163, 184)    # Slate-400 (Subtext)
TEXT_BODY = RGBColor(226, 232, 240)     # Slate-200 (Body)

ACCENT_BLUE = RGBColor(59, 130, 246)    # Blue-500
ACCENT_CYAN = RGBColor(6, 182, 212)     # Cyan-500
ACCENT_EMERALD = RGBColor(16, 185, 129) # Emerald-500
ACCENT_PURPLE = RGBColor(139, 92, 246)  # Purple-500
ACCENT_ROSE = RGBColor(244, 63, 94)     # Rose-500
ACCENT_AMBER = RGBColor(245, 158, 11)   # Amber-500

FONT_NAME = "Segoe UI"

def set_slide_background(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_transition(slide, trans_type="fade", direction=None):
    if direction:
        xml = f'<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:{trans_type} p:dir="{direction}"/></p:transition>'
    else:
        xml = f'<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:{trans_type}/></p:transition>'
    slide.element.append(parse_xml(xml))

def add_header(slide, category, action_title, subtitle=""):
    # Category Pill / Tag
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8), Inches(0.35))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.name = FONT_NAME
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = ACCENT_CYAN

    # Action Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.7))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = action_title
    p_t.font.name = FONT_NAME
    p_t.font.size = Pt(20)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE

    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(0.4))
        tf_s = sub_box.text_frame
        tf_s.word_wrap = True
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.name = FONT_NAME
        p_s.font.size = Pt(11.5)
        p_s.font.color.rgb = TEXT_MUTED

def add_card(slide, left, top, width, height, bg=CARD_BG, border=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg
    shape.line.color.rgb = border
    shape.line.width = Pt(1)
    return shape

# Initialize Presentation
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# =============================================================
# SLIDE 1: Title Slide
# =============================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1)
add_transition(s1, "fade")

# Decorative top accent line
acc_line = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(1.2), Inches(0.06))
acc_line.fill.solid()
acc_line.fill.fore_color.rgb = ACCENT_CYAN
acc_line.line.fill.background()

# Title text box
t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.5))
tf1 = t_box.text_frame
tf1.word_wrap = True

p_badge = tf1.paragraphs[0]
p_badge.text = "RESEARCH HANDBOOK & MULTI-AGENT ENGINE"
p_badge.font.name = FONT_NAME
p_badge.font.size = Pt(11)
p_badge.font.bold = True
p_badge.font.color.rgb = ACCENT_CYAN
p_badge.space_after = Pt(12)

p_main = tf1.add_paragraph()
p_main.text = "Legend-Level PPT Skills"
p_main.font.name = FONT_NAME
p_main.font.size = Pt(40)
p_main.font.bold = True
p_main.font.color.rgb = TEXT_WHITE
p_main.space_after = Pt(10)

p_sub = tf1.add_paragraph()
p_sub.text = "Deterministic, research-grounded presentation engineering for AI agents. Native OOXML generation, in-place reference deck surgical editing, closed-loop visual QA, and multi-agent ecosystem deployment."
p_sub.font.name = FONT_NAME
p_sub.font.size = Pt(14)
p_sub.font.color.rgb = TEXT_MUTED

# 3 Highlight Feature Badges at Bottom
badges = [
    ("55 Master Sources", "19 pinned git repos + 10 slide tools + Claude docs", ACCENT_BLUE),
    ("Native OOXML Focus", "Real shapes, text boxes, tables & charts (no flat bitmaps)", ACCENT_EMERALD),
    ("Universal Agent Ready", "Claude Code, OpenAI Codex, Cursor, Cline & OpenCode", ACCENT_PURPLE),
]

for i, (title, desc, color) in enumerate(badges):
    bx = Inches(0.8 + i * 3.95)
    card = add_card(s1, bx, Inches(4.7), Inches(3.8), Inches(1.8))
    
    tb = s1.shapes.add_textbox(bx + Inches(0.2), Inches(4.85), Inches(3.4), Inches(1.5))
    tf_b = tb.text_frame
    tf_b.word_wrap = True
    
    p1 = tf_b.paragraphs[0]
    p1.text = title
    p1.font.name = FONT_NAME
    p1.font.size = Pt(16)
    p1.font.bold = True
    p1.font.color.rgb = color
    p1.space_after = Pt(6)
    
    p2 = tf_b.add_paragraph()
    p2.text = desc
    p2.font.name = FONT_NAME
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_BODY

# =============================================================
# SLIDE 2: Problem Statement vs Legend Solution
# =============================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2)
add_transition(s2, "push", "r")
add_header(s2, "The Industry Problem & Solution", 
           "AI Presentation Tools Fail by Outputting Static Screenshots Instead of Software",
           "Comparing conventional single-prompt slide generators with Legend-Level PPT engineering.")

# Left Card: The Conventional Failure
card_left = add_card(s2, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.0), bg=RGBColor(24, 18, 25), border=RGBColor(120, 30, 50))
tb_l = s2.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.5))
tf_l = tb_l.text_frame
tf_l.word_wrap = True

p_lh = tf_l.paragraphs[0]
p_lh.text = "❌ The Conventional AI Trap"
p_lh.font.name = FONT_NAME
p_lh.font.size = Pt(17)
p_lh.font.bold = True
p_lh.font.color.rgb = ACCENT_ROSE
p_lh.space_after = Pt(12)

flaws = [
    ("Uneditable Flat Bitmaps:", "Flattens entire slides into images. Users cannot fix a single typo or update monthly numbers."),
    ("Hallucinated Metric Visuals:", "Asks diffusion models to draw bar charts; numbers, labels, and proportions are completely made up."),
    ("Regenerative Destruction:", "Asking for a small edit re-runs the entire prompt, destroying corporate branding, masters, and unchanged slides."),
    ("Zero Quality Loop:", "Declares 'presentation completed' without ever rendering or verifying text overflows, collisions, or contrast."),
]

for title, desc in flaws:
    p = tf_l.add_paragraph()
    p.text = f"• {title} "
    p.font.name = FONT_NAME
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(8)
    
    run = p.add_run()
    run.text = desc
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# Right Card: Legend-Level Engineering
card_right = add_card(s2, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.0), bg=RGBColor(18, 28, 26), border=RGBColor(20, 85, 60))
tb_r = s2.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.5))
tf_r = tb_r.text_frame
tf_r.word_wrap = True

p_rh = tf_r.paragraphs[0]
p_rh.text = "✓ Legend-Level PPT Engineering"
p_rh.font.name = FONT_NAME
p_rh.font.size = Pt(17)
p_rh.font.bold = True
p_rh.font.color.rgb = ACCENT_EMERALD
p_rh.space_after = Pt(12)

solutions = [
    ("Native OOXML Objects:", "Builds real Microsoft PowerPoint shapes, tables, and data charts with 100% editability."),
    ("Dual-Lane Asset Routing:", "Strict routing: numeric data stays native vector/chart; AI image generation is reserved strictly for hero art."),
    ("Surgical In-Place Preservation:", "Modifies only target XML nodes in existing decks while keeping corporate masters and fonts 100% intact."),
    ("Closed-Loop Visual QA:", "Renders slides via headless LibreOffice and programmatically asserts zero bounding-box overlaps or contrast errors."),
]

for title, desc in solutions:
    p = tf_r.add_paragraph()
    p.text = f"• {title} "
    p.font.name = FONT_NAME
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(8)
    
    run = p.add_run()
    run.text = desc
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# =============================================================
# SLIDE 3: Research Scale & Empirical Data Metrics
# =============================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3)
add_transition(s3, "push", "r")
add_header(s3, "Empirical Foundation & Research Scale",
           "Research Scale: 55 Authoritative Sources Across 6 Knowledge Domains",
           "Building on comprehensive comparative audits of presentations, design systems, and motion libraries.")

stats = [
    ("55", "Master Sources", "19 GitHub repos, 10 slide tools, 11 Claude docs, 8 engines & 7 image repos", ACCENT_BLUE),
    ("68", "Research Files", "516 KB of structured markdown analysis and operational engineering specifications", ACCENT_CYAN),
    ("7,456", "Lines of Knowledge", "Documented failure modes, XML internals, design tokens & validation algorithms", ACCENT_EMERALD),
    ("9+", "Agent Frameworks", "Production configs for Claude Code, Codex, Cursor, Cline, OpenCode, OpenClaw & Antigravity", ACCENT_PURPLE),
]

for i, (num, label, desc, color) in enumerate(stats):
    cx = Inches(0.8 + i * 2.95)
    card = add_card(s3, cx, Inches(1.9), Inches(2.8), Inches(4.9))
    
    tb = s3.shapes.add_textbox(cx + Inches(0.15), Inches(2.1), Inches(2.5), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p_num = tf.paragraphs[0]
    p_num.text = num
    p_num.font.name = FONT_NAME
    p_num.font.size = Pt(38)
    p_num.font.bold = True
    p_num.font.color.rgb = color
    p_num.space_after = Pt(4)
    
    p_lbl = tf.add_paragraph()
    p_lbl.text = label
    p_lbl.font.name = FONT_NAME
    p_lbl.font.size = Pt(14)
    p_lbl.font.bold = True
    p_lbl.font.color.rgb = TEXT_WHITE
    p_lbl.space_after = Pt(14)
    
    p_desc = tf.add_paragraph()
    p_desc.text = desc
    p_desc.font.name = FONT_NAME
    p_desc.font.size = Pt(11)
    p_desc.font.color.rgb = TEXT_MUTED

# =============================================================
# SLIDE 4: Comparative Breakdown: Upstream Landscape
# =============================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4)
add_transition(s4, "wipe", "l")
add_header(s4, "Competitive Synthesis",
           "Competitive Landscape: How Claude and Existing Tools Handle PPTX",
           "Evaluating editability, preservation, and asset generation trade-offs across current platforms.")

# Table comparing tools
table_shape = s4.shapes.add_table(5, 5, Inches(0.8), Inches(1.9), Inches(11.7), Inches(4.8))
table = table_shape.table

# Column widths
table.columns[0].width = Inches(2.3)
table.columns[1].width = Inches(2.4)
table.columns[2].width = Inches(2.3)
table.columns[3].width = Inches(2.3)
table.columns[4].width = Inches(2.4)

headers = ["Capability", "Claude for PowerPoint", "Claude Slides (Artifact)", "Anthropic PPTX Skill", "Legend-Level PPT"]
for col_idx, text in enumerate(headers):
    cell = table.cell(0, col_idx)
    cell.fill.solid()
    cell.fill.fore_color.rgb = RGBColor(40, 53, 75)
    p = cell.text_frame.paragraphs[0]
    p.text = text
    p.font.name = FONT_NAME
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE

rows_data = [
    ("Native Object Export", "Full OOXML via Add-in", "Flattens charts to bitmaps", "Yes (via PptxGenJS)", "Full Native OOXML Objects"),
    ("In-Place Editing", "Yes (Active Office Context)", "No (Canvas Only)", "Weak on complex decks", "Surgical Manifest Patcher"),
    ("Visual QA Loop", "Manual User Review", "Visual Canvas Inspection", "Contact Sheet Render", "Headless Render + Linter"),
    ("Asset Separation", "Relies on manual inserts", "Code & HTML visuals", "Scripts & Code", "Dual-Lane Strict Routing")
]

for row_idx, data in enumerate(rows_data):
    for col_idx, val in enumerate(data):
        cell = table.cell(row_idx + 1, col_idx)
        cell.fill.solid()
        if row_idx % 2 == 0:
            cell.fill.fore_color.rgb = RGBColor(25, 34, 50)
        else:
            cell.fill.fore_color.rgb = RGBColor(20, 27, 40)
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = FONT_NAME
        p.font.size = Pt(11)
        if col_idx == 4:
            p.font.bold = True
            p.font.color.rgb = ACCENT_EMERALD
        elif col_idx == 0:
            p.font.bold = True
            p.font.color.rgb = TEXT_WHITE
        else:
            p.font.color.rgb = TEXT_BODY
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE

# =============================================================
# SLIDE 5: 6-Stage Deterministic Generation Pipeline
# =============================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5)
add_transition(s5, "push", "r")
add_header(s5, "System Architecture",
           "The 6-Stage Pipeline: Eliminating Drift from Brief to Native PPTX",
           "Treating presentation generation as deterministic software engineering.")

stages = [
    ("1", "Audience Objective", "Extract stakeholder goal and outcome shift (from X to Y).", ACCENT_BLUE),
    ("2", "Story Spine", "Draft narrative spine and formulate strict conclusion action titles.", ACCENT_CYAN),
    ("3", "Design Tokens", "Compile color palette, typography scale, and 16:9 layout grid.", ACCENT_EMERALD),
    ("4", "Dual-Lane Assets", "Route metrics to OOXML charts and hero visuals to curated images.", ACCENT_AMBER),
    ("5", "OOXML Assembly", "Generate native presentationML shapes and tables via code.", ACCENT_PURPLE),
    ("6", "Closed-Loop QA", "Render slides via headless LibreOffice and assert 0 collisions.", ACCENT_ROSE)
]

for i, (step, title, desc, color) in enumerate(stages):
    row = i // 3
    col = i % 3
    cx = Inches(0.8 + col * 3.95)
    cy = Inches(1.9 + row * 2.5)
    
    card = add_card(s5, cx, cy, Inches(3.8), Inches(2.3))
    
    tb = s5.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.15), Inches(3.4), Inches(2.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p_step = tf.paragraphs[0]
    p_step.text = f"STAGE {step}"
    p_step.font.name = FONT_NAME
    p_step.font.size = Pt(10.5)
    p_step.font.bold = True
    p_step.font.color.rgb = color
    p_step.space_after = Pt(2)
    
    p_t = tf.add_paragraph()
    p_t.text = title
    p_t.font.name = FONT_NAME
    p_t.font.size = Pt(15)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE
    p_t.space_after = Pt(6)
    
    p_d = tf.add_paragraph()
    p_d.text = desc
    p_d.font.name = FONT_NAME
    p_d.font.size = Pt(11)
    p_d.font.color.rgb = TEXT_MUTED

# =============================================================
# SLIDE 6: Dual-Lane Asset Routing Principle
# =============================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6)
add_transition(s6, "wipe", "l")
add_header(s6, "Asset Engineering Strategy",
           "Dual-Lane Asset Routing: Separate Data Vectors from Conceptual Heroes",
           "Eliminating hallucinated metrics by establishing strict media boundaries.")

# Lane A Card
add_card(s6, Inches(0.8), Inches(1.9), Inches(5.7), Inches(5.0), bg=RGBColor(20, 32, 50), border=RGBColor(40, 80, 140))
tb_a = s6.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.5))
tf_a = tb_a.text_frame
tf_a.word_wrap = True

p_ah = tf_a.paragraphs[0]
p_ah.text = "Lane A: Structured Data & Vectors"
p_ah.font.name = FONT_NAME
p_ah.font.size = Pt(17)
p_ah.font.bold = True
p_ah.font.color.rgb = ACCENT_CYAN
p_ah.space_after = Pt(10)

lane_a_items = [
    ("Numerical Charts:", "Native Bar, Line, Scatter, and Donut charts bound to tabular data series."),
    ("Data Tables:", "Styled native PowerPoint tables with explicit cell padding and formatting."),
    ("Process Diagrams:", "Vector shapes, step chevrons, flow connectors, and matrix cards."),
    ("Iconography:", "Clean, scalable SVG vector paths with consistent stroke weights.")
]

for title, desc in lane_a_items:
    p = tf_a.add_paragraph()
    p.text = f"✔ {title} "
    p.font.name = FONT_NAME
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(8)
    
    run = p.add_run()
    run.text = desc
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# Lane B Card
add_card(s6, Inches(6.8), Inches(1.9), Inches(5.7), Inches(5.0), bg=RGBColor(35, 25, 45), border=RGBColor(100, 60, 140))
tb_b = s6.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.5))
tf_b = tb_b.text_frame
tf_b.word_wrap = True

p_bh = tf_b.paragraphs[0]
p_bh.text = "Lane B: Concept Art & Photography"
p_bh.font.name = FONT_NAME
p_bh.font.size = Pt(17)
p_bh.font.bold = True
p_bh.font.color.rgb = ACCENT_PURPLE
p_bh.space_after = Pt(10)

lane_b_items = [
    ("Hero Art & Photography:", "Atmospheric visual photography establishing emotional context."),
    ("Moodboards & Textures:", "Subtle background patterns, gradient overlays, and brand imagery."),
    ("Unified Art Direction:", "Consistent prompt parameters (Leonxlnx style) across all slides."),
    ("Strict Negative Constraint:", "NEVER prompt an image model to draw text, labels, numbers, or tables.")
]

for title, desc in lane_b_items:
    p = tf_b.add_paragraph()
    p.text = f"✦ {title} "
    p.font.name = FONT_NAME
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(8)
    
    run = p.add_run()
    run.text = desc
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

# =============================================================
# SLIDE 7: Reference Deck Surgical Editing
# =============================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7)
add_transition(s7, "push", "r")
add_header(s7, "Reference-Based Preservation",
           "In-Place Surgical Editing: Updating Data Without Breaking Templates",
           "Guaranteed preservation of master slides, brand layouts, and untouched slides.")

# 3 Horizontal Cards illustrating the workflow
steps_ref = [
    ("Step 1: Intake & Manifest", 
     "Validates against reference-edit-manifest.schema.json. Records file hashes, slide scope, and identifies target shape IDs without mutating source.", 
     ACCENT_BLUE),
    ("Step 2: Surgical XML Patching", 
     "Mutates exact <a:t> text nodes and cached chart data inside ppt/slides/slide{N}.xml. Leaves master slides and layouts 100% untouched.", 
     ACCENT_CYAN),
    ("Step 3: Verifiable Diff & QA", 
     "Ensures package openability, verifies byte invariance of non-target slides, and outputs an audit report of updated metrics.", 
     ACCENT_EMERALD),
]

for i, (title, desc, color) in enumerate(steps_ref):
    cx = Inches(0.8 + i * 3.95)
    card = add_card(s7, cx, Inches(1.9), Inches(3.8), Inches(4.9))
    
    tb = s7.shapes.add_textbox(cx + Inches(0.2), Inches(2.2), Inches(3.4), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p_t = tf.paragraphs[0]
    p_t.text = title
    p_t.font.name = FONT_NAME
    p_t.font.size = Pt(16)
    p_t.font.bold = True
    p_t.font.color.rgb = color
    p_t.space_after = Pt(12)
    
    p_d = tf.add_paragraph()
    p_d.text = desc
    p_d.font.name = FONT_NAME
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = TEXT_BODY
    p_d.space_after = Pt(14)

# =============================================================
# SLIDE 8: Universal Multi-Agent Plugin Deployment
# =============================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8)
add_transition(s8, "fade")
add_header(s8, "Ecosystem Integration",
           "Universal Plugin Architecture: One Standard Across Every Agent",
           "Deployed and ready for Claude Code, OpenAI Codex, Cursor, Cline, OpenCode, OpenClaw & Antigravity.")

platforms = [
    ("Anthropic Claude Code", ".claude-plugin/plugin.json & marketplace manifests for code agents.", ACCENT_AMBER),
    ("OpenAI Codex & ChatGPT", ".codex-plugin/plugin.json and .agents/ ecosystem standards.", ACCENT_CYAN),
    ("Cursor IDE & Rules", ".cursor/rules/legend-ppt.mdc with glob filtering on .pptx files.", ACCENT_BLUE),
    ("Cline / Roo Code", ".clinerules/legend-ppt.md enforcing native object preservation.", ACCENT_EMERALD),
    ("OpenCode & OpenClaw", "5 native slash commands in .opencode/ and mirrored skills in .openclaw/.", ACCENT_PURPLE),
    ("Google Gemini / Antigravity", "gemini-extension.json and global plugin registration in ~/.gemini/config.", ACCENT_ROSE),
]

for i, (name, details, color) in enumerate(platforms):
    row = i // 3
    col = i % 3
    cx = Inches(0.8 + col * 3.95)
    cy = Inches(1.9 + row * 2.5)
    
    card = add_card(s8, cx, cy, Inches(3.8), Inches(2.3))
    
    tb = s8.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.18), Inches(3.4), Inches(2.0))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p_n = tf.paragraphs[0]
    p_n.text = name
    p_n.font.name = FONT_NAME
    p_n.font.size = Pt(15)
    p_n.font.bold = True
    p_n.font.color.rgb = color
    p_n.space_after = Pt(6)
    
    p_det = tf.add_paragraph()
    p_det.text = details
    p_det.font.name = FONT_NAME
    p_det.font.size = Pt(11)
    p_det.font.color.rgb = TEXT_MUTED

# =============================================================
# SLIDE 9: Conclusion & Next-Gen Roadmap
# =============================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9)
add_transition(s9, "push", "r")
add_header(s9, "Strategic Outlook",
           "The Road Ahead: Building the Autonomous Presentation Engineering Standard",
           "Transforming presentation synthesis from uneditable guessing into deterministic software.")

# 2 Wide Summary Cards
card_top = add_card(s9, Inches(0.8), Inches(1.9), Inches(11.7), Inches(2.3), bg=RGBColor(24, 32, 48), border=RGBColor(45, 70, 110))
tb_top = s9.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(11.1), Inches(1.9))
tf_top = tb_top.text_frame
tf_top.word_wrap = True

p_th = tf_top.paragraphs[0]
p_th.text = "🎯 Delivered Milestones"
p_th.font.name = FONT_NAME
p_th.font.size = Pt(16)
p_th.font.bold = True
p_th.font.color.rgb = ACCENT_CYAN
p_th.space_after = Pt(6)

p_tb = tf_top.add_paragraph()
p_tb.text = "• 55-source authoritative research register covering all 19 primary repos, iArt packs, Claude workflows & technical libraries.\n• Full multi-agent plugin suite deployed across Claude, Codex, Cursor, Cline, OpenCode, OpenClaw and Antigravity.\n• Formally specified reference edit schema (reference-edit-manifest.schema.json) for 100% template-safe updates."
p_tb.font.name = FONT_NAME
p_tb.font.size = Pt(11.5)
p_tb.font.color.rgb = TEXT_BODY

card_bot = add_card(s9, Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.3), bg=RGBColor(22, 38, 35), border=RGBColor(35, 95, 75))
tb_bot = s9.shapes.add_textbox(Inches(1.1), Inches(4.7), Inches(11.1), Inches(1.9))
tf_bot = tb_bot.text_frame
tf_bot.word_wrap = True

p_bh = tf_bot.paragraphs[0]
p_bh.text = "🚀 Next-Generation Implementation Horizons"
p_bh.font.name = FONT_NAME
p_bh.font.size = Pt(16)
p_bh.font.bold = True
p_bh.font.color.rgb = ACCENT_EMERALD
p_bh.space_after = Pt(6)

p_bb = tf_bot.add_paragraph()
p_bb.text = "• Headless LibreOffice visual regression testing suite with automated bounding box collision assertions.\n• Live CLI utility for applying surgical reference manifests directly to incoming client decks in seconds.\n• Curated token design galleries integrating Open Design & UI-UX Pro Max style scales directly into PPTX themes."
p_bb.font.name = FONT_NAME
p_bb.font.size = Pt(11.5)
p_bb.font.color.rgb = TEXT_BODY

# Save the presentation
output_path = "d:\\legend level ppt skills\\Legend_Level_PPT_Skills_Presentation.pptx"
prs.save(output_path)
print(f"Presentation successfully created at: {output_path}")
