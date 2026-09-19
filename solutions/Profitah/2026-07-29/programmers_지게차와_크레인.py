"""
컨테이너 격자판에서 지게차(1글자 명령)는 외부와 연결된(접해 있는) 컨테이너만 꺼낼 수 있고, 

크레인(2글자 명령)은 외부 연결 여부와 상관없이 해당 종류의 모든 컨테이너를 꺼냅니다. 

모든 요청을 처리한 후 남은 컨테이너의 개수를 구하는 문제입니다. 

"""



from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    # 1. 외곽에 1칸씩 패딩을 두어 (n+2) x (m+2) 격자 생성
    # '.' : 빈 공간(공기), 알파벳 : 컨테이너
    grid = [['.'] * (m + 2) for _ in range(n + 2)]
    for r in range(n):
        for c in range(m):
            grid[r + 1][c + 1] = storage[r][c]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for req in requests:
        target = req[0]

        # [크레인 명령] 2글자: 해당 알파벳 전체 제거
        if len(req) == 2:
            for r in range(1, n + 1):
                for c in range(1, m + 1):
                    if grid[r][c] == target:
                        grid[r][c] = '.'
        
        # [지게차 명령] 1글자: 외부 공기와 맞닿은 컨테이너만 제거
        else:
            # BFS로 (0,0)부터 탐색하여 현재 외부 공기 영역 파악
            visited = [[False] * (m + 2) for _ in range(n + 2)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            
            to_remove = []

            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        
                        # 빈 공간이면 계속해서 공기 영역 확장
                        if grid[nx][ny] == '.':
                            queue.append((nx, ny))
                        # 외부 공기와 접한 타겟 컨테이너를 찾으면 제거 목록에 추가
                        elif grid[nx][ny] == target:
                            to_remove.append((nx, ny))

            # 탐색 완료 후 외부와 접한 타겟 컨테이너 일괄 제거
            for r, c in to_remove:
                grid[r][c] = '.'

    # 2. 남은 컨테이너 개수 세기
    remaining = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if grid[r][c] != '.':
                remaining += 1

    return remaining