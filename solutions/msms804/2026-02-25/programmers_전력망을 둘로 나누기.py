from collections import deque

def bfs(start, visited, tree):
    # 송전탑 개수
    cnt = 1
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
        for i in tree[v]:
            if visited[i]:
                continue
            q.append(i)
            cnt += 1
            visited[i] = True
    return cnt
    
    
def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n + 1)]
    
    # 트리 만들기
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
        
    # 간선 끊기
    for start, split in wires:
        visited = [False] * (n + 1)
        visited[split] = True
        cnt = bfs(start, visited, tree)
        
        # 더 차이가 적은것으로 갱신
        if abs(cnt - (n - cnt)) < answer:
            answer = abs(cnt - (n - cnt))
        
    return answer