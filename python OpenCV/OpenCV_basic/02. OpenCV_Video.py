import cv2

###### 2. 동영상 파일 출력 #####

def Video_print():
    cap = cv2.VideoCapture('C:\\Users\\Blackstorm_plecios\\Desktop\\python OpenCV\\OpenCV_basic\\cat.mp4')

    while cap.isOpened(): # 동영상 파일이 올바로 열렸는지 확인
        ret, frame = cap.read() #  ret : 성공 여부, frame : 받아온 이미지 (프레임)
        if not ret:
            print("더이상 가져올 프레임 없음")
            break
        
        cv2.imshow('video', frame) # 출력창 열기
        
        # 키값이 들어오면 열려있는 창이 닫힘
        if cv2.waitKey(1) == ord('q'): # Key 값 비교는 위해서 ord 함수 사용 (waitKey 값으로 영상 속도 조정)
            print("사용자 입력에 의해 종료")
            break

    cap.release() # 자원 해제
    cv2.destroyAllWindows()
    
# 2-1 카메라 출력
def Video_camera():
    cap = cv2.VideoCapture(0) # 0번째 카메라 장치 (Device ID)
    if not cap.isOpened(): # 카메라가 잘 열리지 않은 경우
        exit() # 프로그램 종료
        
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) == ord('q'): # 사용자가 q를 입력하면 창 닫기
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
Video_print()