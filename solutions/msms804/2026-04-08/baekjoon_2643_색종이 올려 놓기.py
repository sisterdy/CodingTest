import sys

N = int(sys.stdin.readline())

papers = []

for _ in range(N):
    w, h = map(int, sys.stdin.readline().split())
    papers.append( (max(w,h), min(w,h)) )

papers.sort()

# i번째 색종이를 맨 위로 했을 때 쌓을 수 있는 최대 개수
dp = [1] * N

for i in range(N):
    for j in range(i):
        if papers[i][0] >= papers[j][0] and papers[i][1] >= papers[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(max(dp))