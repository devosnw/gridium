# gridium makefile

TEST_OPTS =

.PHONY: clean test

clean:
	find . -path './venv' -prune -and -not -path './venv' \
	       -or -name '*.pyc' \
	       -or -name '*.pyo' \
	       -or -name '__pycache__' -type d \
	       -exec rm -rf {} \+

test:
	python -m unittest discover $(TEST_OPTS)
