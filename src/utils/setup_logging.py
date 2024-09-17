import sys
import logging


LOG_LEVEL = logging.DEBUG
logger = logging.getLogger("pong")

def setup_logging(logfile=None):
    """
    Sets up logging to stout and to the given file
    Args:
        logfile (Path): The path of logging file
        
    Raises:
        InvalidPath: An error if the given file path is invalid.
    """
    global logger
    logger.propagate = False
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', "%H:%M:%S")
    logger.setLevel(LOG_LEVEL)
    streamhandler = logging.StreamHandler(sys.stdout)
    streamhandler.setLevel(LOG_LEVEL)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    if logfile:
        try:
            filehandler = logging.FileHandler(logfile)
            filehandler.setLevel(LOG_LEVEL)
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
        except FileNotFoundError as e:
            logger.warning(e)