import uiautomator2 as u2 # uiautomator2 필수 임포트 항목
# import unittest
# import os
# from appium import webdriver
# from appium.webdriver.webdriver import AppiumOptions
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

# # opencv를 사용하기 위해 아래 모듈을 import합니다.
# import cv2
# import numpy as np
# import time, datetime

dev1 = "RFCT42DTEQP" # 연결할 디바이스 udid
dev2 = "R3CT10K3G1X" # 연결할 디바이스 udid

d = u2.connect(dev1) # connect할 디바이스 변수 생성
c = u2.connect(dev2) # connect할 디바이스 변수 생성

app_apckage = "com.UnityTechnologies.com.unity.template.urpblank" # 사용할 앱 패키지 이름 변수 생성


d.app_uninstall("com.UnityTechnologies.com.unity.template.urpblank") # 설치된 앱 삭제
c.app_uninstall("com.UnityTechnologies.com.unity.template.urpblank") # 설치된 앱 삭제

d.app_install(r"C:\SeleniumServer\sailor.apk") # 앱 설치
c.app_install(r"C:\SeleniumServer\sailor.apk") # 앱 설치

def test():
    d.app_start(app_apckage) # 설치된 앱 실행
    c.app_start(app_apckage) # 설치된 앱 실행
    
    sleep(22) # 앱 실행 후 20초 기다림
    
    d.xpath('//android.widget.FrameLayout[1]').click() # 해당 구역 클릭
    c.xpath('//android.widget.FrameLayout[1]').click() # 해당 구역 클릭
    # d.click(1080, 2131)

test()