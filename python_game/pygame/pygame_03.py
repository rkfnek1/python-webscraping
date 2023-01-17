import pygame
import sys
import math

WHITE = (255, 255, 255) # 색 정의 : 흰색
BLACK = (0, 0, 0) # 색 정의 : 검은색
RED = (255, 0, 0) # 색 정의 : 빨강색
GREEN = (0, 255, 0) # 색 정의 : 초록색
BLUE = (0, 0 , 255) # 색 정의 : 파랑색
GOLD = (255, 216, 0) # 색 정의 : 금색
SILVER = (192, 192, 192) # 색 정의 : 은색
COPPER = (192, 112, 48) # 색 정의 : 동색

def main():
    pygame.init() # pygame 모듈 초기화 
    pygame.display.set_caption("도형 출력") # 윈도우창 타이틀 설정
    screen = pygame.display.set_mode((800, 600)) # 윈도우창 화면 초기화
    clock = pygame.time.Clock() # clock 오브젝트 초기화
    tmr = 0 # 시간관리 변수 선언
    
    while True: # 무한 반복
        tmr = tmr + 1 # tmr 값 1씩 증가
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 윈도우창 종료
                
        screen.fill(BLACK) #  지정한 생으로 윈도우창의 화면을 전체 클리어
        
        '''
        1. Surface는 도형을 표시할 화면
        2. color는 10진수 RGB 값으로 지정
        3. Rect는 사각형의 왼쪽 위 모서리 좌표와 크기, 즉 [x, y, 폭, 높이]를 지정
        4. pointlist는 [[x0, y0], [x1, y1], [x2, y2], ...]와 같이 여러 좌표를 지정
        5. width는 선의 굵기 width=0으로 설정한 것, 아무것도 지정하지 않으면 도형의 내부를 칠함
        6. 원호의 start_angle(시작 각)과 stop_angle(종료 각)은 라디안(radian)으로 지정
        7. lines로 시작점과 완료점을 연결하려면 closed를 True로
        '''
        pygame.draw.line(screen, RED, [0, 0], [100, 200], 10) # 선 표시 - (surface, color, start_pos, end_pos, width=1)
        pygame.draw.lines(screen, BLUE, False, [[50, 300], [150, 400], [50, 500]]) # 선 표시(좌표 연속 지정) - (surface, color, closed, pointlist, width=1)
        
        pygame.draw.rect(screen, RED, [200, 50, 120, 80]) # 사각형 표시 - (surface, color, Rect, width=0)
        pygame.draw.rect(screen, GREEN, [200, 200, 60, 100], 5) # 사각형 표시
        
        pygame.draw.polygon(screen, BLUE, [[250, 400], [200, 500], [300, 500]], 10) # 다각형 표시 - (surface, color, pointlist, width=0)
        pygame.draw.circle(screen, GOLD, [400, 100], 60) # 원표시 - (surface, color, pos, radius, width=0)
        
        pygame.draw.ellipse(screen, SILVER, [400 -80, 300 - 40, 160, 80]) # 타원 표시 - (surface, color, Rect, width=0)
        pygame.draw.ellipse(screen, COPPER, [400 - 40, 500 - 80, 80, 160], 20) # 타원 표시
        
        ang = math.pi * tmr / 36 # 원호 각도 계산
        pygame.draw.arc(screen, BLUE, [600 - 100, 300 - 200, 200, 400], 0, math.pi * 2) # 원호 표시 - (surface, color, Rect, start_angle, stop_angle, width=0)
        pygame.draw.arc(screen, WHITE, [600 - 100, 300 - 200, 200, 400], ang, ang + math.pi / 2, 8) # 원호 표시
        
        pygame.display.update() # 화면 업데이트
        clock.tick(10) # 프레임 레이트 지정

if __name__ == '__main__':
    main()
    