import logging
import logging.handlers

LOG_FILENAME = 'log_file.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=2e+6, backupCount=5)

my_logger.addHandler(handler)

# Log some messages
for n in range(50):
    my_logger.debug(print(n))
