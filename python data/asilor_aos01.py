import unittest
import os
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# opencv를 사용하기 위해 아래 모듈을 import합니다.
import cv2
import numpy as np
import time, datetime

class Matching():

    def detectimage(self, screenshotPath, detectImagePath):

        sourceimage = cv2.imread(screenshotPath, 0)
        template = cv2.imread(detectImagePath, 0)
        w, h = template.shape[::-1]

        method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(sourceimage, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print('\nmax_val: %d' % max_val)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (top_left[0] + int(w/2), top_left[1] + int(h/2))

        color = (0, 0, 255)
        cv2.rectangle(sourceimage, top_left, bottom_right, color, thickness=8)

        detectshotPath = screenshotPath[:-4] + '-detect.png'
        cv2.imwrite(detectshotPath, sourceimage)

        return center


class GrandchaseLoginOutTest(unittest.TestCase):

    def makeTS(self):
        return str(int(datetime.datetime.now().timestamp()))

    def strDatetime(self):
        return str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        
    def setUp(self):
        
        # Kakao Game SDK Test App 경로
        app = os.path.join(os.path.dirname(__file__), r'C:\SeleniumServer', 'sailor.apk')
        app = os.path.abspath(app)
        
        android_options = AppiumOptions()
        android_options.set_capability('app', app)
        android_options.set_capability('platformName', 'Android')
        android_options.set_capability('platformVersion', '13')
        android_options.set_capability('deviceName', 'Galaxy S22+')
        android_options.set_capability('automationName', 'uiautomator2')
        android_options.set_capability('newCommandTimeout', 300)
        android_options.set_capability('appPackage', 'com.UnityTechnologies.com.unity.template.urpblank')
        android_options.set_capability('appActivity', 'com.unity3d.player.UnityPlayerActivity')
        android_options.set_capability('udid', 'RFCT42DTEQP')
        
        # Set up appium
        # Appium 서버의 포트는 4001로 지정합니다.
        # 그리고 desired_capabilities에 연결하려는 디바이스(V10)의 정보를 넣습니다.
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723', options=android_options
            # desired_capabilities={
            #     'app': app,
            #     'platformName': 'Android',
            #     'platformVersion': '13',
            #     'deviceName': 'Galaxy S22+',
            #     'automationName': 'Appium',
            #     'newCommandTimeout': 300,
            #     'appPackage': 'com.UnityTechnologies.com.unity.template.urpblank',
            #     'appActivity': 'com.unity3d.player.UnityPlayerActivity',
            #     'udid': 'RFCT42DTEQP'
            # }
        )      
        
    def test_search_field(self):

        matching = Matching()

        # 스크린샷을 저장할 폴더를 생성합니다.
        # test_folder_name = self.strDatetime()
        # currentPath = '%s/' % os.getcwd()
        # test_Directory = currentPath + test_folder_name + '/'
        
        # if not os.path.exists(test_Directory):
        #     os.makedirs(test_Directory)

        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GrandchaseLoginOutTest)
    unittest.TextTestRunner(verbosity=2).run(suite)