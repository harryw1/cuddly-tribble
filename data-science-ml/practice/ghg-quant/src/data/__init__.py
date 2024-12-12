# src/data/__init__.py
"""Data processing and cleaning functionality."""

from .ingestion import DataIngestion
from .preprocess import clean_data, validate_data

__all__ = ["DataIngestion"]
