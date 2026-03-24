"""
원본과 폭파문자열을 비교.
폭파문자열을 제외하며 원본이 어떻게 변하는지 출력하자 

문자열만 검사 -> 원본 문자열 폭파 이후 문자열을 처음부터 검사하기 때문에 효율성이 떨어진다. :: 시간초과 판정.

원본을 문자 단위로 쪼개 스택에 담고,
 폭파문자열의 길이만큼 스택에서 꺼내어 폭파문자열과 비교하여 같다면 스택에서 제거하는 방식으로 구현하자. 
 
 :: 시간초과 판정 해결.
"""


import sys

# 입력값 처리
S = sys.stdin.readline().strip() # 파이썬은 공백도 문자열에 포함함으로 공백을 제외하고 문자열 입력받기
explosion_string = sys.stdin.readline().strip() # 역시나 공백을 제외하고 폭발 문자열 입력받기

# rstript과 stript의 차이 : 




# stack으로 문자열 폭발 구현
stack = [] # 폭발 문자열이 완성될 때마다 제거하기 위해 stack 사용
ex_len = len(explosion_string) # 입력받은 폭발문자열의 길이를 변수에 저장.

for i in range(len(S)): # 문자열 S의 문자열 길이만큼 반복하며 
    stack.append(S[i]) # stack에 문자열 S의 각 문자를 하나씩 추가
    if ''.join(stack[-ex_len:]) == explosion_string: # 만약, 구분자 없이 이어 붙인 stack의 마지막 ex_len 길이의 문자열이 폭발 문자열과 같다면]
        for j in range(ex_len): # 폭발 문자열의 길이만큼 반복하며
            stack.pop() # 스택에서 제거합니다.

# 결과 출력
if stack:
    print(''.join(stack)) # 이 과정을 반복하며 스택에 남아있는 문자열을 이어붙여 출력한다.
else:
    print('FRULA') # 스택이 비었다면 "FRULA"를 출력하며 폭파한다!!!!