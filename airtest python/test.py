# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.api import connect_device

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/",],)
    
dev1 = connect_device("Android://127.0.0.1:5037/RFCT42DTEQP") # 첫번때 휴대 전화에 연결
dev2 = connect_device("Android://127.0.0.1:5037/R3CT10K3G1X") # 두번째 휴대 전화에 연결

# script content
print("start...")

def setup(): # 앱 설치 및 삭제 함수
    # uninstall("com.UnityTechnologies.com.unity.template.urpblank") # 앱 삭제
    install(r"C:\SeleniumServer\sailor.apk") # 앱 설치
    snapshot(msg="앱 아이콘 확인") # 설치 확인 스크린샷
    start_app("com.UnityTechnologies.com.unity.template.urpblank") #앱 실행 # 약관동의 팝업 출력까지 대기
    sleep(4)
    
setup() # 첫번째 전화에서 앱 설치 및 삭제 함수 실행

set_current(1) # 첫번째 전화에서 두번째 전화로 연결 변경

setup() # 두번째 전화에서 앱 설치 및 삭제 함수 실행