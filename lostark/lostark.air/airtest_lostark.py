# -*- encoding=utf8 -*-
__author__ = "Blackstorm_plecios"
import pywinauto as py

from airtest.core.api import *

auto_setup(__file__)

win = device()

# 에어테스트 클릭 형식
########################################################################
# touch((1615, 341)) # airtest 마우스 왼쪽 클릭
# sleep(1) # 1초 대기

# touch((1549, 178))
# sleep(1) # 1초 대기

# touch((949, 179), right_click = "Ture") # airtest 마우스 오른쪽 클릭
# sleep(2) # 1초 대기

# touch(Template(r"\\192.168.0.252\blackstorm\QA\airtest_lostark_img\tpl1652159108077.png", record_pos=(0.382, -0.115), resolution=(2508, 1411))) # airtest 이미지 클릭
# sleep(1) # 1초 대기

# touch((1544, 119))
# sleep(1) # 1초 대기

# touch(Template(r"\\192.168.0.252\blackstorm\QA\airtest_lostark_img\tpl1652159371000.png"))# airtest 이미지 지정 클릭
# sleep(1)
#########################################################################

# pywinauto 클릭 형식
#######################################################################
# py.mouse.click('left', (2111, 444)) # pywinauto 마우스 왼쪽 클릭
# sleep(1)

# py.mouse.click('right', (893, 337)) # pywinauto 마우스 오른쪽 클릭
# sleep(1)

# py.mouse.right_click((669, 827)) # pywinauto 마우스 오른쪽 클릭
# sleep(1)

# py.mouse.press('right', (669, 827)) # 마우스 오른쪽 클릭 유지
# sleep(2)
# py.mouse.release('right') # 마우스 오른쪽 클릭 해제

# py.mouse.press('left', (669, 827)) # 마우스 왼쪽 클릭 유지
# sleep(4)
# py.mouse.release('left') # 마우스 왼쪽 클릭 해제
#########################################################################

# wait 원하는 이미지가 나올때 까지 대기
#######################################################################
# wait(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080))) # 해당 이미가 출력될때 까지 대기
# sleep(1)
# touch(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)), right_click = "Ture") # 해당 이미지 오른쪽 클릭

# wait(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)), timeout = 5) # 해당 이미지가 나올때 까지 5초 대기

# wait(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)), timeout = 6, interval = 3) # 해당 이미지가 나올때 까지 6초 동안 3초마다 체크

# def mgs():
#     print("찾는중")

# wait(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)), intervalfunc = mgs) # 이미지를 찾을때 까지 Log Viewer에 "찾는중" 메세지 출력

########################################################################

# swipe 화면을 드래그 진행
#######################################################################
# swipe((1101, 804), (1293, 697)) # 첫번째 좌표에서 두번째 좌표로 드래그 이동

# swipe(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)), vector = [-0.4, -0.4]) # 해당 이미지를 찾아 vector값의 좌표로 드래그

# swipe((1736, 591), Template(r"tpl1652239633393.png", record_pos=(0.4, -0.075), resolution=(1920, 1080))) # 첫번째 좌표에서 두번째 이미지까지 드래그

# swipe((1101, 804), (1293, 697), duration = 1, steps = 6) # 드래그가 1초 동안 6번 진행
########################################################################

# exists 지정한 이미지가 화면에 있는지 확인
#######################################################################

# 지정된 이미지를 찾고 이미지가 있으면 마우스 오른쪽 클릭

# if exists(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080))):
#     touch(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)), right_click = "Ture")

# exists를 변수로 지정해서 사용
# img = exists(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)))
# if img:
#     touch(img, right_click = "Ture")
########################################################################

# text 텍스트 입력 창이 활성화 상태일 때 텍스트 입력
#######################################################################
# text("보석") # 보석 텍스트 입력 (로스트 아크에서 enter 값은 적용되지 않음)

# text("보석", enter = False) # 텍스트 입력 후 enter 사용하지 않음

# text("보석", search = True) # 텍스트 입력 후 검색 버튼 클릭
########################################################################

# keyevent 키보드 입력
#######################################################################
# keyevent("{F2}") # F2키 입력
# sleep(1)
# keyevent("{F2}")
# sleep(1)

# keyevent("{VK_NUMPAD1}") # NUMPAD1 입력 
# sleep(1)
# keyevent("{VK_NUMPAD1}")
# sleep(1)
########################################################################

# snapshot 스크린샷 찍기
#######################################################################

# snapshot() # 기본 스크린샷 저장
# sleep(1)

# snapshot(filename = "d.png") # 파일 이름을 d.png로 해서 저장
# sleep(1)

# snapshot(filename = "메세지.png", quality = 50) # 파일 이름을 메세지.png로 저장 하고 스크린샷 퀄리티를 50으로 해서 저장 quality는 기본 10으로 지정되어있고 1 ~ 99까지 설정 가능
# sleep(1)

# snapshot(filename = "사이즈.png", max_size = 600) # 파일 이름을 사이즈.png로 저장 하고 이미지 사이즈는 600*600을 초과하지 않게 저장
# sleep(1)

# snapshot(filename = "ms.png", quality = 60, max_size = 1200) # 파일 이름을 ms.png로 저장 하고 이미지 퀄리티를 60으로 이미지 사이즈는 1200*1200을 초과하지 않게 저장
########################################################################

# sleep 지정한 시간 동안 대기
#######################################################################

# 이미지를 클릭 후 10초 후에 다음 행동 진행
# touch(Template(r"\\192.168.0.252\blackstorm\QA\airtest_lostark_img\tpl1652159108077.png", record_pos=(0.382, -0.115), resolution=(2508, 1411)))

# sleep(10) # 10초 대기

# touch((1544, 119)) # 해당 좌표 클릭
########################################################################

# assert_exists 화면에서 지정한 이미지가 있는지 체크 만약 이미지를 찾지 못하면 AssertionError 출력
#######################################################################

# assert_exists(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)))
########################################################################

# assert_not_exists 화면에서 지정한 이미지가 없는지 체크 만약 이미지를 찾은면 AssertionError 출력
#######################################################################

# assert_not_exists(Template(r"tpl1652231387181.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)))
########################################################################

