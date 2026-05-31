.PHONY: help install dev test lint format clean run db-init db-migrate

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make dev          - Install development dependencies"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linting checks"
	@echo "  make format       - Format code"
	@echo "  make clean        - Clean up temporary files"
	@echo "  make run          - Run the bot"
	@echo "  make db-init      - Initialize database"

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements.txt

test:
	pytest tests/ -v --cov=src

lint:
	flake8 src tests
	mypy src

format:
	black src tests
	isort src tests

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
	rm -rf build dist *.egg-info .pytest_cache .coverage htmlcov

run:
	python -m src.bot.main

db-init:
	python -m src.database.init_db
