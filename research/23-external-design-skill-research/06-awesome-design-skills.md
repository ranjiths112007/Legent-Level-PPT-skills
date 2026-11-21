# 06 — bergside/awesome-design-skills: Visual Style Preset Library

## Repository identity

- Repository: https://github.com/bergside/awesome-design-skills
- Pinned revision: f631a09b4fcc0166f2e2c1a8c81906ef680c57e8
- Root license observed: MIT; individual font/asset references may carry separate licenses.
- Snapshot: 215 files, 67 style SKILL.md documents.
- Main purpose: a collection of reusable visual-style instruction presets.

Sources:
- [Repository README](https://github.com/bergside/awesome-design-skills/blob/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8/README.md)
- [Skill index/tree](https://github.com/bergside/awesome-design-skills/tree/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8/skills)

## 1. What this repository actually is

This collection is best understood as a **style library**, not a full design agent or PowerPoint generation engine. Each style skill is a compact specification for a visual direction: brand mood, palette, typography, layout preferences, decorative language, accessibility, writing tone and do/don't rules.

It is useful when an agent needs to pick or explain a deliberate visual system. It does not by itself provide:
- a deck storyboard;
- an editable PPTX renderer;
- an asset-generation backend;
- a slide-by-slide data mapper;
- an automated PowerPoint layout validator.

These systems must be supplied separately.

## 2. The 67 style names

The 67 observed skill names are:

1. agentic
2. ant
3. artistic
4. basic
5. bento
6. bold
7. brutalism
8. cafe
9. claude
10. claymorphism
11. clean
12. codex
13. colorful
14. contemporary
15. corporate
16. cosmic
17. creative
18. dithered
19. doodle
20. dramatic
21. editorial
22. enterprise
23. expressive
24. fantasy
25. fiction
26. flat
27. friendly
28. futuristic
29. geometric
30. glassmorphism
31. gradient
32. immersive
33. impeccable
34. levels
35. lingo
36. material
37. matrix
38. minimal
39. modern
40. mono
41. neobrutalism
42. neon
43. neumorphism
44. pacman
45. paper
46. perspective
47. power
48. premium
49. professional
50. pulse
51. refined
52. retro
53. riso
54. roku
55. sega
56. shadcn
57. sketch
58. skeumorphism
59. sleek
60. spacious
61. square
62. stitch
63. storytelling
64. terracotta
65. tetris
66. vibrant
67. vintage

The precise spelling “skeumorphism” is used by the folder name in the inspected tree. Do not silently correct the slug when retrieving the file.

## 3. How the style skills are structured

The common pattern includes:
- mission or intended visual direction;
- brand personality;
- style foundations;
- typography;
- colour;
- components or surface treatment;
- accessibility notes;
- writing tone;
- do/don't rules;
- expected behaviour or implementation guidance;
- guideline authoring workflow.

The document works like a policy card the agent reads before building. The style instructions influence concrete design choices instead of leaving the model to invent all CSS from scratch.

## 4. Style families and what they mean

The styles can be grouped into broader visual families. These are analytical groupings for easier retrieval, not official repository categories.

### Minimal, editorial and professional
- minimal;
- editorial;
- refined;
- professional;
- corporate;
- enterprise;
- contemporary;
- spacious;
- mono;
- clean;
- premium;
- claude.

Typical design signals include restraint, typography hierarchy, whitespace, controlled colour and fewer decorative effects.

### Grid, structure and analytical
- bento;
- geometric;
- square;
- levels;
- ant;
- matrix;
- power;
- material;
- shadcn.

Useful for structured information, dashboards, technical presentations and component-based composition.

### Bold, raw and poster-like
- bold;
- brutalism;
- neobrutalism;
- expressive;
- creative;
- dramatic;
- artistic;
- riso;
- doodle;
- sketch;
- paper.

Typical signals include strong shape/typographic contrast, visible printing/handmade texture, hard geometry and intentionally expressive colour.

### Digital, futuristic and technical
- futuristic;
- neon;
- cosmic;
- immersive;
- matrix;
- gradient;
- glassmorphism;
- claymorphism;
- neumorphism;
- dithered;
- pacman;
- sega;
- tetris.

These can support technology or product storytelling, but may be inappropriate for analytical/client presentations unless restrained.

### Warm, tactile and lifestyle
- cafe;
- terracotta;
- vintage;
- retro;
- friendly;
- colorful;
- vibrant;
- fiction;
- fantasy.

### Named/brand-adjacent style vocabularies
- codex;
- stitch;
- lingo;
- impeccable;
- pulse;
- roku.

Treat named/brand-adjacent styles as visual references, not permission to copy third-party brand assets or trademarks.

## 5. Examples of concrete style directions

The source skills describe specific, operational directions rather than just adjectives:

- **Editorial:** serif display type, restrained body fonts, information hierarchy and spacious composition.
- **Bento:** modular tile/grid composition in which each card carries a clearly separated idea.
- **Brutalism / neobrutalism:** visible structure, strong borders, flat geometry, deliberate contrast and minimal decorative effects.
- **Riso:** limited-colour print palette, paper texture and ink/registration character.
- **Dithered:** pixel/dot texture and reduced colour rendering.
- **Futuristic:** display/technical type pairing, high contrast and controlled electronic/industrial details.
- **Terracotta:** warm paper/earth palette, expressive but restrained display typography and tactile surfaces.
- **Claude/research journal:** warm stone/ivory, slate-like neutrals and quiet editorial hierarchy.

The styles vary in specificity. Some are broad guidance systems; others encode a narrow visual theme. The agent must read the selected file rather than assume the style name alone defines all details.

## 6. How to select a style for a presentation

Do not randomise styles. Use this sequence:
1. infer the audience and context;
2. infer the emotion and level of formality;
3. identify the core content type (research, operations, finance, product launch, narrative, training);
4. choose two plausible design styles;
5. check whether their type/colour/texture language is consistent with the intended content;
6. confirm readability, contrast, slide distance and data clarity;
7. commit to one style for the whole deck.

Do not mix:
- paper editorial with neon cyberpunk;
- glassmorphism with harsh print brutalism;
- playful cartoon with institutional financial reporting;
unless the user specifically requests a deliberate hybrid and the rules are reconciled.

## 7. PPT-specific adaptation

Represent each style preset in a machine-readable schema:
- style ID and intended audience;
- mood/personality;
- palette tokens with semantic roles;
- title/body/mono/caption font roles;
- title and body size ranges;
- spacing and grid;
- shape geometry/radius;
- image treatment and preferred aspect ratios;
- chart palette and data-label rules;
- icon language;
- motif and decorative patterns;
- accessibility constraints;
- examples and anti-patterns.

This lets the PPT system build a design system and pass it to a deterministic PowerPoint renderer.

## 8. Limitations

- These are style specifications, not empirical quality rankings.
- A visual style can be attractive but wrong for the content/audience.
- Some visual motifs, fonts and brand names may require separate licensing review.
- Style rules must be adapted to PowerPoint's fixed-canvas geometry and editability model; a web-style preset cannot be pasted into a PPTX layout unchanged.
- Do not let a theme preset override the user's existing reference deck in exact-preservation mode.