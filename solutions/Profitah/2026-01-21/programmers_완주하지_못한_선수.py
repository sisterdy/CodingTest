"""
출력해야할 것은 : 완주하지 못한 선수의 이름.
["leo", "kiki", "eden"]	["eden", "kiki"] 가 주어졌을때
완주하지 못한 사람은 completion 배열에 없는 "leo"
"""
from collections import Counter # 딕셔너리 형태로 저장, 이름개수 세기 위해 필요

def solution(participant, completion):
    # 참가자 명단의 이름 개수를 세서 딕셔너리 형태로 저장
    p_count = Counter(participant)
    
    # 완주자 명단의 이름 개수를 세서 저장
    c_count = Counter(completion)
    
    # 참가자 - 완주자 = 완주하지 못한 사람만 남음
    answer = p_count - c_count
    
    # 딕셔너리에 남아 있는 유일한 키(완주 못한 선수 이름) 반환
    return next(iter(answer))
