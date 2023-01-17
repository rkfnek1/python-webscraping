import cv2
import numpy as np

##### 3. 도형 그리기 #####

# 세로 480 * 가로 640, 3 Channel(rgb)에 해당하는 스케치북 만들기
def sketchbook():
    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성
    img[:] = (255, 255, 255) #스케치북 전체 공간을 흰색으로 채우기 (값에 따라 색깔은 변경됨) 기본은 검은색 공간
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 스케치북의 일부 영역 색칠
def sketch():
    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성

    # img[:] = (255, 255, 255)
    img[100:200, 200:300] = (255, 255, 255) # [세로 영역 값, 가로 영역 값] 기준으로 원하는 색을 채움

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 직선 그리기
def line():
    # 직선의 종류 (line type)
    cv2.LINE_4 # 상하좌우 4 방향으로 연결된 선
    cv2.LINE_8 # 대각선을 포함한 8 방향으로 연결된 선 (기본값)
    cv2.LINE_AA # 부드러운 선 (anti-aliasing)
    
    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성
    
    COLOR = (0, 255, 255) # BGR : Yellow 선 색깔
    COLOR2 = (255, 0, 255)
    COLOR3 = (255, 255, 0)
    THICKNESS = 3 # 선 두께
    
    line_4 = cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_4) # 그릴 위치, 시작 점, 끝 점, 색깔, 두께, 선 종류
    line_8 = cv2.line(img, (50, 200), (400, 150), COLOR2, THICKNESS, cv2.LINE_8)
    line_AA = cv2.line(img, (50, 300), (400, 200), COLOR3, THICKNESS, cv2.LINE_AA)
    
    # cv2.imshow('img', line_4)
    # cv2.imshow('img', line_8)
    # cv2.imshow('img', line_AA)
    
    cv2.imshow('img', img)
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 원 그리기
def circle():
    # 직선의 종류 (line type)
    cv2.LINE_4 # 상하좌우 4 방향으로 연결된 선
    cv2.LINE_8 # 대각선을 포함한 8 방향으로 연결된 선 (기본값)
    cv2.LINE_AA # 부드러운 선 (anti-aliasing)
    
    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성
    
    COLOR = (0, 255, 255) # BGR : Yellow 선 색깔
    COLOR2 = (255, 0, 255)
    COLOR3 = (255, 255, 0)
    RADIUS = 50 # 반지름
    THICKNESS = 10 # 선 두께
    
    
    # 그릴 위치, 원의 중심점, 반지름, 색깔, 선의 두께, 선의 종류
    cv2.circle(img, (200, 100), RADIUS, COLOR3, THICKNESS, cv2.LINE_AA) # 속이 빈 원
    cv2.circle(img, (400, 100), RADIUS, COLOR3, cv2.FILLED, cv2.LINE_AA) # 속이 꽉찬 원
    
    cv2.imshow('img', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# 사각형 그리기
def Square():
    # 직선의 종류 (line type)
    cv2.LINE_4 # 상하좌우 4 방향으로 연결된 선
    cv2.LINE_8 # 대각선을 포함한 8 방향으로 연결된 선 (기본값)
    cv2.LINE_AA # 부드러운 선 (anti-aliasing)
    
    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성
    
    COLOR = (0, 255, 255) # BGR : Yellow 선 색깔
    COLOR2 = (255, 0, 255)
    COLOR3 = (255, 255, 0)
    THICKNESS = 3 # 선 두께
    
    
    # 그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
    cv2.rectangle(img, (100, 100), (200, 200), COLOR2, THICKNESS) # 속이빈 사각형
    cv2.rectangle(img, (300, 100), (400, 300), COLOR2, cv2.FILLED) # 속이 꽉찬 사각형
    
    cv2.imshow('img', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 다각형 그리기
def polygon():
    # 직선의 종류 (line type)
    cv2.LINE_4 # 상하좌우 4 방향으로 연결된 선
    cv2.LINE_8 # 대각선을 포함한 8 방향으로 연결된 선 (기본값)
    cv2.LINE_AA # 부드러운 선 (anti-aliasing)
    
    img = np.zeros((480, 640, 3), dtype=np.uint8) # 스케치북 생성
    
    COLOR = (0, 0, 255) # 선 색깔
    THICKNESS = 3 # 선 두께
    
    # 그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
    pts1 = np.array([[100, 100], [200, 100], [100, 200]]) # 3개의 좌표를 잇는 도형을 그리기 위한 준비
    pts2 = np.array([[200, 100], [300, 100], [300, 200]])
    pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]]) # 리스트 형태로 필요한 모든 좌표를 입력 가능
    
    # 그릴 위치, 그릴 좌표, 닫힘 여부, 색깔, 두께, 선 종류
    # cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA) # True 일때는 끝점이 잇는다 False 일때는 끝점을 잇지 않는다
    # cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
    # cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 리스트 형태로 2개의 좌표를 같이 그리는게 가능함
    cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA) #꽉찬 다각형 모든 좌표가 리스트 형태로 있으면 좌표 부분에[]를 사용 안해도됨 - 그릴 위치, 그릴 좌표(리스트 형태), 색깔, 선 종류
    
    
    cv2.imshow('img', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()