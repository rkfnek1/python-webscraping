import tkinter
import random

index = 0 # 게임 진행 관리 변수
timer = 0 # 시간 관리 변수
score = 0 # 점수용 변수
hisc = 1000 # 최고 점수용 변수
difficulty = 0 # 난이도 관리 변수
tsugi = 0 # 다음에 놓을 고양이 값 대입 변수

cursor_x = 0 # 커서의 x 좌표
cursor_y = 0 # 커서의 y 좌표
mouse_x = 0 # 마우스 포인터의 x 좌표
mouse_y = 0 # 마우스 포이넡의 y 좌표
mouse_c = 0 # 마우스 포인터 클릭 역부 변수(플레그)

def mouse_move(e): # 마우스 포인터 이동 함수
    global mouse_x, mouse_y # mouse_x, mouse_y 전역 변수로 선언
    mouse_x = e.x # mouse_x에 마우스 포인터 x 좌표 대입 
    mouse_y = e.y # mouse_y에 마우스 포인터 y 좌표 대입
    
def mouse_press(e): # 마우스 클릭 실행 함수
    global mouse_c # mouse_c 전역 변수로 선언
    mouse_c = 1 # mouse_c에 1 대입

# neko = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0]
# ] # 위치를 관리할 2차원 리스트

neko = [] # 칸을 관리할 2차원 리스트
check = [] # 판정용 2차원 리스트
for i in range(10): # i는 0부터 10까지 1씩 증가
    neko.append([0, 0, 0, 0, 0, 0, 0, 0]) # append() 명령으로 리스트 초기화
    check.append([0, 0, 0, 0, 0, 0, 0, 0]) # append() 명령으로 리스트 초기화

def draw_neko(): # 고양이 이미지 표시 함수
    cvs.delete("NEKO")
    for y in range(10): # y는 0부터 9까지 1씩 증가
        for x in range(8): # x는 0부터 7까지 1씩 증가
            if neko[y][x] > 0: # neko에 있는 리스트의 값이 0보다 크면
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO") # 고양이 이미지 표시
                
def check_neko(): # 고양이 이미지가 가로, 세로. 대각선 3개인지 확인하는 함수
    for y in range(10): # y는 0부터 9까지 1씩 증가
        for x in range(8): # x는 0부터 7까지 1씩 증가
            check[y][x] = neko[y][x] # 판정용 리스트인 check에 고양이 값 복사
        
    for y in range(1, 9): # y는 1부터 8까지 1씩 증가
        for x in range(8): # x는 0부터 7까지 1씩 증가
            if check[y][x] > 0: # 칸에 고양이 이미지가 있고
                # 고양이 이미지 위아래가 같은 고양이 이미지면 해당 칸을 발자국 이미지로 변경
                if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7
                        
    for y in range(10): # y는 0부터 9까지 1씩 증가
        for x in range(1, 7): # x는 1부터 6까지 1씩 증가
            if check[y][x] > 0: # 칸에 고양이 이미지가 있고
                # 고양이 이미지 좌우가 같은 고양이 이미지면 해당 칸을 발자국 이미지로 변경
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7
                        
    for y in range(1, 9): # y는 1부터 8까지 1씩 증가
        for x in range(1, 7): # x는 1부터 6까지 1씩 증가
            if check[y][x] > 0: # 칸에 고양이 이미지가 있고
                # 고양이 이미지 왼쪽 위, 오른쪽 아래에 같은 고양잉 이미지가 있으면 해당 칸을 발자국 이미지로 변경
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7
                # 고양이 이미지 왼쪽 아래, 오른쪽 위에 같은 고양잉 이미지가 있으면 해당 칸을 발자국 이미지로 변경
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7

def sweep_neko(): # 나란히 놓인 발자국 이미지 삭제 함수
    num = 0 # 지운 수 카운트 변수
    for y in range(10): # y는 0부터 9까지 1씩 증가 (반복)
        for x in range(8): # x는 0부터 8까지 1씩 증가(반복)
            if neko[y][x] == 7: # 만약 칸이 발자국 이미지 이면
                neko[y][x] = 0 # 발자국 이미지 삭제
                num = num + 1 # 지운 수 1 증가
    return num # 지운 수 반환

