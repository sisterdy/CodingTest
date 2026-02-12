"""
일단 lambda를 이용해서
list[0]의 내림차순, list[0]이 같은 경우 list[1]은 오름차순으로 정렬
근데 이렇게 하면 테스트 케이스를 통과할 수 없다. [50, 40]이 이미 2번째 원소가 돼서 피로도를 40이나 깎아버리기 때문.

어떻게 하면, 최소 피로도를 우선으로 하면서, 소모 피로도를 최소화하는 선택을 해서 최대 탐험 던전 수를 구할 수 있지...?

dungeons를 순회하면서
만약 dungeons[i][0] 이 k보다 낮으면 answer += 1

여기까지 와서 생각해보니 나는 이 문제를 그리디로 풀고 있었다. 이 문제는 그리디로 풀 수 없었다...
dfs 백트래킹을 사용해서 모든 던전 탐험의 경우의 수를 탐색하며 현재 상태에서 도달할 수 있는 최대 깊이를 찾는 게 맞다.

기존 코드: 
def solution(k, dungeons):
    answer = 0
    dungeons.sort(key=lambda x: (-x[0], x[1]))
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            answer += 1
            k -= dungeons[i][1]
            
        else:
            break
    return answer
"""
def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def dfs(current_k, count):
        max_depth = count
        
        for i in range(len(dungeons)):
            req, use = dungeons[i]      # 최소 필요 피로도, 소모 피로도
            
            if not visited[i] and current_k >= req:     # 방문하지 않았고, 최소 필요도를 충족하는 던전이라면
                visited[i] = True
                
                result = dfs(current_k - use, count + 1)    # 재귀
                
                if result > max_depth:  # 재귀에서 반환된 값이 현재 max_depth보다 크다면
                    max_depth = result  # 갱신
                    
                visited[i] = False  # 백트래킹
                
        return max_depth
    
    return dfs(k, 0)