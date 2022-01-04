install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

test:
	poetry run pytest

.PHONY:	install lint build test