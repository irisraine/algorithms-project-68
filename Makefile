install:
	poetry install

lint:
	poetry run flake8 router

tests:
	poetry run pytest
	
coverage:
	poetry run pytest --cov=router tests/ --cov-report xml	
