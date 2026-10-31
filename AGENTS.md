# AGENTS.md — Build & Test Guide

## Overview

This repository contains a beginner's manual on AI-powered journaling, built as
a static HTML site from Markdown sources in `docs/`. Printable journal
templates live in `templates/`.

## Prerequisites

- Python 3.8+
- Python `markdown` module (`pip install markdown`)

## Build Commands

```bash
# Build the static site (converts docs/*.md -> site/*.html)
python3 build.py

# Clean generated files
make clean

# Full rebuild
make build
```

## Test / Verify

```bash
# Run all checks
make test

# What it checks:
#   1. build.py runs without errors
#   2. site/index.html and all pages are generated
#   3. HTML files are well-formed (basic tag balance check)
#   4. No secrets, API keys, or personal data in source files
#   5. LICENSE copyright line is correct
#   6. README credits Asdale Dynamics, LLC
#   7. Templates are present and printable
```

## Project Layout Rules

- Source: `docs/*.md`
- Output: `site/*.html`
- Templates: `templates/*.html` + `templates/printable.css`
- Never commit anything under `.kilo/` or `.opencode/`
- Do not add `.github/workflows/` files

## Commit Guidelines

- Plain commit messages
- No `Co-authored-by` trailers
- Never push or create remote repos
- Include only source files; `site/` output is committed for convenience
