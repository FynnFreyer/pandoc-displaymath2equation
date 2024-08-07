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

.PHONY: pdfs
pdfs:
	mkdir -p "pdfs"
	pandoc --filter displaymath2equation tst/assets/labeled.md -o labeled.pdf
	pandoc --filter displaymath2equation tst/assets/refs_in_lists.md -o refs_in_lists.pdf
	pandoc --filter displaymath2equation tst/assets/eqs_in_lists.md -o eqs_in_lists.pdf
