# 03 — cathrynlavery/diagram-design: Semantic Diagrams and Branded SVG

## Repository identity

- Repository: https://github.com/cathrynlavery/diagram-design
- Pinned revision: d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0
- Root license: MIT.
- Tree inventory: 776 files; one primary skill document.
- Install route documented by its README: npx skills add cathrynlavery/diagram-design.
- Scope: diagram generation from natural-language requirements, diagram imports/exports, brand onboarding and validation.

Sources:
- [Repository README](https://github.com/cathrynlavery/diagram-design/blob/d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0/README.md)
- [Primary diagram skill](https://github.com/cathrynlavery/diagram-design/blob/d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0/skills/diagram-design/SKILL.md)
- [Agent guidance](https://github.com/cathrynlavery/diagram-design/blob/d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0/AGENTS.md)

## 1. Core idea: determine meaning before drawing

The skill's central method is **semantic-first diagram selection**. The model should first understand what relationship the user is trying to communicate, then select the diagram type best suited to that relationship.

A process with ordered stages is not the same thing as a system architecture. A timeline is not the same as a sequence diagram. A comparison matrix is not the same as a data-flow map. Asking the model to draw a generic “diagram” often produces the wrong visual grammar.

The workflow is therefore:
1. understand entities and relationships;
2. determine whether time, flow, hierarchy, grouping, comparison, distribution, risk or dependency is the main semantic dimension;
3. select a diagram type;
4. choose the visual style;
5. map brand colours and typography;
6. lay out nodes, labels and connectors;
7. validate readability and structural correctness;
8. export in the requested format.

## 2. Diagram catalogue

The skill describes 51 diagram families. They cover several groups.

### System and engineering
- system architecture;
- architecture delta;
- IT current state;
- deployment diagram;
- data flow;
- medallion architecture;
- database schema;
- ER/data model;
- UML class;
- sequence diagram;
- state machine;
- dependency graph;
- arc diagram;
- event modeling;
- requirements traceability;
- security/integration matrix.

### Process and operations
- flowchart;
- process;
- numbered steps;
- swimlane;
- timeline;
- Gantt;
- schedule network;
- kanban;
- user journey;
- service blueprint;
- story map;
- flywheel;
- decision tree.

### Strategy and conceptual frameworks
- quadrant;
- radar;
- polar;
- nested diagram;
- tree;
- org chart;
- layer stack;
- axonometric;
- Venn;
- pyramid;
- funnel;
- fishbone;
- Wardley map.

### Quantitative and data-oriented
- treemap;
- Marimekko;
- unit grid;
- heatmap;
- bar;
- dumbbell;
- waterfall;
- line;
- slopegraph;
- ridgeline;
- streamgraph;
- bump chart;
- scatter;
- bubble;
- beeswarm;
- box plot;
- Sankey.

The exact set is defined in the primary skill. The categories above regroup it for easier retrieval.

## 3. Output formats and compatibility

The repository's primary diagram output is an HTML wrapper with inline SVG. SVG is important because it remains vector-based and can be inspected or edited as a structured drawing. The HTML wrapper is useful for preview and presentation, but it is not itself a native PowerPoint deck.

Supported import formats named by the project:
- Draw.io files;
- Mermaid source;
- Excalidraw files;
- PlantUML source.

Export routes include SVG and PNG. The repository describes commands/plugins for export, import, profile and doctor-style checks.

**Important:** “editable SVG” and “native PowerPoint shapes” are not interchangeable. SVG may be inserted as a scalable visual object; native PowerPoint shapes offer more direct element-level editing inside PowerPoint. Our renderer should preserve both options and identify which is being delivered.

## 4. Design constraints

The style system deliberately limits visual noise:
- use a 4px grid;
- avoid CSS shadows;
- keep node density relatively low (target around 4/10);
- use accent colour for one or two focal elements;
- favour hairline strokes;
- keep labels readable and connectors unambiguous;
- choose a style-guide profile for the brand before rendering.

The skill contains three named style variants:
- minimal-light;
- minimal-dark;
- full-editorial.

It also requires first-time style onboarding when brand information is not already available. Brand profile extraction can include palette and fonts from a URL or project context.

The guiding principle is that a diagram's layout should reduce cognitive effort, not maximise the number of elements.

## 5. Connector and layout discipline

The drawing instructions place emphasis on:
- clear node-to-node connector direction;
- appropriate spacing between connected and unrelated elements;
- avoiding line crossings where possible;
- maintaining readable labels;
- avoiding decorative complexity that makes relationships harder to understand;
- using a complexity budget so large diagrams are split or simplified.

A summary card or short takeaway can accompany a large diagram so the reader understands the main message without decoding every node.

## 6. Why the skill argues against Mermaid slop

The project criticises default-looking Mermaid diagrams when they are used as the final visual in a polished presentation. The issue is not Mermaid itself; it is the tendency to produce undifferentiated node-and-arrow diagrams with poor hierarchy and density.

The repository recognises that Mermaid remains useful for:
- documentation;
- pull requests;
- code review;
- diagrams frequently changed as text;
- situations where version-control diffs are valuable.

For a designed deck, the key lesson is to treat the diagram as a visual composition with an explicit type, grid, hierarchy and visual grammar. Mermaid can still be the source representation for simpler cases.

## 7. Frameworks, libraries and tools

Directly documented format/tool references include:
- inline SVG as the core editable vector drawing output;
- HTML for wrapping and previewing diagrams;
- Draw.io import;
- Mermaid import;
- Excalidraw import;
- PlantUML import;
- SVG export;
- PNG export;
- an install mechanism through the Skills CLI;
- command/plugin routes for import, export, profiling and health checks.

The repository includes Node and Python CI package manifests for its own validation/build checks. Do not infer an exact production rendering dependency list from the GitHub Actions CI package files. Inspect the actual scripts and package manifests before locking runtime versions.

## 8. How to apply this to PPT

A diagram planner in our presentation engine should have a structured decision function:

| User's information | Preferred diagram family |
|---|---|
| Ordered tasks/stages | Process flow or timeline |
| System components and dependencies | Architecture/data-flow diagram |
| Sequence of messages/actions | Sequence diagram |
| Status/state transitions | State-machine diagram |
| Responsibilities across roles | Swimlane or service blueprint |
| Comparison of two or more options | Matrix or aligned comparison |
| Relative performance across dimensions | Radar, bar or dumbbell |
| Distribution/variation | Box plot, histogram or beeswarm |
| Contribution to a total | Stacked bar, treemap or unit grid |
| Movement across stages | Funnel or Sankey |
| Strategy/market positioning | Quadrant or Wardley map |
| Milestones and ownership | Gantt or roadmap |
| Entity relationships | ER/data-model diagram |

Use native PowerPoint shapes/connectors for diagrams that users may want to edit. Use SVG for highly complex vector artwork or where the generator cannot reliably create individual PowerPoint shapes. Always render and inspect.

## 9. Limitations

- This is a diagram capability, not a general presentation generator.
- SVG output does not guarantee that each visual primitive can be edited as a native PowerPoint object.
- Diagram type selection still depends on correct interpretation of source relationships.
- Large diagrams need simplification, splitting or a summary; shrinking everything until it fits is not an acceptable solution.
- The repository's own diagram style preferences should not be treated as universal laws for all brands or audiences.