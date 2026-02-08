.PHONY: help install validate

help:
	@echo "Targets:"
	@echo "  make install   - install dev dependencies"
	@echo "  make validate  - validate sample log against schema"

install:
	python -m pip install --upgrade pip
	python -m pip install jsonschema

validate:
	python scripts/validate.py
