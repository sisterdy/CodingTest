# for문 돌리면 안되나? -> 시간초과 뜸 o(n^2)
# 스택으로 해야 o(n)
def solution(numbers):
    answer = [-1] * len(numbers)
    stk = []
    
    # 새로운 숫자가 들어올때마다 스택의 맨 위보다 크면 계속 팝한다.
    for i in range(len(numbers)):
        while stk and numbers[stk[-1]] < numbers[i]:
            top = stk[-1] # 스택의 탑의 요소의 인덱스 저장
            answer[top] = numbers[i] # 해당 answer에 가까운 큰 수 저장
            stk.pop()
            
        stk.append(i) 
    
    return answer