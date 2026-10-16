"""
구해야하는 것 : n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용

사용한 알고리즘 : 프림알고리즘.

풀이 방식 : 우선순위 큐(최소 힙)를 써서 "지금까지 연결된 섬들에서 뻗어나가는 다리 중 가장 싼 것"을 계속 골라 붙여 나간다.
"""
import heapq as hq

def solution(n, costs):
    answer = 0                                   # 선택한 다리 비용의 총합
    from_to = list(list() for _ in range(n))     # 인접 리스트: from_to[a] = [(이웃 섬, 비용), ...]
    visited = [False] * n                        # 각 섬이 이미 연결(트리에 포함)됐는지 여부
    priority = []                                # 최소 힙: (비용, 도착 섬) 형태로 저장

    # 다리는 양방향이므로 양쪽 섬 모두에 간선 정보를 기록
    for a, b, cost in costs:
        from_to[a].append((b, cost))
        from_to[b].append((a, cost))

    # 0번 섬을 시작점으로 삼음. 시작점은 다리 없이 포함되므로 비용 0
    hq.heappush(priority, (0, 0))

    # 아직 연결 안 된 섬이 하나라도 있으면 반복
    while False in visited:
        # 힙에서 비용이 가장 작은 (비용, 섬)을 꺼냄
        cost, start = hq.heappop(priority)

        # 이미 연결된 섬이면 이 다리는 불필요(사이클) → 버림
        if visited[start]: continue

        # 처음 도달한 섬이므로 연결 확정, 이 다리 비용을 합산
        visited[start] = True
        answer += cost

        # 방금 연결한 섬에서 나가는 다리들을 후보로 힙에 추가
        for end, cost in from_to[start]:
            if visited[end] : continue           # 이미 연결된 섬으로 가는 다리는 제외
            else:
                hq.heappush(priority, (cost, end))

    return answer