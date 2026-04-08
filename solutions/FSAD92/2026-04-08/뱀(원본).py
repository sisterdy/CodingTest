"""
비얌 시뮬레이션

뱀은 매 초마다 이동. 초기 위치는 (1,1)이며, 오른쪽으로 이동한다.
먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

시간을 관리할 변수 t
머리와 꼬리를 포함한 몸의 좌표를 deque에 저장하고, pop, leftpop으로 머리와 꼬리를 추가/삭제 하는 방향으로 하자.
"""
import sys
from collections import deque

N = int(sys.stdin.readline().strip())   # 보드 크기
K = int(sys.stdin.readline().strip())   # 사과 개수

# 보드 생성. 1-based 인덱스로 간다.
grid = [[0] * (N + 1) for _ in range(N + 1)]

# 사과는 1로 표기
for _ in range(K):
    r, c = map(int, sys.stdin.readline().strip().split())
    grid[r][c] = 1

L = int(sys.stdin.readline().strip())   # 방향 변환 횟수

# 방향 변환 정보 저장. 시간 t를 key로 조회함.
turns = {}
for _ in range(L):
    x, c = sys.stdin.readline().strip().split()
    turns[int(x)] = c

# 방향 벡터: 우, 하, 좌, 상 (시계 방향 배치)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기화
queue = deque()
queue.append((1, 1))
grid[1][1] = 2          # 뱀의 몸통이 존재하는 곳은 2로 표시

direction = 0           # 초기 방향은 오른쪽
t = 0                   # 경과 시간
curr_r, curr_c = 1, 1   # 현재 비얌 머리 위치

# 시뮬 시작
while True:
    t += 1
    
    # 머리를 다음 칸으로 이동
    curr_r += dx[direction]
    curr_c += dy[direction]

    # 벽에 부딪히거나 자기 몸(2)에 부딪히면 종료
    if curr_r < 1 or curr_r > N or curr_c < 1 or curr_c > N or grid[curr_r][curr_c] == 2:
        break

    # 사과 유무 확인 및 꼬리 처리
    if grid[curr_r][curr_c] != 1:
        # 사과가 없으면 꼬리를 한 칸 당김
        tail_r, tail_c = queue.popleft()
        grid[tail_r][tail_c] = 0
        
    # 머리를 보드와 큐에 새로 배치 (사과가 있었으면 꼬리는 그대로 두고 머리만 추가됨)
    queue.append((curr_r, curr_c))
    grid[curr_r][curr_c] = 2

    # 방향 전환 확인
    if t in turns:
        # 모듈로를 이용해서 0,1,2,3 반복하게끔
        if turns[t] == 'D':
            direction = (direction + 1) % 4  # 오른쪽으로 90도 회전
        else:
            direction = (direction - 1) % 4  # 왼쪽으로 90도 회전

print(t)