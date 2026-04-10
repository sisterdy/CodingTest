import sys
from collections import deque

N = int(sys.stdin.readline()) # 보드의 크기
K = int(sys.stdin.readline()) # 사과의 개수
board = [[0] * N for _ in range(N)]
snake = deque([(0, 0)]) # 뱀의 좌표를 큐에 보관(y, x)
answer = 0 # 몇 초에 끝나는지
turns = [] # 방향 저장

# 사과의 위치
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = 1

L = int(sys.stdin.readline()) # 방향 변환 횟수

# 방향 저장
for _ in range(L):
    t, d = sys.stdin.readline().split() # t초 뒤 방향
    turns.append((int(t), d))

# 방향(우, 하, 좌, 상)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dir = 0
idx = 0

while True:
    answer += 1
    head_y, head_x = snake[0]
    ny = head_y + dy[dir]
    nx = head_x + dx[dir]

    # 벽과 충돌
    if nx < 0 or nx >= N or ny < 0 or ny >= N: 
        break
    # 뱀이 이동하기 전 체크
    if (ny, nx) in snake: 
        break

    if board[ny][nx] == 1: # 뱀이 사과 먹는 경우
        # 뱀의 머리 추가, 꼬리는 내버려두기
        snake.appendleft((ny, nx)) 
        board[ny][nx] = 0 # 보드에서 사과 없애기
    else:
        # 뱀의 머리 추가, 꼬리는 pop
        snake.pop() # 꼬리를 먼저 pop해야함, 왜냐하면 이 자리를 머리가 지나기도 문제가 없기 때문
        snake.appendleft((ny, nx))

    for t, d in turns:
        if t == answer:
            if d == "L": # 왼쪽 90도
                dir = (dir - 1) % 4
            else: # 오른쪽 90도
                dir = (dir + 1) % 4
    

print(answer)