import sys
import heapq
# 정점, 간선 개수
V, E = map(int , sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]

def dijkstra(graph, start):
    INF = float('inf')
    dist = [INF] * (V + 1) # 시작점부터 해당 정점까지의 최단거리
    dist[start] = 0
    pq = [(0, start)] # (거리, 정점)

    while pq:
        # here_cost : 시작점 ~ 현재 노드 u까지의 비용(거리)
        # 현재까지 가장 짧은 거리의 노드 꺼냄
        here_cost, u = heapq.heappop(pq)

        # 이미 더 짧은 경로가 dist[u]에 있다면 무시
        if dist[u] < here_cost:
            continue

        # 현재 노드 u에서 갈 수 있는 모든 인접 노드 탐색
        for v, weight in graph[u]:
            # u를 거쳐 v로 가는 새로운 경로 비용
            new_cost = here_cost + weight

            # 최단거리 갱신
            if new_cost < dist[v]:
                dist[v] = new_cost
                # 후보 추가 
                heapq.heappush(pq, (new_cost, v))

    return dist

for _ in range(E):
    u, v, w = map(int , sys.stdin.readline().split())
    graph[u].append((v, w)) # 방향 그래프


dist = dijkstra(graph, start)

for i in range(1, V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])