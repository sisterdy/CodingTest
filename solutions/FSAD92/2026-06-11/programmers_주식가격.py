"""
가격이 떨어지지 않은 기간은 몇 초인지를 return
중요한 것은... 떨어진 순간도 1초 카운팅 한다는 것...!
"""

def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            answer[i] += 1      # 떨어진 순간도 1초가 지나간 것이니까...
            
            if prices[j] < prices[i]:
                break
    return answer
