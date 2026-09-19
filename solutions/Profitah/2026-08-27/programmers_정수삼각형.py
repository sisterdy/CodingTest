"""
2차원리스트, triangle 원본을 직접 수정하는 방식은 입력 데이터를 훼손할 우려가 있음을 깨달음.
-> 원본은 그대로 두고, 별도의 dp 배열을 새로 생성해서 계산하도록 수정함.
"""


def solution(triangle):
    n = len(triangle)  # 삼각형의 전체 층(행) 개수 구하기

    dp = [[0] * len(row) for row in triangle]  # triangle과 동일한 크기의 dp 테이블 생성

    dp[0][0] = triangle[0][0]  
    for i in range(1, n):  
        for j in range(len(triangle[i])): 
            if j == 0:  
                dp[i][j] = dp[i-1][j] + triangle[i][j]  

            elif j == len(triangle[i]) - 1:  
                dp[i][j] = dp[i-1][j-1] + triangle[i][j] 

            else:  
                # 현재 층의 중간 칸인 경우
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]  


    return max(dp[-1])  # dp의 마지막 층(리스트) 중 가장 큰 값이 정답