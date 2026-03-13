"""
경우의 수를 출력
동전 재사용 가능
n = 동전 종류(동전 가치는 전부 다름)
k = 목표 값

냅색?

dp[i][x] = 앞에서부터 i번째 동전까지 사용해 x원을 만드는 방법의 수
모든 동전을 사용해야 하는 건 아니라고 한다(지선생님)

그렇다면 dp[i][x]는 i번째 동전을 안 쓰는 경우 + 쓰는 경우

근데 이렇게 하니까 메모리 초과 뜸...

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []  # 동전 가치 리스트
for _ in range(n):
    coins.append(int(input()))

dp = []
for i in range(n):
    row = []
    for x in range(k + 1):
        row.append(0)
    dp.append(row)

for i in range(n):
    dp[i][0] = 1

# 첫 번째 동전만 사용하는 경우 [2,3,5] 케이스에서 (2,2,2,2,2)
first_coin = coins[0]
for x in range(1, k + 1):
    if x % first_coin == 0:
        dp[0][x] = 1

# 1번 동전부터 n-1번 동전까지
for i in range(1, n):
    coin = coins[i]
    for x in range(1, k + 1):
        # i번째 동전을 안 쓰는 경우
        dp[i][x] = dp[i - 1][x]

        # 쓰는 경우
        if x >= coin:
            dp[i][x] += dp[i][x - coin]

print(dp[n - 1][k])

2차원 배열로 하면 메모리 초과가 뜨나보다.
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for x in range(coin, k + 1):
        dp[x] += dp[x - coin]

print(dp[k])