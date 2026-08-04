import sys

# 백트래킹?

N = int(sys.stdin.readline())

visited = [False] * (N + 1)
answer = []

def dfs(depth):
    if depth == N:
        print(*answer)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)

            dfs(depth + 1)

            visited[i] = False
            answer.pop()


dfs(0)