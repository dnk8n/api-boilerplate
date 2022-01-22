lint:
	poetry run isort --check .
	poetry run black --check .
	poetry run flake8
	poetry run mypy -p src -p api -p tests

test:
	poetry run pytest --cov=src --cov=api --cov-report=term-missing --cov-report=html
