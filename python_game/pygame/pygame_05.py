import pygame
import sys

BLACK = (0, 0, 0) # 색 정의 : 흰색
LBLUE = (0, 192, 255) # 색 정의 : 하늘색
PINK = (255, 0, 224) # 색 정의 : 분홍색

def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("마우스 입력") # 윈도우창 타이틀 지정
    screen = pygame.display.set_mode((800, 600)) # 왼도우창 화면 초기화
    clock = pygame.time.Clock() # clock 오브젝트 초기화
    font = pygame.font.Font(None, 60) # font 오브젝트 초기화
    
    while True:
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 프로그램 종료
        
        mouseX, mouseY = pygame.mouse.get_pos() # 변수에 마우스 포인트 좌표 대입
        txt1 = font.render("{},{}".format(mouseX, mouseY), True, LBLUE) # 좌표 값을 표시할 Surface
        mBtn1, mBtn2, mBtn3 = pygame.mouse.get_pressed() # 변수에 마우스 버튼 상태 대입
        txt2 = font.render("{},{},{}".format(mBtn1, mBtn2, mBtn3), True, PINK) # 마우스 버튼 상태를 표시할 Surface
        
        screen.fill(BLACK) # 지정한 색으로 윈도우창 화면 클리어
        screen.blit(txt1, [100, 100]) # 윈도우창에 문자열을 표시한 Surface 전송 (txt1)
        screen.blit(txt2, [100, 200]) # 윈도우창에 문자열을 표시한 Surface 전송 (txt2)
        pygame.display.update() # 화면 업데이트
        clock.tick(10) # 프레임 플레이트 지정
        
if __name__ == '__main__':
    main()