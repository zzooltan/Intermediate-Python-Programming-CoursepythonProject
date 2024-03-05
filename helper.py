import logging
import logging.config

logging.config.fileConfig('logging.conf')
# logging.config.dictConfig('dict_logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')



'''
logger = logging.getLogger(__name__)
# create  handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level an d format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')
'''

