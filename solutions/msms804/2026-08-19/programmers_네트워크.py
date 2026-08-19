# 네트워크 개수를 리턴 => connected component 개수 구하기
# [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# 1번은 자기자신과 연결 , 2번과 연결 / 2번은 1번과 연결, 자기자신과 연결 / 3번은 자기자신과만 연결
def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(x):
        visited[x] = True
        for i in range(n):
            if not visited[i] and computers[x][i] == 1:
                dfs(i)
                
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer