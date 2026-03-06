# dfs? 백트래킹
# 순열로도 풀 수 있는거같음

answer = 0
def dfs(k, cnt, dungeons, visited):
    global answer
    
    # answer을 최대값으로 갱신
    if cnt >= answer:
        answer = cnt
    for i in range(len(dungeons)):
        # 방문하지 않았고, 남은 필요도가 소모필요도보다 높다면
        if not visited[i] and dungeons[i][0] <= k:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False
            
    return

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer