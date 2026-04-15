"""
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 문제

그래프의 최단거리를 구할 수 있는 다익스트라 알고리즘으로 구할거임.

---

[문제]
시작 정점 K에서 다른 모든 정점까지의 최단 거리 구하기.

[구해야 하는 것]
시작 정점에서 각 정점까지의 최단 거리.
도달할 수 없으면 INF 출력.

[풀이 흐름]
1. 그래프를 인접 리스트로 저장
2. 시작 정점 거리 0으로 설정
3. 우선순위 큐(heap)에 시작 정점 삽입
4. 가장 짧은 거리 정점을 계속 선택
5. 연결된 정점 거리 갱신(relaxation)
6. 모든 정점 최단 거리 출력

[핵심 알고리즘]
다익스트라(Dijkstra) + 우선순위 큐(heapq)
"""
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    INF = float('inf')
    distances = [INF] * (V + 1)
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # 이미 더 짧은 경로가 있으면 skip
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# 실행문
# 정점 수, 간선 수
V, E = map(int, input().split())
# 시작 정점
K = int(input())

# 그래프 초기화
graph = [[] for _ in range(V + 1)]

# 간선 입력 (u, v, w 유지)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distances = dijkstra(K)

# 출력
INF = float('inf')
for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])


# 다익스트라를 양방향 그래프에도 쓸수 있나?

# 대답 : 네, 다익스트라 알고리즘은 양방향 그래프에서도 사용할 수 있습니다.
# 양방향 그래프에서는 각 간선이 두 방향으로 연결되어 있기 때문에, 
# 간선을 입력할 때 양쪽 방향으로 추가해주면 됩니다. 예를 들어, 간선 (u, v, w)가 주어지면, 그래프에 (v, w)도 추가하여 양방향으로 연결하면 됩니다. 
# 이렇게 하면 다익스트라 알고리즘이 양방향 그래프에서도 올바르게 작동하여 최단 경로를 계산할 수 있습니다.


# inf대신 높은 숫자써도 되는데 왜 inf를 쓰는거지?
# inf는 무한대를 나타내는 특별한 값으로, 어떤 수보다도 크다는
# 특성을 가지고 있습니다. 따라서 최단 경로 알고리즘에서 초기 거리를 inf로 설정하면, 실제로 존재하는 경로의 거리보다 항상 크기 때문에, 알고리즘이 올바르게 작동할 수 있습니다.
# 반면에, 높은 숫자를 사용하면, 실제로 존재하는 경로의 거리보다
# 작은 경우가 발생할 수 있어서, 알고리즘이 잘못된 결과를 낼 수 있습니다. 예를 들어, 높은 숫자를 10^9로 설정했을 때, 실제로 존재하는 경로의 거리가 10^9보다 작다면, 알고리즘이 그 경로를 최단 경로로 인식하지 못할 수 있습니다. 따라서 inf를 사용하는 것이 더 안전하고 일반적으로 권장되는 방법입니다.
