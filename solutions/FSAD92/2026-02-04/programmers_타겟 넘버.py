"""
DFS로 모든 경우의 수를 찾아야 할 것 같다.
numbers[i]가 주어지면, +numbers[i], -numbers[i] 두 갈림길로 나뉘어야 할 것 같은데..
"""

def solution(numbers, target):
    answer = 0
    stack = [(0, 0)]
    
    while stack:
        index, current_sum = stack.pop()    # (다음으로 갈 인덱스, 현재까지 합계)
        
        if index == len(numbers):   # 모든 숫자를 다 확인했는지
            if current_sum == target:   # 최종 합계가 목표값과 같은지
                answer += 1     # 같으면 카운트 증가
                
        else:
            stack.append((index + 1, current_sum + numbers[index]))
            stack.append((index + 1, current_sum - numbers[index]))
            
    return answer