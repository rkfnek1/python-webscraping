# -*- encoding=utf8 -*-
__author__ = "Blackstorm_plecios"

import shutil
import json
import cv2
import numpy as np
import os
import pyautogui
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
from airtest.core.api import *
from PIL import ImageGrab

auto_setup(__file__)

w = device()
SELF_PATH = os.path.dirname(os.path.realpath(__file__))


def Kill_App(app_name): # 매개 변수를 (app_name)로 지정
    print("kill App") # kill App 글씨출력
    os.system("taskkill /F /T /IM \"{0}.exe\"".format(app_name)) # {0} 부분에 app_name을 넣고 프로세스에서 해당 앱을 종료
    
# Kill_App('notepad') # def Kill_App 함수 실행 코드


zone_info_file = os.path.join(SELF_PATH, "zone_info.json") # zone_info.json 파일 위치를 zone_info_file 변수로 지정
zone_info = dict()
print(zone_info)

zone_scripts_path = os.path.join(SELF_PATH, "zone_script_files") # zone_script_files 파일 위치를 zone_scripts_path 변수로 지정
zone_scripts = []
print(zone_scripts)

def safexcopyfile(SrcFile, DestFile):
    if os.path.exists(SrcFile) and os.path.isfile(SrcFile): # SrcFile 매개변수에 저장된 파일의 이름이 있는지 확인하고 없으면 False를 return한다
        shutil.copyfile(SrcFile, DestFile) # 해당 매개 변수에 저장된 파일을 복사 한다.
    else:
        print(srcFile + " not exists or not file") # 파일을 발견하지 못하면 srcFile 매개 변수에 지정된 "파일 이름 not exists or not file" 해당 메세지를 출력함
        
def get_json_from_file(filepath): # 매개 변수를 filepath로 지정
    data = {} # {}를 data 변수로 지정 
    if os.path.exists(filepath): # filepath 지정된 파일 찾기
        with open(filepath, "r", encoding="utf-8") as f: # filepath 지정된 파일을 열고 f로 지정
            data = json.load(f) # f로 지정된 json파일을 로드하고 data로 지정
    return data # data로 지정된 파일을 리턴

def load_zone_info_and_scripts():
    global zone_info, zone_scripts
    with open(zone_info_file, 'r', encoding="utf-8") as f:
        zone_info = json.load(f)
        print(zone_info)

    for zone_script in os.listdir(zone_scripts_path):
        if len(zone_script.split('.')) > 1:
            zone_scripts.append(zone_script.split('.')[0])



def get_d41_config():
    # root_folder = SELF_PATH[0 : SELF_PATH.find("static")+6]
    # print(root_folder)
    d41_file = os.path.join(SELF_PATH, "d41.json") # 현재의 폴더 경로와 d41.json 파일을 합져서 d41_file 변수에 저장
    if not os.path.exists(d41_file): # d41_file 지정된 파일이 없는지 체크
        print("not exist d41 file") # 파일이 없으면 not exist d41 file 해당 메세지 출력
        return None
    d41_config = get_json_from_file(d41_file) # d41_file에 지정된 파일이 있다면 파일 오픈하고 오픈 상태를 d41_config 변수로 지정
    global report_folder # report_folder 전역 변수로 사용하겠다고 지정
    report_folder = d41_config["report_folder"] # d41.json 파일 안에 내용중 "report_folder" 항목을 가져와 report_folder 변수로 지정
    
