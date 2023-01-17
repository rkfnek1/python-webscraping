import tkinter

mouse_x = 0 # 마우스 포인터의 x 좌표
mouse_y = 0 # 마우스 포인터의 y 좌표
mouse_c = 0 # 마우스 포인터 클릭 역부 변수(플레그)

def mouse_move(e): # 마우스 포인터 이동 실행 함수
    global mouse_x, mouse_y # mouse_x, mouse_y 전역 변수로 선언
    mouse_x = e.x # mouse_x에 마우스 포인터의 x 좌표 대입
    mouse_y = e.y # mouse_y에 마우스 포인터의 y 좌표 대입
    
def mouse_press(e): # 마우스 클릭 실행 함수
    global mouse_c # mouse_c 전역 변수로 선언
    mouse_c = 1 # mouse_c에 1 대입
    
def mouse_release(e): # 마우스 클릭 해제 실행 함수
    global mouse_c # mouse_c 전역 변수로 선언
    mouse_c = 0 # mouse_c에 0 대입 
    
def game_main(): # 실시간 처리 수행 함수
    fnt = ("돋움체", 30) # 폰트 지정 변수
    txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c) # 표시할 문자열 변수(마우스 좌표값과 클릭 여부)
    cvs.delete("TEST") # 문자열 삭제
    cvs.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST") # 캔버스에 문자열 표시
    root.after(100, game_main) # 0.1초 후 game_main 함수 재실행
    
root = tkinter.Tk() # 윈도우 객체 생성
root.title("마우스 입력") # 윈도우 제목 지정
root.resizable(False, False) # 윈도우 크기 변경 불가 설정

root.bind("<Motion>", mouse_move) # 마우스 포인터 이동 시 실행할 함수 지정
root.bind("<ButtonPress>", mouse_press) # 마우스 클릭 시 실행할 함수 지정
root.bind("<ButtonRelease>", mouse_release) # 마우스 클릭 해제 시 실행할 함수 지정

cvs = tkinter.Canvas(root, width=912, height=768) # 캔버스 컴포넌트 생성
cvs.pack() # 캔버스 컴포넌트 배치

game_main() # 실시간 처리 함수 실행

root.mainloop() # 윈도우 표시