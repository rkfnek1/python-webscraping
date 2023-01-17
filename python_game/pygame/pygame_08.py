import pygame
import sys

WHITE = (255, 255, 255) # 색 정의 : 하얀색

imgBtlBG = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\btlbg.png") # 전투 배경 이미지 로딩
imgEnemy = None # 적 이미지를 로딩할 변수 준비

emy_num = 0 # 로딩할 이미지 번호 관리 변수
emy_x = 0 # 적 캐릭터 표시 위치 x 좌표
emy_y = 0 # 적 캐릭터 표시 위치 y 좌표

def init_battle(): # 전투 개시 준비 함수
    global imgEnemy, emy_num, emy_x, emy_y # 전역 변수 선언
    emy_num = emy_num + 1 # 적 이미지 관리 번호 증가 변수
    if emy_num == 5: # 관리 번호가 5가 되면
        emy_num = 1 # 관리 번호를 1로 되돌림
    imgEnemy = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\enemy" + str(emy_num) + ".png") # 관리 번호에 맞는 적 캐릭터 이미지 로딩
    emy_x = 440 - imgEnemy.get_width() / 2 # 이미지 폭으로 부터 표시 위치(x 좌표) 계산
    emy_y = 560 - imgEnemy.get_height() # 이미지 폭으로 부터 표시 위치(y 좌표) 계산
    
def draw_battle(bg, fnt): # 전투 화면 표시 함수
    bg.blit(imgBtlBG, [0, 0]) # 배경 이미지 표시
    bg.blit(imgEnemy, [emy_x, emy_y]) # 적 캐릭터 이미지 표시
    sur = fnt.render("enemy" + str(emy_num) + ".png", True, WHITE) # 파일명을 표시할 Surface
    bg.blit(sur, [360, 580]) # 문자열을 표시할 Surface를 화면으로 전송
    
def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("전투 개시 처리") # 윈도우창 타이틀 지정
    screen = pygame.display.set_mode((880, 720)) # 윈도우창 화면 초기화
    clock = pygame.time.Clock() # clock 객체 초기화
    font = pygame.font.Font(None, 40) # font 객체 초기화
    
    init_battle() # 전투 개시 준비 함수 호출
    
    while True:
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 윈도우창 닫기
            if event.type == pygame.KEYDOWN: # 키를 누른 이벤트 발생 처리
                if event.key == pygame.K_SPACE: # 스페이스 키를 누른 경우
                    init_battle() # 전투 개시 준비 함수 호출
                    
        draw_battle(screen, font) # 전투 화면 표시
        pygame.display.update() # 화면 업데이트
        clock.tick(5) # 프레임 레이트 지정
        
if __name__ == '__main__':
    main()