# 앞자리를 최대한 크게만들기

def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        # num보다 작으면 계속 pop
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)
    
    # k가 남았으면 뒤에서 제거(ex) 111111 인 경우)
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)