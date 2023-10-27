"""Configuration loader for DEEPaaS API."""
import os
import logging
from importlib import metadata
from pathlib import Path


# Get AI model metadata
API_NAME = "deepaas_full"
MODEL_METADATA = metadata.metadata(API_NAME)  # .json

# Fix metadata for emails from pyproject parsing
_EMAILS = MODEL_METADATA["Author-email"].split(", ")
_EMAILS = map(lambda s: s[:-1].split(" <"), _EMAILS)
MODEL_METADATA["Author-emails"] = dict(_EMAILS)

# Fix metadata for authors from pyproject parsing
_AUTHORS = MODEL_METADATA.get("Author", "").split(", ")
_AUTHORS = [] if _AUTHORS == [""] else _AUTHORS
_AUTHORS += MODEL_METADATA["Author-emails"].keys()
MODEL_METADATA["Authors"] = sorted(_AUTHORS)

# DEEPaaS can load more than one installed models. Therefore, in order to
# avoid conflicts, each default PATH environment variables should lead to
# a different folder. The current practice is to use the path from where the
# model source is located.
BASE_PATH = Path(__file__).resolve(strict=True).parents[1]

# Path definition for data folder
DATA_PATH = os.getenv("DATA_PATH", default=BASE_PATH / "data")
DATA_PATH = Path(DATA_PATH)
# Path definition for the pre-trained models
MODELS_PATH = os.getenv("MODELS_PATH", default=BASE_PATH / "models")
MODELS_PATH = Path(MODELS_PATH)

# logging level across API modules can be setup via API_LOG_LEVEL,
# options: DEBUG, INFO(default), WARNING, ERROR, CRITICAL
ENV_LOG_LEVEL = os.getenv("API_LOG_LEVEL", default="INFO")
LOG_LEVEL = getattr(logging, ENV_LOG_LEVEL.upper())
