import logging.config

logging.config.fileConfig('4_logging/logging.conf')
logger = logging.getLogger()

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")