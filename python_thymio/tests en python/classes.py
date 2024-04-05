from tdmclient import ClientAsync, aw
import matplotlib.pyplot as plt
import numpy as np
import time

# class threading.Event :


class Thymio :

    def __init__ (self) :

        self.move_front = False
        self.prox_horizontal = []
        self.prox_ground = []

        self.button_center = 0
        self.button_forward = 0
        self.button_backward = 0
        self.button_right = 0
        self.button_left = 0

        self.buttonCenter = 0
        self.buttonForward = 0        
        self.buttonBackward = 0        
        self.buttonRight = 0        
        self.buttonLeft = 0

        self.motor_target_left=0
        self.motor_target_right=0

        self.motor_left_speed=0
        self.motor_right_speed=0

    def getProxHorizontal(self, node):
        aw(node.wait_for_variables({"prox.horizontal"}))
        self.prox = list(node.v.prox.horizontal)
    
    def getProxGround(self, node):
        aw(node.wait_for_variables({"prox.ground"}))
        self.prox = list(node.v.prox.ground)

    def getCenterButton(self, node):
        aw(node.wait_for_variables({"button.center"}))
        self.button_center = node.v.button.center

    def getButtons(self, node):
        aw(node.wait_for_variables({"button.center"}))
        self.button_center = node.v.button.center

        aw(node.wait_for_variables({"button.forward"}))
        self.button_forward = node.v.button.forward

        aw(node.wait_for_variables({"button.left"}))
        self.button_left = node.v.button.left

        aw(node.wait_for_variables({"button.right"}))
        self.button_right = node.v.button.right

        aw(node.wait_for_variables({"button.backward"}))
        self.button_backward = node.v.button.backward

    # def setButtons(self, value) : 

    #     self.buttonCenter = value
    #     # aw(node.set_variables({"button.center": [value]}))

    #     self.buttonForward = value
    #     #aw(node.set_variables({"button.forward": [value]}))
        
    #     self.buttonBackward = value
    #     #aw(node.set_variables({"button.backward": [value]}))
        
    #     self.buttonRight = value
    #    # aw(node.set_variables({"button.right": [value]}))
        
    #     self.buttonLeft = value
       # aw(node.set_variables({"button.left": [value]}))
    def setLEDCircle(self, node, color):
        #led = {"leds.top": colors,} 
        ledCircle = {"leds.circle" : color}
        aw(node.set_variables(ledCircle))
    
    def setLEDTop(self, node, color):

        ledTop = {"leds.top" : color}
        aw(node.set_variables(ledTop))

    def setSpeedLeft(self,speed,node):
        self.motor_target_left=speed
        aw(node.set_variables({"motor.left.target": [speed]}))
    
    def setSpeedRight(self,speed,node):
        self.motor_target_right=speed
        aw(node.set_variables({"motor.right.target": [speed]}))

    def getSpeeds(self,node):
        aw(node.wait_for_variables({"motor.left.speed", "motor.right.speed"}))
        self.motor_left_speed = node["motor.left.speed"]
        self.motor_right_speed = node["motor.right.speed"]
