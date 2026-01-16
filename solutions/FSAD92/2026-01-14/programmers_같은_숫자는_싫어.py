"""
배열 arr의 각 원소는 숫자 0~9
연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
(단 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지)

arr의 첫번째 원소부터 left pop을 한다. 이 때 left pop을 하려면 arr을 deque로 변환해야 한다.
조건은 left pop한 값이 answer[-1]의 값과 일치하지 않을 때!

기존 코드
"""

from collections import deque

def solution(arr):
    answer = []
    deque_arr = deque(arr)
    
    while deque_arr:
        pop_val = deque_arr.popleft()
        if len(answer) == 0 or pop_val != answer[-1]:
            answer.append(pop_val)
            
    return answer