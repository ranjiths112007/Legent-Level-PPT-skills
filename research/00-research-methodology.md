# Research Methodology

**Status:** Foundation  
**Last reviewed:** 2026-11-21

## Purpose

This is a living research document, not a claim that every possible presentation issue has already been discovered. Models, renderers, Office versions, design practices, and agent frameworks change. Research must be updated and tested.

## Evidence hierarchy

1. Standards and official file-format/API documentation.
2. Official product documentation and release notes.
3. Peer-reviewed papers and reproducible technical reports.
4. Maintained open-source implementations and issue trackers.
5. User discussions (Reddit, forums, Q&A).
6. Personal observations and hypotheses.

User discussions are valuable for discovering pain points, but should not override technical specifications without explanation.

## Research a user pain point

For each candidate issue:
- Save the canonical discussion URL.
- Record date, community, and product context.
- Summarize neutrally without overgeneralizing.
- Record independent reports.
- Identify the workflow stage.
- Classify consequence: visual defect, data error, editability loss, accessibility, time/cost, compatibility, or trust.
- Seek an independent reproduction or product issue.
- Assign confidence.

Do not infer prevalence from votes or a small number of posts.

## Research a technical topic

Define inputs/outputs, authoritative specifications, implementation options and versions, constraints, failure modes, test fixture, expected/actual behavior, rendering output, compatibility, licensing, and acceptance tests.

## Issue record template

```yaml
id: PPT-000
title: Example issue
category: rendering
evidence_type: user-report
source_url: https://example.com
observed_at: YYYY-MM-DD
affected_tool_versions: unknown
severity: medium
frequency: unknown
reproduction: not-yet-reproduced
impact: describe user-visible impact
hypothesis: possible cause, not confirmed
proposed_test: reproducible validation
confidence: low
status: discovered
```

## Confidence

- **High:** authoritative source or repeatable test, scope stated.
- **Medium:** credible but incomplete evidence, or limited reproduction.
- **Low:** isolated report, inference, or untested explanation.

## Known limits of this snapshot

- Reddit examples are discovery leads, not a representative survey.
- No independent benchmark yet compares all competitors.
- No deck has yet been tested across PowerPoint desktop/web/macOS and LibreOffice.
- Image-model capabilities are provider- and model-version-specific.
- Product behavior must be rechecked before implementation.
