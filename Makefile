.PHONY: help install test lint clean build docs

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	poetry install

install-dev: ## Install development dependencies
	poetry install --with dev

test: ## Run tests
	poetry run pytest

test-verbose: ## Run tests with verbose output
	poetry run pytest -v

test-coverage: ## Run tests with coverage
	poetry run pytest --cov=plottings --cov-report=html

lint: ## Run linting
	poetry run flake8 plottings/
	poetry run black --check plottings/

format: ## Format code
	poetry run black plottings/

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: ## Build package
	poetry build

publish: ## Publish to PyPI
	poetry publish

docs: ## Build documentation
	poetry run sphinx-build -W -b html docs docs/_build/html

docs-serve: ## Serve documentation locally
	poetry run sphinx-autobuild docs docs/_build/html

shell: ## Activate Poetry shell
	poetry shell

add-deps: ## Add a dependency (usage: make add-deps DEP=package_name)
	poetry add $(DEP)

add-dev-deps: ## Add a development dependency (usage: make add-dev-deps DEP=package_name)
	poetry add --group dev $(DEP)
