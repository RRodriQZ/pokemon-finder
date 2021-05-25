import logging


class Log:
    def __init__(self):
        self.LOG_FILENAME = 'log/LOG.log'
        logging.basicConfig(
            filename=self.LOG_FILENAME, level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S')

    @staticmethod
    def get_logger(route):
        return logging.getLogger(route)
