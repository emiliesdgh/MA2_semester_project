import classes
from classes import Thymio

from tdmclient import ClientAsync, aw
# import matplotlib.pyplot as plt
import numpy as np
# import time

# client = ClientAsync()
# node = aw(client.wait_for_node())
# aw(node.lock())
# aw(node.wait_for_variables())

# #Classes initialization
# robot = Thymio()

def setButtons(Thymio, value) : 

        Thymio.buttonCenter = value
        Thymio.buttonForward = value        
        Thymio.buttonBackward = value        
        Thymio.buttonRight = value        
        Thymio.buttonLeft = value


def see_costume(Thymio, node, obs_threshold) :

    proxG = list(node["prox.ground.ambiant"]) + [0]

    print(proxG[0])
    print(proxG[1])


def ext_interaction(Thymio, node, motor_speed=100, obs_threshold=500) :

    prox = list(node["prox.horizontal"]) + [0]

    if prox[5] > prox[6] :

        Thymio.setSpeedLeft(motor_speed, node)
        Thymio.setSpeedRight(-motor_speed, node)

    elif prox[6] > prox[5] : # Thymio needs to contourn the obstacle counterclockwise

        Thymio.setSpeedLeft(-motor_speed, node)
        Thymio.setSpeedRight(motor_speed, node)

    else :

        Thymio.setSpeedLeft(0, node)
        Thymio.setSpeedRight(0, node)

def stop_program(Thymio, node, motor_speed=100) :

    Thymio.setSpeedLeft(0, node)
    Thymio.setSpeedRight(0, node)


def programFront (Thymio, node, client) :

    Thymio.setSpeedLeft(50, node)
    Thymio.setSpeedRight(-50, node)

    aw(client.sleep(2))

    Thymio.setSpeedLeft(-50, node)
    Thymio.setSpeedRight(50, node)

    aw(client.sleep(2))


def acc():
    global acc, leds_top
    if acc[0]>18 or acc[0]<-18: #Thymio is blue when placed on one of its sides
        leds_top=[0,0,32]
    if acc[1]>18 or acc[1]<-18: #Thymio is red when placed on its front or backside
        leds_top=[32,0,0]
    if acc[2]>18 or acc[2]<-18: #Thymio is green when placed on its wheels or upside-down
        leds_top=[0,32,0]

def clockwise(node) :

    '''This function verrifies if the obstacle to avoid is more on its right or left,
        therefore, the Thymio will contourn it accordingly.'''

    prox = list(node["prox.horizontal"]) + [0]

    if prox[1] > prox[3] :

        return True # returns True if the obstacle is closer to the sensor [1] rather than the sensor [3]

    return False



def obstacle_avoidance(Thymio, node, client, motor_speed=100, obs_threshold=500): #, clockwise = False):

    '''Wall following behaviour of the FSM
    param motor_speed: the Thymio's motor speed
    param wall_threshold: threshold starting which it is considered that the sensor saw a wall'''

    clockwises_true = False  # Booleen to state if the Thymio has to contourn on the left or right

    prev_state = "turning" # Stated of movement of the Thymio

    while not Thymio.obs_avoided :     # As long as the obstacle isn't avoided, stay in the while loop

        if see_costume(Thymio, node, obs_threshold) :

            if prev_state == "turning": # little rotation on it's own to then do the contourning

                if clockwise(node) :

                    Thymio.setSpeedLeft(motor_speed, node)
                    Thymio.setSpeedRight(-motor_speed, node)

                    clockwise_true = True   # Thymio needs to contourn the obstacle clockwise

                else : # Thymio needs to contourn the obstacle counterclockwise

                    Thymio.setSpeedLeft(-motor_speed, node)
                    Thymio.setSpeedRight(motor_speed, node)

                prev_state = "contourning" # Change the state so the Thymio countourns the obstacle fully

        else:
            if prev_state == "contourning":

                if clockwise_true :

                    Thymio.setSpeedLeft(motor_speed-40, node)
                    Thymio.setSpeedRight(motor_speed, node)

                    prev_state = "turning"

                    aw(client.sleep(18))

                    Thymio.setSpeedLeft(motor_speed, node)
                    Thymio.setSpeedRight(-motor_speed, node)

                    aw(client.sleep(2))

                    Thymio.obs_avoided = True  # obstacle has been avoided, change the state booleen

                else :

                    Thymio.setSpeedLeft(motor_speed,node)
                    Thymio.setSpeedRight(motor_speed-40,node)

                    prev_state="turning"

                    aw(client.sleep(18))

                    Thymio.setSpeedLeft(-motor_speed,node)
                    Thymio.setSpeedRight(motor_speed,node)

                    aw(client.sleep(2))

                    Thymio.obs_avoided = True  # obstacle has been avoided, change the state booleen

        aw(client.sleep(0.1)) #otherwise, variables would not be updated


