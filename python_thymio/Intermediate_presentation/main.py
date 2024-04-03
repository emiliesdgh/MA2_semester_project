from tdmclient import ClientAsync, aw
import asyncio
import matplotlib.pyplot as plt
import numpy as np
import copy

import logging
import threading
import time

#import the classes from the other modules
from classes import Thymio

# import W6_T1_PS_24_03_30
# import W6_T1_PS_24_04_02
# import W6_T1_PS_24_04_03

import doubledCostume_24_03_30
import allPrograms_24_04_03
import modifiedCostume_24_04_03

client = ClientAsync()
node = aw(client.wait_for_node())
aw(node.lock())
aw(node.wait_for_variables())


#Classes initialization
robot = Thymio()

def update_sensors_data(robot, node):

    # get proximity & button values
    robot.getProxHorizontal(node)
    robot.getButtons(node)


while(1) :

    update_sensors_data(robot, node)
    robot.setLEDTop(node, [32,32,32])

########

    if (robot.button_center) :

        doubledCostume_24_03_30.setButtons(robot, 0)

        print(robot.button_center)
        allPrograms_24_04_03.stop_program(robot, node, motor_speed=0)
        aw(node.unlock())
        break

######## MODIFIED COSTUME

    # prox = list(node["prox.horizontal"]) + [0]

    # if(prox[2]) :
    #     update_sensors_data(robot, node)
    #     print(prox[2])

    #     modifiedCostume_24_04_03.see_costume(robot, node, motor_speed=50)
    # else :
    #     modifiedCostume_24_04_03.no_costume(robot, node, motor_speed=0)
    #     print(prox[2])

######## DOUBLED COSTUME

    doubledCostume_24_03_30.ext_interaction(robot, node, motor_speed=100, obs_threshold=500)

    if (robot.button_forward and not(robot.buttonForward)) :

        doubledCostume_24_03_30.setButtons(robot, 0)

        robot.buttonForward = 1

    elif (robot.button_forward and robot.buttonForward) :

        robot.buttonForward = 0
        robot.setLEDTop(node, [0,0,32])
        aw(client.sleep(2))

    if (robot.buttonForward) :

        doubledCostume_24_03_30.programFront(robot, node, client)

########

    if (robot.button_backward) :

        doubledCostume_24_03_30.setButtons(robot, 0)

        robot.buttonBackward = 1

    if (robot.buttonBackward) :

        doubledCostume_24_03_30.programBack(robot, node, client)
