# GATE Statistics (ST) PYQ Guide, 2019–2025

A topic-wise study guide for all **455 questions** from the seven GATE Statistics papers (2019–2025): 385 Statistics/Maths questions plus 70 General Aptitude questions.

Every question comes with:

- the **answer**
- the **concept** it tests
- a **step-by-step worked solution**
- a **shortcut / formula** box
- a **common trap** box, where there is one
- links to the **same pattern** and the **same question family** in other years

Each of the 15 topics also has a **formula & shortcut sheet** and a **repeated-patterns table** showing which kind of question appeared in which year.

## Topics

| Group | Topics |
|---|---|
| Mathematics | Calculus, Linear Algebra |
| Probability | Probability & Events, Random Variables, Joint Distributions, Limit Theorems, Markov Chains & Poisson Process |
| Inference | Point Estimation, Interval Estimation, Testing of Hypotheses, Nonparametric Inference |
| Applied | Regression, Multivariate Analysis, Design of Experiments |
| Aptitude | General Aptitude |

## Repository layout

```
solutions/   Worked solutions, one file per paper (2019.txt … 2025.txt, ga.txt)
formulas/    Formula & shortcut sheet per topic (Markdown + LaTeX)
scripts/     Pipeline: PDF → cleaned question images → site data, plus checks
site/        The static web app (index.html + data/*.json)
```

### Solution file format

```
=== 2019 17
topic: EST
pattern: Basu's theorem: complete sufficient vs ancillary
type: MCQ
ans: A
concept: …
solution:
…
shortcut: …
trap: …
```

`topic` is one of the codes in `scripts/build.py`. Questions with the same `pattern` text are linked to each other. `scripts/families.py` groups patterns into broader question families.

## Running it

The question images are **not** in this repo, because they come from a copyrighted coaching PDF. Without them the site still works: it shows every solution, formula sheet and pattern table, with a placeholder where each question image would be.

```bash
pip install -r requirements.txt     # plus poppler-utils for pdftotext / pdftoppm
make site                           # build site/data from solutions/ and formulas/
make serve                          # open http://localhost:8000
```

To generate the question images from your own copy of the PDF:

```bash
mkdir -p source && cp /path/to/GATE_2019-2025_PYQ.pdf source/pyq.pdf
make images site
```

The pipeline:

1. `strip_watermark.py` removes the watermark image objects from the PDF.
2. `find_questions.py` locates each question-number marker using `pdftotext -bbox`.
3. `crop_questions.py` renders the pages and crops each question. It also pulls tall displays such as matrices above the marker back into the right question, and stitches questions that cross a page break.
4. `trim_tail.py` and `trim_slivers.py` clean up stray edges.
5. `build.py` packs everything into per-topic JSON for the site.

## Verification

- `make check` compares every answer against the PDF's key and runs Monte Carlo checks on the harder numerical answers.
- Where my answer differs from the PDF's key, the solution explains why. The differences are:
  - **Errors in the PDF's key:** 2021 Q40, Q43, Q44, Q47; 2022 Q46; 2023 Q56; 2024 Q54.
  - **Arithmetic or rounding slips in the PDF:** 2019 Q32, 2021 Q64, 2024 Q65.

## Disclaimer

The GATE questions belong to the IITs/IISc that set the exam. The solutions, explanations and formula sheets here are original. This is a personal study aid; check anything critical against official answer keys.
