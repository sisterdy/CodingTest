"""
화면 1
클립보드 0

화면 1
클립보드 1
화면 2 -> 1

화면 1
클립보드 1
화면 2 -> 1

엥???

손도 못댔음...
"""
from collections import deque
import sys

input = sys.stdin.readline

S = int(input())

# 최적 경로에서 S를 훨씬 넘게 갈 이유는 거의 없으므로 2*S까지만 탐색
MAX = 2 * S

# visited[화면 개수][클립보드 개수] 상태를 이미 큐에 넣어봤는지 체크함
# visited[1][2] 체크하는 그런 로직이죠

visited = []
for _ in range(MAX + 1):
    row = []
    for _ in range(MAX + 1):
        row.append(False)
    visited.append(row)

# 큐에 들어갈 원소는 3가지 상태를 동시에 관리함
# 큐 원소: (화면 이모티콘 수, 클립보드 이모티콘 수, 시간)
queue = deque()
queue.append((1, 0, 0))

visited[1][0] = True    # 영선이가 이미 화면에 이모티콘 1개 입력한 것

while queue:
    screen, clip, time = queue.popleft()

    # 화면 개수가 목표에 도달하면, 그게 곧 최소 시간
    if screen == S:
        print(time)
        break

    # 화면의 모든 이모티콘을 클립보드에 복사. (screen, screen)
    if not visited[screen][screen]:
        visited[screen][screen] = True
        queue.append((screen, screen, time + 1))

    # 붙여넣기(클립보드가 비어 있지 않을 떄). (screen + clip, clip)
    if clip > 0 and screen + clip <= MAX:
        if not visited[screen + clip][clip]:
            visited[screen + clip][clip] = True
            queue.append((screen + clip, clip, time + 1))

    # 삭제(화면에 적어도 1개 존재). (screen - 1, clip)
    if screen > 0:
        if not visited[screen - 1][clip]:
            visited[screen - 1][clip] = True
            queue.append((screen - 1, clip, time + 1))