"""
그냥 result deque 하나에 쑤셔넣으니 시간 초과가 떴음...
데큐를 2개 적용했어야 했다...

단순히 문제 해결 뿐만 아니라 시간복잡도나 공간복잡도도 계속 생각해야 한다는 것을 깨닫는다ㅠ
"""
import sys
from collections import deque

left = deque(sys.stdin.readline().strip())   # 커서 기준 왼쪽 문자열
right = deque()                              # 커서 기준 오른쪽 문자열
M = int(sys.stdin.readline().strip())

def move_left():
    if left:
        right.appendleft(left.pop())

def move_right():
    if right:
        left.append(right.popleft())

def backspace():
    if left:
        left.pop()

def put(x):
    left.append(x)

command_dict = {
    "L": move_left,
    "D": move_right,
    "B": backspace
}

for _ in range(M):
    command = sys.stdin.readline().strip()

    if command.startswith("P"):
        nothing, x = command.split()
        put(x)
    else:
        command_dict[command]()

print("".join(left) + "".join(right))