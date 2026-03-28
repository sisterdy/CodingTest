"""
파란색(B)과 흰색(W)으로 이루어진 격자판에서, 각 색깔의 연결된 영역 크기의 제곱합을 구하는 문제.
- 흰색 제곱합 = 아군 병사 위력의 합, 
- 파란색 제곱합 = 적군 병사 위력의 합.
이것들 출력할 것임.


풀이 방식:
- BFS로 연결된 같은 색 영역을 탐색하며 칸의 수를 센다.
- 각 영역 크기를 제곱해서 색깔별로 합산한다.

흐름: 
- 미방문 칸 발견 -> BFS로 연결된 영역 탐색 -> 칸 수 제곱 -> 색깔별 합산
"""

from collections import deque

# 상하좌우 이동 방향 정의 (위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]  # 행 이동 방향
dy = [0, 0, -1, 1]  # 열 이동 방향

"""
    BFS를 이용해 연결된 같은 색깔의 병사 수를 세는 함수
    - x, y: 탐색 시작 좌표
    - color: 탐색할 팀의 색깔 ('W' 또는 'B')
    """

def bfs(x, y, color):

    q = deque()
    q.append((x, y))      # 시작 좌표를 큐에 추가
    visited[x][y] = True  # 시작 칸 방문 처리 (중복 탐색 방지)
    count = 1             # 시작 칸 포함해서 1부터 카운트

    while q:  # 큐가 빌 때까지 (탐색할 칸이 없을 때까지) 반복
        x, y = q.popleft()  # 큐에서 현재 좌표를 꺼내 탐색 시작

        for i in range(4):  # 상하좌우 4방향 순서대로 탐색
            nx = x + dx[i]  # 이동할 행 좌표
            ny = y + dy[i]  # 이동할 열 좌표

            if 0 <= nx < n and 0 <= ny < m:                       # 격자 범위 안이고,
                if not visited[nx][ny] and array[nx][ny] == color: # 미방문 + 같은 색이면
                    visited[nx][ny] = True  # 방문 처리 (중복 탐색 방지)
                    q.append((nx, ny))      # 큐에 추가해서 이 칸도 4방향 탐색 예약
                    count += 1              # 연결된 영역 칸 수 증가

    return count  # 연결된 영역의 전체 칸 수 반환


m, n = map(int, input().split())  # 열 크기(m), 행 크기(n) 입력받기

array = [] # 격자판이 저장될 리스트 초기화
for i in range(n): # n행 만큼 반복해서
    array.append(list(input()))  # array에 각 행의 문자열(=격자판의 한 줄)을 리스트로 변환해서 추가한다. (예: 'BWWB' -> ['B', 'W', 'W', 'B'])

visited = [[False] * m for i in range(n)]  # 방문 여부 체크를 위한 2차원 리스트 (초기값: False)
blue = 0   # 파란 영역 크기 제곱합 누적
white = 0  # 흰 영역 크기 제곱합 누적

for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == 'B':     # 미방문 파란 칸이면
            blue += bfs(i, j, array[i][j]) ** 2          # 영역 칸 수 제곱을 blue에 합산
        elif not visited[i][j] and array[i][j] == 'W':   # 미방문 흰 칸이면
            white += bfs(i, j, array[i][j]) ** 2         # 영역 칸 수 제곱을 white에 합산

print(white, blue)  # 흰색(아군) 제곱합, 파란색(적군) 제곱합 순으로 출력