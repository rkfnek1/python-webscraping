import cv2
from cv2 import FILLED
import numpy as np
from PIL import ImageFont, ImageDraw, Image # PIL (Python Image Library) - 한글 표시하기 위해 사용하는 라이브러리

# 10. 이미지 변형(흑백, 흐림(blur), 원근)

# 불러온 이미지를 흑백으로 변경
def Gray_scale():
    # img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    
    dat = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 이미지를 흑백으로 변경
    
    cv2.imshow('img', img)
    cv2.imshow('img2', dat)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
### 불러온 이미지를 블러 처리 (가우시안 블러) ###
# 커널 사이즈 변화에 따른 흐림
def blur_kernel():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    
    kernel_3 = cv2.GaussianBlur(img, (3, 3), 0) # 가로안의 (3, 3)이 커널값
    kernel_5 = cv2.GaussianBlur(img, (5, 5), 0)
    kernel_7 = cv2.GaussianBlur(img, (7, 7), 0)
    
    cv2.imshow('img', img)
    cv2.imshow('kernel_3', kernel_3)
    cv2.imshow('kernel_5', kernel_5)
    cv2.imshow('kernel_7', kernel_7)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 표준 편차 변화에 따른 흐림
def blur_sigmax():
    # sigmax 사이즈 변화에 따른 흐림
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg')
    
    sigma_1 = cv2.GaussianBlur(img, (0, 0), 1) # sigmax - 가우시안 커널의 X 방향의 표준 편차
    sigma_2 = cv2.GaussianBlur(img, (0, 0), 2)
    sigma_3 = cv2.GaussianBlur(img, (0, 0), 3)
    
    cv2.imshow('img', img)
    cv2.imshow('sigma_1', sigma_1)
    cv2.imshow('sigma_2', sigma_2)
    cv2.imshow('sigma_3', sigma_3)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 펼쳐진 이미지의 원하는 부분을 세워서 출력 (원근1)
def perspective_1():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\newspaper.jpg')
    
    width, height = 640, 240 # 가로 크기 640, 세로 크기 240으로 결과물 출력을 위한 크기 지정
        
    src = np.array([[523, 353], [999, 345], [1117, 583], [467, 583]], dtype=np.float32) # input 4개 지점
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32) # outnput 4개 지점
    # 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)
    
    matrix = cv2.getPerspectiveTransform(src, dst) # Matrix 얻어옴
    result = cv2.warpPerspective(img, matrix, (width, height)) # Matrix 대로 변환을 함
    
    cv2.imshow('img', img)
    cv2.imshow('result', result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#회전된 이미지를 올바르게 세우기 (원근2)
def perspective_2():
    img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\poker.jpg')
    
    width, height = 530, 710 # 가로 크기 640, 세로 크기 240으로 결과물 출력을 위한 크기 지정
    
    src = np.array([[700, 147], [1128, 418], [720, 999], [281, 695]], dtype=np.float32) # input 4개 지점
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32) # outnput 4개 지점
    # 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)
    
    matrix = cv2.getPerspectiveTransform(src, dst) # Matrix 얻어옴
    result = cv2.warpPerspective(img, matrix, (width, height)) # Matrix 대로 변환을 함
    
    cv2.imshow('img', img)
    cv2.imshow('result', result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

### 미니 프로젝트 : 반자동 문서 스캐너 ###
point_list = [] # 마우스 클릭 값을 저장하고 있을 리스트
src_img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\poker.jpg') # 이미지 불러오기
COLOR = (255, 0, 255) # 마우스 클릭 위치 표시할 때 색깔값
THICKNESS = 3
drawing = False # 선을 그릴지 여부

# 마우스 이벤트 함수
def mouse_handler(event, x, y, flags, param):
    # if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 down
    #     print('왼쪽 버튼 Down')
    #     print(x,y)
    # elif event == cv2.EVENT_LBUTTONUP:# 마우스 왼쪽 버튼 up
    #     print('왼쪽 버튼 up')
    #     print(x,y)
    # elif event == cv2.EVENT_LBUTTONDBLCLK: # 마우스 왼족 버튼 더블 클릭
    #     print('왼쪽 버튼 더블 Double Click')
    # elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동
    #     print('마우스 이동')
    # elif event == cv2.EVENT_RBUTTONDOWN: # 마우스 오른쪽 버튼 down
    #     print('오른쪽 버튼 Down')
    
    global drawing # global 키워드를 통해서 전역부분에 drawing을 쓴다고 정의
    dst_img = src_img.copy() # 기존 이미지를 카피 만드는 새로운 이미지를 계속 출력하게 하기위해
    
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 down
        drawing = True # 선을 그리기 시작
        point_list.append((x,y)) # x,y 좌표 값을 리스트에 저장
        
    # 클릭한 위치에 점을 찍고 선을 그림
    if drawing:
        prev_point = None # 직선의 시작점
        for point in point_list:
            cv2.circle(dst_img, point, 15, COLOR, FILLED) # 마우스가 클릭된 좌표에 동그라미 표시
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point # 점이 찍힐 때 prev_point에 저장
            
        
        # 4개의 점이 찍히면 마지막 클릭지점과 첫번째 클릭 지점을 선으로 연결
        next_point = (x, y) # mouse_handler에서 받아오는 x, y
        if len(point_list) == 4: # 점이 찍힌 갯수 계산
            show_result() # 결과 출력
            next_point = point_list[0] # 첫 번째 클릭한 지점
            
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
        
    cv2.imshow('img', dst_img)
    
# 마우스가 클릭된 곳을 기준으로 새로운 윈도우창 출력
def  show_result():
    width, height = 530, 710 # 가로 크기 530, 세로 크기 710으로 결과물 출력을 위한 크기 지정
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32) # outnput 4개 지점
    # 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)
    
    matrix = cv2.getPerspectiveTransform(src, dst) # Matrix 얻어옴
    result = cv2.warpPerspective(src_img, matrix, (width, height)) # Matrix 대로 변환을 함
    
    cv2.imshow('result', result)
    
# 작업을 진행할 이미지 불러오기
def document_scanner_project():
    cv2.namedWindow('img') # img 란 이름의 윈도우를 먼저 만들어두는 것. 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
    cv2.setMouseCallback("img", mouse_handler)
    cv2.imshow('img', src_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

document_scanner_project()