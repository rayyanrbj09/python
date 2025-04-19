from logger import logging

def test_logging(a, b):
    logging.debug('Addition is taking place')
    return a + b
    
logging.info('Starting the test')
test_logging(1, 2)