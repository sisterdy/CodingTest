"""
prices[i]를 뒤에 있는 원소들과 비교한다.
prices[i]가 뒤에 있는 원소보다 크거나 같다면 지금 가격을 증가, 그렇지 않다면 지금 가격을 answer에 append 한다.
"""

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 아직 떨어진 순간을 못 만난 인덱스들(가격이 아직 안 내려감)
    
    for t in range(n):
        # '지금' 가격 princes[t]이 더 싸면,
        # stack에 있던 더 비싼 시점들은 바로 지금 가격이 떨어진 게 확정
        while stack and prices[stack[-1]] > prices[t]:
            i = stack.pop()     # 떨어진 순간을 찾은 i를 스택에서 제거
            answer[i] = t - i # i 시점부터 t 시점까지 버틴 시간을 기록
            
        stack.append(t) # 현재 시점인 t는 떨어질지 아닐지 모르니 후보로 저장
        
    while stack:    # 끝까지 돌았는데도 스택이 남아있다면? 끝까지 가격이 한 번도 안 떨어진 경우...
        i = stack.pop()     # 하나씩 꺼내서
        answer[i] = (n - 1) - i     # 마지막 시점까지 버틴 시간을 기록
        
    return answer 