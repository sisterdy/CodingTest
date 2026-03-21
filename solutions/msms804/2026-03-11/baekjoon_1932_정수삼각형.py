import sys

n = int(sys.stdin.readline())

triangle = []
dp = [[0] * n for _ in range(n)]

# 입력
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    triangle.append(row)

dp[0][0] = triangle[0][0]

# i는 행, j는 열
for i in range(1, n):
    for j in range(i + 1): # 삼각형 구조이므로
        if j == 0: # 왼쪽
            dp[i][j] = triangle[i][j] + dp[i - 1][j]
        elif i == j: # 오른쪽
            dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(triangle[i][j] + dp[i - 1][j], triangle[i][j] + dp[i - 1][j - 1])

print(max(dp[n - 1]))