import os
from sys import path_importer_cache
import pyautogui
import cv2
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

SELF_PATH = os.path.dirname(os.path.realpath(__file__)) # 현재 실행 파일이 있는 폴더 경로를 SELF_PATH로 선언
ocr = PaddleOCR(use_angle_cls=True, lang="korean") # (use_angle_cls=True(각도 체크), lang="korean"(언어))
# ocr = PaddleOCR(lang="korean")

def snap_shot(x, y, w, h, pic_name): # 매개변수(x=좌표, y=좌표, w=너비, h=높이, 저장할 이름)
    pic_name_name = pic_name + '.png' # 함수를 사용할 때 넣은 저장할 이름 매개변수와 .png를 합친 텍스트를 pic_name_name로 선언
    img = pyautogui.screenshot(region = [x,y,w,h]) # # 저장할 스크린샷의 시작 좌표 및 크기 (x=좌표, y=좌표, w=너비, h=높이)
    img.save(os.path.join(SELF_PATH,pic_name_name), 'png') # # pic_dir 변수에 저장된 위치에 찍은 스크린샷을 png로 저장

def ocr_1(img_name): # 매개변수 (사용할 스크린샷의 이름)
    pic = img_name + '.png' # 사용할 스크린샷의 이름을 img_so 넣고 .png와 합친 텍스트를 pic로 선언
    path = os.path.join(SELF_PATH, pic).replace('\\', "/") # SELF_PATH에 선언된 경로와 pic에 선언된 이미지 경로를 합치고 해당 파일의 경로의 \\을 /로 변경 후 path에 선언
    img_ch = ocr.ocr(path, cls = True) # path에 선언된 이미지를 ocr 기능으로 텍스트를 체크하여 img_ch에 선언
    # img_ch = ocr.ocr(path)
    
    images = Image.open(os.path.join(SELF_PATH, pic)) #  SELF_PATH에 선언된 경로와 pic에 선언된 이미지 경로를 합치고 해당 파일을 오픈
    boxes = [line[0] for line in img_ch] # 이미지에 박스 표시
    txts = [line[1][0] for line in img_ch] # 이미지에 텍스트 표시
    scores = [line[1][1] for line in img_ch] # 이미지에 신뢰도 표시
    imgshow = draw_ocr(images, boxes, txts, scores, font_path='malgun.ttf') # ocr된 이미지에 텍스트에 빨간색 사각형이 출력되고 추출된 텍스트와 신뢰도를 맑은 고딕으로 표시
    imgshow = Image.fromarray(imgshow) # fromarray 함수를 사용하여 배열을 이미지로 변환
    imgshow.save(path) # 해당 이미지 저장
   
    print(img_ch) # ocr된 텍스트 출력
    return(img_ch)

# snap_shot(570, 90, 450, 90, "ma") # x=좌표, y=좌표, w=너비, h=높이 수치에 맞는 스크린샷을 찍고 ma란 제목으로 저장
text = ocr_1('as') # 영수증이란 파일을 찾아 ocr 함수를 실행시키고 해당 값을 text로 선언
print(text[14][1][0]) # ocr된 내용에서 text[14][1][0]해당 부분의 텍스트 출력

if '승민' in text[14][1][0]: # 대표지(찾을 텍스트)란 텍스트를 ocr된 내용에서 찾기
    print("텍스트 확인 완료") # 찾으면 확인 텍스트 출력
else:
    print("텍스트 확인 실패") # 못찾으면 실패 텍스트 출력