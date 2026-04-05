import sys

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수

n = int(sys.stdin.readline()) # 컴퓨터의 수
k = int(sys.stdin.readline()) # 컴퓨터 쌍의 수
visited = [False] * (n + 1)
adj = [[] for _ in range(n + 1)]
answer = 0

for _ in range(k):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(pc):
    global answer
    visited[pc] = True
    answer += 1

    for v in adj[pc]:
        # 인접한 컴퓨터가 방문하지 않았다면 재귀
        if not visited[v]:
            dfs(v)

dfs(1)

# 1번 자기 자신은 제외
print(answer - 1)