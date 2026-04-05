import sys
from itertools import combinations
# 백트래킹? 조합?
# 조합쓰면 끝 아님?
# 흠.. 백트래킹? depth가 6에 도달하면 끝
# 6개 고르기

while True:
    data = list(map(int, sys.stdin.readline().split()))

    # 종료 조건
    if data[0] == 0:
        break

    k = data[0]
    nums = data[1:]
    answer = []

    # way 2 백트래킹
    def dfs(start, depth):
        if depth == 6:
            print(*answer)
            return
        
        for i in range(start, k):
            answer.append(nums[i])
            dfs(i + 1, depth + 1)
            answer.pop()

    dfs(0, 0)
    # 띄어 쓰기
    print()

    


