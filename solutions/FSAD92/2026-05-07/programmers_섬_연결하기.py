"""
0: 1, 2
1: 0, 2, 3
2: 0, 1, 3
3: 1, 2

플로이드 워셜? 다익스트라?
그리디? 0부터 제일 비용이 적은 노드만 따라가볼까?
근데 그렇게 하면 0 -> 1-> 3까지는 이어지지만, 0 -> 2로는 이어지지가 않는데...

이 문제는 모든 노드가 연결되도록 하되, 사용된 전체 간선의 합을 최소로 만드는 MST(최소 신장 트리)를 사용해야 한다고 한다.
일단 그리디니까 costs를 비용 순으로 오름차순 정렬을 하고, union-find로 노드끼리 연결해보자
"""

def solution(n, costs):
    answer = 0
    bridge_count = 0
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n)]
    
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        root_a = find(parent, a)
        root_b = find(parent, b)
        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
    
    for island_a, island_b, cost in costs:
        if find(parent, island_a) != find(parent, island_b):
            union(parent, island_a, island_b)
            answer += cost
            bridge_count += 1
            
            if bridge_count == n - 1:
                break
                
    return answer