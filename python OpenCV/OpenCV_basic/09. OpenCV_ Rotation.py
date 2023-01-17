import cv2
from matplotlib import image
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

# 09. 이미지 회전

# 시계 방향으로 90도 회전
def Angle_90 ():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    
    rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 시계 방향으로 90도 회전
    
    cv2.imshow('img', img)
    cv2.imshow('rotate_90', rotate_90)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 180도 회전
def Angle_180():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    
    rotate_180 = cv2.rotate(img, cv2.ROTATE_180) # 180도 회전
    
    cv2.imshow('img', img)
    cv2.imshow('rotate_180', rotate_180)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 시계 반대 방향 90도 회전 (시계 방향 270도 회전)
def counterclockwise_90():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    
    rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대 방향으로 90도
    
    cv2.imshow('img', img)
    cv2.imshow('rotate_270', rotate_270)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# Angle_90()
# Angle_180()
counterclockwise_90()