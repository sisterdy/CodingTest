"""
간선 가중치가 있는 방향 그래프
다익스트라

주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램

모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정
"""
import sys, heapq
V, E = map(int, sys.stdin.readline().split(' '))    # V: 정점의 개수, E: 간선의 개수
start_node = int(sys.stdin.readline().strip())

graph = {}
for i in range(1, V + 1):
    graph[i] = []

# u,v,w
# u -> v, 가중치는 w
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split(' '))
    graph[u].append((v, w))

#print(graph)

distances = [float('inf')] * (V + 1)
distances[start_node] = 0
queue = [(0, start_node)]
distance = 0

while queue:
    curr_dist, curr_node = heapq.heappop(queue)

    # 현재 방문 노드가 방문한 적 있는 노드라면 continue
    if distances[curr_node] < curr_dist:
        continue

    for next_node, weight in graph[curr_node]:
        distance = curr_dist + weight

        if distance < distances[next_node]:
            distances[next_node] = distance
            heapq.heappush(queue, (distance, next_node))
            
#print(graph)
for i in range(1, V + 1):
    if distances[i] != float('inf'):
        print(distances[i])
    else:
        print('INF')