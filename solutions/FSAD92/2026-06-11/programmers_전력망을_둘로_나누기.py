"""
기존 문제는 bfs로 전선을 하나씩 끊고 계산하고 복구했었음

전력망은 트리 형태로 연결되어 있다고 하니 이번에는 루트 노드를 기준으로 부모,자식 관계로 만들어서
각 노드 밑에 몇 개의 노드가 있는지 미리 카운트 해놓기

즉 송전탑 개수의 차이 = n - 자식 트리의 크기
"""
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    answer = float('inf')
    
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
        
    parent = [0] * (n + 1)
    childtree_size = [1] * (n + 1)      # 각 노드는 자기 자신을 포함하므로 기본 크기가 1(like 리프 노드)
    
    def dfs(node, prev):
        parent[node] = prev     # 현재 노드의 부모를 기록
        
        for next_node in graph[node]:
            if next_node == prev:
                continue
                
            dfs(next_node, node)
            childtree_size[node] += childtree_size[next_node]
            
    dfs(1, 0)
    
    for u, v in wires:
        if parent[u] == v:
            child = u
        else:
            child = v
        
        count_a = childtree_size[child]
        count_b = n - count_a
        
        answer = min(answer, abs(count_a - count_b))    # 최소 차이 갱신

    return answer
