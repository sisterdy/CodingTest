"""
비밀코드는 숫자의 순서가 중요하지 않다
즉 순열이 아니라 조합 -> combinations
"""
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    # 후보 코드랑 공통 숫자를 and 연산으로 구하기 위해 각 시도에서 입력한 숫자들을 set으로 바꾸기
    attempt_sets = []
    for attempt in q:
        attempt_sets.append(set(attempt))
        
    
    # 1~n까지의 숫자 중 서로 다른 숫자 5개 고르기(순서 상관 없음)
    for candidate in combinations(range(1, n + 1), 5):
        candidate_set = set(candidate)
        is_possible = True
        
        for attempt_set, expected_count in zip(attempt_sets, ans):
            same_count = len(candidate_set & attempt_set)
            
            if same_count != expected_count:
                is_possible = False
                break
                
        if is_possible:
            answer += 1
    
    return answer