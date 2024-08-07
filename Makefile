.PHONY: requirements.txt
requirements.txt:
	python3 -m piptools compile --generate-hashes -o requirements.txt

.PHONY: requirements-dev.txt
requirements-dev.txt:
	python3 -m piptools compile --generate-hashes --extra dev -o requirements-dev.txt

logs:
	mkdir -p "logs"

.PHONY: test
test: logs
	date -Ih >> logs/pytest.log
	python3 -m pytest 2>&1 | tee  -a logs/pytest.log

.PHONY: type-check
type-check: logs
	date -Ih >> logs/mypy.log
	python3 -m mypy src/ 2>&1 | tee -a logs/mypy.log

.PHONY: lint
lint: logs
	date -Ih >> logs/mypy.log
	python3 -m pylint displaymath2equation/ tst/ 2>&1 | tee -a logs/pylint.log

PANDOC := pandoc -d tst/assets/defaults.yaml
MD     := tst/assets/markdown
OUT    := out
PANLOG := logs/pandoc

RENDER = $(PANDOC) $(MD)/$@.md -o $(OUT)/$@.pdf --log $(PANLOG)/$@.log

.PHONY: pdf_dirs labeled refs_in_lists eqs_in_lists
pdf_dirs:
	mkdir -p $(OUT)
	mkdir -p $(PANLOG)

.PHONY: labeled refs_in_lists eqs_in_lists
labeled:
	$(RENDER)
refs_in_lists:
	$(RENDER)
eqs_in_lists:
	$(RENDER)

.PHONY: pdfs
pdfs: logs pdf_dirs labeled refs_in_lists eqs_in_lists
