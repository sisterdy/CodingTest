"""
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았을때, results를 읽고
정확하게 순위를 매길 수 있는 선수의 수를 return 할 것.

※ results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미이다.


"""

def solution(n, results):
    # 내가 이긴 사람들을 저장하는 그래프
    win_graph = [[False] * (n+1) for _ in range(n+1)]
    # 나를 이긴 사람들을 저장하는 그래프
    lose_graph = [[False] * (n+1) for _ in range(n+1)]
    
    # 승패그래프
    for a, b in results:
        win_graph[a][b] = True   
        lose_graph[b][a] = True  
    
    # 플로이드 워셜 함수로 최단거리 측정 
    def floyd(graph):
        for k in range(1, n+1):          # 거쳐 가는 노드
            for i in range(1, n+1):      # 출발 노드
                for j in range(1, n+1):  # 도착 노드
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = True   # 간선
    
    floyd(win_graph)
    floyd(lose_graph)
    
    answer = 0
    
    # 모든 선수에 대해 확인
    for i in range(1, n+1):
        # i가 이긴 사람 수
        win_count = sum(win_graph[i])
        # i가 진 사람 수
        lose_count = sum(lose_graph[i])
        
        # 순위를 매길 수 있는 선수라면 answer에 1추가
        if win_count + lose_count == n - 1:
            answer += 1
    
    return answer