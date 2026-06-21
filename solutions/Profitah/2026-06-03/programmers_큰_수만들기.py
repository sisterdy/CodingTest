"""
숫자 문자열에서 정확히 k개의 숫자를 제거하여 만들 수 있는 가장 큰 수를 구하는 문제
"""


def solution(number, k):
    stack = []

    # 1. 숫자 문자열을 왼쪽부터 한 글자씩 순회
    for num in number:

        # 2. 현재 숫자가 제거할 수 있는 횟수(k)보다 크고, 스택이 비어있지 않고, 스택 맨 위 숫자보다 크면
        while k > 0 and stack and stack[-1] < num:
            stack.pop() # 스택 맨 위의 작은 숫자를 제거 (더 큰 숫자를 앞자리에 두어야 큰 수가 됨)
            k -= 1       # 제거 횟수 차감

        # 3. 현재 숫자를 스택에 추가
        stack.append(num)

    # 4. 순회가 끝난 후에도 제거 횟수가 남아있다면
    #    스택 뒤에서부터 남은 횟수 k만큼 제거
    #    ex) k=2, stack=[4321] → [43] (맨 뒤의 2개 제거)
    if k > 0:
        stack = stack[:-k]

    # 5. 스택의 숫자들을 이어 붙여 문자열로 반환
    return ''.join(stack)