# Contributing

___
## Installing new packages

Update `pyproject.toml` with the package required, on a new line under appropriate section, e.g under [tool.poetry.dev-dependencies]: `requests = "^2.27.1"`

Run `$ poetry lock --no-update` (ommit --no-update in the case you are ready to test against packages of latest point release)

Run tests using tox, and commit if tests run without regression. Then to install these new packages in the virtual environment, run `$ poetry install`

To see possible latest package versions run, `poetry show -l -o`

___
## Running tests and using tox

[Tox](https://tox.wiki/en/stable/) is used to automate and standardize testing of Python applications: `tox`

The following targets exist, for linting (`lint`) and testing
(`test`). You can run a specific target: `tox -e <target>`

___
## Code formatting

In this repository, a linting step runs checks for code formatting compliance,
using the following packages, in order:

- [isort](https://isort.readthedocs.io/en/stable/) sorts and seperates library
imports alphabetically and by type. To automatically fix the conflicts, run:
`$ poetry run isort .`

- [black](https://black.readthedocs.io/en/stable/) formats code. To
automatically fix the conflicts, run: `$ poetry run black .`

- [flake8](https://flake8.readthedocs.io/en/stable/) helps to enforce the
style guide. To check for conflicts, run: `$ poetry run flake8` (best avoided,
as this command is included in tox[testenv:lint])

- [mypy](https://mypy.readthedocs.io/en/stable/) checks static typing. To
check for conflicts, run: `$ poetry run mypy -p [<package-path> ...]`
(best avoided, as this command is included in tox[testenv:lint])

___
## Test coverage

[pytest](https://docs.pytest.org/en/stable/), with the addition of
[pytest-cov](https://pytest-cov.readthedocs.io/en/stable/) for test coverage,
is used in the testing step. To run tests, run: `$ poetry run pytest` (best
avoided, as a more detailed command is included in tox[testenv:test])

Inspect the console output of test results and html reports at
`htmlcov/index.html` when run via `tox`
___
