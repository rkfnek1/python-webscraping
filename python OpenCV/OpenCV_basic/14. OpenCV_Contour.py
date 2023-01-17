import cv2
from cv2 import THRESH_BINARY
# from cv2 import FILLED
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

### 이미지 검출 (윤곽선) ###
    # 윤곽선 (Contour) : 경계선을 연결한 선

# 이미지의 윤곽선 그리기
def Contour():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\card.png')
    target_img = img.copy() # 사본 이미지
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 원본 이미지를 흑백 이미지로 변환
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # 윤관선 정보 - contours
    # 윤곽선 구조 - hierarchy
    # 이미지 - otsu
    # 윤곽선 찾는 모드 (mode) - cv2.RETR_LIST
    # 윤곽선 찾으때 사용하는 근사치 방법 (method) - cv2.CHAIN_APPROX_NONE (모든 좌표 반환), cv2.CHAIN_APPROX_SIMPLE (꼭지점 좌표만 반환)
    
    COLOR = (0, 200, 0) # 녹색
    
    cv2.drawContours(target_img, contours, -1, COLOR, 2) # 윤곽선 그리기
    # 대상 이미지(target_img), 윤곽선 정보(contours), 인덱스 (-1 이면 전체), 색깔(COLOR), 두께(2)
    
    cv2.imshow('img', img)
    # cv2.imshow('gray', gray)
    # cv2.imshow('otsu', otsu)
    cv2.imshow('contours', target_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 윤곽선 찾기 모드
def Contour_find_mode():
    cv2.RETR_EXTERNAL # 가장 외곽의 윤관선만 찾음
    cv2.RETR_LIST # 모든 윤곽선 찾음 (계층 정보 없음)
    cv2.RETR_TREE # 모든 윤곽선 찾음 (계층 정보를 트리 구조로 생성)
    
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\card.png')
    target_img1 = img.copy()
    target_img2 = img.copy()
    target_img3 = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    contours1, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours2, hierarchy = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours3, hierarchy = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    COLOR = (0, 200, 0)
    
    cv2.drawContours(target_img1, contours1, -1, COLOR, 2)
    cv2.drawContours(target_img2, contours2, -1, COLOR, 2)
    cv2.drawContours(target_img3, contours3, -1, COLOR, 2)
    
    cv2.imshow('img', img)
    # cv2.imshow('gray', gray)
    # cv2.imshow('otsu', otsu)
    cv2.imshow('contours1', target_img1)
    cv2.imshow('contours2', target_img2)
    cv2.imshow('contours3', target_img3)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 경계 사각형 (boundingRect)
def Contour_Square():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\card.png')
    target_img = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    COLOR = (0, 200, 0)
    
    for cnt in contours:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, 2) # 사각형 그림
    
    cv2.imshow('img', img)
    # cv2.imshow('gray', gray)
    # cv2.imshow('otsu', otsu)
    cv2.imshow('contours', target_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 윤곽선의 면적 (contourArea)
def Contour_area():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\card.png')
    target_img = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    COLOR = (0, 200, 0)
    
    for cnt in contours:
        if cv2.contourArea(cnt) > 25000: # 카드 한장 크기 (가로 X 세로)
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, 2) # 사각형 그림
    
    cv2.imshow('img', img)
    # cv2.imshow('gray', gray)
    # cv2.imshow('otsu', otsu)
    cv2.imshow('contours', target_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
### 미니 프로젝트 : 개별 카드 추출해서 파일 저장 ###
def card_extraction():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\card.png')
    target_img = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    COLOR = (0, 200, 0)
    
    idx = 1
    for cnt in contours:
        if cv2.contourArea(cnt) > 25000: # 카드 한장 크기 (가로 X 세로)
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, 2) # 사각형 그림

            crop = img[y:y+height, x:x+width] # 원본에서 찾은 윤곽선 만큼 자른걸 crop에 저장
            cv2.imshow(f'card_crop_{idx}', crop) # 추출된 카드 이미지 출력
            cv2.imwrite(f'card_crop_{idx}.png', crop) # 추출된 카드 이미지 저장
            idx += 1 # idx가 늘어나게 하기위해 작성
    
    cv2.imshow('img', img)
    # cv2.imshow('gray', gray)
    # cv2.imshow('otsu', otsu)
    cv2.imshow('contours', target_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()