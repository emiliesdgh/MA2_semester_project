import classes
from classes import Thymio

from tdmclient import ClientAsync, aw
# import matplotlib.pyplot as plt
import numpy as np

def stop_program(Thymio, node, motor_speed=0) :

    Thymio.setLEDTop(node, [32,32,32])

    Thymio.setSpeedLeft(motor_speed, node)
    Thymio.setSpeedRight(motor_speed, node)