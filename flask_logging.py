import logging.config
logging.config.fileConfig('logging_config.ini',
disable_existing_loggers=False)
logger = logging.getLogger(__name__)
