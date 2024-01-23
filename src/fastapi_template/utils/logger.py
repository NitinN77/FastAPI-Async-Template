import logging.config
from logging import getLogger

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": "[%(levelname)s] [%(asctime)s] %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "json"},
        "api": {
            "level": "INFO",
            "class": "logging.handlers.SysLogHandler",
            "formatter": "json",
        },
    },
    "loggers": {
        "api": {
            "handlers": ["console", "api"],
            "level": "INFO",
            "propagate": True,
        }
    },
}


logging.config.dictConfig(LOGGING)
logger = getLogger("api")
