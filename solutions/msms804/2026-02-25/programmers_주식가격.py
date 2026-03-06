# 스택? 큐?
# 뭔가 스택일듯. 스택의 탑보다 작은 수가 나타나면 pop?
# 인덱스를 answer에 넣어야한다고..

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    # 끝까지 안 떨어진 애들 처리
    while stack:
        j = stack.pop()
        answer[j] = (n - 1) - j
        
    return answer