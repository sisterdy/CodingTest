"""
출력해야할 것은 : 완주하지 못한 선수의 이름.
["leo", "kiki", "eden"]	["eden", "kiki"] 가 주어졌을때
완주하지 못한 사람은 completion 배열에 없는 "leo"
"""
from collections import Counter # 딕셔너리 형태로 저장, 이름개수 세기 위해 필요

def solution(nums):
    solution = set(nums)  # nums 배열을 set으로 변환 (중복 제거)
    return min(len(solution), len(nums) // 2)  
    """ set의 크기(len(solution)) = 폰켓몬 종류 수 와
     배열 길이 // 2 = 선택할 수 있는 최대 마리 수 중
     더 작은 값을 반환 """
