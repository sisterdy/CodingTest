import sys

n = int(sys.stdin.readline())

boxes = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

# boxes들을 돌면서 해당 박스보다 앞에 있는것들이 더 크기가 작으면 +1?
for i in range(n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))