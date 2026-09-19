"""
구해야할 것 : 문자열 s에서 인접한 같은 문자 쌍을 반복 제거했을 때, 모두 제거되는지(1) 아닌지(0) 판별

사용한 알고리즘 : 스택(Stack)
"""

def solution(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:  # 스택 top과 같으면 짝 제거
            stack.pop()
        else:  # 다르면 스택에 쌓기
            stack.append(ch)
    return 1 if not stack else 0