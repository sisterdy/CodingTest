"""
백트래킹인가 싶었는데 N의 크기가 최대 100,000이라...

DP
카데인 알고리즘?

일단 크게 2가지로 나뉜다
1. 제거 안했을 때
2. 제거 했을 때

제거 안했을 때는 음수가 섞여있으니 2가지로 나뉜다
1. 현재 원소
2. (이전까지의 합 + 현재원소)

제거 했을 때도 2가지로 나뉜다
1. 현재 원소를 제거한 후의 합(즉 이전까지의 합)
2. (어떤 원소를 제거한 이전까지의 합 + 현재 원소)

일단 첫번째 원소는 뭐가 됐든 가장 큰 값이겠지
"""
import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
deleted_dp = [0] * N

# 제거를 안 한 연속합을 저장할 dp, 원소가 하나 제거된 연속합 deleted_dp
dp[0] = nums[0]
deleted_dp[0] = nums[0]
curr_max = nums[0]
max_num = nums[0]

for i in range(1, N):
    # 제거 안 한 경우
    dp[i] = max(nums[i], dp[i-1] + nums[i])

    # 제거 한 경우
    deleted_dp[i] = max(dp[i-1], deleted_dp[i-1] + nums[i]) # 현재 원소(nums[i])를 제거한 경우, 어떤 원소를 제거한 이전까지의 합 + 현재 원소(nums[i])

    curr_max = max(dp[i], deleted_dp[i])
    
    if curr_max > max_num:
        max_num = curr_max

print(max_num)