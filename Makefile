install:
	poetry install

lint:
	poetry run flake8 router

tests:
	poetry run pytest
