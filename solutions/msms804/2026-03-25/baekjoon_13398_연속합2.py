import sys
# 연속된 합 중 최댓갑 구하기
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

dp = [[0]*2 for _ in range(n)]
dp[0][0] = nums[0]
dp[0][1] = nums[0]
answer = nums[0]
# dp[i][0] = i번째까지 왔을 때, 삭제 없이 만들 수 잇는 연속 최대합
# dp[i][1] = i번째까지 왔을 때, 하나 삭제하고 만들 수 잇는 연속 최대합

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + nums[i], nums[i]) # 이전합이 음수면 새로시작이 나음
    dp[i][1] = max(dp[i - 1][1] + nums[i], dp[i - 1][0]) # 현재 숫자를 건너뜀
    answer = max(answer, dp[i][0], dp[i][1]) # 최댓값 매번 갱신

print(answer)
