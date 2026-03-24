"""
동전 문제 (DP)

동전들을 이용해 금액 k를 만드는 "경우의 수"를 구하자.

예시
동전 : 1 2 5
목표 : 5

1원을 만드는 방법
1

2원을 만드는 방법
1+1
2

3원을 만드는 방법
1+1+1
1+2

이처럼
각 금액을 만들 수 있는 경우의 수를 누적해서 계산한다.

dp[i] = i원을 만드는 방법의 수

점화식

dp[j] += dp[j - coin]

현재 동전을 사용하면
(j - coin)을 만드는 경우에 coin을 추가해서 j를 만들 수 있다.
"""


n, k = map(int, input().split())  # 동전 종류 수, 목표 금액

coins = []  # 동전 리스트

for i in range(n):
    coins.append(int(input()))

dp = [0] * (k + 1)  # dp[i] = i원을 만드는 방법의 수

dp[0] = 1  # 0원을 만드는 방법은 1가지 (아무것도 사용하지 않음)

# 각 동전을 기준으로 경우의 수 계산
for coin in coins:

    # coin부터 k까지 확인
    for j in range(coin, k + 1):

        # coin을 하나 사용하는 경우 추가
        dp[j] = dp[j] + dp[j - coin]

# k원을 만드는 방법 출력
print(dp[k])