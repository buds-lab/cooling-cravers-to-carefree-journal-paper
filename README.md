# Cooling Cravers to the Carefree: Behavioral archetypes of thermal preference from city-scale longitudinal smartwatch micro-surveys

Public repository for the paper **“Cooling cravers to the carefree: Behavioral archetypes of
thermal preference from city-scale longitudinal smartwatch micro-surveys,”** prepared for
*Building and Environment*. The paper asks whether people can be grouped by their
thermal-preference **behavior** rather than by physiology alone, using a longitudinal
Cozie-Apple smartwatch micro-survey deployment collected in Singapore.

The analysis draws on **9,520 geolocated thermal-preference responses from 104 eligible
participants** (of the 106-participant deployment), each paired with a matched outdoor heat
index and an environmental-control context defined by how likely the occupied space is to be
air-conditioned. Three person-level behaviors — the tendency to prefer cooler conditions, the
tendency to prefer warmer conditions, and the sensitivity of cooling demand to outdoor heat —
are stabilized with empirical-Bayes shrinkage and clustered into four behavioral archetypes:

| Archetype | Mnemonic | Share | Behavior in one line |
|:----------|:---------|:------|:---------------------|
| Constant Cool-Seekers | **Craver** | 22.1% | Prefers cooler more often, even in air-conditioned space |
| Often Over-Cooled | **Captive** | 11.5% | Prefers warmer more often, especially where others control the A/C |
| Normatively Responsive | **Conventional** | 33.7% | Cooling demand rises with outdoor heat, as physiology predicts |
| Heat-Unbothered | **Carefree** | 32.7% | Reports "no change" most consistently, even outdoors |

This repository contains the manuscript source, the publication figures, and a self-contained
companion notebook that documents the analysis and regenerates every data figure. It contains
**no personal or private participant data**; the underlying privacy-protected datasets live in
the two source repositories listed below.

## How to cite

Please cite this paper as:

