"""
dp?

예제에서
dp[0][0] = 7
dp[1][0] = 10, dp[1][1] = 15

dp[i][j]는 i,j까지 모두 더했을 때 최대값

근데 dp[2][j]부터는 양 끝은 부모 노드가 하나 뿐임
즉 양 끝은 비교할 것 없이 현재 노드 + 유일한 부모 노드 1개

양 끝이 아니면, 현재 노드 + max(부모 노드 2개)
이런 식으로 업데이트하고...

삼각형의 밑면에 닿으면 dp[n-1] 중 max값을 반환하면 되겠다
"""
import sys
input = sys.stdin.readline

n = int(input())

triangle = []

# 입력으로 주어진 삼각형 -> 2차원 배열
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

# dp도 삼각형 모양이랑 똑같이 2차원 배열로 만들기
dp = [[triangle[0][0]]] # 일단 dp[0][0]을 미리 넣어둠

for i in range(1, n):   # 나머지는 0으로 채우기
    row = []
    for j in range(i + 1):
        row.append(0)
    dp.append(row)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 맨 왼쪽 놈
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:    # 맨 오른쪽 놈
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:   # 가운데
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

answer = max(dp[n - 1])
print(answer)