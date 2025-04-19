import logging

# Configuring the logging format
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level= logging.DEBUG,
    format = '%(asctime)s-%(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)