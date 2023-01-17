import pygame
import sys

WHITE = (255, 255, 255) # 색정의 : 하얀색
BLACK = (0, 0, 0) # 색정의 : 검은색

def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("첫번째 Pygame") # 윈도우 창에 표시할 타이틀 지정
    screen = pygame.display.set_mode((800, 600)) # 윈도우창에 그릴 화면 초기화
    clock = pygame.time.Clock() # clock 오브젝트 초기화
    font = pygame.font.Font(None, 80) # font 오브젝트 초기화
    tmr = 0 # 시간 관리 변수 선언
    
    while True: # 무한 반복
        tmr = tmr + 1 # tmr 값 1씩 증가
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우 창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 프로그램 종료 
                
        txt = font.render(str(tmr), True, WHITE) # Surface에 문자열 표시
        screen.fill(BLACK) # 지정한 색으로 윈도우창 화면 전체 채움
        screen.blit(txt, [300, 200]) # 문자열 표시한 surface를 화면에 전송
        pygame.display.update() # 화면 업데이트
        clock.tick(10) # Framerate 지정
        
if __name__ == '__main__': # 이 프로그램을 직접 실행 시
    main() # main() 함수 호출