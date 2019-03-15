# -*- coding:utf-8 -*-
import logging

class LOG:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.formatter = logging.Formatter('%(asctime)s -- %(levelname)s: %(message)s')

        self.consle = logging.StreamHandler()
        self.consle.setLevel(logging.INFO)
        self.consle.setFormatter(self.formatter)
        self.logger.addHandler(self.consle)

    def info(self, msg):
        self.logger.info(msg)
        self.logger.removeHandler(self.consle)


LOG().info('15451212')
