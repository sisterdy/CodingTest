"""
고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 맹글어야 한다.
3중 for문으로도 되려나.
"""
import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

candidate = 0
max_sum = 0

for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            sum = cards[i] + cards[j] + cards[k]
            if sum > M:
                break
            max_sum = max(max_sum, sum)

print(max_sum)