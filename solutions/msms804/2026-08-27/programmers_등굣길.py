# 최단 경로의 개수 구하기
# [y - 1][x] 의 경로의 수와 [y][x - 1]의 경로의 수를 합친게 [y][x]에 들어감
# dp배열의 값은 그 칸까지 오는 경로의 개수

def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    mod = 1_000_000_007

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: # 이때는 1가지 이므로 덮어씌우면 안되므로 무시
                continue
            if [j, i] in puddles:    # [열, 행]
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

    return dp[n][m]