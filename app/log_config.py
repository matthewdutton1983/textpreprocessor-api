import logging

class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger()


    def get_logger(self):
        return self.logger
