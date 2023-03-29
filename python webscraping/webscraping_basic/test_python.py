import pyautogui as py
import pytest, sys, logging
from time import sleep
import random
import string

# print(py.position())
# print(py.size())

# py.moveTo(25, 60)
# py.click()

# py.click(25, 60, button="right")

# py.moveTo(32, 1366)
# py.doubleClick()

# def test_function_01():
#     # logging.info(sys._getframe(0).f_code.co_name)
#     py.click(3353, 840)
#     # py.typewrite("Hello world!", interval=0.1)
#     # py.press('enter')
#     # py.typewrite(["a", "b", "c", "d"], interval=0.1)
#     # print(py.KEYBOARD_KEYS)
#     # py.click(center1)
#     # py.click()
#     py.typewrite("Hello world!", interval=0.1)


# def test_function_02():
#     """스크리샷을 찍는 함수"""
#     py.screenshot("my_screenshot.png")  # my_screenshot.png 파일로 스크린샷을 찍는다.


# def test_function_03():
#     # (0, 0, 300, 300) 영역을 스크린샷으로 찍어 my_region.png 파일로 저장한다.
#     py.screenshot("my_region.png", region=(0, 0, 300, 300))


# def test_function_04():
#     p = 1
#     p + 1 == 4  # p + 1이 4와 같은지 확인한다.

def p4v_Revision():
    try:
        print("p4v_Revision 시작")
        py.doubleClick(561, 245)
        sleep(2)
        py.press('enter')
        sleep(4)
        py.click(750, 426, button="right")
        sleep(1)
        py.hotkey("ctrl", "shift", "g")
        sleep(15)
        py.click(346,785)
        sleep(1)
        py.moveTo(1923, 235)
        sleep(1)
        py.click()
        sleep(2)
        print("p4v_Revision 성공")
    except:
        print("p4v_Revision 실패")
        pass
    
def Nexter_uproject():
    try:
        print("Nexter_uproject 시작")
        py.doubleClick(38, 46)
        sleep(2)
        cla = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\webscraping_basic\cla.png")
        py.click(cla)
        sleep(1)
        pj = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\webscraping_basic\pj.png")
        py.doubleClick(pj)
        sleep(30)
        print("Nexter_uproject 성공")
    except:
        print("Nexter_uproject 실패")
        pass

def Nexter_login():
    try:
        print("Nexter_login 시작")
        sleep(2)
        
        py.click(1224, 637)
        py.click(1224, 637)
        sleep(2)
        
        st = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\webscraping_basic\st.png")
        py.moveTo(412, 88)
        py.moveTo(411, 88)
        py.click(st)
        sleep(1)
        
        py.click(1341, 708)
        sleep(2)
        
        py.click(1241, 657)
        sleep(1)
        
        ls = 3
        # ls2 = 2
        # ls3 = 2
        
        random_num = string.digits # 숫자 텍스트 만들기
        # random_id = string.ascii_lowercase
        
        result = ""
        # result2 = ""
        # result3 = ""
        
        for i in range(ls):
            result += random.choice(random_num)
            
        # for i in range(ls2):
        #     result2 += random.choice(random_id)
            
        # for i in range(ls3):
        #     result3 += random.choice(random_id)
        
        py.typewrite("xt_qa_" + result, interval=0.1)
        sleep(1)
        
        py.click(1260, 750)
        sleep(1)
        
        py.click(1252, 422)
        sleep(3)
        
        py.moveTo(1258, 725)
        py.click()
        py.moveTo(1256, 725)
        py.click()
        sleep(10)
        
        py.click(703, 888)
        sleep(2)
        
        rd = [1 , 2, 3]
        ch3 = random.choice(rd)
        if 1 == ch3:
            py.moveTo(822, 926) # k
        elif 2 == ch3:
            py.moveTo(1011, 932) # 헤라
        elif 3 == ch3:
            py.moveTo(1172, 928) # 큐레이
        sleep(2)
        py.click()
        sleep(4)
        
        chc = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\webscraping_basic\chc.png")
        py.click(chc)
        sleep(2)
        py.click(1262, 945)
        sleep(3)
        
        ls4 = 5
        random_chname = string.ascii_lowercase # 소문자 텍스트 만들기
        
        result4 = ""
        
        for i in range(ls4):
            result4 += random.choice(random_chname)
        
        py.typewrite(result4, interval=0.1)
        sleep(4)
        
        chs = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\webscraping_basic\chs.png")
        py.click(chs)
        
        print("Nexter_login 성공")
    except:
        print("Nexter_login 실패")
        pass

p4v_Revision()
Nexter_uproject()
Nexter_login()