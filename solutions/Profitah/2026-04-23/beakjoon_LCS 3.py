"""
문제
세 개의 문자열이 주어졌을 때, 세 문자열의 LCS(최장 공통 부분 수열)의 길이를 구하라

구해야 할 것
세 문자열 A, B, C에 모두 공통으로 존재하는 부분 수열 중 가장 긴 것의 길이

풀이 흐름
1. 세 문자열 A, B, C를 입력받음
2. 3차원 dp 테이블 초기화 (dp[i][j][k] = A[0:i], B[0:j], C[0:k]의 LCS 길이)
3. A, B, C를 한 글자씩 비교하며 dp 테이블 채움
    - A[i-1] == B[j-1] == C[k-1] 이면 → 이전 LCS 길이 + 1
    - 하나라도 다르면 → 세 방향(i-1, j-1, k-1) 중 최댓값
4. dp[la][lb][lc] 출력 (세 문자열 전체의 LCS 길이)
"""


A = input().strip() # 문자열 A 입력받기, 양쪽 공백 제거
B = input().strip() # 문자열 B 입력받기, 양쪽 공백 제거
C = input().strip() # 문자열 C 입력받기, 양쪽 공백 제거

length_A = len(A) # 문자열 A의 길이
length_B = len(B) # 문자열 B의 길이
length_C = len(C) # 문자열 C의 길이

dp = [[[0] * (length_C + 1) for _ in range(length_B + 1)] for _ in range(length_A + 1)] # 3차원 배열에 문자열 길이 저장. 0으로 초기화 (Top-down 써도 되긴 할듯 한데, 전 그냥 이거 씀)
for i in range(1, length_A + 1): # 문자열 A의 각 문자에 대해 반복 (1부터 시작하여 dp 인덱스와 맞춤)
    for j in range(1, length_B + 1): # 문자열 B의 각 문자에 대해 반복
        for k in range(1, length_C + 1): # 문자열 C의 각 문자에 대해 반복

            if A[i-1] == B[j-1] == C[k-1]: # A, B, C의 현재 문자들이 모두 같으면
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1 # 이전 LCS 길이에 1 더하기
            else: # 하나라도 다르면
                dp[i][j][k] = max( # A, B, C 중 하나라도 다르면 세 문자열이 일치 했던 이전 상태에서 가장 긴 길었던 것을 선택해
                    dp[i-1][j][k], # A에서 한 글자 뺀 상태의 LCS 길이
                    dp[i][j-1][k], # B에서 한 글자 뺀 상태의 LCS 길이
                    dp[i][j][k-1]  # C에서 한 글자 뺀 상태의 LCS 길이
                )

print(dp[length_A][length_B][length_C]) # 출력