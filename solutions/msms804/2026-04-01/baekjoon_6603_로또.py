import sys
from itertools import combinations
# 백트래킹? 조합?
# 조합쓰면 끝 아님?
# 흠.. 백트래킹? depth로 도달하면 끝
# 6개 고르기

while True:
    data = list(map(int, sys.stdin.readline().split()))

    # 종료 조건
    if data[0] == 0:
        break

    k = data[0]
    nums = data[1:]

    # way 1 조합 날먹

    for i in combinations(nums, 6):
        # 튜플을 언팩해서 출력
        print(*i)
    
    print()

    


