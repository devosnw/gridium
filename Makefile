# gridium makefile

.DEFAULT_GOAL := test
TEST_OPTS =

.PHONY: clean install test

clean:
	find . -path './venv' -prune -and -not -path './venv' \
	       -or -name '*.pyc' \
	       -or -name '*.pyo' \
	       -or -name '__pycache__' -type d \
	       -exec rm -rf {} \+

install:
	pip install --requirement requirements.txt

test:
	python -m unittest discover $(TEST_OPTS)
