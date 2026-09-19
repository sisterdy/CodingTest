"""
뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
뒷큰수를 구합시다.

"""

def solution(numbers):
    answer = [-1] * len(numbers)  # 결과 배열 (-1: 뒷큰수 없음)
    stack = []  # 뒷큰수를 못 찾은 인덱스 저장

    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()      # 뒷큰수 찾은 인덱스
            answer[idx] = num      # 뒷큰수 저장
        stack.append(i)            # 현재 인덱스 대기

    return answer