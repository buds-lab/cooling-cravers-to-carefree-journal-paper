# Same Heat, Different Preference

Manuscript source for a planned *Building and Environment* article that analyzes behavioural thermal-comfort archetypes in the Cozie Singapore smartwatch micro-survey cohort.

## Working Scope

The manuscript is organized around the analysis in
`../orenth-usk-data-INTERNAL/6_analysis_humans/`:

- derivation of four participant-level behavioural thermal archetypes from cooling preference, over-cooling preference, and heat sensitivity;
- mechanistic scrutiny of thermal-preference dose responses to outdoor heat and indoor control context; and
- robustness checks that position the archetypes as a descriptive behavioural typology rather than a hard classifier.

The analysis uses the public, privacy-protected survey dataset maintained in the companion `cozie-singapore-journal` repository. Regenerate publication figures from the two source notebooks before adding them under `figures/` and uncommenting their LaTeX figure environments.

## Repository Layout

```text
cravers-to-carefree.tex     # Main Elsevier / Building and Environment manuscript
cravers-to-carefree.bib     # Working numeric bibliography (seeded from Cozie Singapore)
figures/                               # Regenerated manuscript-ready figure assets
tables/                                # LaTeX tables included by the manuscript
elsarticle.cls                         # Elsevier document class supplied with the template
elsarticle-num.bst                     # Numeric Elsevier bibliography style
```

## Build

```bash
latexmk -pdf cravers-to-carefree.tex
```

The main file uses Elsevier's `final,5p,times,twocolumn` production-style layout with numeric citations. Placeholder text is included only to preview the layout and must be replaced before submission.

## Before Submission

1. Replace all `TODO(author)` fields, including title, author/affiliation metadata, abstract, and acknowledgments.
2. Add and verify data-derived figures and tables from the analysis notebooks.
3. Verify every numerical claim against executed notebook output.
4. Complete the competing-interests, CRediT, funding, data-availability, and AI-use statements according to the final submission requirements.
5. Build with `latexmk` and resolve all warnings and undefined references.
