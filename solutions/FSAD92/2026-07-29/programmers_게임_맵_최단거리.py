"""
기존 코드는 maps 자체를 수정해 방문 여부와 거리를 기록하는 방식
이번에는 distance 배열에 방문 여부와 최단거리를 따로 저장하는 방식으로 원본맵은 건드리지 말고 풀어보자
"""
from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    # 시작점이나 도착점이 벽이라면 이동 불가
    if maps[0][0] == 0 or maps[rows - 1][cols - 1] == 0:
        return -1

    distance = []

    for _ in range(rows):
        distance.append([-1] * cols)

    # 상, 하, 좌, 우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()

    # 시작점의 거리는 시작 칸을 포함해서 1
    queue.append((0, 0))
    distance[0][0] = 1

    while queue:
        row, col = queue.popleft()

        # BFS에서 도착점을 처음 꺼냈다면 현재 거리가 최단거리
        if row == rows - 1 and col == cols - 1:
            return distance[row][col]

        for row_move, col_move in directions:
            next_row = row + row_move
            next_col = col + col_move

            # 맵 경계
            if next_row < 0 or next_row >= rows:
                continue
            if next_col < 0 or next_col >= cols:
                continue

            # 벽은 통과 불가 
            if maps[next_row][next_col] == 0:
                continue

            # 재방문 방지
            if distance[next_row][next_col] != -1:
                continue

            # 현재 칸까지의 거리에서 1을 더해 기록
            distance[next_row][next_col] = distance[row][col] + 1
            queue.append((next_row, next_col))

    # 상대 팀 진영 도착 불가 시 -1 return
    return -1