import os
import yaml
from pathlib import Path
from typing import List
from box import ConfigBox, BoxError
from ensure import ensure_annotations
from textSummary.logging import logger  # Ensure logger is properly configured


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns its contents as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If YAML file is empty or cannot be loaded.
        FileNotFoundError: If the file does not exist.

    Returns:
        ConfigBox: Parsed contents of the YAML file wrapped in a ConfigBox.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxError as e:
        raise ValueError("YAML file is empty") from e
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {path_to_yaml}") from e
    except yaml.YAMLError as e:
        raise ValueError(f"Error loading YAML file: {e}") from e
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create directories if they do not exist.

    Args:
        path_to_directories (List[Path]): List of paths of directories to create.
        verbose (bool, optional): Whether to log directory creation messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

# Configuring the logger
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummaryLogger")
