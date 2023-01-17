import pygame
import sys
import random
from pygame.locals import *

WHITE = (255, 255, 255) # 색 정의 : 하얀색
BLACK = (0, 0, 0) # 색 정의 : 검은색

imgBtlBG = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\btlbg.png") # 전투 배경 이미지 로딩
imgEffect = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\effect_a.png") # 공격 효과 이미지 로딩
imgEnemy = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\enemy4.png") # 적 이미지를 로딩
emy_x = 440 - imgEnemy.get_width() / 2 # 적 캐릭터 표시 위치 x 좌표
emy_y = 560 - imgEnemy.get_height() # 적 캐릭터 표시 위치 y 좌표
emy_step = 0 # 적 캐릭터 이동 관리 변수
emy_blink = 0 # 적 캐릭터 깜빡임 효과 관리 변수
dmg_eff = 0 # 화면 흔들림 효과 관리 변수
COMMAND = ["[A]ttack", "[P]otion", "[B]lazegem", "[R]un"] # 전투 명령어 리스트 정의

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
    global emy_blink, dmg_eff # 전역 변수 선언
    bx = 0 # 배경 표시 위치 x 좌표
    by = 0 # 배경 표시 위치 y 좌표
    if dmg_eff > 0: # 화면 흔들림 효과 변수가 설정되어 있다면
        dmg_eff = dmg_eff - 1 # 해당 변수값 1 감소
        bx = random.randint(-20, 20) # 난수로 x 좌표 결정
        by = random.randint(-10, 10) # 난수로 y 좌표 결정
    bg.blit(imgBtlBG, [bx, by]) # (bx, by) 위치에 배경 표시
    if emy_blink % 2 == 0: # 적을 깜빡이기 위함 if 구문
        bg.blit(imgEnemy, [emy_x, emy_y + emy_step]) # 적 캐릭터 표시
    if emy_blink > 0: # 적을 깜빡이기 위한 변수가 설정되어 있다면
        emy_blink = emy_blink - 1 # 해당 변수값 1 감소
        for i in range(10): # 10번 반복
            draw_text(bg, message[i], 600, 100 + i * 50, fnt, WHITE) # 전투 메시지 표시
            
def battle_command(bg, fnt): # 전투 명령어 표시 함수
    for i in range(4): # 4번 반복
        draw_text(bg, COMMAND[i], 20, 300 + 60 * i, fnt, WHITE) # 전투 명령어 표시
        
def main():
    global emy_step, emy_blink, dmg_eff # 전역 변수 선언
    idx = 10 # 게임 진행 관리 인덱스
    tmr = 0 # 게임 진행 관리 타이머 변수
    
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("전투 중 메시지") # 윈도우창 타이틀 지정
    screen = pygame.display.set_mode((800, 720)) # 윈도우창 화면 초기화
    clock = pygame.time.Clock() # clock 객체 초기화
    font = pygame.font.Font(None, 30) # font 객체 초기화
    
    init_message() # 메시지 설정 함수 호출
    
    while True:
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 윈도우창 닫기
        
        draw_battle(screen, font) # 전투 화면 표시
        tmr = tmr + 1 # tmr 값 1 증가
        key = pygame.key.get_pressed() # 리스트 key에 모든 키 상태 대입
        
        if idx == 10: # idx 10 처리 - 전투 개시
            if tmr == 1: set_message("Encounter!") # tmr 값이 1 이면 메시지 설정
            if tmr == 6: # tmr 값이 6이면
                idx = 11 # 플레이어 입력 대기로 이동
                tmr = 0
        
        elif idx == 11: # idx 11 처리 - 플레이어 입력 대기
            if tmr == 1: set_message("Your turn") # tmr 값이 1 이면 메시지 설정
            battle_command(screen, font) # 전투 명령어 표시 처리
            if key[K_a] == 1 or key[K_SPACE] == 1: # A 키 또는 스페이스 키를 눌렀다면
                idx = 12 # 플레이어 공격으로 이동
                tmr = 0
        
        elif idx == 12: # idx 12 처리 - 플레이어 공격
            if tmr == 1: set_message("Your attack!") # tmr 값이 1 이면 메시지 설정
            if 2 <= tmr and tmr <= 4: # tmr 값이 2에서 4 사이이면
                screen.blit(imgEffect, [700 - tmr * 120, -100 + tmr * 120]) # 공격 효과 표시
            if tmr == 5: # tmr 값이 5 이면
                emy_blink = 5 # 적을 깜빡임 효과 변수 설정
                set_message("***pts of damage!") # 메시지 설정
            if tmr ==16: # tmr 값이 16 이면
                idx = 13 # 적 턴으로 이동
                tmr = 0

        elif idx == 13: # idx 13 처리 - 적 턴, 적 공격
            if tmr == 1: set_message("Enemy turn.") # tmr 값이 1 이면 메시지 설정
            if tmr == 5: # # tmr 값이 5 이면
                set_message("Enemy attack!") # 메시지 설정
                emy_step = 30 # 적 이동 변수 설정
            if tmr == 9: # tmr 값이 9 이면
                set_message("***pts of damage!") # 메시지 설정
                dmg_eff = 5 # 화면 흔들림 변수 값 설정
                emy_step = 0 # 적을 원래 위치로 이동
            if tmr == 20: # tmr 값이 20 이면
                idx = 11 # 플레이어 입력 대기로 이동
                tmr = 0
        
        pygame.display.update() # 화면 업데이트
        clock.tick(5) # 프레임 레이트 지정
        
if __name__ == '__main__':
    main()