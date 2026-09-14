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
elsarticle.cls                               Elsevier document class
elsarticle-num.bst                           Elsevier numeric bibliography style
```

The manuscript uses Elsevier’s `final,5p,times,twocolumn` layout and numeric citations.

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
