# Image Generation and Visual Assets

**Status:** Research map  
**Last reviewed:** 2026-11-21

- [Image generation workflow](workflow.md)
- [Prompt engineering](prompt-engineering.md)
- [Asset management, cropping and placement](asset-management.md)
- [Licensing, privacy and provenance](licensing-and-provenance.md)

## Asset decision

```mermaid
flowchart TD
  A[Need a visual] --> B{Purpose?}
  B -->|Data/process/relationship| C[Editable chart or native shapes]
  B -->|Simple symbol| D[Licensed icon or SVG]
  B -->|Photography/complex artwork| E{Suitable source image?}
  E -->|Yes| F[Use with license record]
  E -->|No| G{Generation permitted?}
  G -->|Yes| H[Generate controlled asset]
  G -->|No| I[Placeholder or ask user]
  F --> J[Crop, optimize, alt text]
  H --> J
  C --> K[Place in PPTX]
  D --> K
  J --> K
```

Do not generate every visual. Charts, flowcharts, timelines, tables and simple diagrams are often better as native editable objects.
