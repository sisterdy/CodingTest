"""
dp?

dp[i]부터 정의해야겠지
dp[i]는 i번째 상자를 가장 바깥 상자로 포함했을 때, 중첩할 수 있는 상자의 최대 갯수
"""
import sys
n = int(sys.stdin.readline().strip())
boxes = list(map(int, sys.stdin.readline().split(' ')))
#print(boxes)

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j] + 1)
#print(dp)
print(max(dp))