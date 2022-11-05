"""
Simple config for custom logger
"""

logger_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s\t%(levelname)s\t%(filename)s\t%(message)s",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "logs/model.log",
            "formatter": "simple",
        },
    },
    "loggers": {
        "file_logger": {
            "level": "DEBUG",
            "handlers": ["file_handler"],
        },
    },
}