> Miller, Clayton. *Cooling cravers to the carefree: Behavioral archetypes of thermal
> preference from city-scale longitudinal smartwatch micro-surveys* (September 14, 2026).
> Available at [SSRN: 7457562](https://ssrn.com/abstract=7457562) or
> [https://doi.org/10.2139/ssrn.7457562](https://doi.org/10.2139/ssrn.7457562).

The foundational dataset should be cited as:

> Miller, C., Frei, M., & Chua, Y. X. (2026, August 1). *Cozie Singapore: Scalable
> crowdsourced smartwatch micro-surveys to capture longitudinal in-situ urban heat and noise
> perception*. Available at [SSRN: 7407399](https://ssrn.com/abstract=7407399) or
> [https://doi.org/10.2139/ssrn.7407399](https://doi.org/10.2139/ssrn.7407399).

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/). See [`LICENSE`](./LICENSE) for the full terms.

## Related publications and research lineage

This paper is one output of a multi-year smartwatch deployment built on the open-source
**Cozie-Apple** platform. The publications below trace that lineage — from the first pilot and
platform description, through a public machine-learning competition on the collected data, to
the just-in-time adaptive intervention (JITAI) results and the urban-space perception study.
**This paper reanalyzes the same Singapore deployment at the level of the person**, asking how
individuals differ in thermal-preference behavior, rather than characterizing spaces or
intervention outcomes.

| Year | Publication | Role in the lineage | DOI |
|:-----|:------------|:--------------------|:----|
| 2022 | **Towards smartwatch-driven just-in-time adaptive interventions (JITAI) for building occupants** — Miller, Chua, Frei, Quintana. *BuildSys '22*, pp. 336–339. | First methods and pilot-data showcase — introduces the smartwatch-driven JITAI concept. | [10.1145/3563357.3566135](https://doi.org/10.1145/3563357.3566135) |
| 2023 | **Cozie Apple: An iOS mobile and smartwatch application for environmental quality satisfaction and physiological data collection** — Tartarini, Frei, Schiavon, Chua, Miller. *J. Phys.: Conf. Ser.* **2600** 142003. | Describes the open-source data-collection platform. | [10.1088/1742-6596/2600/14/142003](https://doi.org/10.1088/1742-6596/2600/14/142003) |
| 2023 | **Introducing the Cool, Quiet City Competition: Predicting Smartwatch-Reported Heat and Noise with Digital Twin Metrics** — Miller, Quintana, Frei, Chua, Fu, Picchetti, Yap, Chong, Biljecki. *BuildSys '23*, pp. 298–299. | Launches a public (Kaggle) machine-learning competition built on this dataset. | [10.1145/3600100.3626269](https://doi.org/10.1145/3600100.3626269) |
| 2025 | **The Cool, Quiet City machine learning competition: Overview and results** — Miller, Ibrahim, Akbar, Picchetti, Chua, Frei, Biljecki, Chong, Quintana, Fu. *J. Phys.: Conf. Ser.* **3140** 112017. | Reports the design and results of that competition. | [10.1088/1742-6596/3140/11/112017](https://doi.org/10.1088/1742-6596/3140/11/112017) |
| 2025 | **Make yourself comfortable: Nudging urban heat and noise mitigation with smartwatch-based Just-in-time Adaptive Interventions (JITAI)** — Miller, Chua, Quintana, Lei, Biljecki, Frei. *Building and Environment* **284** 113388. | Reports the JITAI **intervention outcomes** of the deployment; also the source of this paper's onboarding measures. [Repository](https://github.com/buds-lab/make-yourself-comfortable-jitai-journal-paper). | [10.1016/j.buildenv.2025.113388](https://doi.org/10.1016/j.buildenv.2025.113388) |
| 2026 | **Cozie Singapore: Scalable crowdsourced smartwatch micro-surveys to capture longitudinal in-situ urban heat and noise perception** — Miller, Frei, Chua. *SSRN preprint*. | Characterizes the **reported experience across urban spaces**; the source of this paper's survey dataset. [Repository](https://github.com/buds-lab/cozie-singapore-journal). | [10.2139/ssrn.7407399](https://doi.org/10.2139/ssrn.7407399) |
| 2026 | **Cooling cravers to the carefree** *(this paper)* — Miller. *SSRN preprint*. | Reanalyzes the same deployment at the **person level**, deriving behavioral thermal-preference archetypes. | [10.2139/ssrn.7457562](https://doi.org/10.2139/ssrn.7457562) |

> **Relationship to the source studies.** *Cozie Singapore* and *Make yourself comfortable*
> analyze the deployment at the level of **spaces** and **interventions**, respectively. This
> paper analyzes it at the level of the **person**: it treats each participant's repeated
> thermal-preference votes as a behavioral signature and asks how those signatures cluster.
> All three studies share one participant cohort and can be joined on the pseudonymous
> `id_participant` field.

## Key findings

- **Thermal preference is substantially behavioral.** Four archetypes emerge from behavior
  alone; two (*Conventional*, *Craver*) behave as thermal physiology predicts, while two
  (*Captive*, *Carefree*) are largely decoupled from the outdoor heat around them.
- **Air conditioning relieves some but not all.** Prefer-cooler responses fall as spaces
  become more likely air-conditioned for most groups, but the *Craver* keeps seeking cooler
  even in cooled space.
- **Over-cooling is contextual.** The *Captive*'s "too cold" votes concentrate in
  likely-air-conditioned spaces controlled by others, not in the weather.
- **Genuine tolerance, not avoidance.** The *Carefree* stays comfortable even when hot and
  outdoors, so their contentment is not an artifact of low heat exposure.
- **Not a physiological or trait artifact.** The archetypes are undifferentiated on wearable
  physiology and on most stable onboarding traits; only personality **openness** shows a
  modest association (Kruskal–Wallis ε² = 0.137, *p* = 0.003), running highest in the
  *Carefree*.
- **Robust but soft-edged.** The four-way partition is seed-stable (adjusted Rand index ≈ 0.94)
  and reproduces under subsampling (≈ 0.77), with softer boundary membership as the hot/cool
  threshold moves (≈ 0.47–0.65) — a behavioral continuum best read as four descriptive types.

## Requirements

The companion notebook requires Python 3 with the analysis stack:

```bash
python -m pip install -r analysis/requirements.txt
```

Compiling the manuscript requires a LaTeX distribution with `latexmk`, `pdflatex`, and BibTeX
(the Elsevier `elsarticle` class and `elsarticle-num` style are vendored in this repository).
The Figure 1 citation-numbering tools additionally use [`python-pptx`](https://python-pptx.readthedocs.io/)
and [PyMuPDF](https://pymupdf.readthedocs.io/).

## Organization

```text
cravers-to-carefree.tex          Manuscript source (Elsevier elsarticle, final,5p,times,twocolumn)
cravers-to-carefree.bib          Numeric bibliography
cravers-to-carefree.pdf          Compiled manuscript
LICENSE                          Creative Commons BY-NC 4.0 license
elsarticle.cls                   Vendored Elsevier document class
elsarticle-num.bst               Vendored Elsevier numeric bibliography style
figures/                         Manuscript-ready PDF figures (see below)
figures/figure1builders/         Reproducible Figure 1 source and citation-numbering tools
analysis/                        Self-contained companion analysis notebook + regenerated outputs
```

The `figures/` directory holds the 13 data figures (tagged `00_*`, `01_*`, `02_*`), the Cozie
interface schematic (`cozie_diagram.pdf`, Figure 2), and the influence-family schematic
(`thermal_preference_elements_v15_190mm_1.pdf`, Figure 1).

## Data

This repository does not redistribute the underlying data. The analysis draws on **two public,
privacy-protected source repositories**, linked by the pseudonymous `id_participant` field:

| Source | Repository | Provides | Read with |
|:-------|:-----------|:---------|:----------|
| Survey dataset | [`cozie-singapore-journal`](https://github.com/buds-lab/cozie-singapore-journal) | `data/cozie_singapore_survey_dataset.parquet.gzip` (9,962 × 431): thermal preference, matched outdoor heat index, space type, and wearable-physiology aggregates | `pandas.read_parquet(..., engine='fastparquet')` |
| Onboarding survey | [`make-yourself-comfortable-jitai-journal-paper`](https://github.com/buds-lab/make-yourself-comfortable-jitai-journal-paper) | `1_data/1_onboarding_survey_all_participants.csv`: TIPI personality, SWLS life satisfaction, HSP sensory sensitivity, demographics, acclimatization | `pandas.read_csv(...)` |

Each source repository provides its own data dictionary and privacy notes; home coordinates in
the survey dataset are spatially generalized at the source. None of the figures in this paper
use coordinates. To run the companion notebook, clone the two source repositories **next to
this one** under a common parent directory:

```text
parent/
├── cooling-cravers-to-carefree-journal-paper/   (this repository)
├── cozie-singapore-journal/
└── make-yourself-comfortable-jitai-journal-paper/
```

The notebook locates them automatically regardless of the kernel's working directory.

## Companion analysis notebook

[`analysis/Thermal_Archetype_Companion_Analysis.ipynb`](./analysis/Thermal_Archetype_Companion_Analysis.ipynb)
is a self-contained, deterministic notebook that reproduces the full analysis end to end —
from the raw Cozie Singapore micro-surveys to every data figure — with step-by-step markdown
documentation so it can be read alongside the manuscript. It derives the four archetypes, runs
the mechanistic scrutiny and robustness checks, and regenerates the manuscript data figures in
the manuscript's Times New Roman style and archetype palette. Every number quoted in the paper
is produced by executed cells; a QC gate reproduces the headline cohort figures (9,520
responses, 106 participants, 34.1 °C median heat index, 104 qualifying, archetype sizes
23/12/35/34).

Regenerated figures are written to `analysis/figures/` and participant-level tables to
`analysis/outputs/`; the notebook **does not** overwrite the manuscript figures in `figures/`.

| Manuscript | Tag | Content |
|:-----------|:----|:--------|
| Figure 3  | `00_A2` | Survey composition and thermal preference by space type |
| Figure 4  | `00_C1` | Empirical-Bayes feature construction |
| Figure 5  | `01_S1` | Four-archetype overview schematic |
| Figure 6  | `00_D2` | Clustering diagnostics (PCA + silhouette) |
| Figure 7  | `00_D3` | Standardized archetype signatures |
| Figure 8  | `01_A3` | Prefer-cooler responses across control contexts |
| Figure 9  | `01_B1` | Over-cooling anatomy |
| Figure 10 | `01_C3` | Heat dose-response across control supergroups |
| Figure 11 | `01_C2` | Heat coupling by archetype |
| Figure 12 | `01_D1` | Outdoor exposure and provoked comfort |
| Figure 13 | `01_E1` | Independent survey behaviors |
| Figure 14 | `01_E3` | Wearable physiology |
| Figure 15 | `02_B1` | Onboarding measures |

Figures 1 (influence-family schematic) and 2 (Cozie interface) are illustrations with no data
dependency and are not produced by the notebook. Run it with:

```bash
pip install -r analysis/requirements.txt
jupyter lab analysis/Thermal_Archetype_Companion_Analysis.ipynb
```

## Manuscript build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error cravers-to-carefree.tex
```

The output is `cravers-to-carefree.pdf`. Temporary LaTeX build products are excluded through
`.gitignore`. Before distributing a new build, check the log for undefined citations or
references, LaTeX errors, and overfull boxes.

### Figure 1 numbered citations

Figure 1 embeds numbered citations that must match the order assigned by the manuscript
bibliography. Its editable source, extracted specification, placeholder exports, citation maps,
and builder scripts live in [`figures/figure1builders/`](./figures/figure1builders/):

- `citation_numbers.csv` — each figure citation token, BibTeX key, and assigned number;
- `figure_spec_numbered.json` — the figure specification with numbered brackets;
- `figure_numbered.pptx` — editable numbered PowerPoint output;
- `thermal_preference_elements_v15_190mm_1.pdf` — the clean 190 mm PDF used by the manuscript.

If citation order changes, rebuild the manuscript first so `cravers-to-carefree.bbl` reflects
the new order, update the `number` column in `citation_numbers.csv`, then regenerate:

```bash
cd figures/figure1builders
python renumber_citations.py --map citation_numbers.csv
python render_numbered_pdf.py --map citation_numbers.csv \
  --out ../thermal_preference_elements_v15_190mm_1.pdf
cd ../..
latexmk -pdf -interaction=nonstopmode -halt-on-error cravers-to-carefree.tex
```

Numbers within a bracket are sorted automatically; verify every key against the current `.bbl`
after bibliography changes.

## Contributions and acknowledgments

Clayton Miller (College of Integrative Studies, Singapore Management University) is the sole
author. The author acknowledges Mario Frei and Yun Xuan Chua for their contributions to the
conceptualization, methodology, deployment, validation, and data curation of the Cozie
Singapore study that provided the foundation for this analysis, and the student researchers who
assisted with data collection and processing: Charis Boey, Kristi Maisha, Annabel Sim, Aisyah
Iskandar, Lum Jun Chao, and S Aravindkugesh.

This research was supported by the Singapore Ministry of Education (MOE) Tier 1 Grants *The
Internet-of-Buildings (IoB) Platform — Testing of Visual Analytics for AI Technologies towards
a Well and Green Built Environment* (A-0008305-01-00) and *Ecological Momentary Assessment
(EMA) for Built Environment Research* (A0008301-01-00).

## Use of AI tools

AI assistance (Runcell AI) was used to help organize and format the LaTeX manuscript, arrange
figure and table placement, assemble the companion notebook from the analysis code, and
copy-edit author-written text. The tools were not used to generate or analyze the study data,
nor to create or alter any figure, its underlying values, or the reported results. The author
reviewed and verified all AI-assisted output and takes full responsibility for the research,
analysis, interpretation, and final content.
