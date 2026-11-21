# Typography and Font Engineering

**Status:** Reference · **Last reviewed:** 2026-11-21

## Type roles
Display/title, slide headline, section heading, subheading, body, labels, captions/citations, KPI numerals, code.

Specify family, fallback, weight, size, line spacing, paragraph spacing, case, color and maximum line length.

## Font choice
Choose for legibility, tone, language coverage, licensing and target-platform availability. Keep pairings simple. Decorative fonts are generally poor for dense body text.

## Font substitution
If the target machine lacks a font and it is not embedded or otherwise available, software may substitute another. Different metrics can alter wrapping and geometry.

Mitigations: prefer widely available fonts where compatibility matters; check embedding rights; define fallback maps; render in intended environment; validate on a second environment where possible.

## Text fitting
Prefer shortening copy without losing meaning, rebalancing layout, splitting content, and only then modestly adjusting type size within readable bounds. Do not solve all overflow by shrinking.

## Localization
Consider text expansion, glyph coverage, RTL direction, numeral/currency conventions, script-specific fallback and line-breaking.

## QA
Check missing fonts, substitution, clipped glyphs, tiny type, inconsistent styles, broken hyphenation and collisions.