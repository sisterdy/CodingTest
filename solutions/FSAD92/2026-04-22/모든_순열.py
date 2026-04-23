"""
브루트포스
백트래킹
dfs?


근데 솔직히 이쯤 되면 permutations를 써도 되지 않을까
"""
import itertools, sys

n = int(input())
#visited = [False] * (n + 1)

arr = [0] * n
for i in range(n):
    arr[i] = i + 1

permutations = list(itertools.permutations(arr))

for i in range(len(permutations)):
    print(*permutations[i])