import pygame
import sys

WHITE = (255, 255, 255) # 색 정의 : 하얀색
BLACK = (0, 0, 0) # 색 정의 : 검은색

imgBtlBG = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\btlbg.png") # 전투 배경 이미지 로딩
imgEnemy = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\enemy1.png") # 적 이미지를 로딩
emy_x = 440 - imgEnemy.get_width() / 2 # 적 캐릭터 표시 위치 x 좌표
emy_y = 560 - imgEnemy.get_height() # 적 캐릭터 표시 위치 y 좌표

message = [""] * 10 # 전투 메시지 입력 리스트
def init_message(): # 메시지 초기화 함수
    for i in range(10): # 10번 반복
        message[i] = "" # 리스트에 빈 문자열 대입
        
def set_message(msg): # 메시지 설정 함수
    for i in range(10): # 10번 반복
        if message[i] == "": # 문자열이 설정되어 있지 않다면
            message[i] = msg # 새로운 문자열 대입
            return # 함수 처리 종료
        for i in range(9): # 9번 반복
            message[i] = message[i + 1] # 메시지를 한 문자씩 슬라이드
        message[9] = msg # 마지막 행에 새로운 문자열 대입

def draw_text(bg, txt, x, y, fnt, col): # 문자열 그림자 처리 함수
    sur = fnt.render(txt, True, BLACK) # 검은 색으로 문자열을 표시할 Surface
    bg.blit(sur, [x + 1, y + 2]) # 지정 좌표의 약간 오른쪽 아래에 문자열 전송
    sur = fnt.render(txt, True, col) # 지정한 색으로 문자열을 표시할 Surface
    bg.blit(sur, [x, y]) # 지정 좌표에 문자열 전송

def draw_battle(bg, fnt): # 전투 화면 표시 함수
    bg.blit(imgBtlBG, [0, 0]) # 배경 표시
    bg.blit(imgEnemy, [emy_x, emy_y]) # 적 캐릭터 표시
    for i in range(10): # 10번 반복
        draw_text(bg, message[i], 600, 100 + i * 50, fnt, WHITE) # 전투 메시지 표시
        
def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("전투 중 메시지") # 윈도우창 타이틀 지정
    screen = pygame.display.set_mode((800, 720)) # 윈도우창 화면 초기화
    clock = pygame.time.Clock() # clock 객체 초기화
    font = pygame.font.Font(None, 40) # font 객체 초기화
    
    init_message() # 메시지 설정 함수 호출
    
    while True:
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 윈도우창 닫기
            if event.type == pygame.KEYDOWN: # 키를 누른 이벤트 발생한 경우
                set_message("KEYDOWN " + str(event.key)) # 키 값을 메시지에 추가
                
        draw_battle(screen, font) # 전투 화면 표시
        pygame.display.update() # 화면 업데이트
        clock.tick(5) # 프레임 레이트 지정
        
if __name__ == '__main__':
    main()