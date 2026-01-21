"""
이 문제는 정글에 백준에서 풀어본 기억이 있다.
"""

from collections import deque

def solution(s):
    temp = []   # 개인적으로 이 문제는 temp라는 이름이 잘 어울리는 것 같다
    
    for ch in s:    # 주어진 문자열의 문자를 하나씩 순회하며,
        
        # 해당 문자가 괄호를 닫는 ')'이고 큐가 비어있지 않으면서 큐의 가장 최신으로 들어온 놈이 '('이면
        if temp and (temp[-1] == '(' and ch == ')'):    
            temp.pop()  # temp에서 가장 최신으로 들어온 놈을 pop 한다.
        else:   # 그게 아니라면 temp에 추가한다.
            temp.append(ch)
            
    return len(temp) == 0   # 간단히 temp의 길이가 0이면 True, 아니라면 False를 리턴한다.