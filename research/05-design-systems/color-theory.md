# Color Theory and Palette Engineering

**Status:** Reference  
**Last reviewed:** 2026-11-21

## Semantic roles

Background, surface, primary/secondary text, primary brand, secondary brand, accent, positive/warning/negative status, chart series, borders/dividers.

## Color models

- HEX/RGB: common digital representation.
- HSL/HSV: intuitive hue/saturation/lightness controls, not perceptually uniform.
- CIELAB/LCH: useful for perceptual relationships.
- CMYK: print-oriented; does not replace screen checks.

## Palette strategies

Monochromatic; analogous; complementary; split-complementary; triadic. Usually choose one dominant role and restrain accents.

## Charts

Use stable series colors. Do not rely on color alone; add labels, symbols or patterns. Avoid red/green as the only distinction. Use sequential palettes for ordered magnitude, diverging for values around a meaningful midpoint, and categorical palettes for distinct groups.

## Common failures

Accent everywhere; low text/background contrast; too many unrelated colors; inconsistent series mapping; similar series colors; unintended cultural/status associations.

## Validation

- [ ] Contrast checked for intended viewing conditions.
- [ ] Status not communicated by color alone.
- [ ] Chart categories distinguishable.
- [ ] Palette consistent.
- [ ] Semantic color roles defined.
- [ ] Grayscale/print considered where relevant.
- [ ] Brand colors taken from an authoritative source.

WCAG is a web standard; it can inform contrast practice but is not a complete presentation-viewing standard. See sources.
