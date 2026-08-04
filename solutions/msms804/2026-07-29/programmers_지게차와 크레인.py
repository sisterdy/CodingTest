from collections import deque

# 1. 패딩을 만들고
# 2. 외부와 이어진 빈공간을 visited배열로 표현한다(bfs돌면서)
def solution(storage, requests):
    answer = 0
    storage = [list(row) for row in storage]
    n = len(storage)
    m = len(storage[0])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 외부와 연결된 .인지 판별하는 visited배열 리턴
    def bfs():
        # 패딩 추가
        board = [["."] * (m + 2)]           

        for row in storage:
            board.append(["."] + row + ["."])

        board.append(["."] * (m + 2))       

        visited = [[False] * (m + 2) for _ in range(n + 2)]

        q = deque([(0, 0)])                
        visited[0][0] = True

        while q:
            x, y = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if not (0 <= ny < m + 2 and 0 <= nx < n + 2):
                    continue

                if visited[nx][ny]:        
                    continue

                if board[nx][ny] == ".":
                    visited[nx][ny] = True
                    q.append((nx, ny))

        return visited

    for request in requests:
        # 크레인
        if len(request) > 1:
            for i in range(n):              
                for j in range(m):          
                    if storage[i][j] == request[0]:
                        storage[i][j] = "."

        # 지게차
        else:
            visited = bfs()

            remove = []

            for i in range(n):
                for j in range(m):

                    if storage[i][j] != request:
                        continue

                    for k in range(4):
                        ny = j + dy[k] + 1     # 패딩을 만들었으므로 +1
                        nx = i + dx[k] + 1      

                        if visited[nx][ny]:
                            remove.append((i, j))
                            break

            for x, y in remove:
                storage[x][y] = "."

    for i in range(n):
        for j in range(m):
            if storage[i][j] != ".":
                answer += 1

    return answer