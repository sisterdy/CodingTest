"""
피로도 시스템: 0 이상의 정수로 표현
각 던전마다 최소 필요 피로도, 소모 피로도 존재

하루에 한 번씩 탐험할 수 있는 던전이 여러개, 한 유저가 오늘 이 던전들을 최대한 많이 탐험해야 함
자료구조로 풀만한 문제는 아니고 dfs 백트래킹으로 끝까지 들어가야 할 듯
"""

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    
    def dfs(current_k, depth):
        max_depth = depth
        
        for i in range(n):
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                
                result = dfs(current_k - dungeons[i][1], depth + 1)
                max_depth = max(max_depth, result)
                
                visited[i] = False
                
        return max_depth
    
    return dfs(k, 0)