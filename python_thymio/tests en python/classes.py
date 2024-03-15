from tdmclient import ClientAsync, aw
import matplotlib.pyplot as plt
import numpy as np
import time

class Thymio :

    def __init__ (self) :

        self.obs_avoided = False
        self.prox_horizontal = []
        self.button_center = 0

        self.motor_target_left=0
        self.motor_target_right=0

        self.motor_left_speed=0
        self.motor_right_speed=0

    def getProxHorizontal(self, node):
        aw(node.wait_for_variables({"prox.horizontal"}))
        self.prox = list(node["prox.horizontal"]) + [0]

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
