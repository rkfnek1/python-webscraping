import cv2
from matplotlib import image
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

# 8. 이미지 대칭

# 좌우 대칭
def left_right_symmetry_img():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    flip_horizontal = cv2.flip(img, 1) # flip은 대칭 함수 flipCode > 0 : 좌우 대칭 horizontal
    
    cv2.imshow('img', img)
    cv2.imshow('flip_horizontal', flip_horizontal)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 상하 대칭
def up_down_symmetry_img():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    flip_vertical = cv2.flip(img, 0) # flip은 대칭 함수 flipCode == 0 : 상하 대칭 vertical
    
    cv2.imshow('img', img)
    cv2.imshow('flip_vertical', flip_vertical)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 상하 좌우 대칭
def up_down_left_right_symmetry_img():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    flip_both = cv2.flip(img, -1) # flip은 대칭 함수 flipCode < 0 : 상하 좌우 대칭
    
    cv2.imshow('img', img)
    cv2.imshow('flip_both', flip_both)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()