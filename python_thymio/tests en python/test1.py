from tdmclient import ClientAsync, aw
import matplotlib.pyplot as plt
import numpy as np
# import time
# import copy
import fonction_test1

client = ClientAsync()
node = aw(client.wait_for_node())
aw(node.lock())
aw(node.wait_for_variables())


while(1) :
    