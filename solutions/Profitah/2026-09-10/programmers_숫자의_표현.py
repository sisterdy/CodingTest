"""
구해야하는 것 : n을 만들 수 있는 누적합의 개수

사용한 알고리즘 : 브루트포스, 완전탐색

"""

def solution(n):
    result = 0 
    
    # 시작 숫자를 1부터 n까지 반복
    for i in range(1, n + 1):
        total = 0
        # i부터 시작해서 n범위까지 연속된 숫자를 더해감
        for j in range(i, n + 1):
            total += j
            if total == n: # 누적합으로 n이 만들어진다는 것을 확인하면
                result += 1 #result에 +1 
                break
            elif total > n: # total이 n보다 
                break
                
    return result