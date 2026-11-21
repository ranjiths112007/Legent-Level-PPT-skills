# Image Generation and Visual Assets

Topic map:
- [Generation workflow](workflow.md)
- [Prompt engineering](prompt-engineering.md)
- [Asset management, cropping and placement](asset-management.md)
- [Licensing, privacy and provenance](licensing-and-provenance.md)

```mermaid
flowchart TD
 A[Need a visual] --> B{Purpose?}
 B -->|Data/process/relationship| C[Editable chart or shapes]
 B -->|Simple symbol| D[Licensed icon or SVG]
 B -->|Photo/complex artwork| E{Suitable source image?}
 E -->|Yes| F[Use with license record]
 E -->|No| G{Generation permitted?}
 G -->|Yes| H[Generate controlled asset]
 G -->|No| I[Placeholder or ask user]
 F --> J[Crop, optimize, alt text]
 H --> J
 C --> K[Insert into PPTX]
 D --> K
 J --> K
```

Do not generate every visual. Charts, flowcharts, timelines, tables and simple diagrams are often better as native editable objects.