def recording(fps, start, end, recording_file_path):
    curScreen  = ImageGrab.grab() # 스크린샷의 이미지를 가져와서 curScreen 변수로 지정 
    height, width = curScreen.size # 가져온 스크린샷의 크기를 height와 width로 지정
    
    video = cv2.VideoWriter(recording_file_path, cv2.VideoWriter_fourcc(*'H264'), fps, (height, width)) # VideoWriter 객체 생성 (비디오 파일 이름, 코덱 지정, fps, 프레임 크기)
    
    imageNum = 0 # imageNum을 0으로 지정
    while True:
        imageNum += 1 # imageNum에 +1 진행
        captureImage = ImageGrab.grab() # 스크린샷의 이미지를 가져와서 captureImage 변수로 지정
        frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR) #이미지를 백터 연산으로 불러오고 RGB형식의 이미지를 BGR형식의 이미지로 변환 
    
        cv2.imshow('capturing', np.zeros((1, 255), np.uint8)) # capturing 이름으로된 창을 생성하고 1줄에 255개의 0을 생성
    
        cv2.moveWindow('capturing', height - 100, width - 100) # capturing 이름으로 출려된 창을 height - 100, width - 100 한 위치로 이동
        if imageNum > fps * start:
            video.write(frame)

        if cv2.waitKey(50) == ord('q') or imageNum > fps * end:
            break
    video.release()
    cv2.destroyAllWindows()

    
SELF_PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 파일이 있는 폴더 경로를 SELF_PATH로 선언
ocr = PaddleOCR(use_angle_cls=True, lang="korean") # (use_angle_cls=True(각도 체크), lang="korean"(언어))

def snap_shot(x, y, w, h, pic_name): # 매개변수(x=좌표, y=좌표, w=너비, h=높이, 저장할 이름)
    pic_name_name = pic_name + '.png' # 함수를 사용할 때 넣은 저장할 이름 매개변수와 .png를 합친 텍스트를 pic_name_name로 선언
    img = pyautogui.screenshot(region = [x,y,w,h]) # # 저장할 스크린샷의 시작 좌표 및 크기 (x=좌표, y=좌표, w=너비, h=높이)
    img.save(os.path.join(SELF_PATH,pic_name_name), 'png') # # pic_dir 변수에 저장된 위치에 찍은 스크린샷을 png로 저장

def ocr_1(img_so): # 매개변수 (사용할 스크린샷의 이름)
    pic = img_so + '.png' # 사용할 스크린샷의 이름을 img_so 넣고 .png와 합친 텍스트를 pic로 선언
    path = os.path.join(SELF_PATH, pic).replace('\\', "/") # SELF_PATH에 선언된 경로와 pic에 선언된 이미지 경로를 합치고 해당 파일의 경로의 \\을 /로 변경 후 path에 선언
    img_ch = ocr.ocr(path, cls = True) # path에 선언된 이미지를 ocr 기능으로 텍스트를 체크하여 img_ch에 선언
    
    images = Image.open(os.path.join(SELF_PATH, pic)) #  SELF_PATH에 선언된 경로와 pic에 선언된 이미지 경로를 합치고 해당 파일을 오픈
    boxes = [line[0] for line in img_ch] # 이미지에 박스 표시
    txts = [line[1][0] for line in img_ch] # 이미지에 텍스트 표시
    scores = [line[1][1] for line in img_ch] # 이미지에 점수 표시
    imgshow = draw_ocr(images, boxes, txts, scores, font_path='malgun.ttf') # ocr된 이미지에 박스, 텍스트, 점수를 맑은 고딕으로 표시 
    imgshow = Image.fromarray(imgshow) # fromarray 함수를 사용하여 배열을 이미지로 변환
    imgshow.save(path) # 해당 이미지 저장
   
    print(img_ch) # ocr된 텍스트 출력
    return(img_ch)

# snap_shot(570, 90, 450, 90, "ma") # 해당 위치를 ma란 제목으로 스크린샷 저장
text = ocr_1('ma') # ma란 파일을 찾아 ocr 함수를 실행시키고 해당 값을 text로 저장
print(text[0][1][0]) # ocr된 내용 출력
if '보기' in text[0][1][0]: # 보기(찾을 텍스트)란 텍스트를 ocr된 내용에서 찾기
    print("확인") # 찾으면 확인 텍스트 출력
else:
    print("실패") # 못찾으면 실패 텍스트 출력