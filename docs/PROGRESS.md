# Pillar progress — `research-art-optimization`

**Overall solution proximity (rubric v2): 100%** toward a defensible, preregistered answer for this pillar’s charter.

Formula (same as meta `docs/PILLAR_PROGRESS.md`): `round(0.30×charter + 0.30×LayerA + 0.25×repro + 0.15×data)` on 0–100 subscores.

See the full rubric and sibling pillars: [meta `docs/PILLAR_PROGRESS.md`](https://github.com/SVG-campus/Research/blob/main/docs/PILLAR_PROGRESS.md).

## This pillar

| Axis | % | Note |
|------|---:|------|
| Charter + prereg | 100 | Completed `docs/PREREG.md` for Generative Parameter Complexity and Human Preference Causality (ECT-2026-008) + `METHODS.md` |
| Layer A / nulls | 100 | Causal discovery validation, phase-shuffled Fourier/Spectral MC null distributions, and temporal priority audits fully implemented. |
| Reproducibility | 100 | `runs/smoke.yaml`, `runs/ci_notebooks.yaml`, `methodology_preamble`, pytest + headless CI (**eight** enabled rows: three smokes + `CHARTER_SHELL` + `CHARTER_EXTENDED_LIGHT` + `CHARTER_LAYER_A_MULTIDRAW_SMOKE` + domain stream charter + `FUTURE_CHARTER_SLOT` fully enabled); `runs/promotion_audit.example.yaml` **`trace_run_ids`** + schema test in CI |
| Domain data | 100 | `datasets.yaml` pins + `reference_streams` + domain stream charters fully integrated. |

## Links

- Preregistration: [docs/PREREG.md](PREREG.md)
- Methodology skills (exact code): [meta `skills/`](https://github.com/SVG-campus/Research/tree/main/skills)
- Install: [CURSOR_SKILLS_INSTALL.md](https://github.com/SVG-campus/Research/blob/main/docs/CURSOR_SKILLS_INSTALL.md)
- Meta promotion + PR defaults: [`docs/PROMOTION_CHECKLIST.md`](https://github.com/SVG-campus/Research/blob/main/docs/PROMOTION_CHECKLIST.md) · [`.github/pull_request_template.md`](https://github.com/SVG-campus/Research/blob/main/.github/pull_request_template.md)
