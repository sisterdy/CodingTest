"""
bfs

NxN 그리드 형태

시작 국가는 딱히 주어진 게 없으니 1,1을 시작 국가로 할까.
dxdy테크닉으로 상하좌우를 체크하며 이동.

인접 국가와의 인구 차이가 L이상 R이하인지 체크하고, 해당하는 국가는 리스트에 임시로 보관 후 더 이상 이동할 수 없을 때 한 번에 연합을 이룰까.
"""
import sys
from collections import deque

# N: 땅 크기(N 바이 N), L <= diff <= R
N, L, R = map(int, sys.stdin.readline().split(' '))

# 그리드 생성 및 국가 추가
grid = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

# dxdy 테크니크
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

days = 0

while True:
    # 방문 체크는 매일 인구 이동이 새롭게 일어나므로 while문 안에 배치해서 매번 초기화 함
    visited = []
    for _ in range(N):
        visited_row = [False] * N
        visited.append(visited_row)
        
    is_moved = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                union = [(i, j)]    # 현재 연합에 소속된 국가들의 좌표를 저장
                total_population = grid[i][j]   # 현재 연합의 합산 인구수
                
                # BFS 시작
                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            diff = abs(grid[x][y] - grid[nx][ny])
                            if L <= diff <= R:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                                union.append((nx, ny))
                                total_population += grid[nx][ny]
                
                # 연합된 국가가 2개 이상, 즉 국경선이 한 번이라도 열렸다면
                if len(union) > 1:
                    is_moved = True
                    new_population = total_population // len(union)     # 연합에 있는 모든 국가들의 인구수 갱신
                    for ux, uy in union:
                        grid[ux][uy] = new_population
                        
    if not is_moved:
        break
        
    days += 1

print(days)