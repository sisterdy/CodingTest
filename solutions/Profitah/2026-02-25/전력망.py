"""
완전탐색 (전력망을 둘로 나누기)

간선을 하나씩 제거한 뒤 BFS/DFS로 두 네트워크 크기 차이를 계산하는 문제이다.
"""

from collections import defaultdict, deque

def solution(n, wires):
    answer = n

    for i in range(len(wires)):                         # 1. 간선을 하나씩 제거
        graph = defaultdict(list)

        for j in range(len(wires)):                     # 2. 제거한 상태로 그래프 구성
            if i == j:
                continue
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        queue = deque([1])                              # 3. BFS 시작
        visited.add(1)

        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)

        diff = abs(len(visited) - (n - len(visited)))   # 4. 두 네트워크 크기 차이 계산
        answer = min(answer, diff)                      # 5. 최소값 갱신

    return answer