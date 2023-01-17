import pygame
import sys
import random

BLACK = (255, 255, 255) # 색 정의 : 검은색

MAZE_W = 11 # 미로 가로 방향 길이 (가로 칸 수)
MAZE_H = 9 # 미로 세로 방향 길이 (세로 칸 수)
maze = [] # 미로 데이터 관리 리스트
for y in range(MAZE_H): # 반복
    maze.append([0] * MAZE_W) # append() 명령으로 리스트 초기화

DUNGEON_W = MAZE_W * 3 # 던전 가로 방향 길이 (가로 칸 수)
DUNGEON_H = MAZE_H * 3 # 던전 세로 방향 길이 (세로 칸 수)
dungeon = [] # 던전 데이터 관리 리스트
for y in range(DUNGEON_H): # 반복
    dungeon.append([0] * DUNGEON_W) # append() 명령으로 리스트 초기화

imgWall = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\wall.png") # 던전 벽 이미지 로드
imgFloor = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\floor.png") # 던전 길 이미지 로드
imgPlayer = pygame.image.load(r"C:\Users\Blackstorm_plecios\Desktop\python game\pygame\player.png") # 플레이어 이미지 로드

# 던전 상 위치
pl_x = 4 # 플레이어 이미지 x 좌표
pl_y = 4 # 플레이어 이미지 y 좌표

def make_dungeon(): # 던전 자동 생성 함수
    XP = [0, 1, 0, -1] # 기둥에서 벽을 그리기 위한 값 정의
    YP = [-1, 0, 1, 0] # 기둥에서 벽을 그리기 위한 값 정의

# 테두리를 벽으로 둘러싸고 회색 위치가 벽 이고, 하늘색 위치가 통로이고 내부는 모두 통로
#######################################################################################################
    # 주변 벽 그리기
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W - 1] = 1
        
    # 벽안을 통로로 그리기
    for y in range(1, MAZE_H - 1):
        for x in range(1, MAZE_W - 1):
            maze[y][x] = 0
#######################################################################################################

# 내부에 1칸씩 벽 생성
#######################################################################################################
    # 기둥
    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            maze[y][x] = 1
#######################################################################################################

# 내부에 1칸씩 생성된 벽에서 상하좌우 중 하나의 방향으로 벽을 생성
#######################################################################################################
    # 기둥에서 상하좌우로 벽 생성
    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            d = random.randint(0, 3)
#######################################################################################################            
            
# 가장 왼쪽 열의 벽에서 부터 상하좌우 중 하나에 벽을 생성하고 그다음 열에서 부터는 상,하,우 3방향 중 하나에서 벽 생성
#######################################################################################################            
            if x > 2: # 2번째 열부터 왼쪽으로는 벽을 만들지 않음
                d = random.randint(0, 2)
            maze[y + YP[d]][x + XP[d]] = 1
#######################################################################################################
    
    # 미로에서 던전 생성
    # 전체를 벽으로 만듬
    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            dungeon[y][x] = 9 # dungeon 값을 모두 9(벽)로 설정
    
    # 방과 미로 배치
    for y in range(1, MAZE_H, 1):
        for x in range(1, MAZE_W - 1):
            dx = x * 3 + 1
            dy = y * 3 + 1
            if maze[y][x] == 0: # 만약 미로 데이터 확인, 칸이 통로라면
                if random.randint(0, 99) < 20: # 방 생성 (방 생성 여부를 부작위로 결정)
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            dungeon[dy + ry][dx + rx] = 0 # 3 * 3 칸을 방으로 만듬
                else: # 통로 생성 (방을 만들지 않는 경우 통로 생성)
                    dungeon[dy][dx] = 0 # 3 * 3칸 중앙을 통로로
                    if maze[y - 1][x] == 0: # 만약 미로의 위 칸이 길이라면
                        dungeon[dy - 1][dx] = 0 # 통로를 위로 연장
                    if maze[y + 1][x] == 0: # 만약 미로의 아래 칸이 길이라면
                        dungeon[dy + 1][dx] = 0 # 통로를 아래로 연장
                    if maze[y][x - 1] ==0: # 만약 미로의 왼쪽 칸이 길이라면
                        dungeon[dy][dx - 1] = 0 # 통로를 왼쪽으로 연장
                    if maze[y][x + 1] ==0: # 미로 오른쪽 칸이 길이라면
                        dungeon[dy][dx + 1] = 0 # 통로를 오른쪽으로 연장

