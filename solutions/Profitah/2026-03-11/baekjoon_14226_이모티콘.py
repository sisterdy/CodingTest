"""
이모티콘 문제 (그래프 + BFS)

화면에 S개의 이모티콘을 만들기 위한
최소 연산 횟수를 구하자.

가능한 연산

1. 화면 이모티콘 모두 복사
2. 클립보드 붙여넣기
3. 이모티콘 하나 삭제

상태

(화면 이모티콘 수, 클립보드 이모티콘 수)

이 상태를 그래프로 보고
최소 연산 횟수를 BFS로 탐색한다.
"""

from collections import deque

S = int(input())  # 목표 이모티콘 개수

queue = deque()

queue.append((1, 0, 0))
# (화면 이모티콘, 클립보드, 시간)

visited = set()

visited.add((1, 0))

while queue:

    screen, clip, time = queue.popleft()

    # 목표 도달
    if screen == S:
        print(time)
        break

    # 1 복사
    if (screen, screen) not in visited:

        visited.add((screen, screen))
        queue.append((screen, screen, time + 1))

    # 2 붙여넣기
    if clip > 0 and (screen + clip, clip) not in visited:

        visited.add((screen + clip, clip))
        queue.append((screen + clip, clip, time + 1))

    # 3 삭제
    if screen > 0 and (screen - 1, clip) not in visited:

        visited.add((screen - 1, clip))
        queue.append((screen - 1, clip, time + 1))