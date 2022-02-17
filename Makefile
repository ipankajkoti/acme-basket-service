
dev-install:
	pipenv install --dev

pre-commit-hook: dev-install
	pipenv run pre-commit install

format:
# If you're running this for the first time, please make sure to run 'make dev-install' first
	pipenv run autopep8  --in-place --recursive app/

lint:
# If you're running this for the first time, please make sure to run 'make dev-install' first
	pipenv run flake8 app/

sort-imports:
# If you're running this for the first time, please make sure to run 'make dev-install' first
	pipenv run isort app/

commit-check: sort-imports format lint

run-precommit: dev-install
	pipenv run pre-commit run --all-files
