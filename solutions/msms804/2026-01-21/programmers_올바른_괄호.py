# ( 이거나 스택이 비었을 경우 무조건 푸시
# ) 인 경우 만약 stack의 top이 (라면 pop, 아니라면 푸시
def solution(s):
    answer = True
    stack = []
    for e in s:
        if not stack or e == "(":
            stack.append(e)
        else:
            if stack[-1] == "(":
                stack.pop()
            else: 
                stack.push(e)
    
    if stack:
        return False
    return True