def drop_neko(): # 고양이 이미지 낙하 함수
    flg = False # 낙하 여부 플레그 (False = 낙하 하지 안았음)
    for y in range(8, -1 , -1): # y는 8부터 0까지 1씩 감소
        for x in range(8): # x는 0부터 7까지 1식 증가
            if neko[y][x] != 0 and neko[y + 1][x] == 0: # 고양이 이미지가 있는 칸의 아래에 칸이 비었다면 
                neko[y + 1][x] = neko[y][x] # 빈 칸에 고양이 이미지를 넣음
                neko[y][x] = 0 # 원래 고양이가 있던 칸을 비움
                flg = True # 낙하 여부 플래그를 세움
    return flg # 플래그 값 반환

def over_neko(): # 가장 윗줄 도달 여부 확인 함수
    for x in range(8): # x는 0부터 7까지 1씩 증가 (반복)
        if neko[0][x] > 0: # 만약 가장 윗줄에 고양이 이미지가 있다면
            return True #  True 반환
    return False # False 반환

def set_neko(): # 가장 윗줄에 고양이 이미지를 놓는 함수
    for x in range(8): # x 0부터 7까지 1씩 증가 (반복)
        neko[0][x] = random.randint(0, difficulty) # 가장 윗줄에 무작위로 고양이 이미지 배치
        
def draw_txt(txt, x, y, siz, col, tg): # 그림자 문자열 표시 함수
    fnt = ("돋움체", siz, "bold") # 폰트 지정
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg) # 대각선으로 2픽셀 이동, 검은 문자열 표시 (그림자)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg) # 지정한 색으로 문자열 표시

# def yoko_neko(): # 같은 고양이 이미지가 가로로 3개 놓였는지 확인하는 함수
#     for y in range(10): # y는 0부터 9까지 1씩 증가
#         for x in range(1, 7): # x는 1부터 6까지 1씩 증가
#             if neko[y][x] > 0: # 칸에 고양이 이미지가 있고
#                 if neko[y][x - 1] == neko[y][x] and neko[y][x + 1] == neko[y][x]: # 좌우에 같은 고양이 이미지가 있다면
#                 # if neko[y-1][x] == neko[y][x] and neko[y+1][x] == neko[y][x]:
#                     # 해당 칸들을 발자국 이미지로 변경
#                     neko[y][x - 1] = 7
#                     neko[y][x] = 7
#                     neko[y][x + 1] = 7
#                     # neko[y-1][x] = 7
#                     # neko[y][x] = 7
#                     # neko[y+1][x] = 7

