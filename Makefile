.PHONY: requirements.txt
requirements.txt:
	python3 -m piptools compile --generate-hashes -o requirements.txt

.PHONY: requirements-dev.txt
requirements-dev.txt:
	python3 -m piptools compile --generate-hashes --extra dev -o requirements-dev.txt

logs:
	mkdir "logs"

test: logs
	date -Ih >> logs/pytest.log
	python3 -m pytest 2>&1 | tee  -a logs/pytest.log

type-check: logs
	date -Ih >> logs/mypy.log
	python3 -m mypy src/ 2>&1 | tee -a logs/mypy.log

lint: logs
	date -Ih >> logs/mypy.log
	python3 -m pylint displaymath2equation/ tst/ 2>&1 | tee -a logs/pylint.log