"""
스택/큐 (주식가격)

각 시점에서 가격이 떨어지지 않은 기간을 구하는 문제이다.
모든 시점을 기준으로 이후 시점을 비교하는 완전탐색 방식으로 해결 가능하다.
"""

def solution(prices):
    n = len(prices)
    answer = [0] * n

    for i in range(n):                          # 1. 각 시점을 기준으로 설정
        for j in range(i + 1, n):               # 2. 다음 시점부터 끝까지 비교
            answer[i] += 1                      # 3. 가격이 유지되면 시간 증가
            if prices[j] < prices[i]:           # 4. 가격이 떨어지면
                break                           #    반복 종료

    return answer                               # 5. 결과 반환