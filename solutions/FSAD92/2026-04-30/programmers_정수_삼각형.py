"""
카테고리가 DP니까 DP를 쓰긴 써야 할텐데...
탑다운? 바텀업?
문제에서는 노골적으로 삼각형의 꼭대기에서 바닥까지 이어지는 경로라고 언급했으니 탑다운 방식으로 풀까?

dp[i][j] = dp[i][j] + 윗줄 대각선 방향 중 더 큰 수치
"""

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:  # 왼쪽 끝일 때
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1: # 오른쪽 끝일 때
                triangle[i][j] += triangle[i-1][j-1]
            else:   
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
                            
    return max(triangle[-1])