def game_main(): # 실시간 처리 함수
    global index, timer, score, hisc, difficulty, tsugi # 전역 변수 선언
    global cursor_x, cursor_y, mouse_c # 전역 변수 선언
    if index == 0: # index 0처리 - 타이틀 로고
        draw_txt("고양이", 312, 240, 100, "violet", "TITLE") # 타이틀 로고 텍스트 표시
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width = 0, tag="TITLE") # Easy 문자를 하늘색으로 칠함
        draw_txt("Easy", 312, 420, 40, "white", "TITLE") # Easy 문자 표시
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width = 0, tag="TITLE") # Normal 문자를 연두색으로 칠함
        draw_txt("Normal", 312, 564, 40, "white", "TITLE") # Normal 문자 표시
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width = 0, tag="TITLE") # Hard 문자를 주황색으로 칠함
        draw_txt("Hard", 312, 708, 40, "white", "TITLE") # Hard 문자 표시
        # draw_txt("Click to start.", 312, 560, 50, "orange", "TITLE") # 타이틀에 Click to start. 텍스트 표시
        index = 1 # index에 1 대입
        mouse_c = 0 # 클릭 플래그 해제
    elif index == 1: # index 1 처리 - 타이틀 화면 / 시작 대기
        difficulty = 0 # difficulty에 0 대입
        if mouse_c == 1: # 만약 마우스 포인터를 클릭 했다면
            if 168 < mouse_x and mouse_x < 456 and 384 < mouse_y and mouse_y < 456: # 만약 Easy 텍스트를 클릭했다면
                difficulty = 4 # difficulty에 4 대입
            if 168 < mouse_x and mouse_x < 456 and 528 < mouse_y and mouse_y < 600: # 만약 Normal 텍스트를 클릭했다면
                difficulty = 5 # difficulty에 5 대입
            if 168 < mouse_x and mouse_x < 456 and 672 < mouse_y and mouse_y < 744: # 만약 Hard 텍스트를 클릭했다면
                difficulty = 6 # difficulty에 6 대입
        if difficulty > 0: # difficulty 값이 설정되었다면
            for y in range(10): # y는 0부터 9까지 1씩 증가 (반복)
                for x in range(8): # x는 0부터 7까지 1씩 증가 (반복)
                    neko[y][x] = 0 # 칸 클리어
            mouse_c = 0 # 클릭 플래그 해제
            score = 0 # 점수 0점 대입
            tsugi = 0 # 다음에 배치할 고양이 우선 지움
            cursor_x = 0 # 커서 위치를 외쪽위로 이동
            cursor_y = 0
            set_neko() # 가장 윗줄에 고양이 이미지 배치
            draw_neko() # 고양이 이미지 표시
            cvs.delete("TITLE") # 타이틀 화면 문자 삭제
            index = 2 # index에 2 대입
    elif index == 2: # index 2 처리 - 낙하
        if drop_neko() == False: # 고양이 이미지 낙하, 낙하할 고양이 이미지가 없다면 
            index = 3 # index에 3 대입
        draw_neko() # 고양이 이미지 표시
    elif index == 3: # index 3 처리 - 고양이 이미지가 나란히 놓였는가?
        check_neko() # 같은 고양이 이미지가 나란히 놓였는지 확인
        draw_neko() # 고양이 이미지 표시
        index = 4 # index에 4 대입
    elif index == 4: # index 4 처리 - 나란히 놓인 고양이 이미지가 있다면 삭제
        sc = sweep_neko() # 발자국 이미지 삭제 , 삭제한 수를 sc에 대입
        score = score + sc * difficulty * 2 # 점수 추가
        if score > hisc: # 점수가 최고 점수를 넘었다면
            hisc = score # 최고 점수 업데이트
        if sc > 0: # 만약 삭제한 발자국 이미지가 있다면
            index = 2 # index 2 처리로 이동(다시 낙하)
        else: # 그렇지 않다면
            if over_neko() == False: # 만약 가장 윗줄에 도달하지 않았다면
                tsugi = random.randint(1, difficulty) # 다음에 배치할 고양이 이미지를 랜덤 결정
                index = 5 # index에 5 대입
            else: # 그렇지 않으면 (가장 윗줄에 도달)
                index = 6 # index 6 대입
                timer = 0 # timer 0 대입
        draw_neko() # 고양이 표시
    elif index == 5: # index 5 처리 - 마우스 입력 대기
        if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10: # 마우스 포인터 좌표가 게임 영역 내에 있으면
            cursor_x = int((mouse_x - 24) / 72) # 포인터의 x 좌표에서 커서의 x 좌표 계산
            cursor_y = int((mouse_y - 24) / 72) # 포인터의 y 좌표에서 커서의 y 좌표 계산
            if mouse_c == 1: # 만약 마우스 버튼을 클릭 했다면
                mouse_c = 0 # 클릭 플래그 해제
                set_neko() # 가장 윗줄 고양이 설정
                neko[cursor_y][cursor_x] = tsugi # 커서 칸에 고양이 이미지 배치
                tsugi = 0 # 다음에 배치할 고양이 이미지 삭제
                index = 2 # index에 2 대입
        cvs.delete("CURSOR") # 커서 삭제
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR") # 새로운 위치에 커서 표시
        draw_neko() # 고양이 이미지 표시
    elif index == 6: # index 6 처리 - 게임 오버
        timer = timer + 1 # timer 값 1 증가 
        if timer == 1: # 만약 timer 값이 1 이라면
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER") # "GAME OVER" 문자를 빨간색으로 표시
        if timer == 50: # timer 값이 50 이라면
            cvs.delete("OVER") # GAME OVER 문자열 삭제 
            index = 0 # index에 0 대입
    # if 660 <= mouse_x and mouse_x < 840 and 100 <= mouse_y and mouse_y < 160 and mouse_c == 1: # 해당 좌표를 클릭하면
    #     mouse_c = 0 # 클릭 플래그 해제
    #     # yoko_neko() # 같은 고양이 이미지가 가로로 3개 놓였는지 확인하는 함수 실행
    #     check_neko() # 고양이 연결 확인 함수 실행
    # # drop_neko() # 고양이 이미지 낙하 함수 호출    
    # if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10: # 마우스 포인터 좌표가 게임 영역 내에 있으면
    #     cursor_x = int((mouse_x - 24) / 72) # 포인터의 x 좌표에서 커서의 x 좌표 계산
    #     cursor_y = int((mouse_y - 24) / 72) # 포인터의 y 좌표에서 커서의 y 좌표 계산
    #     if mouse_c == 1: # 마우스를 클릭 했다면
    #         mouse_c = 0 # 클릭 플래그 해제
    #         neko[cursor_y][cursor_x] = random.randint(1, 6) # 커서 위치 칸에 무작위로 고양이 이미지 배치
    cvs.delete("INFO") # 점수 표시 삭제
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO") # 파란색 글씩로 점수 표시
    draw_txt("HISC " + str(hisc), 450, 60, 32, "yellow", "INFO") # 노랑색 글씨로 최고 점수 표시
    if tsugi > 0: # 만약 다음에 배치할 고양이 이미지 값이 설정되어 있다면
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO") # 해당 고양이 이미지 표시
    # cvs.delete("CURSOR") # 커서 이미지 삭제
    # cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR") # 새로운 위치에 커서 표시
    # cvs.delete("NEKO") # 고양이 이미지 삭제
    # draw_neko() # 고양이 이미지 표시
    root.after(100, game_main) # 0.1초 후 메인 함수 재호출

