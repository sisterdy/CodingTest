"""
기존 2차원 DP를 1차원 DP로 풀 수 있다...?

dp[x] <- 바로 위쪽 칸의 경로 수
dp[x-1] <- 바로 왼쪽 칸의 경로 수

dp[x]가 왜 바로 위쪽 칸의 경로 수가 될 수 있냐면, 아직 갱신하기 전이기 때문에 이전 '행'의 값이 남아있기 때문...
dp[x-1]은 dp[x]와는 달리 이미 갱신된 상태
"""
def solution(m, n, puddles):
    # 웅덩이s는 튜플 좌표라 그대로 set으로 변환
    puddle_set = set(map(tuple, puddles))
    dp = [0] * (m + 1)
    dp[1] = 1   # 시작점은 (1,1) 밖에 없으니...

    for y in range(1, n + 1):
        for x in range(1, m + 1):

            # 웅덩이 처리
            if (x, y) in puddle_set:
                dp[x] = 0
                continue

            dp[x] = (dp[x] + dp[x - 1]) % 1000000007

    return dp[m]