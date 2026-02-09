"""
bfs? deque.
일단 (1,1) 기준 동서남북으로 갈 수 있는 후보를 찾아야 한다 -> dx, dy
하지만 행이 1일 때는 -1, n일 때는 +1을 할 수 없고
똑같이 열이 1일 때는 -1, n일 떄는 +1을 할 수 없다. <- 맵 이탈 방지 조건
그리고 maps[i][j] == 1 인 조건이어야 한다. 왜냐면 벽을 0으로 표현했기 때문.
visited를 따로 만들기보다는 도착지점까지 가면서 각 타일마다 +1을 하면서 가자.
"""
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 방향 벡터 설정
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        curr = maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = curr + 1
                queue.append((nx, ny))
    
    answer = maps[n-1][m-1]
    if n == 1 and m == 1:    # 만약 1x1짜리 맵이면
        return 1 if maps[0][0] == 1 else -1     # (1,1)이 벽이면 -1, 벽이 아니면 1을 리턴
    
    return answer if answer > 1 else -1   # answer가 1보다 커야 방문했다는 뜻. 모든 탐색이 끝났는데도 목적지에 도달하지 못했다면 -1