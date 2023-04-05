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

def p4v_Revision():
    try:
        logging.info("p4v_Revision 시작")
        print("p4v_Revision 시작")
        py.doubleClick(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\red_img\p4v.png") # p4v 실행
        sleep(2)
        py.press('enter') # p4v 로그인
        sleep(4)
        py.click(750, 426, button="right") # 워크스페이스에서 마우스 오른족 클릭
        sleep(1)
        py.hotkey("ctrl", "shift", "g") # ctrl + shift + g 키 누르기
        sleep(15)
        py.click(346,785) # 바탕화면 클릭
        sleep(1)
        # py.moveTo(1923, 235)
        csh = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\red_img\csh.png") # 최소화 버튼 중앙으로 이동
        py.click(csh) # 최소화 버튼 클릭
        sleep(2)
        print("p4v_Revision 성공")
        logging.info("p4v_Revision 성공")
    except:
        print("p4v_Revision 실패")
        logging.error("p4v_Revision 실패")
    
def Nexter_uproject():
    try:
        logging.info("Nexter_uproject 시작")
        print("Nexter_uproject 시작")
        py.doubleClick(38, 46) # 내 pc 실행
        sleep(2)
        cla = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\red_img\cla.png") # 즐겨찾기의 Client 폴더 중앙으로 이동
        py.click(cla) # Client 폴더 클릭
        sleep(1)
        pj = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\red_img\pj.png") # Nexter.uproject 파일 중앙으로 이동
        py.doubleClick(pj) # Nexter.uproject 실행
        sleep(80)
        print("Nexter_uproject 성공")
        logging.info("Nexter_uproject 시작")
    except:
        logging.error("Nexter_uproject 실패")
        print("Nexter_uproject 실패")

def Nexter_login():
    try:
        print("Nexter_login 시작")
        sleep(2)
        
        for i in range(2):
            py.click(1224, 637) # 해당 위치 클릭
        sleep(2)
        
        st = py.locateCenterOnScreen(r"C:\Users\Blackstorm_plecios\Desktop\python webscraping\red_img\st.png") # 스타트 버튼 중앙으로 이동
        py.moveTo(412, 88) # 해당 위치로 마우스 이동
        py.moveTo(411, 88) # 해당 위치로 마우스 이동
        py.click(st) # 스타트 버튼 클릭
        sleep(1)
        
        py.click(1341, 708) # 해당 위치 클릭
        sleep(2)
        
        py.click(1241, 657) # 해당 위치 클릭
        sleep(1)
        
        ls = 3
        # ls2 = 2
        # ls3 = 2
        
        random_num = string.digits # 숫자 텍스트 만들기
        # random_id = string.ascii_lowercase
        
        result = ""
        # result2 = ""
        # result3 = ""
        
        # 랜덤한 임의의 3자리 숫자 텍스트 생성
        for i in range(ls):
            result += random.choice(random_num) 
            
        # for i in range(ls2):
        #     result2 += random.choice(random_id)
            
        # for i in range(ls3):
        #     result3 += random.choice(random_id)
        
        py.typewrite("xt_qa_" + result, interval=0.1) # 로그인 화면에서 "xt_qa_생성된 랜덤 숫자" 입력
        # py.typewrite("xt_qa_58", interval=0.1)
        sleep(1)
        
        py.click(1260, 750) # 해당 위치 클릭
        sleep(1)
        
        py.click(1252, 422) # 해당 위치 클릭
        sleep(3)
        
        py.moveTo(1258, 725) # 해당 위치로 마우스 이동
        py.click() # 클릭
        py.moveTo(1256, 725) # 해당 위치로 마우스 이동
        py.click() # 클릭
        sleep(10)
        
        py.click(703, 888) # 해당 위치 마우스 클릭
        sleep(2)
        
        rd = [1, 2, 3]
        ch3 = random.choice(rd) # 랜덤 숫자 선택
        if 1 == ch3:
            py.moveTo(822, 926) # k 위치로 마우스 이동
        elif 2 == ch3: 
            py.moveTo(1011, 932) # 헤라 위치로 마우스 이동
        elif 3 == ch3:
            py.moveTo(1172, 928) # 큐레이 위치로 마우스 이동
        sleep(2)
        py.click() # 클릭
        
        sleep(7)
        
        py.click(1975, 960) # 해당 위치 클릭
        sleep(2)
        
        py.click(1262, 945) # 해당 위치 클릭
        sleep(3)
        
        ls4 = 5
        random_chname = string.ascii_lowercase # 소문자 텍스트 만들기
        
        result4 = ""
        
        # 랜덤한 다섯자의 영어 텍스트 생성 
        for i in range(ls4): 
            result4 += random.choice(random_chname)
        
        py.typewrite(result4, interval=0.1) # 랜덤하게 생셩된 영어 텍스트 입력
        sleep(4)
        
        py.click(1946, 943) # 해당 위치 클릭
        sleep(26)
        
        print("Nexter_login 성공")
    except:
        print("Nexter_login 실패")
        
def move():
    try:
        print("move 시작")
        py.click(1224, 637) # 해당 위치 클릭
        sleep(1)
        
        py.keyDown('w') # 키보드 w 키 누르기
        sleep(2)
        py.keyUp('w') # 키보드 w 키 때기
        
        py.keyDown('s') # 키보드 s 키 누르기
        sleep(2)
        py.keyUp('s') # 키보드 s 키 때기
        
        py.keyDown('a') # 키보드 a 키 누르기
        sleep(2)
        py.keyUp('a') # 키보드 a 키 때기
        
        py.keyDown('d') # 키보드 d 키 누르기
        sleep(2)
        py.keyUp('d') # 키보드 d 키 때기
        
        # 키보드 space 3번 눌렀다 때기
        for i in range(3):
            py.keyDown("space")
            sleep(1)
            py.keyUp('space')
            
        print("move 성공")
    except:
        print("move 실패")

# logging.basicConfig(filename="exampie.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
p4v_Revision()
Nexter_uproject()
Nexter_login()
move()