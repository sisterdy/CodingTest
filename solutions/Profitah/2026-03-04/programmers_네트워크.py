"""
DFS (깊이 우선 탐색) + 그래프

🎯 우리가 구하는 것
→ 전체 네트워크(연결 요소)의 개수
→ 서로 연결된 컴퓨터 그룹이 몇 개인지

📌 문제 해석
- computers[i][j] == 1 이면 i와 j는 연결
- 한 번 연결되면 간접적으로도 모두 같은 네트워크

📌 핵심 전략

1. 방문 여부를 저장할 visited 배열 생성
2. 모든 컴퓨터를 하나씩 확인
3. 아직 방문하지 않은 컴퓨터라면
   → DFS 시작
   → 연결된 모든 컴퓨터를 방문 처리
4. DFS를 한 번 시작할 때마다 네트워크 개수 +1

👉 왜 이렇게?
DFS 한 번은 "하나의 연결 요소"를 전부 탐색한다.
따라서 DFS 시작 횟수 = 네트워크 개수
"""

def solution(n, computers):
    visited = [False] * n  # 각 컴퓨터 방문 여부
    
    def dfs(node):
        visited[node] = True  # 현재 컴퓨터 방문 처리
        
        # 현재 컴퓨터와 연결된 다른 컴퓨터 확인
        for next_node in range(n):
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)  # 연결된 컴퓨터 재귀 탐색
    
    count = 0  # 네트워크 개수
    
    # 모든 컴퓨터를 하나씩 확인
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않았다면
            dfs(i)          # 해당 네트워크 전체 탐색
            count += 1      # 네트워크 하나 발견
    
    return count