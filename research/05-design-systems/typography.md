# Typography and Font Engineering

**Status:** Reference  
**Last reviewed:** 2026-11-21

## Type roles

Display/title, slide headline, section heading, subheading, body, labels, captions/citations, numeric KPIs, code snippets.

Specify family, fallback, weight, size, line spacing, paragraph spacing, case, color and maximum line length.

## Font choice

Choose for legibility, tone, language coverage, licensing and platform availability. Avoid decorative fonts for dense body text. A simple display/body pairing is often safer than many families.

## Substitution risk

If the target machine lacks a font and it is not embedded/available, software may substitute another. Different glyph metrics can change wrapping and geometry.

Mitigations: prefer widely available fonts when compatibility matters; check licenses and embedding rights; provide fallback maps; render with intended environment; validate on a second environment where possible.

## Text fitting

Prefer shortening copy without losing meaning, rebalancing layout, splitting content, and only then modestly adjusting font size within readable bounds. Do not solve every overflow by shrinking text.

## Localization

Consider text expansion, glyph coverage, RTL direction, numeral/currency conventions, script-specific fallback and line-breaking.

## QA

Missing fonts, substitution, clipped glyphs, unreadably small text, inconsistent styles, broken hyphenation, and collisions.
