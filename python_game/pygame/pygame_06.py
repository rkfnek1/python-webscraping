import pygame
import sys

WHITE = (255, 255, 255) # 색 정의 : 흰색
BLACK = (0, 0, 0) # 색 정의 : 검은색
CYAN = (0, 255, 255) # 색 정의 : 하늘색

def main():
    pygame.init() # pygame 모듈 초기화 
    pygame.display.set_caption("사운드 출력") # 윈도우창 타이틀 지정
    screen = pygame.display.set_mode((900, 600)) # 윈도우창 화면 초기화
    clock = pygame.time.Clock() # clock 오브젝트 초기화
    font = pygame.font.Font(None, 60) # font 오브젝트 초기화
    
    try: # 예외처리
        pygame.mixer.music.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\pygame_bgm.ogg") # BGM 로딩
        se = pygame.mixer.Sound(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\pygame_se.ogg") #  sc 로딩
    except: # 예외 발생 시
        print("ogg 파일이 맞지 않거나, 오디오 기기와 접속되어 있지 않습니다.") # 메시지 출력
        
    while True:
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 프로그램 종료
                
        key = pygame.key.get_pressed() # 리스트 key에 모든 키 상태 대입
        if key[pygame.K_p] == 1: # 만약 p키를 눌렀다면
            if pygame.mixer.music.get_busy() == False: # 만약 bgm이 정지 중이라면
                pygame.mixer.music.play(-1) # bgm 재생
        if key[pygame.K_s] == 1: # 만약 s키를 눌렀다면
            if pygame.mixer.music.get_busy() == True: # 만약 bgm이 재생 중이라면
                pygame.mixer.music.stop() # bgm 정지
        if key[pygame.K_SPACE] == 1: # 만약 SPACE키를 눌렀다면
            se.play() # SE 재생
            
        pos = pygame.mixer.music.get_pos() # 변수에 BGM 재생 시간 대입
        txt1 = font.render("BGM pos" + str(pos), True, WHITE) # 재생 시간을 표시할 Surface
        txt2 = font.render("[P]lay bgm : [S]top bgm : [SPACE] se", True, CYAN) # 조작 방법을 표시할 surface
        
        screen.fill(BLACK) # 지정한 색으로 스크린 전체 클리어
        screen.blit(txt1, [100, 100]) # 스크린에 문자열을 표시한 surface 전송 (txt1)
        screen.blit(txt2, [100, 200]) # 스크린에 문자열을 표시한 surface 전송 (txt2)
        pygame.display.update() # 화면 업데이트
        clock.tick(10) # 프레임 레이트 지정
        
if __name__ == '__main__':
    main()