"""
오랜만에 LCS dp 테이블을 그려봤다.
같으면 dp[i][j][k] = ↖️ 방향 값 + 1
다르면 dp[i][j][k] = ⬆️ or ⬅️ 값 중 큰 거

첫 번째와 두 번째 문자열의 LCS를 구하고, 그 결과로 세 번째 문자열과의 LCS를 구해야 하나?

반례
abcdef
defabc
abc

첫 번째와 두 번째 문자열의 LCS는 abc or def
만약 def를 고른다면? 결과는 0이 됨

그래서 이 문제는 3차원 dp로 풀어야 함
"""
import sys

s1, s2, s3 = sys.stdin.read().split()

# dp 테이블 생성
dp = []
for i in range(len(s1) + 1):
    floor = []
    for j in range(len(s2) + 1):
        row = []
        for k in range(len(s3) + 1):
            row.append(0)
        floor.append(row)
    dp.append(floor)

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        for k in range(1, len(s3) + 1):
            
            # 같으면
            if s1[i-1] == s2[j-1] == s3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1

            # 하나라도 다르면
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(s1)][len(s2)][len(s3)])