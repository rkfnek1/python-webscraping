# -*- encoding=utf8 -*-
__author__ = "Blackstorm_plecios"

import os
import pyautogui
import time
import ctypes
from airtest.core.api import *

auto_setup(__file__)

w = device()

def LOG(level, suiteName, caseName, caseResult): # 매개 변수 (레벨, Log 파일 이름, 케이스 이름, 케이스 결과)
    caseResult = caseResult or "NULL" # 케이스 결과를 반환 하거나 NULL로 반환
    logmsg = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) # Log 메세지에서 2022-05-17 12:35:15 같은 형태로 표시
    logmsg = logmsg + "|" + level + "|" + caseName + "|" + caseResult + "<br>\n\r" #  Log 메세지 에서 2022-05-17 12:35:15 | 레벨 | 케이스 이름 | 케이스 결과 결과 마다 다음줄로 이동 시키고 커서를 맨앞으로 이동

    with open(suiteName + ".log", "a+", encoding='utf-8') as logfile: # 설정한 log 파일 이름.log으로 파일을 열고 같은 이름의 파일이 있으면 그파일에 계속 log 작성 변수 이름을 logfile로 지정
        logfile.write(logmsg) # logmsg의 내용을 파일에 입력
        logfile.close() # 열려져있는 log파일 닫기
        
# LOG('3', '2', '1', '') # ('레벨', '파일이름', '케이스 이름', '케이스 결과')

def LOG_START(suiteName, caseName): # 매개 변수 (파일 이름, 케이스 이름)
    log_name = suiteName + ".log" # 지정한 log 이름을 log_name로 지정
    if os.path.exists(log_name): # 지정한 log 이름이 있는지 확인
        os.remove(log_name) # 같은 이름의 log가 있는면 파일 삭제
    LOG("StartTest", suiteName, caseName, "TestCaseStarted") # 
        
# LOG_START('2', '4')

#  GM 명령 입력
def input_gm(w, *gm_args): # 매개변수(w = deviec(), 가변 매개변수)
    try:
        w.key_press('Enter') # 키보드 Enter 누름
        w.key_release('Enter') # 누르고 있는 Enter 해제
        text("//gm") # //gm 텍스트 입력
        for gm in gm_args:
            w.key_press('Space') # 키보드 Space 누름
            w.key_release('Space') # 누르고 있는 Space 해제
            text(gm) # 가변 매개변수에 지정된 텍스트 입력
            
        w.key_press('Enter') # 키보드 Enter 누름
        w.key_release('Enter') # 누르고 있는 Enter 해제
    except Exception as e: # Exception 오류가 발생시 e에 오류 메시지 담기
        print(e) # 오류 메세지 표시
    finally: # 사용한 리소스를 close할 때 사용
        return
    
# 치트키 입력 함수 위에 input_gm 함수와 같이 사용됨
def init_myself():
    input_gm(w, 'clear', 'Inventory', '1') # 엔터가 눌러진 상태에서 //gm clear Inventory 1 을 입력하고 엔터
    input_gm(w, 'clear', 'Inventory', '2') # 엔터가 눌러진 상태에서 //gm clear Inventory 2 을 입력하고 엔터
    
init_myself()
              
SELF_PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 폴더 경로를 SELF_PATH 변수로 만듬
compare_pic = os.path.join(SELF_PATH, 'pic') # SELF_PATH 변수에 저장된 경로와 pic 파일명과 합치기

# 위에 def input_gm 함수 및 def init_myself 함수와 같이 사용
def recase_white_equip():
    print("테스트 시작——start") # 테스트 시작
    touch((624, 380)) # 해당 위치 클릭
    touch((624, 380)) # 해당 위치 클릭
    init_myself() # 위에 def init_myself 함수 실행
    input_gm(w, 'addItem','2605221','1') # gm 치트 입력
    
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    touch((624, 380),right_click = True) # 해당 좌표 오른쪽 클릭
    
    if not exists(Template(os.path.join(compare_pic, 'dom.png'))): # compare_pic 변수에 저장된 위치와 dom.png 이미지 이름을 합치고 이미지 체크
        print("없음!，error!") # 이미지를 찾지 못하면 출력되는 메세지
    elif exists(Template(os.path.join(compare_pic, 'dom.png'))): # compare_pic 변수에 저장된 위치와 dom.png 이미지 이름을 합치고 이미지 체크
        print("찾음， check!") # 이미지를 찾으면 출력되는 메세지
    else: # 모두 해당 되지 않으면
        print("스크립트 오류，error!") # 위에가 모두 실패하면 출력되는 메세지
    print("테스트 종료——end") # 모든 코드를 수행하면 "테스트 종료" 메세지 출력

pic_dir = os.path.join(SELF_PATH, 'pic') # SELF_PATH 변수에 저장된 경로에 pic 폴더를 추가

