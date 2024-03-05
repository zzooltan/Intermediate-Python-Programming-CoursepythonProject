import logging
import time
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# s, m, h, d, midnight, w
handler_t = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)

logger.addHandler(handler)
for _ in range(10000):
    logger.info('hello, world!')

logger.addHandler(handler_t)
for _ in range(6):
    logger.info('hello, world!')
    time.sleep(5)