root = tkinter.Tk() # 윈도우 객체 생성
root.title("클릭해서 고양이 놓기") # 윈도우 제목 설정
root.resizable(False, False) # 윈도우 크기 변경 불가 설정

root.bind("<Motion>", mouse_move) # 마우스 포인터 이동 시 실행할 함수 지정
root.bind("<ButtonPress>", mouse_press) # 마우스 클릭 시 실행할 함수 지정

cvs = tkinter.Canvas(root, width=912, height=768) # 캔버스 컨포넌트 생성
cvs.pack() # 캔버스 컴포넌트 배치

bg = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko_bg.png") # 배경 이미지 로딩
cursor = tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko_cursor.png") # 커서 이미지 로딩

img_neko = [
    None,
    tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko1.png"),
    tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko2.png"),
    tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko3.png"),
    tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko4.png"),
    tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko5.png"),
    tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko6.png"),
    tkinter.PhotoImage(file="C:\\Users\\Blackstorm_plecios\\Desktop\\python game\\3Chapter\\neko_niku.png")
] # 리스트로 고양이 이미지 관리하고 img_neko는 아무것도 없는 값으로 선언

cvs.create_image(456, 384, image=bg) # 캔버스에 배경 그리기
# cvs.create_rectangle(660, 100, 840, 160, fill="white") # 배경의 풍선안에 테두리 그리기
# cvs.create_text(750, 130, text="테스트", fill="red", font=("돋움체", 30)) # 테두리 안에 테스트 문자 표시

game_main() # 실시간 처리 함수 호출

root.mainloop() # 윈도우 표시