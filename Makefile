install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml