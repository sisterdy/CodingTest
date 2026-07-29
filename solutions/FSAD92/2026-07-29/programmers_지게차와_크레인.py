"""
너무 어려운데...
bfs?
근데 최외곽에 있는 걸 꺼낸 후에는 그 최외곽을 또 어떻게 관리하지?
내부 빈 칸과 최외곽이 만나는 때는 어떡하지?
"""
from collections import deque


def solution(storage, requests):
    row_count = len(storage)
    col_count = len(storage[0])

    EMPTY = '.'

    # 원래 창고의 상하좌우에 빈칸을 한 줄씩 추가한다
    board = []

    for _ in range(row_count + 2):
        board.append([EMPTY] * (col_count + 2))

    # 원래 창고를 패딩 안쪽에 복사하기
    for row in range(row_count):
        for col in range(col_count):
            board[row + 1][col + 1] = storage[row][col]

    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

    remaining_count = row_count * col_count

    def find_forklift_targets(target):
        # 이번 지게차 요청에서 제거할 위치를 저장
        targets = []

        # 요청마다 현재 창고 상태를 기준으로 외부 공간을 다시 탐색
        # 이전에는 막혀 있던 내부 공간이 새롭게 외부와 연결될 수도 있기 때문
        visited = []

        for _ in range(row_count + 2):
            visited.append([False] * (col_count + 2))

        # 외부에서 bfs 시작
        queue = deque()
        queue.append((0, 0))
        visited[0][0] = True

        while queue:
            current_row, current_col = queue.popleft()

            for row_move, col_move in directions:
                next_row = current_row + row_move
                next_col = current_col + col_move

                if next_row < 0 or next_row >= row_count + 2:
                    continue
                if next_col < 0 or next_col >= col_count + 2:
                    continue
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True

                # 빈칸은 외부에서 지게차가 이동할 수 있는 통로
                if board[next_row][next_col] == EMPTY:
                    queue.append((next_row, next_col))

                # 요청한 종류의 컨테이너를 만나면 제거 대상으로 기록. 기록만 한다.
                # 중간에 삭제해버리면 자료구조가 깨져버릴 수도 있기 때문.
                elif board[next_row][next_col] == target:
                    targets.append((next_row, next_col))

                # 다른 종류의 컨테이너는 벽처럼 막혀 있으므로 지나가지 않는다.

        return targets

    def find_crane_targets(target):
        # 크레인은 외부 접근 여부와 상관없이 해당 종류의 컨테이너를 모두 제거
        targets = []

        for row in range(1, row_count + 1):
            for col in range(1, col_count + 1):
                if board[row][col] == target:
                    targets.append((row, col))

        return targets

    for request in requests:
        target = request[0]

        # 한 글자 요청은 지게차다.
        if len(request) == 1:
            removed_positions = find_forklift_targets(target)

        # 두 글자 요청은 크레인이다.
        else:
            removed_positions = find_crane_targets(target)

        # 제거 대상을 모두 찾은 다음 한꺼번에 빈칸으로 바꾼다.
        for row, col in removed_positions:
            board[row][col] = EMPTY

        remaining_count -= len(removed_positions)

    return remaining_count