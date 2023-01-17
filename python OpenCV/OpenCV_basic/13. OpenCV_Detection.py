import cv2
from cv2 import THRESH_BINARY
# from cv2 import FILLED
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

### 이미지 검출 ###

# 경계선 검출 (Canny Edge Detection)
def Canny():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\snowman.png')

    canny = cv2.Canny(img, 150, 200) # 대상 이미지, minVal(하위 임계값), maxVal(상위 임계값)

    cv2.imshow('img', img)
    cv2.imshow('canny', canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 스크롤바로 경계선 조절
def empty(pos):
    pass

def Canny2():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\snowman.png')
    
    name = "Trackbar"
    cv2.namedWindow(name)
    cv2.createTrackbar('threshold1', name, 0, 255, empty) # minVal
    cv2.createTrackbar('threshold2', name, 0, 255, empty) # maxVal

    while True:
        threshold1 = cv2.getTrackbarPos('threshold1', name)
        threshold2 = cv2.getTrackbarPos('threshold2', name)
    
        canny = cv2.Canny(img, threshold1, threshold2) # 대상 이미지, minVal(하위 임계값), maxVal(상위 임계값)

        cv2.imshow('img', img)
        cv2.imshow(name, canny)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()
    
Canny2()