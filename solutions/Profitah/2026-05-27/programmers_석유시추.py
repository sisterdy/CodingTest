"""
[문제 핵심]

석유가 있는 땅(1)들이 서로 연결되어 있을 때,
시추관을 세로로 하나 꽂아 얻을 수 있는
최대 석유량을 구하는 문제.


---

1. BFS를 사용해 연결된 석유 덩어리를 찾는다.

2. BFS 탐색 중:
   - 현재 석유 덩어리 크기
   - 가장 왼쪽 열(min_y)
   - 가장 오른쪽 열(max_y)
   를 함께 구한다.

3. 탐색이 끝나면:
   min_y ~ max_y 범위의 모든 열에
   현재 석유 덩어리 크기를 더해준다.

4. 이렇게 하면:
   각 열(column)마다 뽑을 수 있는
   총 석유량이 result 리스트에 누적된다.

5. 마지막에:
   result 중 가장 큰 값을 반환한다.
"""

from collections import deque


def solution(land):

    # 최종 정답 저장 변수
    answer = 0

    # 땅의 세로 길이
    row_size = len(land)

    # 땅의 가로 길이
    col_size = len(land[0])

    # 상하좌우 이동 방향
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 각 열(column)마다 얻을 수 있는 석유량 저장
    oil_amount_per_col = [0 for _ in range(col_size)]

    # 방문 여부 체크 배열
    visited = [
        [0 for _ in range(col_size)]
        for _ in range(row_size)
    ]

    # BFS 탐색 함수
    def bfs(start_x, start_y):

        # 현재 석유 덩어리 크기
        oil_count = 0

        # 시작 위치 방문 처리
        visited[start_x][start_y] = 1

        # BFS 큐 생성
        queue = deque()

        # 시작 위치 삽입
        queue.append((start_x, start_y))

        # 현재 석유 덩어리가 포함된 최소 열 번호
        min_col = start_y

        # 현재 석유 덩어리가 포함된 최대 열 번호
        max_col = start_y

        # BFS 시작
        while queue:

            # 현재 위치 꺼내기
            current_x, current_y = queue.popleft()

            # 최소 열 번호 갱신
            min_col = min(min_col, current_y)

            # 최대 열 번호 갱신
            max_col = max(max_col, current_y)

            # 현재 석유 칸 개수 증가
            oil_count += 1

            # 4방향 탐색
            for direction in range(4):

                # 다음 x 좌표
                next_x = current_x + dx[direction]

                # 다음 y 좌표
                next_y = current_y + dy[direction]

                # 1. 범위를 벗어나면 건너뛰기
                if (
                    next_x < 0
                    or next_y < 0
                    or next_x >= row_size
                    or next_y >= col_size
                ):
                    continue

                # 2. 아직 방문하지 않았고 석유가 있는 경우
                if (
                    visited[next_x][next_y] == 0
                    and land[next_x][next_y] == 1
                ):

                    # 방문 처리
                    visited[next_x][next_y] = 1

                    # 큐에 추가
                    queue.append((next_x, next_y))

        # 3. 현재 석유 덩어리가 지나가는 모든 열에 석유량 추가
        for col in range(min_col, max_col + 1):
            oil_amount_per_col[col] += oil_count

    # 4. 모든 위치 탐색
    for row in range(row_size):

        for col in range(col_size):

            # 아직 방문하지 않은 석유 칸이면 BFS 시작
            if (
                visited[row][col] == 0
                and land[row][col] == 1
            ):
                bfs(row, col)

    # 가장 많은 석유를 얻을 수 있는 열 선택
    answer = max(oil_amount_per_col)

    return answer