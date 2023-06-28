# `Gendiff`
[![Actions Status](https://github.com/BogdanBarylo/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/BogdanBarylo/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/06860799108b157ebc77/maintainability)](https://codeclimate.com/github/BogdanBarylo/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/06860799108b157ebc77/test_coverage)](https://codeclimate.com/github/BogdanBarylo/python-project-50/test_coverage)
[![Python CI](https://github.com/BogdanBarylo/python-project-50/actions/workflows/github-actions-demo.yml/badge.svg)](https://github.com/BogdanBarylo/python-project-50/actions/workflows/github-actions-demo.yml)

## Welcome to the difference generator!

The difference generator is a program that determines the difference between two data structures. 
Features of the utility:
Supports different input formats: yaml, json
Report generation as plain, stylish and json

#незабыть добавить аксинему плоского сравнения
1. Comparison of json files and yaml files, if you don't choose a formatter, default one will be used.
[![asciicast](https://asciinema.org/a/xkvqF9bg9rfYnCbabdmlKYooa.svg)](https://asciinema.org/a/xkvqF9bg9rfYnCbabdmlKYooa)

2. Comparison of json files and yaml files, using a 'plain' formatter.
[![asciicast](https://asciinema.org/a/bsfcSJ3UriJL3lq77151M21or.svg)](https://asciinema.org/a/bsfcSJ3UriJL3lq77151M21or)

3. Comparison of json files and yaml files, using the 'json' formatter.
[![asciicast](https://asciinema.org/a/nsrEEdiHLQOW4TUXOAqFxYVVV.svg)](https://asciinema.org/a/nsrEEdiHLQOW4TUXOAqFxYVVV)

## Installation requirements

- Python: 3.10
- Poetry: 1.4.0
- `flake8`: 6.0.0
- `pytest`: 7.3.1

## Installation instructions

1. You need to download this repository to your computer.

2. Log in to the project root repository, enter in the terminal `make install`

3. The next command should be `make package-install`

4. To start searching for differences, you need to add to gendiff the path to your files, if you want to change the format of gendiff -f your chosen format and the path to the files. For example:

```bash
geniff file_1_path.json file_2_path.json
geniff -f plain file_1_path.json file_2_path.yaml 
geniff -f json file_1_path.json file_2_path.yaml
```