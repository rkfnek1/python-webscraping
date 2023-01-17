import cv2
from cv2 import THRESH_BINARY
# from cv2 import FILLED
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

### 퀴즈 ###
# OpenCV를 이용하여 가로로 촬영된 영상을 세로로 회전하는 프로그램을 작성하시오
    # 조건
        # 1. 회전 : 시계 반대방향으로 90도
        # 2. 재생속도 (FPS) : 원본 X 4
        # 3  출력 파일명 : city_output.avi(코덱 : DIVX)
def OpenCV_Quiz():
    cap = cv2.VideoCapture(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\city.mp4')
    
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 코덱 정의
    width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # round로 받아와 정수 처리
    height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # round로 받아와 정수 처리
    fps = cap.get(cv2.CAP_PROP_FPS) # * (숫자)를 하면 저장된 영상의 재생 속도가 2배
    
    out = cv2.VideoWriter('city_output.avi', fourcc, fps * 4, (height, width)) # 저장 파일명, 코덱, fps, 크기(width, height)
    
    while cap.isOpened(): # 동영상 파일이 올바로 열렸는지 확인
        ret, frame = cap.read() #  ret : 성공 여부, frame : 받아온 이미지 (프레임)
        if not ret:
            break
        
        rotate_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대 방향으로 90도 회전
        out.write(rotate_frame) # 영상 데이터만 저장 (소리 x)
        cv2.imshow('city_output', frame) # 출력창 열기
        
        # 키값이 들어오면 열려있는 창이 닫힘
        if cv2.waitKey(1) == ord('q'): # Key 값 비교는 위해서 ord 함수 사용 (waitKey 값으로 영상 속도 조정)
            break
    
    out.release() # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

OpenCV_Quiz()