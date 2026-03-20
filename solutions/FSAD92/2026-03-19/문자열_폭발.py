"""
기존 코드
그냥 while문 돌면서(explode가 sentence에 있는 동안) replace 함수로 교체하면 될 줄 알았음.
근데 시간 초과 뜸.

import sys

sentence = sys.stdin.readline().strip()
explode = sys.stdin.readline().strip()

while explode in sentence:
    sentence = sentence.replace(explode, "")

if sentence:
    print(sentence)
else:
    print("FRULA")
    
    
이게 테트리스처럼 폭발 후 '또 폭발'이 일어날 수 있는 문제 같은데 내가 이해한 게 맞나?
그렇다면 스택에 문자열을 왼쪽부터 차례차례 집어넣으면서 스택의 맨 위에 '폭발 문자열'과 일치한지 확인하다가 또 pop하고
다시 문자열을 집어넣고 하는 방식을 반복하면 되려나?
"""
import sys

sentence = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []
bomb_len = len(bomb)
bomb_last = bomb[-1]    # 방금 스택에 삽입한 ch를 이 폭발 문자열 마지막 글자와 비교하기 위해... 안 그러면 매번 비교해야 하니까

for ch in sentence:
    stack.append(ch)

    if ch == bomb_last and len(stack) >= bomb_len:
        is_bomb = True

        for i in range(bomb_len):
            if stack[len(stack) - bomb_len + i] != bomb[i]:
                is_bomb = False
                break

        if is_bomb:
            for _ in range(bomb_len):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")