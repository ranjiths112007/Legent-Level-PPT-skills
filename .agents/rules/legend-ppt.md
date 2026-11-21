# Legend-Level PPT Agent Rule

Apply these instructions whenever creating, editing, inspecting, or reviewing presentation files (.pptx, slide outlines, charts, or pitch decks).

1. **Native OOXML Objects Only:** Use real PowerPoint text boxes, tables, shapes, and charts. Never paste full-slide flat images.
2. **Action Titles:** Every slide title must state an active business takeaway or conclusion, never a generic static topic.
3. **Reference-Deck Immutability:** When modifying an existing deck, never regenerate the file from scratch. Edit target objects in `slide{N}.xml` directly or via safe in-place mutations. Keep layouts, masters, and untouched slides 100% intact.
4. **Dual-Lane Visuals:** Process diagrams, matrices, and charts must be native vectors. Diffusion images are reserved for hero photography. Never generate text/tables inside AI images.
5. **Closed-Loop QA:** Validate bounding-box collisions, contrast ratios, and font fallbacks before completion.
