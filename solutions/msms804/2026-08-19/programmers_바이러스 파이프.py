# 최대한 많은 배양체 감염시키기
# dfs? 백트래킹?
# 배양체 개수, 감염된 배양체, 파이프정보, 최대행동수

from collections import deque
def solution(n, infection, edges, k):  
    answer = 0
    graph = [[] for _ in range(n + 1)]
    infected = {infection} # 감염된 노드 하나 set에 저장하기
    
    for x, y, type in edges:
        graph[x].append((y, type))
        graph[y].append((x, type))
    
    # 새로 감염된 노드들의 집합 리턴
    def spread(type):
        queue = deque(infected) # 감염된것부터 시작
        visited = set(infected)
        new_infected = []
        
        while queue:
            node = queue.popleft()
            
            for next_node, pipe_type in graph[node]:
                # 타입 불일치시 무시
                if pipe_type != type:
                    continue
                # 방문했다면 무시
                if next_node in visited:
                    continue
                    
                queue.append(next_node)
                visited.add(next_node)
                new_infected.append(next_node)
            
        return new_infected
    
    def dfs(depth):
        nonlocal answer
        answer = max(answer, len(infected))
        if depth == k:
            return
        # 해당노드에서 A, B, C를 각각 돌린다..?
        for type in [1, 2, 3]:
            # 1. type 파이프 열기
            new_infected = spread(type)
            
            # 2. 새로 감염된 애들 추가
            for node in new_infected:
                infected.add(node)
                
            dfs(depth + 1)
            
            # 3. 백트래킹
            for node in new_infected:
                infected.remove(node)
            
    dfs(0) 
    
    return answer