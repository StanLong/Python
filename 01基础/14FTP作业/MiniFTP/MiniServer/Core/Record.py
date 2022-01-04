# -*- coding:utf-8 -*-


import logging

def record(filename):
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)

    screen=logging.StreamHandler()
    screen.setLevel(logging.INFO)

    file=logging.FileHandler(filename)
    file.setLevel(logging.INFO)

    formater=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    screen.setFormatter(formater)
    file.setFormatter(formater)

    logger.addHandler(screen)
    logger.addHandler(file)

    return logger