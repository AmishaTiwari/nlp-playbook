# config.py

from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parents[1]

# Data paths
DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"

# Model paths
MODEL_DIR = BASE_DIR / "models"