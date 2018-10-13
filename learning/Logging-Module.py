import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message') # WARNING:root:This is a warning message
logging.error('This is an error message') # ERROR:root:This is an error message
logging.critical('This is a critical message') # CRITICAL:root:This is a critical message

###################################################################################

# Formatting the Output

import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning') # WARNING:root:This is a Warning


import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
