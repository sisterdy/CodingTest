"""
number 원소를 앞에서부터 하나씩 stack에 넣어야겠다.
그리고 stack의 맨 위의 원소와 현재 numbers 원소를 비교해서
answer[previous_index] = numbers[i]로 저장해야겠다.
"""
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
    # 스택에 원소가 있고, 현재 numbers 원소가 stack의 맨 위 원소보다 크다면
        while stack and numbers[i] > numbers[stack[-1]]:
            previous_index = stack.pop()
            answer[previous_index] = numbers[i]
        stack.append(i)
    return answer