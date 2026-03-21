import sys
from collections import deque

S = int(sys.stdin.readline())
visited = [[0] * 1001 for _ in range(1001)]

def bfs():
    q = deque()
    q.append((1, 0))
    while q:
        screen, clipboard = q.popleft()

        if screen == S:
            print(visited[screen][clipboard])
            break

        # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
        if not visited[screen][screen]:
            visited[screen][screen] += visited[screen][clipboard] + 1
            q.append((screen, screen))

        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 
        if clipboard > 0 and screen + clipboard <= 1000:
            if not visited[screen + clipboard][clipboard]:
                visited[screen + clipboard][clipboard] += visited[screen][clipboard] + 1
                q.append((screen + clipboard, clipboard))

        # 3. 화면에 있는 이모티콘 중 하나를 삭제
        if screen > 0:
            if not visited[screen - 1][clipboard]:
                visited[screen - 1][clipboard] += visited[screen][clipboard] + 1
                q.append((screen - 1, clipboard))

bfs()