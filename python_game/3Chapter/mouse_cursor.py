import tkinter

cursor_x = 0 # 커서의 x 좌표
cursor_y = 0 # 커서의 y 좌표
mouse_x = 0 # 마우스 포인터의 x 좌표
mouse_y = 0 # 마우스 포이넡의 y 좌표

def mouse_move(e): # 마우스 포인터 이동 함수
    global mouse_x, mouse_y # mouse_x, mouse_y 전역 변수로 선언
    mouse_x = e.x # mouse_x에 마우스 포인터 x 좌표 대입 
    mouse_y = e.y # mouse_y에 마우스 포인터 y 좌표 대입
    
def game_main(): # 실시간 처리 수행 함수
    global cursor_x, cursor_y # cursor_x, cursor_y 전역 변수로 선언
    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10: # 마우스 포인터 좌표가 게임 영역 내에 있으면
        cursor_x = int((mouse_x - 24) / 72) # 포인터의 x 좌표에서 커서의 x 좌표 계산
        cursor_y = int((mouse_y - 24) / 72) # 포인터의 y 좌표에서 커서의 y 좌표 계산
    cvs.delete("CURSOR") # 커서 삭제
    cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR") # 새로운 위치에 커서 표시
    root.after(100, game_main) # 0.1초 후 game_main 함수 재실행
    
root = tkinter.Tk() # 윈도우 객체 생성
root.title("커서 표시") # 윈도우 제목 설정
root.resizable(False, False) # 윈도우 크기 변경 불가 설정
root.bind("<Motion>", mouse_move) # 마우스 포인터 이동 실행 함수 지정

cvs = tkinter.Canvas(root, width=912, height=768) # 캔버스 컴포넌트 생성
cvs.pack() # 캔버스 컴포넌트 배치

bg = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko_bg.png") # 배경 이미지 로딩

cursor = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko_cursor.png") # 커서 이미지 로딩

cvs.create_image(456, 384, image=bg) # 캔버스에 배경 그리기

game_main() # 실시간 처리 수행 함수 실행

root.mainloop() # 윈도우 표시