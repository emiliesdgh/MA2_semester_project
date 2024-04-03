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





def ext_interaction(Thymio, node, motor_speed=100, obs_threshold=500) :

    prox = list(node["prox.horizontal"]) + [0]

    if prox[5] > prox[6] :

        color = [24,24,24,0,0,0,0,24]
        Thymio.setLEDCircle(node, color)

        Thymio.setSpeedLeft(motor_speed, node)
        Thymio.setSpeedRight(-motor_speed, node)

    elif prox[6] > prox[5] : # Thymio needs to contourn the obstacle counterclockwise
        color = [24,24,0,0,0,0,24,24]
        Thymio.setLEDCircle(node, color)
        
        Thymio.setSpeedLeft(-motor_speed, node)
        Thymio.setSpeedRight(motor_speed, node)

    elif prox[0]+prox[1] > prox[3] + prox[4] :

        color = [0,24,24,24,24,0,0,0]
        Thymio.setLEDCircle(node, color)
         
        Thymio.setSpeedLeft(-motor_speed, node)
        Thymio.setSpeedRight(motor_speed, node)

    elif prox[0]+prox[1] < prox[3] + prox[4] :

        color = [0,0,0,0,24,24,24,24]
        Thymio.setLEDCircle(node, color)
         
        Thymio.setSpeedLeft(motor_speed, node)
        Thymio.setSpeedRight(-motor_speed, node)

    # elif prox[2] > (prox[0] or prox[1] or prox[3] or prox[4]) :

    #     color = [0,0,0,24,24,24,0,0]
    #     Thymio.setLEDCircle(node, color)

    #     Thymio.setSpeedLeft(-motor_speed, node)
    #     Thymio.setSpeedRight(-motor_speed, node)

    else :
        color = [0,0,0,0,0,0,0,0]
        Thymio.setLEDCircle(node, color)

        Thymio.setSpeedLeft(0, node)
        Thymio.setSpeedRight(0, node)


def stop_program(Thymio, node, motor_speed=0) :

    Thymio.setLEDTop(node, [32,32,32])

    Thymio.setSpeedLeft(motor_speed, node)
    Thymio.setSpeedRight(motor_speed, node)


def programFront (Thymio, node, client) :

    Thymio.setLEDTop(node, [20,0,32])
    color = [0,0,0,0,0,0,0,0]
    Thymio.setLEDCircle(node, color)

    Thymio.setSpeedLeft(50, node)
    Thymio.setSpeedRight(-50, node)

    aw(client.sleep(2))

    Thymio.setSpeedLeft(-50, node)
    Thymio.setSpeedRight(50, node)

    aw(client.sleep(2))

def programBack (Thymio, node, client) :

    Thymio.setLEDTop(node, [20,0,32])
    color = [0,0,0,0,0,0,0,0]
    Thymio.setLEDCircle(node, color)

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


