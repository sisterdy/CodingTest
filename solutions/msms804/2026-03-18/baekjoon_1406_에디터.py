import sys
# 흠.. 스택이랑 큐를 다써야하나
# 스택 두개를 써야한다함(커서를 기준으로 스택을 두개 나누는듯)
text = sys.stdin.readline().strip() # \n 없애기
n = int(sys.stdin.readline())

stack_left = list(text)
stack_right = [] # 이건 뒤집어져 있다고 생각해야

for i in range(n):
    edit = sys.stdin.readline()

    # 커서를 왼쪽으로
    if edit[0] == "L" and stack_left:
        char = stack_left.pop()
        stack_right.append(char)
    elif edit[0] == "D" and stack_right:
        char = stack_right.pop()
        stack_left.append(char)
    elif edit[0] == "B" and stack_left: 
        stack_left.pop()
    elif edit[0] == "P":
        stack_left.append(edit[2])
    

print(''.join(stack_left + stack_right[::-1]))