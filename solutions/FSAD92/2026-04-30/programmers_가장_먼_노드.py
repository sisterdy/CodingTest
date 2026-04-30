"""
문제를 다르게 생각하면,
시작 노드에서 특정 노드까지 가는 최단 경로가 가장 긴 노드들을 찾으면 된다.

가중치가 없는 그래프에서 bfs를 적용하면 시작점에서 각 노드까지의 거리는 최단 경로를 보장하므로 bfs를 이용해보자.

graph 탐색에 쓰일 graph도 있어야 하고,
각 노드마다 '시작점으로부터의 거리'를 저장할 distance라는 리스트도 있어야 할 것 같다.

graph를 만들 떄는 양방향 노드를 저장하고
distance[neighbor] = distance[curr] + 1의 로직을 이용해 채워나가면 될 것 같다.

테스트 케이스처럼 가장 멀리 떨어진 노드가 여러 개일 수 있을텐데, 이건 어떻게 구한담?
"""

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1] * (n + 1)
    distance[1] = 0
    queue = deque([1])
    
    while queue:
        curr = queue.popleft()
        
        for neighbor in graph[curr]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[curr] + 1
                queue.append(neighbor)
    
    max_dist = max(distance)
    answer = 0
    
    for i in range(len(distance)):
        if distance[i] == max_dist:
            answer += 1
    #return distance.count(max_dist)
    return answer