def draw_dungeon(bg): # 던전 표시 함수 정의 (던전 표시)
    bg.fill(BLACK) # 지정한 색으로 스크린 전체 클리어
    for y in range(-5, 6):
        for x in range(-5, 6):
            X = (x + 5) * 16 # 화면 표시용 x 좌표 계산
            Y = (y + 5) * 16 # 화면 표시용 y 좌표 계산
            dx = pl_x + x # 던전 칸 x 좌표 계산
            dy = pl_y + y # 던전 칸 y 좌표 계산
            if 0 <= dx and dx < DUNGEON_W and 0 <= dy and dy < DUNGEON_H: # 던전 데이터가 정의된 범위 내에서
                if dungeon[dy][dx] == 0: # 통로면
                    bg.blit(imgFloor, [X, Y]) # 통로 이미지 표시
                if dungeon[dy][dx] == 9: # 벽이면
                    bg.blit(imgWall, [X, Y]) # 벽 이미지 표시
            if x == 0 and y == 0: # 윈도우창 중앙에
                bg.blit(imgPlayer, [X, Y - 8]) # 플레이어 이미지 표시

def move_player(): # 플레이어 이미지 이동 함수 정의 (플레이어 이동)
    global pl_x, pl_y # 필요한 변수를 전역 변수로 선언
    key = pygame.key.get_pressed() # 리스트 key에 모든 키 상태 대입
    if key[pygame.K_UP] == 1: # 방향키 상을 눌렀다면
        if dungeon[pl_y - 1][pl_x] != 9: pl_y = pl_y - 1 # 해당 방향이 벽이 아니면 y 좌표 변경
    if key[pygame.K_DOWN] == 1: # 방향키 하를 눌렀다면
        if dungeon[pl_y + 1][pl_x] !=9: pl_y = pl_y + 1 # 해당 방향이 벽이 아니면 y 좌표 변경
    if key[pygame.K_LEFT] == 1: # 방향키 좌를 눌렀다면
        if dungeon[pl_y][pl_x - 1] !=9: pl_x = pl_x - 1 # 해당 방향이 벽이 아니면 x 좌표 변경
    if key[pygame.K_RIGHT] == 1: # 방향키 우를 눌렀다면
        if dungeon[pl_y][pl_x + 1] !=9: pl_x = pl_x + 1 # 해당 방향이 벽이 아니면 x 좌표 변경

def main():
    pygame.init() # pygame 모듈 초기화
    pygame.display.set_caption("던전내 걷기") # 윈도우창 타이틀 지정
    screen = pygame.display.set_mode((176, 176)) # 윈도우창 화면 초기화
    clock = pygame.time.Clock() # clock 객체 초기화
    
    make_dungeon() # 던전 생성함수 호출
    
    while True:
        for event in pygame.event.get(): # pygame 이벤트 반복 처리
            if event.type == pygame.QUIT: # 만약 윈도우창의 x 버튼을 누른 경우
                pygame.quit() # pygame 모듈 초기화 해제
                sys.exit() # 윈도우창 닫기
            # if event.type == pygame.KEYDOWN: # 키를 누른 이벤트 발생 처리
            #     if event.key == pygame.K_SPACE: # 스페이스 키를 누른 경우
            #         make_dungeon() # 미로 생성 함수 호출
        
        # 확인용 미로 표시            
        # for y in range(MAZE_H): # 2준 반복
        #     for x in range(MAZE_W): # 반복해서 미로 표시
        #         X = x * 48 # 표시할 X 좌표 계산
        #         Y = y * 48 # 표시할 Y 좌표 계산
        #         if maze[y][x] == 0: # 미로 (만약 길이라면)
        #             pygame.draw.rect(screen, CYAN, [X, Y, 48, 48]) # 하늘색 칸으로 채움
        #         if maze[y][x] == 1: # 벽 (만약 벽이라면)
        #             pygame.draw.rect(screen, GRAY, [X, Y, 48, 48]) # 회색으로 칸 채움
        
        # 던전 그리기
        # for y in range(DUNGEON_H):
        #     for x in range(DUNGEON_W):
        #         X = x * 16 + 528 # 표시할 X 좌표 계산
        #         Y = y * 16 # 표시할 Y 좌표 계산
        #         if dungeon[y][x] == 0: # 미로 (만약 길이라면) 
        #             screen.blit(imgFloor, [X, Y]) # 통로 이미지 표시
        #         if dungeon[y][x] == 9: # 벽 (만약 벽이라면)
        #             screen.blit(imgWall, [X, Y]) # 길 이미지 표시
        move_player() # 플레이어 이동 함수 호출
        draw_dungeon(screen) # 던전 표시 함수 호출
        pygame.display.update() # 화면 업데이트
        clock.tick(5) # 프레임 레이트 지정
        
if __name__ == '__main__':
    main()