install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml