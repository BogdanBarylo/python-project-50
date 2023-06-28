install:
	poetry install

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl 

build:
	poetry build

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml