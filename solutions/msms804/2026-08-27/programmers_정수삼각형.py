# 왼쪽 대각선, 오른쪽 대각선 위의 것들 중 큰 것을 누적시킴
def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j] 
            elif i == j:
                triangle[i][j] += triangle[i - 1][j - 1] 
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
                
    return max(triangle[-1])
