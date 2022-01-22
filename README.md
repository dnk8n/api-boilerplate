# Boilerplate repository for an example interview question exposed via an API


## Introduction
[FastAPI](https://fastapi.tiangolo.com) is used for the API.

## Dependencies
[poetry](https://python-poetry.org/) is used to manage dependencies, see
[CONTRIBUTING.md](/CONTRIBUTING.md).

## Getting started
To launch an API instance:
1. [Optional] Test before proceeding, run `tox`
1. Run `poetry install` to setup the configured development virtual environment
   - Note: If you use any other python distribution, like miniconda for
   example, you could run into trouble
   - To workaround, configure your shell's PATH variable so that
   `which python` consistently returns `/usr/bin/python` before performing
   this step
1. Use [./start_app.sh](/start_app.sh) to start the server
1. An instance of Swagger UI (which allows one to visualize and interact with
the API’s resources) is accessible at http://localhost:8000/docs
1. Endpoints are accessible at http://localhost:8000/api/<endpoint_name>
