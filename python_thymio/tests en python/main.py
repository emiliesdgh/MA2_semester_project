from tdmclient import ClientAsync, aw
import matplotlib.pyplot as plt
import numpy as np
import time
import copy


#import the classes from the other modules
from classes import Thymio

import W4_T1_PS_03_24

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
    W4_T1_PS_03_24.see_costume(robot, node, obs_threshold=500)


    W4_T1_PS_03_24.ext_interaction(robot, node, motor_speed=100, obs_threshold=500)

    # if (button_center) :

    if (robot.button_center) :
        
        print(robot.button_center)
        W4_T1_PS_03_24.stop_program(robot, node, motor_speed=0)
        aw(node.unlock())
        break

    # if W4_T1_PS_03_24.stop_program(robot, node, motor_speed=0) :

    #     aw(node.unlock())
    #     break

    # if W4_T1_PS_03_24.see_costume(robot, node, 500):
    #     W4_T1_PS_03_24.obstacle_avoidance(robot,node,client,obs_threshold=500)
    # else:
    #     robot.setSpeedLeft(50, node)
    #     robot.setSpeedRight(50, node)
    #     aw(client.sleep(5))
        # break

# aw(node.unlock())

