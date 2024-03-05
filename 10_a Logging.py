# Logging
import logging
import traceback

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%y %H:%m:%S')
try:
     a = [1, 2, 3]
     val = a[4]
except IndexError as e:
    #logging.error(e, exc_info=True)
    logging.error('The error is %s', traceback.format_exc())



# logging.debug('This is a debug message')
# logging.info('This ia an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')



