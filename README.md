# Example REST Project

## Prerequisites

This project is managed with [Poetry](https://python-poetry.org/).

To install poetry on your system, [follow the instructions
here](https://python-poetry.org/docs/master/#installation).

## Quickstart

Once you have poetry installed, use it to create a virtual environment in your
project directory and install dependencies:

```sh
$ cd example-rest
$ poetry install
```

Then install the `pre-commit` hooks into your local git repository. These will
be used to help ensure consistent formatting using
[black](https://pypi.org/project/black/) and
[flake8](https://flake8.pycqa.org/en/latest/).

```sh
$ poetry run pre-commit install
$ poetry run pre-commit install --hook-type commit-msg
```

Then, execute the project with:

```sh
$ poetry run python -m example_rest
```
