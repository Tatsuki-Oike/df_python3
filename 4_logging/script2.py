import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# formatter設定
formatter = logging.Formatter('%(asctime)s - %(levelname)s:%(name)s - %(message)s')

# file_handler設定
file_handler = logging.FileHandler(
    f'4_logging/log/script2.log',
    mode='w')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# stream_handler設定
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
stream_handler.setFormatter(formatter)

# loggerにhandler設定
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# log
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")