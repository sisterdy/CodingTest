import sys

# 세 개의 문자열에서 순서를 유지하면서 가장 긴 공통 부분 문자열을 찾는 문제
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

n, m, l = len(A), len(B), len(C)

dp = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]

# 문자열이 3개이므로 3차원 dp
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, l + 1):
            if A[i - 1] == B[j - 1] == C[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[n][m][l])

