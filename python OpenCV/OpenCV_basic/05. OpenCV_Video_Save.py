import cv2
from matplotlib import image
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

# 파일 저장 #

# 이미지 저장
def img_save():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기
    result = cv2.imwrite('cat_img_save.png', img) # png 또는 jpg 형태로 저장


# 동영상 저장
def video_save():
    cap = cv2.VideoCapture('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.mp4')

    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 코덱 정의

    # 프레임 크기, FPS
    width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) # * (숫자)를 하면 저장된 영상의 재생 속도가 2배

    out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height)) # 저장 파일명, 코덱, fps, 크기(width, height)

    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        out.write(frame) # 영상 데이터만 저장 (소리 x)
        cv2.imshow('video', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        
    out.release() # 자원 해제
    cap.release()
    cv2.destroyAllWindows()