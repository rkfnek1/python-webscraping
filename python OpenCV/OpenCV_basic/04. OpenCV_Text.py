import cv2
from matplotlib import image
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

##### 4. 텍스트 ##### 

# 글꼴을 적용한 텍스트 출력
def font():
    # OpenCV에서 사용하는 글꼴 종류
    cv2.FONT_HERSHEY_SIMPLEX # 보통 크기의 산 세리프(sans-serif) 글꼴
    cv2.FONT_HERSHEY_PLAIN # 작은 크기의 산 세리프 글꼴
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX # 필기체 스타일 글꼴
    cv2.FONT_HERSHEY_TRIPLEX # 보통 크기의 세리프 글꼴
    cv2.FONT_ITALIC # 기울임 (이탤릭체)

    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성

    SCALE = 1 # 글자 크기
    COLOR = (255, 255, 255) # 색깔
    THICKNESS = 1 # 글자 두께

    # 그릴 위치, 텍스트 내용, 시작 위치, 폰트 종류, 크기, 색깔, 두께
    cv2.putText(img, "Nado Simplex", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS) # 보통 크기의 산 세리프
    cv2.putText(img, "Nado PLAIN", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS) # 작은 크기의 산 세리프
    cv2.putText(img, "Nado SCRIPT_SIMPLEX", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS) # 필기체 스타일
    cv2.putText(img, "Nado TRIPLEX", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS) # 보통 크기의 세리프
    cv2.putText(img, "Nado FONT_ITALIC", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS) # 보통 크기의 세리프에 기울임 적용됨

    cv2.imshow('img', img) # 스케치북 출력

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 한글 우회 방법

def myPutText(src, text, pos, font_size, font_color): # (텍스트가 들어가는 대상, 적용할 텍스트, 위치, 글자 크기, 글자 색깔)
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)
# myPutText 함수는 한글을 출력하게 하기 위해 만든 함수


# 한글 출력
def font_korean():
    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성

    FONT_SIZE = 30 # 글자 크기
    COLOR = (255, 255, 255) # 색깔

    img = myPutText(img, "안녕하세요", (20, 50), FONT_SIZE, COLOR) # (그릴 위치, 내용, 시작 위치, 글자 크기, 글자 색깔)

    cv2.imshow('img', img) # 스케치북에 글자 출력

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
font_korean()