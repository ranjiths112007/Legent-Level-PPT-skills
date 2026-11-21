# 13 — Source, Provenance and License Register

> Snapshot date: 21 November 2026. Repository licenses below were recorded from the pinned revisions listed in the research README. This is an engineering provenance register, not legal advice.

## Pinned repositories

| Source repository | Pinned commit | Root license recorded | Research file |
|---|---|---|---|
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/f6b76575f949707b4e3c37cd86cb44b0b98643e8) | `f6b76575f949707b4e3c37cd86cb44b0b98643e8` | MIT | [01](01-taste-skill.md) |
| [nexu-io/open-design](https://github.com/nexu-io/open-design/tree/e033aad1d15a9d4084316e5223f2c6597fd32619) | `e033aad1d15a9d4084316e5223f2c6597fd32619` | Apache-2.0 | [02](02-open-design.md) |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design/tree/d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0) | `d74d8c2d0c78a9e1efd43137f6a9a51182a8b5f0` | MIT | [03](03-diagram-design.md) |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/2de1134dc4d1cfe112934611ae5803ae17a1bd7e) | `2de1134dc4d1cfe112934611ae5803ae17a1bd7e` | MIT | [04](04-ui-ux-pro-max.md) |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills/tree/62fdcd679747aca0792e5dd6591b10ddfad56825) | `62fdcd679747aca0792e5dd6591b10ddfad56825` | Apache-2.0 | [05](05-stitch-skills.md) |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills/tree/f631a09b4fcc0166f2e2c1a8c81906ef680c57e8) | `f631a09b4fcc0166f2e2c1a8c81906ef680c57e8` | MIT | [06](06-awesome-design-skills.md) |
| [emilkowalski/skills](https://github.com/emilkowalski/skills/tree/64eb3deb9a5fbfa041faf783e0bc3fd635872e9c) | `64eb3deb9a5fbfa041faf783e0bc3fd635872e9c` | MIT | [07](07-emilkowalski-skills.md) |
| [owl-listener/designer-skills](https://github.com/owl-listener/designer-skills/tree/9a6930cf84a822eb458624bd11c61aac5bbdf224) | `9a6930cf84a822eb458624bd11c61aac5bbdf224` | MIT | [08](08-designer-skills.md) |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills/tree/672ae44ace6aaed65b86cbb1e2fd6fbea0e79578) | `672ae44ace6aaed65b86cbb1e2fd6fbea0e79578` | MIT | [09](09-jakubkrehel-skills.md) |
| [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master/tree/63a03673d5c3c928e7f52983a2c8ec65bac30002) | `63a03673d5c3c928e7f52983a2c8ec65bac30002` | MIT | [14](14-ppt-master.md) |
| [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides/tree/9906a34d640d2111f724544cbc50f7f130569ae1) | `9906a34d640d2111f724544cbc50f7f130569ae1` | MIT | [15](15-frontend-slides.md) |
| [Akxan/ppt-agent-skill](https://github.com/Akxan/ppt-agent-skill/tree/e2f97f46a2f92633d3f9b95a1a61b0a668c704b3) | `e2f97f46a2f92633d3f9b95a1a61b0a668c704b3` | MIT | [16](16-ppt-agent-skill.md) |
| [proyecto26/slides-ai-plugin](https://github.com/proyecto26/slides-ai-plugin/tree/1f8505f3a89e6cafd863ebbd0ed8b465db4f3820) | `1f8505f3a89e6cafd863ebbd0ed8b465db4f3820` | MIT | [17](17-slides-ai-plugin.md) |

## Evidence and reuse rules

1. A root repository license is not proof that every bundled image, font, icon, model, video, upstream skill, package or third-party template has the same license.
2. OpenDesign and Stitch Skills are recorded as Apache-2.0 at the pinned revisions; the other seven are recorded as MIT. Re-check the exact LICENSE file and any subdirectory notices before copying code.
3. Some repositories contain catalogue entries that point to upstream projects. The catalogue author's license does not automatically relicense the upstream project.
4. Preserve required copyright, attribution, NOTICE files and license texts when redistributing covered material.
5. Prefer learning from documented ideas and independently implementing the behavior. Do not copy large blocks of skill prose or assets into our repository without checking permission and attribution requirements.
6. Record source URL, commit SHA, file path, retrieval date, license, asset origin and modifications for any reused material.
7. For generated images, retain provider/model, prompt or brief, generation date, source asset references and any applicable provider terms.

## Provenance labels used in this research

- **Observed in source:** directly visible in a pinned source file or tree.
- **Repository claim:** described by the repository, not independently run.
- **Inferred workflow:** reconstructed from several files.
- **Recommendation:** proposed for Legend-Level PPT Skills.
- **Unverified:** requires execution, current documentation or legal review.

## Refresh procedure

Before a new release:
1. Fetch the latest commit SHA for each upstream repository.
2. Rebuild the recursive tree and regenerate `catalogs/external-skill-path-index.json`.
3. Recheck the root and relevant subdirectory licenses.
4. Compare skill inventories and inspect changed files.
5. Update the research snapshot date and note material changes.


## Third-batch motion repositories

| Source repository | Pinned commit | Root license recorded | Research file |
|---|---|---|---|
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760) | `aed9cfd3277740755f6bfc1155c7aa645403b760` | MIT | [19](19-gsap-skills.md) |
| [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/6f55706d1069e512430582ad86e4e57dc07afe1b) | `6f55706d1069e512430582ad86e4e57dc07afe1b` | No standalone root license found; underlying Remotion runtime uses proprietary Remotion License | [20](20-remotion-skills.md) |
| [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill/tree/d77a9fc8cb371cab1ba5420df5bfd232cd14c9bb) | `d77a9fc8cb371cab1ba5420df5bfd232cd14c9bb` | MIT | [21](21-lottiefiles-motion-design-skill.md) |
| [iart-ai/motion-skills](https://github.com/iart-ai/motion-skills/tree/e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f) | `e8ba1f4eb2bcca3d1639d7545b9cd2bcfe4a3c6f` | MIT | [22](22-iart-motion-skills.md) |
| [C-Jeril/framer-motion-skills](https://github.com/C-Jeril/framer-motion-skills/tree/837d7268fc4a3cf5b1f8904616ec97c7485e3eda) | `837d7268fc4a3cf5b1f8904616ec97c7485e3eda` | MIT | [23](23-framer-motion-skills.md) |
| [frankxai/awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills/tree/e7dc6e2e728c918ffcea5edb2d7c94e2a6f7785d) | `e7dc6e2e728c918ffcea5edb2d7c94e2a6f7785d` | CC0-1.0 | [24](24-awesome-motion-design-agent-skills.md) |

### Linked iArt packs inspected

| Repository | Pinned commit | License recorded | Skills |
|---|---|---|---:|
| [iart-ai/data-animation-skills](https://github.com/iart-ai/data-animation-skills/tree/6570c0c4fbc9daa8d7ac1f1163a890352344206b) | `6570c0c4fbc9daa8d7ac1f1163a890352344206b` | MIT | 3 |
| [iart-ai/motion-design-skills](https://github.com/iart-ai/motion-design-skills/tree/b85e50c4cef5ff17aa2187a10d49d2dae9226c74) | `b85e50c4cef5ff17aa2187a10d49d2dae9226c74` | MIT | 9 |
| [iart-ai/explainer-video-skills](https://github.com/iart-ai/explainer-video-skills/tree/3c13a1bc360c08503f24f9c9a99fda6d3d35de56) | `3c13a1bc360c08503f24f9c9a99fda6d3d35de56` | MIT | 5 |

The iArt hub's MIT license does not convert third-party provider terms or linked service licensing into MIT. Likewise, CC0 applies to the FrankX catalogue's own material, not the external projects it lists. Remotion's runtime is separately licensed; review official terms and pricing before bundling or commercial use.
