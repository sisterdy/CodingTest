# 하나씩 스택에 넣는다
# 만약 하나씩 검사하다가 explode랑 같다면 다 pop
import sys

str = sys.stdin.readline().strip()
explode = sys.stdin.readline().strip()
len_explode = len(explode)
stack = []

for s in str:
    stack.append(s)
    # 스택 안에 explode가 있는지 검사..? -> join해서 검사한다
    if ''.join(stack[-len_explode:]) == explode:
        for _ in range(len_explode):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")