# -*- coding: utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler
import sys
import os

LOG_NAME = "qss-design-system"


def get_default_log_path():
    config_file_path = __file__
    paths = config_file_path.split(os.sep)
    default_log_file_name = f"{LOG_NAME}.log"
    log_dir = os.path.dirname(config_file_path)
    if "src" in paths:
        index = paths.index("src")
        log_dir = os.sep.join(paths[:index])
    elif "main" in paths:
        index = paths.index("main")
        log_dir = os.sep.join(paths[:index])
    log_file = os.path.join(log_dir, "logs", default_log_file_name)
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    return log_file


class ShortPathFormatter(logging.Formatter):
    def format(self, record):
        if not hasattr(record, "_original_pathname"):
            # Get absolute path
            abs_path = os.path.abspath(record.pathname)
            # Convert to short form
            parts = list(filter(None, abs_path.split(os.sep)))
            short_path = os.sep.join(
                [
                    part[0] if i < len(parts) - 1 else part
                    for i, part in enumerate(parts)
                ]
            )
            record.pathname = short_path
        return super(ShortPathFormatter, self).format(record)


class LoggerConfig:
    _instance = None

    def __new__(
        cls,
        log_name=LOG_NAME,
        log_file_path=None,
        log_level=logging.INFO,
        encoding="utf-8",
    ):
        if cls._instance is None:
            cls._instance = super(LoggerConfig, cls).__new__(cls)
            if log_file_path is None:
                log_file_path = get_default_log_path()
            cls._instance._initialize(
                log_name=log_name,
                log_file_path=log_file_path,
                log_level=log_level,
                encoding=encoding,
            )
        return cls._instance

    def _initialize(self, log_name, log_file_path, log_level, encoding):
        if not isinstance(log_level, int) or log_level not in {
            logging.DEBUG,
            logging.INFO,
            logging.WARNING,
            logging.ERROR,
            logging.CRITICAL,
        }:
            raise ValueError(
                f"Invalid log level: {
                             log_level}. Must be one of logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, or logging.CRITICAL."
            )

        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)

        if self.logger.hasHandlers():
            return

        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s"
        # console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(ShortPathFormatter(log_format))

        # timed rotating file handler
        file_handler = TimedRotatingFileHandler(
            log_file_path,
            when="midnight",
            interval=1,
            backupCount=30,
            encoding=encoding,
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(ShortPathFormatter(log_format))
        file_handler.suffix = "%Y-%m-%d"

        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger


# log = LoggerConfig(log_name="test",log_file_path="d:\\tmp\\log.test.log",log_level=logging.DEBUG).get_logger()
log = LoggerConfig().get_logger()
