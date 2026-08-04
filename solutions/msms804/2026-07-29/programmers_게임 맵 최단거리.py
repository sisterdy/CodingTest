# 걍 최단거리 구하는 문제 -> bfs
from collections import deque

def bfs(matrix):
    n = len(matrix)
    m = len(matrix[0])
    q = deque()
    visited = [[0] * m for _ in range(n)]
    
    # 시작점 
    visited[0][0] = 1
    q.append((0, 0))
    
    # 방향벡터
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                # 아직 방문 x, 갈 수 있다면
                if not visited[ny][nx] and matrix[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
        
    # 도달 못하는 경우는 -1 리턴
    return visited[n - 1][m - 1] if visited[n - 1][m - 1] else -1

def solution(maps):
    
    return bfs(maps)