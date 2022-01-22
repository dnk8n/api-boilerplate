#!/usr/bin/env bash

set -eu

poetry run uvicorn --reload api.main:app
