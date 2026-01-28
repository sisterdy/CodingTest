def solution(s):
    stack = []  # 여는 괄호 '(' 를 저장할 스택

    for i in range(len(s)):  # 문자열을 인덱스로 하나씩 순회
        if s[i] == '(':      # 현재 문자가 여는 괄호라면
            stack.append('(')  # 스택에 저장
        else:               # 현재 문자가 닫는 괄호 ')' 라면
            if len(stack) == 0:   # 대응할 여는 괄호가 없을 때
                return False      # 올바르지 않은 괄호 → 바로 False 반환
            else:
                stack.pop()       # 가장 최근에 넣은 '(' 하나 제거 (짝 맞추기)

    # 모든 문자를 다 확인한 뒤
    # 스택이 비어 있으면 모든 괄호가 짝이 맞은 것
    # 스택에 '(' 가 남아 있으면 짝이 안 맞은 것
    return len(stack) == 0
