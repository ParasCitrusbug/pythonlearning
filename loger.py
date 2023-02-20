import logging

logging.basicConfig(filename='logs/app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")