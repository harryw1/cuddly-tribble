"""Module to ingest data from raw data files."""

# src/data/ingestion.py
from pathlib import Path
from typing import Union

import pandas as pd

from .validation import GHGDataValidator


class DataIngestion:
    """Class to ingest data from raw data files."""

    def __init__(self, raw_data_path: Union[str, Path]):
        """Initialize data ingestion with path to raw data."""
        self.raw_data_path = Path(raw_data_path)
        self.validator = GHGDataValidator()
        self._setup_logging()

    def read_file(self, filename: str) -> pd.DataFrame:
        """Read and validate a single data file."""
        df = self._read_raw_file(filename)

        # Validate the data
        issues = self.validator.validate_dataframe(df)

        # Log any validation issues
        for issue_type, problems in issues.items():
            for problem in problems:
                self.logger.warning(f"Validation {issue_type}: {problem}")

        # If there are critical issues, raise an exception
        if issues["missing_columns"] or issues["type_errors"]:
            raise ValueError("Critical validation errors found in data")

        return df