# 스크린샷
def snap_shot(x, y, w, h, pic_name): # 매개변수(x=좌표, y=좌표, w=너비, h=높이, 저장할 이름)
    pic_name_name = pic_name + '.png' # 찍은 스크린샷의 이름을 pic_name_name 변수에 넣기
    img = pyautogui.screenshot(region = [x,y,w,h]) # 저장할 스크린샷의 시작 좌표 및 크기 (x=좌표, y=좌표, w=너비, h=높이)
    img.save(os.path.join(pic_dir, pic_name_name), 'png') # pic_dir 변수에 저장된 위치에 찍은 스크린샷을 png로 저장

def back_to_main_town(w):
    w.key_press('ESCAPE') # 키보드 ESC 누름
    w.key_release('ESCAPE') # 누르고 있는 ESC 해제
    sleep(1) # 1초 대기
    try:
        while not exists(Template(os.path.join(compare_pic, 'dom.png'))): # compare_pic 변수에 저장된 위치와 dom.png 이미지 이름을 합치고 이미지 체크
            w.key_press('ESCAPE') # 키보드 ESC 누름
            w.key_release('ESCAPE') # 누르고 있는 ESC 해제
            sleep(1) # 1초 기다리기
    except Exception as e: # Exception 오류가 발생시 e에 오류 메시지 담기
        print(e) # 오류 메세지 표시
        print('초기화 오류 확인해 주세요') # 메세지 출력
    w.key_press('ESCAPE') # 키보드 ESC 누름
    w.key_release('ESCAPE') # 누르고 있는 ESC 해제
    print('초기화 완료') # 메세지 출력

def recast_blue_equip():
    print("다음 아이템 재련-start")
    back_to_main_town(w) # def back_to_main_town 함수 실행
    touch((624, 380)) # 해당 좌표 클릭
    touch((624, 380)) # 해당 좌표 클릭
    init_myself() # def init_myself 함수 실행
    input_gm(w, 'addItem', '2605211', '1') # gm 치트 입력
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    touch((624, 380),right_click = True) # 해당 좌표에서 마우스 오른쪽 클릭
    sleep(0.5) # 0.5초 대기
    snap_shot(717, 610, 150, 33, "recast_without_material") # x=717, y=610좌표에서 150*33 사이즈로 스크린샷을 찍고 recast_without_material 이름으로 저장

# ocr 관련 코드
#     recast_text = run_img_recogize("recast_without_material") # ocr 관련 코드
#     print(recast_text[0][1][0])
#     if "缺少必需材料" in recast_text[0][1][0]:
#         print("材料不足时，尝试重铸蓝色物品-check")
#     else:
#         print("材料不足时，尝试重铸蓝色物品-error")
#     print("测试重铸蓝色装备-end")

    sleep(5) # 5초 대기

    print("파란색 아이템 제련-start")
    back_to_main_town(w) # def back_to_main_town 함수 실행
    touch((624, 380)) # 해당 좌표 클릭
    touch((624, 380)) # 해당 좌표 클릭
    init_myself() # def init_myself 함수 실행
    input_gm(w, 'addItem', '500011','9999999') # gm 치트 입력
    input_gm(w, 'addItem', '2605211', '1') # gm 치트 입력
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    touch((624, 380),right_click = True) # 해당 좌표에서 마우스 오른쪽 클릭
    sleep(0.5) # 0.5초 대기
    touch(Template(os.path.join(compare_pic, 'dom.png'))) # compare_pic 변수에 저장된 위치와 dom.png 이미지 이름을 합치쳐서 이미지를 찾고 클릭
    sleep(0.5) # 0.5초 대기
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    sleep(5) # 5초 대기
    snap_shot(570, 90, 450, 90, "recast_with_material") # x=570, y=90좌표에서 150*33 사이즈로 스크린샷을 찍고 recast_with_material 이름으로 저장

# ocr 관련 코드    
#     recast_text2 = run_img_recogize("recast_with_material") # orc 관련 코드
#     print(recast_text2[0][1][0])
#     if "成功" in recast_text2[0][1][0]:
#         print("重铸蓝色物品-check")
#     else:
#         print("重铸蓝色物品-error")
#     print("测试重铸蓝色装备-end")

def recast_red_equip():
    print("다음 아이템 재련-start")
    back_to_main_town(w) # def back_to_main_town 함수 실행
    touch((624, 380)) # 해당 좌표 클릭
    touch((624, 380)) # 해당 좌표 클릭
    init_myself() # def init_myself 함수 실행
    input_gm(w, 'addItem', '2605211', '1') # gm 치트 입력
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    w.key_press('F') # 키보드 F키 누름
    w.key_release('F') # 누르고 있는 F키 해제
    touch((624, 380),right_click = True) # 해당 좌표에서 마우스 오른쪽 클릭
    sleep(0.5) # 0.5초 대기
    snap_shot(717, 610, 150, 33, "recast_without_material") # x=717, y=610좌표에서 150*33 사이즈로 스크린샷을 찍고 recast_without_material 이름으로 저장

# c언어 문법을 사용하게 해주는 함수 같은데 왜 사용 하는지는 모르겠음
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

if __name__ == '__main__':
    recast_blue_equip()
    sleep(5)
    recast_red_equip()
    if sys.version_info[0] == 3: # 현재 실행되는 파이썬의 버전을 확인
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


