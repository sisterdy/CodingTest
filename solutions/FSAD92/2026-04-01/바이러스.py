"""
bfs
1과 연결된 것만?

다 작성하고 보니 딱히 함수를 작성하지 않아도 됐을 듯
"""
import sys
from collections import deque

com_num = int(sys.stdin.readline().strip())
graph_num = int(sys.stdin.readline().strip())

graph = []
for i in range(com_num + 1):
    graph.append([])

for _ in range(graph_num):
    u, v = map(int, sys.stdin.readline().split())
    
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
visited = [False] * (com_num + 1)

def bfs(start_computer, graph, visited):
    graph_size = 0
    queue.append(start_computer)
    visited[start_computer] = True

    while queue:
        curr = queue.popleft()
        graph_size += 1

        for next_node in graph[curr]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
    return print(graph_size - 1)        # 1번 컴퓨터는 제외!

bfs(1, graph, visited)