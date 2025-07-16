# Aviation

Learn the fundamentals of transform-based low-order modelling and analysis

## Developer Guide

### Dependencies

This repository uses [uv](https://docs.astral.sh/uv/) for comprehensive project management.
Dependency bounds are defined in [`pyproject.toml`](pyproject.toml) and the locked environment is specified in [`uv.lock`](uv.lock).
To create the virtual environment from lockfile, make sure you have uv installed and run:

```
uv sync
```

### Model/Analysis

This repository contains a single analysis script, [`aviation.py`](aviation.py), which implements the simple model for global aviation.
It outputs the required global fleet.
To execute the analysis script, run:

```
uv run python aviation.py
```

### Documentation

This repository uses [MkDocs](https://www.mkdocs.org/) to generate a static documentation site for users.
The source files for the site can be found in the [`docs/`](docs) directory and site configuration in [`mkdocs.yml`](mkdocs.yml).
To serve the site locally, run:

```
uv run mkdocs serve
```
