"""
[구해야 할 것]
- 연결된 컴퓨터 네트워크(연결 요소, Connected Component)의 총 개수

[풀이 흐름]
1. 모든 노드의 방문 여부를 관리할 visited 배열 초기화
2. DFS를 이용해 한 노드와 직간접적으로 연결된 모든 노드를 연속 방문 처리
3. 0번부터 n-1번 노드까지 순회하며 미방문 노드 발견 시 DFS 실행 및 네트워크 개수(count) +1
"""

def solution(n, computers):
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        
        # 현재 노드와 연결되어 있고, 아직 방문하지 않은 이웃 노드로 이동
        for next_node in range(n):
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)

    count = 0

    # 미방문 노드를 만날 때마다 새로운 네트워크 개수 증가 및 연결 노드 전체 방문
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count