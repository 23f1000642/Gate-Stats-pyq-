# Requires poppler-utils (pdftotext, pdftoppm) and your own copy of the PDF at source/pyq.pdf
PY ?= python3

.PHONY: all images site check serve clean

all: images site

images:
	$(PY) scripts/strip_watermark.py
	$(PY) scripts/find_questions.py
	$(PY) scripts/crop_questions.py
	$(PY) scripts/trim_tail.py 2021_22 2023_50
	$(PY) scripts/trim_slivers.py

site:
	$(PY) scripts/build.py

check:
	$(PY) scripts/check_answer_key.py
	$(PY) scripts/verify_simulation.py

serve:
	cd site && $(PY) -m http.server 8000

clean:
	rm -rf build
