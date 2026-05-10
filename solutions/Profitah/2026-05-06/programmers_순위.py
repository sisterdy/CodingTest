"""
구해야할 것 : 순위를 확정할 수 있는 선수의 수
순위를 확정할 수 있는 선수 = 나머지 모든 선수와 승/패 관계가 명확한 선수
내가 이긴 사람 수 + 나를 이긴 사람 수 = n-1 이면 순위 확정


BFS + 역방향 그래프
순위를 확정할 수 있는 선수 = 나머지 모든 선수와 승/패 관계가 명확한 선수.
→ 내가 이긴 사람 수 + 나를 이긴 사람 수 = n-1 이면 순위 확정.

win_graph  : 내가 이긴 사람들을 추적 (순방향 인접리스트)
lose_graph : 나를 이긴 사람들을 추적 (역방향 인접리스트)
이긴 관계와 진 관계를 각각 그래프로 만든 뒤, BFS로 도달 가능한 선수 수를 센다
순위가 확정된 선수들의 총 개수 반환
"""

from collections import deque

def solution(n, results):
    # 인접 리스트로 순방향/역방향 그래프 초기화
    # 내가 이긴 사람들을 저장하는 순방향 그래프
    win_graph = [[] for _ in range(n+1)]
    # 나를 이긴 사람들을 저장하는 역방향 그래프
    lose_graph = [[] for _ in range(n+1)]

    # 경기 결과를 바탕으로 양방향 그래프 구성
    for a, b in results:
        win_graph[a].append(b)   # a → b : a가 b를 이김 (순방향)
        lose_graph[b].append(a)  # b ← a : b는 a에게 짐 (역방향)

    def bfs(start, graph):
        # BFS: 특정 노드에서 출발해 도달 가능한 노드 수를 반환
        visited = [False] * (n+1)
        queue = deque([start])
        visited[start] = True
        count = 0

        while queue:
            cur = queue.popleft()

            for next_node in graph[cur]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1  # 도달 가능한 노드 수 누적

        return count

    answer = 0

    for i in range(1, n+1):
        # win_graph BFS: i가 직·간접적으로 이긴 선수 수
        win_count = bfs(i, win_graph)
        # lose_graph BFS: i를 직·간접적으로 이긴 선수 수
        lose_count = bfs(i, lose_graph)

        # 승/패 관계가 확인된 선수 수의 합이 n-1이면 순위 확정
        if win_count + lose_count == n - 1:
            answer += 1

    return answer