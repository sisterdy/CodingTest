"""
구해야할 것 : 1번 노드에서 가장 멀리 떨어진 노드까지의 거리를 구하고, 그 최단 거리를 가지는 노드의 개수

사용한 알고리즘 : BFS(너비 우선 탐색)
"""

from collections import defaultdict


def bfs(graph, start, distances):
    q = [start]
    visited = set([start])

    while len(q) > 0:
        current = q.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:  # 방문 안 한 노드면
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1  # 거리 = 이전 노드 거리 + 1


def solution(n, edge):
    # 그래프 만들기 (양방향)
    graph = defaultdict(list)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # 1번 노드에서 bfs 탐색하며 각 노드까지의 거리 구하기
    distances = [0] * (n + 1)
    bfs(graph, 1, distances)

    max_distance = max(distances)  # 가장 먼 거리
    answer = 0

    for distance in distances:  # 가장 먼 거리와 같은 노드 개수 세기
        if distance == max_distance:
            answer += 1

    return answer