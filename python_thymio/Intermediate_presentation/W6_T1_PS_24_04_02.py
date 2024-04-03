# test pour les threads

import classes
from classes import Thymio

from tdmclient import ClientAsync, aw

import numpy as np
import logging
import threading
import time

def thread_buttonCenter(name) :

    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
