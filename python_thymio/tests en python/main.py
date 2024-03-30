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

    robot.setLEDTop(node, [32,32,32])

    # print(robot.button_center)
    # W6_T1_PS_24_03_30.see_costume(robot, node, obs_threshold=500)


    W6_T1_PS_24_03_30.ext_interaction(robot, node, motor_speed=100, obs_threshold=500)

    # if (button_center) :

    if (robot.button_center) :
        
        # robot.buttonForward = 0
        W6_T1_PS_24_03_30.setButtons(robot, 0)

        print(robot.button_center)
        W6_T1_PS_24_03_30.stop_program(robot, node, motor_speed=0)
        aw(node.unlock())
        break

    if (robot.button_forward and not(robot.buttonForward)) :

        W6_T1_PS_24_03_30.setButtons(robot, 0)

        robot.buttonForward = 1 

        print(robot.button_forward)

        print(robot.buttonCenter)
        print(robot.buttonForward)
        print(robot.buttonBackward)
        print(robot.buttonLeft)
        print(robot.buttonRight)
    
    elif (robot.button_forward and robot.buttonForward) :
        
        robot.buttonForward = 0
        robot.setLEDTop(node, [0,0,32])
        aw(client.sleep(2))

    
    if (robot.buttonForward) :

        W6_T1_PS_24_03_30.programFront(robot, node, client)

    if (robot.button_backward) :

        W6_T1_PS_24_03_30.setButtons(robot, 0)

        robot.buttonBackward = 1
    
    if (robot.buttonBackward) :

        W6_T1_PS_24_03_30.programBack(robot, node, client)

    # while (robot.buttonForward) :

    #     update_sensors_data(robot, node)


        
    #     W6_T1_PS_24_03_30.programFront(robot, node, client)


