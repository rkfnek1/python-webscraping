# -*- encoding=utf8 -*-
__author__ = "Blackstorm_plecios"

import os
import pyautogui
import time
import ctypes
from airtest.core.api import *

auto_setup(__file__)

w = device()

def Trishion_Move(): # 트리시온 수련장 이동 함수
    w.key_press('F2')
    w.key_release('F2')
    sleep(1)
    
    touch((1423, 405))
    sleep(1)
    
    touch((1462, 878))
    sleep(18)
    
    touch((306, 81), right_click = True)
    sleep(5)
    
    touch((430, 177), right_click = True)
    sleep(4)
    
    touch((966, 892))
    sleep(1)
    
    touch((906, 600))
    sleep(4)

def skill(): # 스킬 사용 함수
    w.key_press('w')
    w.key_release('w')
    sleep(1)
    
    for i in range(2):
        w.key_press('q')
        w.key_release('q')
        sleep(1)
    
    w.key_press('e')
    w.key_release('e')
    sleep(3)
    
    for i in range(2):
        w.key_press('a')
        w.key_release('a')
        sleep(1)
    
    w.key_press('r')
    w.key_release('r')
    sleep(1)
    
    w.key_press('w')
    w.key_release('w')
    sleep(1)
    
    w.key_press('s')
    sleep(1)
    w.key_release('s')
    sleep(1)
    
    for i in range(2):
        w.key_press('q')
        w.key_release('q')
        sleep(1)
    
    w.key_press('d')
    sleep(3)
    w.key_release('d')
    sleep(1)
    
    w.key_press('f')
    w.key_release('f')

Trishion_Move()
skill()