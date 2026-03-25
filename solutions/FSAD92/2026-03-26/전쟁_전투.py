"""
bfs
cluster 크기를 구하는데 cluster가 여러 개 있을 수 있겠다.

일단 2중 for문으로 돌면서 w인지 b인지 체크하고 bfs 들어가는 거로.
굳이 visited는 만들지 않고 방문한 원소는 0으로 바꾸기.
"""
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maps = []
for _ in range(M):
    row = list(sys.stdin.readline().strip())
    maps.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

w_sizes = []
b_sizes = []

for y in range(M):
    for x in range(N):
        if maps[y][x] in ('W', 'B'):
            target = maps[y][x] # 어떤 클러스터를 찾아야 할지 기준이 되어줄 target 변수
            cluster_size = 0
            queue = deque([(y,x)])

            maps[y][x] = 0  # 방문 체크

            while queue:
                curr_y, curr_x = queue.popleft()
                cluster_size += 1

                for i in range(4):
                    ny, nx = curr_y + dy[i], curr_x + dx[i]

                    if 0 <= ny < M and 0 <= nx < N:
                        if maps[ny][nx] == target:
                            maps[ny][nx] = 0
                            queue.append((ny, nx))

            if target == 'W':
                w_sizes.append(cluster_size)
            else:
                b_sizes.append(cluster_size)
                
for i in range(len(w_sizes)):
    w_sizes[i] *= w_sizes[i]

for i in range(len(b_sizes)):
    b_sizes[i] *= b_sizes[i]

print(sum(w_sizes), sum(b_sizes))