import sys

# 걍 dfs, connected component 문제? 

N, M = map(int, sys.stdin.readline().split()) # 가로, 세로

soldiers = [list(sys.stdin.readline().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
white = 0
blue = 0

def dfs(y, x, color):
    visited[y][x] = True
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < M and 0 <= nx < N:
            if not visited[ny][nx] and soldiers[ny][nx] == color:
                cnt += dfs(ny, nx, color) # cnt 누적

    return cnt


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            size = dfs(i, j, soldiers[i][j])
            if soldiers[i][j] == "W":
                white += size * size
            else:
                blue += size * size

print(white, blue)