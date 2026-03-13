from collections import deque

def dfs(start_node, n, graph):
    visited = [False] * (n + 1 )
    queue = deque([start_node])
    visited[start_node] = True
    count = 1
    
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count
    
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
        
    min_diff = float('inf')
    
    for u, v in wires:
        graph[u].remove(v)
        graph[v].remove(u)
        
        count_a = dfs(u, n, graph)
        count_b = n - count_a
        
        min_diff = min(min_diff, abs(count_a - count_b))
        
        graph[u].append(v)
        graph[v].append(u)
        
    return min_diff