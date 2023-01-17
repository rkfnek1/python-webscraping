import cv2
from matplotlib import image
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

# 크기 조정

## 이미지 크기 조정

# 고정 크기로 설정하여 출력
def fixed_size():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg')
    dst = cv2.resize(img, (400, 500)) # 원하는 이미지, 이미지 크기

    cv2.imshow('img', img) # 원본 이미지 출력
    cv2.imshow('resize', dst) # 사이즈 조절된 이미지 출력

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 비율로 설정
def ratio_size():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg')
    dst = cv2.resize(img, None, fx=0.5, fy=0.5) # x, y 비율 정의 (0.5 배로 축소)

    cv2.imshow('img', img) # 원본 이미지 출력
    cv2.imshow('resize', dst) # 사이즈 조절된 이미지 출력

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

## 보간법
# 보간법을 사용한 이미지 축소
def interpolation():
    cv2.INTER_AREA # 크기 줄일 때 사용
    cv2.INTER_CUBIC # 크기 늘릴 때 사용 (속도가 느림, 퀄리티가 좋음)
    cv2.INTER_LINEAR # 크기 늘릴 때 사용 (기본값)

    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg')
    dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) # x, y 비율 정의 (0.5 배로 축소)
    # cubic = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    # linear = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    cv2.imshow('img', img) # 원본 이미지 출력
    cv2.imshow('resize_area', dst) # 사이즈 조절된 이미지 출력
    # cv2.imshow('resize_cubic', cubic)
    # cv2.imshow('resize_linear', linear)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 보간법을 사용한 이미지 확대
def interpolation_enlargement():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg')
    dst = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC) # x, y 비율 정의 (0.5 배로 확대)
    
    cv2.imshow('img', img) # 원본 이미지 출력
    cv2.imshow('resize_area', dst) # 사이즈 조절된 이미지 출력
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#동영상 고정 크기로 설정
def fixed_video_size():
    cap = cv2.VideoCapture('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.mp4')
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_resized = cv2.resize(frame, (400, 500))
        
        cv2.imshow('video', frame_resized)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
#동영상 비율과 보간법으로 출력
def ratio_video__size():
    cap = cv2.VideoCapture('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.mp4')
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_resized = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        
        cv2.imshow('video1', frame)
        cv2.imshow('video', frame_resized)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()