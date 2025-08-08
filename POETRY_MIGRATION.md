# Poetry Migration Guide

This document describes the migration from flit to Poetry for the django-plottings project.

## What Changed

### 1. Build System
- **Before**: Used `flit_core` as the build backend
- **After**: Uses `poetry-core` as the build backend

### 2. Dependencies Management
- **Before**: Dependencies defined in `[project]` section
- **After**: Dependencies organized in groups:
  - `[tool.poetry.dependencies]` - Main dependencies
  - `[tool.poetry.group.dev.dependencies]` - Development dependencies
  - `[tool.poetry.group.docs.dependencies]` - Documentation dependencies

### 3. Version Management
- **Before**: Used `dynamic = ["version"]` for version management
- **After**: Explicit version in `pyproject.toml` (can be managed with `poetry version`)

### 4. Development Tools
Added comprehensive development tooling:
- **Black**: Code formatting
- **Flake8**: Linting
- **isort**: Import sorting
- **pytest-cov**: Test coverage
- **tox**: Multi-environment testing

## New Commands

### Installation
```bash
# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Install with development dependencies
poetry install --with dev
```

### Development
```bash
# Run tests
poetry run pytest

# Format code
poetry run black plottings/

# Check formatting
poetry run black --check plottings/

# Lint code
poetry run flake8 plottings/

# Sort imports
poetry run isort plottings/

# Build package
poetry build

# Activate virtual environment
poetry shell
```

### Using Makefile
```bash
# Show all available commands
make help

# Install dependencies
make install

# Run tests
make test

# Format and lint
make format
make lint

# Build package
make build

# Clean build artifacts
make clean
```

## Configuration Files

### pyproject.toml
- Main Poetry configuration
- Tool configurations for black, isort, pytest, flake8
- Dependency specifications

### poetry.toml
- Poetry-specific settings
- Virtual environment configuration
- Build settings

### .flake8
- Flake8 linting configuration
- Line length and ignore rules

### Makefile
- Convenient shortcuts for common tasks
- Standardized development workflow

## Benefits of Poetry Migration

1. **Better Dependency Management**: Poetry provides more robust dependency resolution
2. **Development Tools**: Integrated code formatting, linting, and testing tools
3. **Virtual Environment Management**: Automatic virtual environment creation and management
4. **Lock File**: Reproducible builds with `poetry.lock`
5. **Modern Python Packaging**: Uses the latest Python packaging standards
6. **Better Developer Experience**: More intuitive commands and better error messages

## Migration Checklist

- [x] Convert `pyproject.toml` to Poetry format
- [x] Update dependencies to compatible versions
- [x] Add development tools (black, flake8, isort, pytest-cov)
- [x] Configure tool settings
- [x] Create Makefile for convenience
- [x] Update documentation
- [x] Test all functionality
- [x] Ensure all tests pass
- [x] Verify build process works

## Notes

- The project now requires Python 3.9+ and Django 4.2+
- All existing functionality is preserved
- The API remains unchanged
- All tests continue to pass
- The package can still be installed via pip from PyPI
