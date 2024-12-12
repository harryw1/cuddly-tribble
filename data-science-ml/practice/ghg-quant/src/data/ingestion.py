# src/data/ingestion.py
"""Module to ingest data from raw data files."""

import logging
from pathlib import Path
from typing import List, Union

import pandas as pd


class DataIngestion:
    """Class to ingest data from raw data files."""

    def __init__(self, raw_data_path: Union[str, Path]):
        """Initialize data ingestion with path to raw data.

        Args:
            raw_data_path: Path to directory containing raw data files

        """
        self.raw_data_path = Path(raw_data_path)
        self._setup_logging()

    def _setup_logging(self):
        """Configure logging for the ingestion process."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)

    def read_file(self, filename: str) -> pd.DataFrame:
        """Read a single data file.

        Args:
            filename: Name of file to read

        Returns:
            DataFrame containing file contents

        """
        file_path = self.raw_data_path / filename
        self.logger.info(f"Reading file: {file_path}")

        if file_path.suffix == ".csv":
            return pd.read_csv(file_path)
        elif file_path.suffix in [".xlsx", ".xls"]:
            return pd.read_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")

    def list_available_files(self) -> List[str]:
        """List all available data files in the raw data directory."""
        return [
            f.name
            for f in self.raw_data_path.glob("*")
            if f.suffix in [".csv", ".xlsx", ".xls"]
        ]
