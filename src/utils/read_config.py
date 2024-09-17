import logging

from config import get_cfg

logger = logging.getLogger('pong')

def reading_config(file_path=None):
    """
    Reads the config settings from config file and makes them accessible to the project using config.py module.
    Args:
        file_path (Path): The path of config file.
    
    Raises:
        FileNotFoundError: If the config file doesn't exist.
    """
    cfg = get_cfg()
    if file_path:
        cfg.merge_from_file(file_path)

    cfg.freeze()
    return cfg