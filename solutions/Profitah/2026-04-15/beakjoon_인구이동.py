"""
인구 이동이 며칠 동안 발생했는지 구하는 문제

서로 이동 가능한 나라들을 하나의 연합으로 묶어
dfs로 연결된 칸들을 탐색하고
평균 인구를 구해서 인구 이동을 시킴
연합이 하나도 생기지 않을 때까지 반복
"""

import sys
input = sys.stdin.readline

# 입력
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수
def dfs(x, y):
    stack = [(x, y)] # 탐색할 칸들을 저장하는 스택
    union = [(x, y)] # 연합에 속한 나라들의 좌표를 저장하는 리스트
    visited[x][y] = True

    total = graph[x][y]

    while stack:
        cx, cy = stack.pop()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:

                    diff = abs(graph[cx][cy] - graph[nx][ny])

                    if L <= diff <= R:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

                        union.append((nx, ny))
                        total += graph[nx][ny]

    return union, total


days = 0

while True:

    visited = [[False] * N for _ in range(N)] # 방문 여부 초기화
    moved = False # 인구 이동 여부

    for i in range(N): # 모든 나라 중 
        for j in range(N): 

            if not visited[i][j]: # 방문하지 않은 나라는

                union, total = dfs(i, j) # 깊이 우선 탐색으로 연합과 총 인구 수 구하기 

                # 연합 크기 2 이상일 때만 이동 발생
                if len(union) > 1:

                    avg = total // len(union) # 연합의 평균 인구 수 계산

                    for x, y in union: # 연합에 속한 나라들의 인구 수를 평균으로 갱신
                        graph[x][y] = avg # 인구 이동 발생

                    moved = True # 방문 체크

    if not moved: # 인구 이동이 발생하지 않으면 종료
        break

    days += 1

print(days)



# ---
# 야 이거 bfs로 푸는거랑 dfs로 푸는거랑 뭐가 더 빠르냐?
# 대답 : 둘 다 시간 복잡도는 O(N^2)로 동일하지만, 
# 일반적으로 BFS가 DFS보다 메모리 사용량이 더 많을 수 있습니다.
#  DFS는 재귀 호출이나 스택을 사용하여 탐색하기 때문에 깊이가 깊어질 경우 스택 오버플로우가 발생할 수 있지만, 
# BFS는 큐를 사용하여 탐색하기 때문에 메모리 사용량이 더 안정적입니다. 따라서, 이 문제에서는 BFS가 더 적합할 수 있습니다.