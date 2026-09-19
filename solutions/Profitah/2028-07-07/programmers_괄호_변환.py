"""

괄호의 개수는 맞지만 짝이 맞지 않는 '불완전한 문자열'을 규칙에 따라 '올바른 괄호 문자열'로 교정하자

의사코드 참고 ㄱㄱ

"""


import sys
# 깊이제한으로 스택 오버플로우를 방지.
sys.setrecursionlimit(2000)

def solution(p):
    # [기저 조건] 입력이 빈 문자열인 경우, 그대로 빈 문자열 반환
    if p == "":
        return ""
    
    u, v = "", ""
    count = 0
    is_correct = True
    
    # 1. 문자열 p를 두 '균형잡힌 괄호 문자열' u, v로 분리
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
            
        # count가 음수가 되는 순간 '('보다 ')'가 먼저 나온 것이므로 '올바른 괄호'가 아님
        if count < 0:
            is_correct = False
            
        # '('와 ')'의 개수가 같아지는 최솟값 지점에서 u와 v를 분리하고 루프 탈출
        if count == 0:
            u = p[:i+1] # 더 이상 쪼갤 수 없는 균형잡힌 문자열 u
            v = p[i+1:] # 남은 문자열 v
            break
            
    # 2. 문자열 u가 '올바른 괄호 문자열'인 경우 v에 대해 재귀 수행 후 결합
    if is_correct:
        return u + solution(v)
        
    # 3. 문자열 u가 '올바른 괄호 문자열'이 아닌 경우 새 문자열 조립
    answer = '(' + solution(v) + ')' # 비어있는 틀 '(' + '재귀(v)' + ')' 생성
    
    # u의 첫 번째와 마지막 문자를 제외하고 나머지 문자의 괄호 방향을 뒤집어서 누적
    for char in u[1:-1]:
        if char == '(':
            answer += ')'
        else:
            answer += '('
            
    return answer