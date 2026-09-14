# Cooling Cravers to the Carefree

Manuscript source and publication figures for **“Cooling cravers to the carefree: Behavioral archetypes of thermal preference from city-scale longitudinal smartwatch micro-surveys,”** prepared for *Building and Environment*.

The paper uses longitudinal Cozie smartwatch micro-surveys collected in Singapore to identify four person-level thermal-preference archetypes: the Craver, Captive, Conventional, and Carefree. The analytical sample contains 9,520 geolocated responses from 104 eligible participants. The archetypes are constructed from empirical-Bayes estimates of prefer-cooler rate, prefer-warmer rate, and sensitivity of cooling demand to outdoor heat, then examined across environmental-control contexts, wearable physiology, onboarding measures, and clustering perturbations.

## Repository contents

```text
cravers-to-carefree.tex                      Main Elsevier manuscript
cravers-to-carefree.bib                      Numeric bibliography
cravers-to-carefree.pdf                      Compiled manuscript
figures/                                     Manuscript-ready PDF figures
figures/figure1builders/                     Reproducible Figure 1 source and citation tools
analysis/                                    Self-contained companion analysis notebook
elsarticle.cls                               Elsevier document class
elsarticle-num.bst                           Elsevier numeric bibliography style
```

The manuscript uses Elsevier’s `final,5p,times,twocolumn` layout and numeric citations.

## Companion analysis notebook

`analysis/Thermal_Archetype_Companion_Analysis.ipynb` is a self-contained, deterministic notebook that reproduces the full analysis behind the paper — from the raw Cozie Singapore micro-surveys to every data figure — with documentation for each step so it can be read alongside the manuscript. It derives the four behavioral thermal-preference archetypes (Craver, Captive, Conventional, Carefree), runs the mechanistic scrutiny and robustness checks, and regenerates the manuscript data figures matching their Times New Roman style and archetype palette.

Every number quoted in the paper is produced by executed cells. The notebook loads data directly from the two public source repositories and writes regenerated figures and tables into `analysis/figures/` and `analysis/outputs/`; it does not overwrite the manuscript figures in `figures/`.

Manuscript data figures reproduced by the notebook:

| Manuscript | Tag | Content |
|-----------|-----|---------|
| Figure 3 | `00_A2` | Survey composition and thermal preference by space type |
| Figure 4 | `00_C1` | Empirical-Bayes feature construction |
| Figure 5 | `01_S1` | Four-archetype overview schematic |
| Figure 6 | `00_D2` | Clustering diagnostics (PCA + silhouette) |
| Figure 7 | `00_D3` | Standardized archetype signatures |
| Figure 8 | `01_A3` | Prefer-cooler responses across control contexts |
| Figure 9 | `01_B1` | Over-cooling anatomy |
| Figure 10 | `01_C3` | Heat dose-response across control supergroups |
| Figure 11 | `01_C2` | Heat coupling by archetype |
| Figure 12 | `01_D1` | Outdoor exposure and provoked comfort |
| Figure 13 | `01_E1` | Independent survey behaviors |
| Figure 14 | `01_E3` | Wearable physiology |
| Figure 15 | `02_B1` | Onboarding measures |

Figures 1 and 2 are illustrations with no data dependency and are not produced by the notebook.

### Running the companion notebook

The notebook requires the two source data repositories (listed under *Foundational data* below) to sit **next to this repository** under a common parent directory; it locates them automatically regardless of the kernel's working directory. Install the dependencies and run all cells:

```bash
pip install -r analysis/requirements.txt
jupyter lab analysis/Thermal_Archetype_Companion_Analysis.ipynb
```

## Build the manuscript

A TeX installation with `latexmk`, `pdflatex`, and BibTeX is required.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error cravers-to-carefree.tex
```

The output is written to `cravers-to-carefree.pdf`. Before distributing a new build, check the log for undefined citations or references, LaTeX errors, and overfull boxes.

## Figure 1 numbered citations

Figure 1 contains numbered citations that must match the order assigned by the manuscript bibliography. Its editable source, extracted JSON specification, placeholder exports, citation maps, and builder scripts are stored in `figures/figure1builders/`.

The current numbered artifacts are:

- `citation_numbers.csv`: each figure citation token, BibTeX key, and assigned manuscript number;
- `figure_spec_numbered.json`: the figure specification with numbered brackets;
- `figure_numbered.pptx`: editable numbered PowerPoint output; and
- `figures/thermal_preference_elements_v15_190mm_1.pdf`: the clean 190 mm PDF used by the manuscript.

If citation order changes, first rebuild the manuscript so `cravers-to-carefree.bbl` contains the new bibliography order. Update the `number` column in `citation_numbers.csv`, then regenerate the numbered source and final PDF from `figures/figure1builders/`:

```bash
cd figures/figure1builders
python renumber_citations.py --map citation_numbers.csv
python render_numbered_pdf.py \
  --map citation_numbers.csv \
  --out ../thermal_preference_elements_v15_190mm_1.pdf
cd ../..
latexmk -pdf -interaction=nonstopmode -halt-on-error cravers-to-carefree.tex
```

Numbers within a bracket are sorted automatically. Every key in `citation_numbers.csv` should be verified against the current `.bbl` after bibliography changes.

The builders require Python 3 with [`python-pptx`](https://python-pptx.readthedocs.io/) and [PyMuPDF](https://pymupdf.readthedocs.io/):

```bash
python -m pip install python-pptx pymupdf
```

## Foundational data and related repositories

The analysis draws on two public, privacy-protected sources linked by pseudonymous participant identifiers:

- [Cozie Singapore](https://github.com/buds-lab/cozie-singapore-journal), containing the smartwatch micro-surveys, matched outdoor weather, and wearable-health aggregates used to construct the archetypes; and
- [Make Yourself Comfortable](https://github.com/buds-lab/make-yourself-comfortable-jitai-journal-paper), containing the onboarding measures used for participant-level scrutiny.

The foundational dataset is described in:

> Miller, C., Frei, M., and Chua, Y. X. (2026). *Cozie Singapore: Scalable crowdsourced smartwatch micro-surveys to capture longitudinal in-situ urban heat and noise perception*. Social Science Research Network. https://doi.org/10.2139/ssrn.7407399

No private participant information is included in this repository.

## Reproducibility checks

Before committing a manuscript update:

1. Verify every reported number against executed analysis output.
2. Rebuild the manuscript after changing the source, bibliography, or any figure.
3. Confirm that citations and cross-references are defined.
4. Inspect the compiled PDF for figure placement, clipping, and excessive whitespace.
5. If bibliography order changes, regenerate and inspect Figure 1 before rebuilding the manuscript.
