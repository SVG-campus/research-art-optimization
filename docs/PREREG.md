# Preregistration — `research-art-optimization`
 
**Pillar:** `research-art-optimization`  
**Title:** Generative Parameter Complexity and Human Preference Causality (ECT-2026-008)
**Date:** 2026-06-14  
**ORCID Identifier:** `0009-0004-9601-5617`

## Charter (one paragraph)

Evaluate the causal dynamics between algorithmic complexity (parameter count, latent dimension size) of generative models and human preference ratings for output art. This study tests whether increased parameter complexity causally drives higher preference ratings or if the relationship is mediated by image readability, validated under OCCA's Kolmogorov MDL and PC graph engines.

## Primary question (Layer A)

- **Question:** Does generative parameter complexity (parameter_complexity) cause changes in human preference ratings (preference_score)?
- **Expected DAG:** `parameter_complexity -> preference_score`
- **Primary metric:** Discovered directed edges and mutual information.
- **Direction / threshold:** $\alpha = 0.05$ for PC algorithm. The discovered headway-to-delay edge must be directed from parameter complexity to preference score, and the correlation must exceed the phase-shuffled Spectral MC null ($p < 0.05$).

## Null / negative controls

- **Null model:** Phase-shuffled Spectral Monte Carlo (FFT surrogate paths).
- **Caps:** Capped at $N = 25$ runs for local smokes (`runs/smoke.yaml`); $N = 1000$ for full remote promotion validation with run ID `charter_art_complexity_preference_run_01`.

## Truth scope & ethics

- **Scope:** Observational generative design and preference metrics under the **ECT-2026** standard.
- **Data rights:** Fashion-MNIST styling subsets and human rating records.

## Promotion rules

Numbers enter `BEST_ANSWERS_OVERVIEW` (meta) only after `methodology_preamble.assert_run_card` passes in the same environment that produced the artifact. Follow the meta checklist [PROMOTION_CHECKLIST.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) before editing canonical summaries.
