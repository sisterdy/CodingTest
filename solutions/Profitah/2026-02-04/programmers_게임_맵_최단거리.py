"""
게임 맵 최단거리 문제는 시작점 (0,0)에서 도착점 (n-1,m-1)까지의
최단 거리를 구하는 문제이다.

모든 이동 비용이 1로 동일하므로,
가까운 칸부터 차례대로 탐색하는 BFS(너비 우선 탐색)를 사용하면
처음 도착하는 순간이 곧 최단 거리이다.

BFS는 큐(Queue)를 사용하여 현재 위치에서 갈 수 있는
다음 위치들을 순서대로 탐색한다.
"""

from collections import deque

def solution(maps):
    n = len(maps)       # 행의 개수
    m = len(maps[0])    # 열의 개수

    queue = deque()
    queue.append((0, 0))   # 시작 위치 (0,0)을 큐에 삽입

    # 상하좌우 이동 방향 정의
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 큐가 빌 때까지 반복 (탐색할 위치가 남아있는 동안)
    while queue:
        x, y = queue.popleft()  # 현재 위치 꺼내기 (가장 먼저 들어온 위치)

        # 현재 위치에서 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 1) 맵 범위 안에 있고
            # 2) 갈 수 있는 길(1)인 경우에만 이동
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이전 칸의 값 + 1 → 거리 누적
                maps[nx][ny] = maps[x][y] + 1
                
                # 다음 탐색을 위해 큐에 삽입
                queue.append((nx, ny))

    # 도착점이 1이면 도달하지 못한 것 → -1 반환
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
