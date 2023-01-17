# -*- encoding=utf8 -*-
__author__ = "Blackstorm_plecios"

import os
import pyautogui
import time
import ctypes
from airtest.core.api import *

auto_setup(__file__)

w = device()

def portal_move():
    w.key_press('M')
    w.key_release('M')
    sleep(1)
    touch((1183, 433))
    sleep(1)
    touch((915, 541))
    sleep(9)

def move():
    touch((123, 633), right_click = True)
    sleep(3)
    touch((1105, 913), right_click = True)
    sleep(3)
    
    
portal_move()
move()