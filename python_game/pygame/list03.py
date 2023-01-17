import tkinter
import time
FNT = ("Time New Roman", 24) # 폰트 정의 변수

class GameCharacter: # 클래스 정의
    def __init__(self, name, life, x, y, imgfile, tagname): # 생성자
        self.name = name # name 속성에 인수값 대입
        self.life = life # life 속성에 인수값 대입
        self.lmax = life # imax 속성에 인수값 대입
        self.x = x # x 속성에 인수값 대입
        self.y = y # y 속성에 인수값 대입
        self.img = tkinter.PhotoImage(file=imgfile) # img 속성에 이미지 로딩
        self.tagname = tagname # tagname 속성에 인수값 대입
        
    def draw(self): # 이미지 및 정보 표시 메서드
        x = self.x # x 속성에 표시 위치(x좌표) 대입
        y = self.y # y 속성에 표시 위치(y좌표) 대입
        canvas.create_image(x, y, image=self.img, tag=self.tagname) # 이미지 표시
        canvas.create_text(x, y + 120, text=self.name, font=FNT, fill="red", tag=self.tagname) # 문자열 표시 (name 속성값)
        canvas.create_text(x, y + 200, text="lifr{}/{}".format(self.life, self.lmax), font=FNT, fill="lime", tag=self.tagname) # 문자열 표시 (life, imax 속성값)
        
    def attack(self): # 공격 처리 수행 메서드
        di = 1 # 이미지 이동 방향
        if self.x >= 400: # 오른쪽 캐릭터인 경우
            di = -1 # 이동 방향 : 왼쪽 설정
        for i in range(5): # 반복 - 공격 동작 (옆으로 움직임)
            canvas.coords(self.tagname, self.x + i * 10 * di, self.y) # cords() 명령 : 표시 위치 변경
            canvas.update() # 캔버스 업데이트
            time.sleep(0.1) # 0.1초 대기
        canvas.coords(self.tagname, self.x, self.y) # 이미지 원위치
            
    def damage(self): # 데미지 시 처리 수행 메서드
        for i in range(5): # 반복 - 데미지 (화면 깜빡임)
            self.draw() # 캐릭터 표시 매서드 실행
            canvas.update() # 캔버스 업데이트
            time.sleep(0.1) # 0.1초 대기
            canvas.delete(self.tagname) # 화면 삭제(우선 지움)
            canvas.update() # 캔버스 업데이트
            time.sleep(0.1) # 0.1초 대기
        self.life = self.life - 30 # life 30 감소
        if self.life > 0: # life가 0보다 크면
            self.draw() # 캐릭터 표시
        else: # 그렇지 않다면
            print(self.name + "는 쓰러졌다...") # 메시지 셸 윈도우 출력

def click_left(): # 왼쪽 버튼 클릭 처리 함수
    character[0].attack() # 검사의 공격 처리 메서드 실행
    character[1].damage() # 닌자의 데미지 처리 메서드 실행
    
def click_right(): # 오른쪽 버튼 클릭 처리 함수
    character[1].attack() # 닌자의 공격 처리 메서드 실행
    character[0].damage() # 검사의 데미지 처리 메서드 실행
    
root = tkinter.Tk() # 윈도우 객체 생성
root.title("전투 게임") # 타이틀 화면 지정
canvas = tkinter.Canvas(root, width=800, height=600, bg="white") # 캔버스 컴포넌트 생성
canvas.pack() # 캔버스 배치

btn_left = tkinter.Button(text="공격 →", command=click_left) # 왼쪽 버튼 생성
btn_left.place(x=160, y=560) # 왼쪽 버튼 배치

btn_right = tkinter.Button(text="← 공격", command=click_right) # 오른쪽 버튼 생성
btn_right.place(x=560, y=560) # 오른쪽 버튼 배치

character = [ # 리스트로 객체 생성
    GameCharacter("태양의 검사 [가이아]", 200, 200, 280, r"C:\Users\Blackstorm_plecios\Desktop\python_game\pygame\swordsman.png", "LC"), # 검사 객체
    GameCharacter("어둠의 닌자 [한조]", 160, 600, 280, r"C:\Users\Blackstorm_plecios\Desktop\python_game\pygame\ninja.png", "RC") # 닌자 객체
]

character[0].draw() # 검사 객체의 draw() 메서드 실행
character[1].draw() # 닌자 객체의 draw() 메서드 실행

root.mainloop() # 윈도우 표시