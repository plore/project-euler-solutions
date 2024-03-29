.PHONY: format
format:
	black .
	isort .

.PHONY: lint
lint:
	black --check .
	isort --check .
	flake8 .
	pylint *.py
	mypy .
