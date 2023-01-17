from turtle import shape
import cv2
from matplotlib import image
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

# 7. 이미지 자르기

# 영역을 잘라서 새로운 윈도우(창)에 출력
def crop_img():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg')
    # img.shape # (390, 640, 3)
    crop = img[100:200, 200:400] # [세로 기준 100:200 까지, 가로 기준 200:400 까지]

    cv2.imshow('img', img)
    cv2.imshow('crop', crop)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 영역을 잘라서 기존 윈도우(창)에 출력
def crop_existing():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg')
    crop = img[100:200, 200:400] # [세로 기준 100:200 까지, 가로 기준 200:400 까지 자름]
    img[100:200, 400:600] = crop # 원본 이미지의 지정된 위치에 자른 이미지를 저장

    cv2.imshow('img', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()