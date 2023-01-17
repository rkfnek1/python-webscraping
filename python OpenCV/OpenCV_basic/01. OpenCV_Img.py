import cv2

# 1. 이미지 출력
def img_print():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg') # 해당 경로의 파일을 읽어오기(파일 위치 지정시 \가 아닌 \\을 사용하는 이유는 \문자는 이스케이프 문자로 해석하기 때문에)
    # img = cv2.imread(r'C:\Users\Blackstorm_plecios\Desktop\python OpenCV\OpenCV_basic\cat.jpg') # 파일 경로 앞에 r을 붙여주면 \만 사용 가능

    cv2.imshow('img', img) # img라는 이름의 창에 img를 표시

    key = cv2.waitKey(0) # 지정된 시간 동안 사용자 키 입력대기 시간은 (ms) 기준
    # print(key)

    cv2.destroyAllWindows() # 모든창 닫기


# 1-2. 읽기 옵션
def img_option():
    cv2.IMREAD_COLOR # 컬러 이미지 투명 영역은 무시 (기본값)
    cv2.IMREAD_GRAYSCALE # 흑백 이미지
    cv2.IMREAD_UNCHANGED # 투명 역역까지 포함

    img_color = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg', cv2.IMREAD_COLOR)
    # img_grayscale = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg', cv2.IMREAD_GRAYSCALE)
    img_grayscale = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\as.png', cv2.IMREAD_GRAYSCALE)
    img_unchanged = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg', cv2.IMREAD_UNCHANGED)

    cv2.imshow('img_color', img_color)
    cv2.imshow('img_grayscale', img_grayscale)
    cv2.imshow('img_unchanged', img_unchanged)


    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_option()

# 1-3. Shape
def img_Shape():
    img = cv2.imread('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.jpg')
    img.shape # 세로, 가로, Channel 정보를 알 수 있음
    print(img.shape)