import cv2
from cv2 import THRESH_BINARY
# from cv2 import FILLED
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

### 이미진 변환 ###

# 팽창 (이미지를 확장하여 작은 구멍에 채움)
    # 흰색 영역의 외각 픽셀 주변에 흰색을 추가
def dilate():
    kernel = np.ones((3,3), dtype=np.uint8)

    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\dilate.png', cv2.IMREAD_GRAYSCALE)
    dilate1 = cv2.dilate(img, kernel, iterations=1) # iterations=반복 횟수
    dilate2 = cv2.dilate(img, kernel, iterations=2)
    dilate3 = cv2.dilate(img, kernel, iterations=3)

    cv2.imshow('img', img)
    cv2.imshow('dilate1', dilate1)
    cv2.imshow('dilate2', dilate2)
    cv2.imshow('dilate3', dilate3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 침식 (이미지를 깎아서 노이즈 제거)
    # 흰색 영역의 외곽 픽셀을 검은색으로 변경
def erode():
    kernel = np.ones((3, 3), dtype=np.uint8)

    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\erode.png', cv2.IMREAD_GRAYSCALE)
    erode1 = cv2.erode(img, kernel, iterations=1) # 1회 반복 
    erode2 = cv2.erode(img, kernel, iterations=2)
    erode3 = cv2.erode(img, kernel, iterations=3)

    cv2.imshow('img', img)
    cv2.imshow('erode1', erode1)
    cv2.imshow('erode2', erode2)
    cv2.imshow('erode3', erode3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#### 열림 & 닫힘 ###  
# 열림
def open():
    # 열림 (Opening) : 침식 후 팽창. 깍아서 노이즈 제거 후 살 찌움
    # dilate(erode(image))
    kernel = np.ones((3 ,3), dtype=np.uint8)
    
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\erode.png', cv2.IMREAD_GRAYSCALE)
    
    erode = cv2.erode(img, kernel, iterations=3)
    dilate = cv2.dilate(erode, kernel, iterations=3)
    
    cv2.imshow('img', img)
    cv2.imshow('erode', erode)
    cv2.imshow('dilate', dilate)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 닫힘
def closed():
    # 닫힘 (Opening) : 팽창 후 침식. 구멍을 메운 후 다시 깎음
    # erode(dilate(image))
    kernel = np.ones((3 ,3), dtype=np.uint8)
    
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\dilate.png', cv2.IMREAD_GRAYSCALE)
    
    dilate = cv2.dilate(img, kernel, iterations=3)
    erode = cv2.erode(dilate, kernel, iterations=3)
    
    cv2.imshow('img', img)
    cv2.imshow('dilate', dilate)
    cv2.imshow('erode', erode)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
closed()