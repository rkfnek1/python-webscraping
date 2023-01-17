import pygame
import sys

WHITE = (255, 255, 255) # 색 정의 : 흰색
BLACK = (0, 0, 0) # 색 정의 : 검은색
RED = (255, 0, 0) # 색 정의 : 빨강색
GREEN = (0, 255, 0) # 색 정의 : 초록색
BLUE = (0, 0 , 255) # 색 정의 : 파랑색

def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("키 입력") # 윈도우창 타이틀 설정
    screen = pygame.display.set_mode((800, 600)) # 윈도우창 화면 초기화
    clack = pygame.time.Clock() # clock 오브젝트 초기화
    font = pygame.font.Font(None, 30) # font 오브젝트 초기화

    while True:
        for evern in pygame.event.get(): # pygame 이벤트 반복 처리
            if evern.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 프로그램 종료
                
        key = pygame.key.get_pressed() # 리스트 key에 모든 키 상태 입력
        txt1 = font.render("UP" + str(key[pygame.K_UP]) + " DOWN" + str(key[pygame.K_DOWN]), True, WHITE, GREEN) # 방향키 상/하 리스트 값을 표시할 surface
        txt2 = font.render("LEFT" + str(key[pygame.K_LEFT]) + " RIGHT" + str(key[pygame.K_RIGHT]), True, WHITE, BLUE) # 방향키 좌/우 리스트 값을 표시할 surface
        txt3 = font.render("SPACE" + str(key[pygame.K_SPACE]) + " ENTER" + str(key[pygame.K_RETURN]), True, WHITE, RED) # 방향키 스페이스/엔터 리스트 값을 표시할 surface
        txt4 = font.render("ESC" + str(key[pygame.K_ESCAPE]) + " LSHIFT" + str(key[pygame.K_LSHIFT]), True, WHITE, RED)
        
        screen.fill(BLACK) # 지정한 색으로 윈도우창 전체 클리어
        screen.blit(txt1, [100, 100]) # 문자열을 표시한 surface를 스크린에 전송(txt1)
        screen.blit(txt2, [100, 130]) # 문자열을 표시한 surface를 스크린에 전송(txt2)
        screen.blit(txt3, [100, 160]) # 문자열을 표시한 surface를 스크린에 전송(txt3)
        screen.blit(txt4, [100, 190])
        pygame.display.update() # 화면 업데이트
        clack.tick(10) # 프레임 레이트 지정
        
if __name__ == '__main__':
    main()