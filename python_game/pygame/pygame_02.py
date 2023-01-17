import pygame
import sys

def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("첫번째 이미지 그리기") # 윈도우창 타이틀 이름 설정
    screen = pygame.display.set_mode((640, 360)) # 윈도우창 화면 초기화
    clock = pygame.time.Clock() # clock 오브젝트 초기화
    
    img_bg = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\pg_bg.png") # 배경 이미지 로딩
    img_chara = [pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\pg_chara0.png"), pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\pg_chara1.png")] # 케릭터 이미지 로딩
    img_chara_1 = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\pg_chara0.png")
    img_s = pygame.transform.scale(img_chara_1, [226, 160]) # 이미지 확대 축소
    img_r = pygame.transform.rotate(img_chara_1, 90) # 이미지 회전
    img_rz = pygame.transform.rotozoom(img_chara_1, 90, 3) # 이미지 회전 + 확대 축소
    
    tmr = 0 # 시간 관리 변수 선언
    
    while True: # 무한 반복 
        tmr = tmr + 1 # tmr 값 1씩 증가
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우찬의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 프로그램 종료
            if event.type == pygame.KEYDOWN: # 키를 누르는 이벤트 발생 처리
                if event.key == pygame.K_F1: # 만약 F1 눌렸다면
                    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN) # 풀 스크린 모드로 전환
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE: # 만약 F2 또는 ESC가 눌렸다면
                    screen = pygame.display.set_mode((640, 360)) # 일반 스크린 모드로 전환
            
            x = tmr % 160 # tmr 값을 배경 스크롤 값으로부터 계산
            for i in range(5): # 반복 해서 옆으로 5장 만큼
                screen.blit(img_bg, [i * 160 - x, 0]) # 배경 이미지 표시
                screen.blit(img_chara[tmr % 2], [224, 160]) # 캐릭터를 애니메이션해서 표시
                # screen.blit(img_rz, [224, 160])
                pygame.display.update() # 화면 업데이트
                clock.tick(5) # 프레임 레이트 지정
                
if __name__ == '__main__':
    main()