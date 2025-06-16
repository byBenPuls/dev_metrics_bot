.PHONY: all

SHELL=/bin/bash -e

all: format

format:
	poetry run ruff format .
	poetry run ruff check --fix .

test:
	poetry run pytest . -p no:logging -p no:warnings

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf `find . -name .pytest_cache`
	rm -rf *.egg-info
	rm -f report.html
	rm -f .coverage
	rm -rf {build,dist,site,.cache,.mypy_cache,.ruff_cache,reports}
