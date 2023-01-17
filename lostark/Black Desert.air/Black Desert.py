# -*- encoding=utf8 -*-
__author__ = "Blackstorm_plecios"

import pyautogui
from airtest.core.api import *

auto_setup(__file__)

# 스크린샷 함수 동작에 사용
#############################################################################
SELF_PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 위치를 반환
pic_dir = os.path.join(SELF_PATH, 'pic') # pic 폴더 확인
#############################################################################

w = device() # 현재 장치는 반환하는 걸 변수 w로 지정

# npc 찾아 이동에 사용
#############################################################################
NPC_location = {
    'enquipment_enforce': [812,307],
    'gold_store': [2850,671],
    'enquipment_recast':[2777,655]
} # 각각의 npc 좌표 함수로 쉽게 사용하기 위해 제작
#############################################################################

# npc 찾아 이동
def go_to_npc(w, name): # 매개면수(w = deviec(), NPC_location의 npc 이름)
    Location_X = NPC_location[name][0] # 함수 실행 시 지정된 이름의 x좌표 값을 변수에 저장
    Location_Y = NPC_location[name][1] # 함수 실행 시 지정된 이름의 y좌표 값을 변수에 저장
    w.key_press('M') # 키보드 M키 누르기
    w.key_release('M') # 누르고 있는 M키 해제
    sleep(3)
    touch((Location_X, Location_Y), right_click = True) # 좌표 값에 해당되는 위치 오른쪽 클릭
    touch((Location_X+1, Location_Y+1)) # 원래의 좌표 값에 +1을한 위치 클릭

# go_to_npc(w, 'enquipment_enforce') # 


# 스크린샷
def snap_shot(x, y, w, h, pic_name): # 매개변수(x, y, w = 너비, h = 높이, 저장할 이름
    pic_name_name = pic_name + '.png' # 저장 스크린샷 이름
    img = pyautogui.screenshot(region = [x,y,w,h]) # 저장할 스크린샷 위치 및 크기
    img.save(os.path.join(pic_dir,pic_name_name), 'png') # 지정된 폴더에 스크린샷 저장
    # return(pic_name)
    
# snap_shot(18, 116, 1000, 1000, 'ww') # 지정한 좌표에서 부터 1000*1000으로 스크린샷을 찍고 파일 이름을 ww.png로 저장

#  GM 명령 입력
def input_gm(w, *gm_args): # 매개변수(w = deviec(), 가변 매개변수)
    try:
        w.key_press('Enter') # 키보드 Enter 누름
        w.key_release('Enter') # 누르고 있는 Enter 해제
        text("//gm") # //gm 텍스트 입력
        for gm in gm_args:
            w.key_press('Space') # 키보드 Space 누름
            w.key_release('Space') # 누르고 있는 Space 해제
            text(gm) # 가변 매개변수 텍스트 입력
            
        w.key_press('Enter') # 키보드 Enter 누름
        w.key_release('Enter') # 누르고 있는 Enter 해제
    except Exception as e: # Exception 오류가 발생시 e에 오류 메시지 담기
        print(e) # 오류 메세지 표시
    finally: # 사용한 리소스를 close할 때 사용
        return

# input_gm(w, "showmethemoney")

# 在进行用例之前，初始化到主城界面
def back_to_main_town(w):
    w.key_press('ESCAPE') # 키보드 ESC 누름
    w.key_release('ESCAPE') # 누르고 있는 ESC 해제
    sleep(1) # 1초 기다리기
    try:
        while not exists(Template(r"C:\Users\Blackstorm_plecios\Desktop\lostark\Black Desert.air\tpl1652757302953.png")): # 해당 이미지가 나오기 전까지 반복
            w.key_press('ESCAPE') # 키보드 ESC 누름
            w.key_release('ESCAPE') # 누르고 있는 ESC 해제
            sleep(1) # 1초 기다리기
    except Exception as e: # Exception 오류가 발생시 e에 오류 메시지 담기
        print(e) # 오류 메세지 표시
        print('초기화 오류 확인해 주세요') # 메세지 출력
    w.key_press('ESCAPE') # 키보드 ESC 누름
    w.key_release('ESCAPE') # 누르고 있는 ESC 해제
    print('초기화 완료') # 메세지 출력
    
# back_to_main_town(w)

