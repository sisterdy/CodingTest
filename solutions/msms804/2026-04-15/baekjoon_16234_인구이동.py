import sys
from collections import deque

# 인접한 나라 사이에서 인구이동이 발생하니 bfs?
# 매번 칸 하나씩 보면서 만약 visited하지 않았다면 bfs돌기
# 인구이동이 더이상 발생하지 않으면 끝
# bfs로 연합 만들고 -> 인구 재분배 -> 반복
N, L, R = map(int, sys.stdin.readline().split())
countries = []
answer = 0
for i in range(N):
    countries.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    union = [(y, x)]
    total = countries[y][x] # 연합국들의 총 인구수

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                # 인접국과 인구 이동할 수 있는지
                if L <= abs(countries[cur_y][cur_x] - countries[ny][nx]) <= R:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    union.append((ny, nx))
                    total += countries[ny][nx]
    # 연합이 2개 이상이면 인구 이동
    if len(union) > 1:
        new_pop = total // len(union)
        for uy, ux in union:
            countries[uy][ux] = new_pop
        return True
    # 인구 이동 없음
    return False

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j):
                    moved = True

    # 더이상 인구이동이 일어나지 않는 경우
    if not moved:
        break
    
    answer += 1
            

print(answer)