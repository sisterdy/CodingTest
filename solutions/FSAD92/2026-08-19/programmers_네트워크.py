"""
기존 문제는 dfs
이번에는 bfs를 써서 한 네트워크를 끝까지 탐색하는 방식
"""
from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0

    # 모든 컴퓨터를 하나씩 확인
    for start in range(n):
        # 이미 다른 BFS에서 방문한 컴퓨터 = 기존 네트워크에 속해 있음
        if visited[start]:
            continue

        # 아직 방문하지 않은 컴퓨터를 발견 = 신규 네트워크 발견
        answer += 1

        queue = deque([start])
        visited[start] = True

        # 현재 네트워크에 속한 컴퓨터를 BFS로 모두 방문
        while queue:
            current = queue.popleft()

            for next_computer in range(n):
                # 현재 컴퓨터와 연결되어 있고 아직 방문하지 않은 컴퓨터라면 BFS에 추가
                if (
                    computers[current][next_computer] == 1
                    and not visited[next_computer]
                ):
                    visited[next_computer] = True
                    queue.append(next_computer)

    return answer