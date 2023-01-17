import cv2
from cv2 import THRESH_BINARY
# from cv2 import FILLED
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

### 11. 이미지 변형 (이진화) ###

# Threshold
def binary_black():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\book.jpg', cv2.IMREAD_GRAYSCALE)

    ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('img', img)
    cv2.imshow('binary', binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Trackbar (값 변화에 따른 변형 확인)
# 출력된 이미지에서 스크롤바로 이미지의 이진화 확인
def empty(pos): # createTrackbar 마지막 값을 지정해주기 위해 생성
    pass


def black_Binary():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\book.jpg', cv2.IMREAD_GRAYSCALE)

    name = 'trackbar'
    cv2.namedWindow(name)

    cv2.createTrackbar('trackbar', name, 1, 255, empty) # bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리

    while True:
        thresh = cv2.getTrackbarPos('trackbar', name) # bar 이름, 창의 이름
        ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
            
        if not ret:
            break
            
        cv2.imshow(name, binary)
        if cv2.waitKey(1) == ord('q'):
            break
            
    cv2.destroyAllWindows()

# threshold의 시작과 최대 값에 따른 출력 확인
def binary_black2():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\threshold.png', cv2.IMREAD_GRAYSCALE)

    ret, binary1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    ret, binary2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, binary3 = cv2.threshold(img, 195, 255, cv2.THRESH_BINARY)
    
    cv2.imshow('fd', img)
    cv2.imshow('binary1', binary1)
    cv2.imshow('binary2', binary2)
    cv2.imshow('binary3', binary3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Adaptive_Threshold(): # Adaptive_Threshold 이미지를 작은 영역으로 나눠서 임계치 적용
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\book.jpg', cv2.IMREAD_GRAYSCALE)

    name = 'trackbar'
    cv2.namedWindow(name)

    cv2.createTrackbar('block_size', name, 1, 255, empty) # 홀수만 가능 1보다는 큰 값
    cv2.createTrackbar('c', name, 3, 10, empty) # 일반적으로 양수의 값을 사용

    while True:
        block_size = cv2.getTrackbarPos('block_size', name) # bar 이름, 창의 이름
        c = cv2.getTrackbarPos('c', name)
        
        if block_size <= 1: # 1 이하면 3 으로
            block_size = 3
            
        if block_size % 2 == 0: # 짝수이면 홀수로
            block_size += 1
            
        binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, block_size, c)
            
        cv2.imshow(name, binary)
        if cv2.waitKey(1) == ord('q'):
            break
            
    cv2.destroyAllWindows()
    
# 오츠 알고리즘 (자동으로 이미지의 임계치를 찾아줌)
def Otsu_Algorithm():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\book.jpg', cv2.IMREAD_GRAYSCALE)

    ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, Otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print('Otsu threshold', ret)

    cv2.imshow('img', img)
    cv2.imshow('binary', binary)
    cv2.imshow('Otsu', Otsu)

    cv2.waitKey(0)
    cv2.destroyAllWindows()