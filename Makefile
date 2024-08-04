.PHONY: requirements.txt
requirements.txt:
	python3 -m piptools compile --generate-hashes -o requirements.txt

.PHONY: requirements-dev.txt
requirements-dev.txt:
	python3 -m piptools compile --generate-hashes --extra dev -o requirements-dev.txt