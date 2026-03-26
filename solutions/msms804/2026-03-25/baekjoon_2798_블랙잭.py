# 걍 다 체크하면 될듯?
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
# 오름차순 정렬
nums.sort()

answer = 0

# 조합으로 3개 뽑기
for i in combinations(nums, 3):
    hap = sum(i)
    if hap > M:
        continue
    answer = max(answer, hap)

# 가장 M에 근사한것 뽑기
print(answer)