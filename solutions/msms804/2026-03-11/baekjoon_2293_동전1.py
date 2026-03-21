import sys
# 동전수, 가격
n, k = map(int, sys.stdin.readline().split())

coins = []
# dp[k] = k원을 만들 수 있는 가지 수
dp = [0] * (k + 1)
dp[0] = 1

for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)


for coin in coins: # 1 2 5 원
    for i in range(coin, k + 1):
        # i원 만드는 경우의수에 i - coin원을 만드는 경우의수를 추가
        dp[i] += dp[i - coin]

print(dp[k])