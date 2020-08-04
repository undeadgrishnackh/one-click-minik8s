#!/usr/bin/env bash

ptw tests/ -- --cov-report term --cov=myproj tests/

echo "This is the okd way to run stuff in Python. Please use 'pipenv shell' and then 'pipenv run watch' instead."