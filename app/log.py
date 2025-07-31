import os
import logging


LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR,
}

gunicorn_logger = logging.getLogger("gunicorn.error")
logger = logging.getLogger("uvicorn.app")
logger.handlers = gunicorn_logger.handlers
logger.setLevel(LOG_LEVELS[LOG_LEVEL.lower()])

def debug(*args, **kwargs):
    logger.debug(*args, **kwargs)

def info(*args, **kwargs):
    logger.info(*args, **kwargs)

def warn(*args, **kwargs):
    logger.warn(*args, **kwargs)

def error(*args, **kwargs):
    logger.error(*args, **kwargs)

def exception(*args, **kwargs):
    logger.exception(*args, **kwargs)
