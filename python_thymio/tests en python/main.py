from tdmclient import ClientAsync, aw
import matplotlib.pyplot as plt
import numpy as np
import time
import copy


#import the classes from the other modules
from classes import Thymio

import W4_T1_PS_24_03_07
import W6_T1_PS_24_03_30

client = ClientAsync()
node = aw(client.wait_for_node())
# aw(node.unlock())
aw(node.lock())
aw(node.wait_for_variables())

# aw(node.register_events([("StopnUnlock", 2)]))

# # The event data are obtained from variable event.args:
# program = """
# onevent StopnUnlock
#     motor.left.target = event.args[0]
#     motor.right.target = event.args[1]
# """
# aw(node.compile(program))
# aw(node.run())


#Classes initialization
robot = Thymio() 

def update_sensors_data(robot, node):

    # get button values
    # robot.getProxHorizontal(node)
    robot.getButtons(node)


while(1) :


    update_sensors_data(robot, node)

    # print(robot.button_center)
    # W6_T1_PS_24_03_30.see_costume(robot, node, obs_threshold=500)


    W6_T1_PS_24_03_30.ext_interaction(robot, node, motor_speed=100, obs_threshold=500)

    # if (button_center) :

    if (robot.button_center) :
        
        robot.buttonForward = 0
        print(robot.button_center)
        W6_T1_PS_24_03_30.stop_program(robot, node, motor_speed=0)
        aw(node.unlock())
        break

    if (robot.button_forward) :

        W6_T1_PS_24_03_30.setButtons(robot, 0)

        robot.buttonForward = 1

        print(robot.button_forward)
        print(robot.buttonForward)

        print(robot.buttonCenter)
        print(robot.buttonForward)
        print(robot.buttonBackward)
        print(robot.buttonLeft)
        print(robot.buttonRight)
    
    # if (robot.buttonForward) :

    #     W6_T1_PS_24_03_30.programFront(robot, node, client)

    while (robot.buttonForward) :

        update_sensors_data(robot, node)

        
        
        W6_T1_PS_24_03_30.programFront(robot, node, client)


