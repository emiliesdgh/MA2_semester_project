# from tdmclient import ClientAsync, aw
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

import W4_T1_PS_24_03_07
import W6_T1_PS_24_03_30
import W6_T1_PS_24_04_02
import W6_T1_PS_24_04_03

client = ClientAsync()
node = aw(client.wait_for_node())
# aw(node.unlock())
aw(node.lock())
aw(node.wait_for_variables())

# aw(node.register_events([("StopnUnlock", )]))

# program = """
# onevent StopnUnlock
#     W6_T1_PS_24_03_30.setButtons(robot, 0)

#     print(robot.button_center)
#     W6_T1_PS_24_03_30.stop_program(robot, node, motor_speed=0)
#     aw(node.unlock())
# """

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
    robot.getProxHorizontal(node)
    robot.getButtons(node)

# def thread_buttonCenter(name) :

#     logging.info("Thread %s: starting", name)
#     time.sleep(2)

#     # aw(node.send_events({"StopnUnlock": }))

#     logging.info("Thread %s: finishing", name)

# def thread_buttonCenter(event) :

#     if (robot.button_center) :
#         # robot.buttonForward = 0
#         W6_T1_PS_24_03_30.setButtons(robot, 0)

#         print(robot.button_center)
#         W6_T1_PS_24_03_30.stop_program(robot, node, motor_speed=0)
#         aw(node.unlock())
        # break


# def main() :

    # INTHREAD = threading.Event()

    # threadToStop = threading.Thread(target=thread_buttonCenter, args=(INTHREAD,))

    # threadToStop.start()

while(1) :

    # aw(client.sleep(0.1))
    update_sensors_data(robot, node)

    robot.setLEDTop(node, [32,32,32])

    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")

    # logging.info("Main    : before creating thread")
    # x = threading.Thread(target=thread_buttonCenter, args=(1,))
    # logging.info("Main    : before running thread")
    # x.start()
    # logging.info("Main    : wait for the thread to finish")
    # # x.join()
    # logging.info("Main    : all done")

    # W6_T1_PS_24_04_02.acc()

########

    if (robot.button_center) :

        # robot.buttonForward = 0
        W6_T1_PS_24_03_30.setButtons(robot, 0)

        print(robot.button_center)
        W6_T1_PS_24_03_30.stop_program(robot, node, motor_speed=0)
        aw(node.unlock())
        break

    proxG = list(node["prox.ground.ambiant"]) + [0]

    print(proxG[0])
    # print(proxG[1])

    

######## MODIFIED COSTUME

    prox = list(node["prox.horizontal"]) + [0]

    if(prox[2]) :
        update_sensors_data(robot, node)
        print(prox[2])

        W6_T1_PS_24_04_03.see_costume(robot, node, motor_speed=50)
    else :
        W6_T1_PS_24_04_03.no_costume(robot, node, motor_speed=0)
        print(prox[2])

######## 05.04.2024

    # print(prox[5])
    # print(prox[6])

    # if (prox[5]>1000 and prox[6]>1000 and proxG[0]>10) :
    
#     W6_T1_PS_24_03_30.programBack(robot, node, client)
    

# ######## DOUBLED COSTUME

#     # if ((prox[5]>1000 and prox[6]<1000) or (prox[5]<1000 and prox[6]>1000)) :

#     W6_T1_PS_24_03_30.ext_interaction(robot, node, motor_speed=100, obs_threshold=500)

#     if (robot.button_forward and not(robot.buttonForward)) :

#         W6_T1_PS_24_03_30.setButtons(robot, 0)

#         robot.buttonForward = 1


#     elif (robot.button_forward and robot.buttonForward) :

#         robot.buttonForward = 0
#         robot.setLEDTop(node, [0,0,32])
#         aw(client.sleep(2))


#     if (robot.buttonForward) :

#         # while (not robot.button_center) :

#         W6_T1_PS_24_03_30.programFront(robot, node, client)

########

    # if (robot.button_backward) :

    #     W6_T1_PS_24_03_30.setButtons(robot, 0)

    #     robot.buttonBackward = 1

    # if (robot.buttonBackward) :

    #     W6_T1_PS_24_03_30.programBack(robot, node, client)

# INTHREAD.set()
# threadToStop.join()


# if __name__ == "__main__":
#         main()