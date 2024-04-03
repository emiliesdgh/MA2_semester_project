import classes
from classes import Thymio

from tdmclient import ClientAsync, aw
# import matplotlib.pyplot as plt
import numpy as np


def see_costume(Thymio, node, motor_speed=50) :

    Thymio.setLEDTop(node, [32,0,0])

    Thymio.setSpeedLeft(motor_speed, node)
    Thymio.setSpeedRight(motor_speed, node)

def no_costume(Thymio, node, motor_speed=0) :

    Thymio.setSpeedLeft(motor_speed, node)
    Thymio.setSpeedRight(motor_speed, node)