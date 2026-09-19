"""
dp로 사칙연산 가능한 모든 경우의 수를 저장.
최솟값을 찾으면 return 

"""

def solution(N, number):
    dp = [set() for i in range(10)]  
    
    for i in range(1, 9): # 최솟값이 8보다 크면 반환값 있으므로 8까지 탐색
        #숫자 N을 i번 사용해서 만들 수 있는 경우(dp[i])에
        #N을 i번 이어붙인 숫자를 하나 추가
        # 숫자를 이어붙이기 - 문자열일때만 가능함으로 문자열로 변환하였다가 다시 정수로 변환하는 것.
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):  
            # i를 j와 (i-j) 두 부분으로 나누는 모든 경우 탐색

            for a in dp[j]:  
                # N을 j번 사용해서 만들 수 있는 값 하나 선택

                for b in dp[i-j]:  
                    # N을 (i-j)번 사용해서 만들 수 있는 값 하나 선택

                    dp[i].add(a + b)  
                    # 두 값을 더한 결과 추가

                    dp[i].add(a - b)  
                    # 두 값을 뺀 결과 추가

                    dp[i].add(a * b)  
                    # 두 값을 곱한 결과 추가

                    if b != 0:  
                        # 0으로 나누는 경우 방지

                        dp[i].add(a // b)  
                        # 정수 나눗셈 결과 추가 (나머지는 버림)
        
        if number in dp[i]:  
            # 현재 i번 사용해서 목표값을 만들 수 있는지 확인

            return i  
            # 만들 수 있다면 최소 사용 횟수이므로 바로 반환
    
    return -1  
    # 1~8번까지 모두 시도했지만 만들 수 없는 경우