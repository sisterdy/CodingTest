"""
dfs를 써야 하나?
dfs니까 스택을 써야 하나?
배열 computers를 순회하면서 각 컴퓨터마다 연결된 것들을 dfs로 추가한다...
예를 들어,
0: 0, 1
1: 0, 1
2: 2

그런데 0과 1은 서로 같은 네트워크를 갖고 있으니
총 2개의 네트워크를 반환...

근데 이걸 어떻게 구현하지?
"""
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            dfs(i, n, computers, visited)
            answer += 1     # dfs가 호출됐다? = 새로운 독립된 네트워크를 찾았다는 것.
    
    return answer
    
def dfs(i, n, computers, visited):
    visited[i] = True
        
    for j in range(n):
        if computers[i][j] == 1 and visited[j] == False:
            dfs(j, n, computers, visited)