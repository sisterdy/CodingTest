from itertools import combinations
from collections import Counter

def solution(orders, course):
    """
    구해야 할 것: 각 course(코스 크기)마다, 손님들이 함께 주문한 메뉴 조합 중
    2번 이상 등장하면서 그 course 크기에서 가장 많이 주문된 조합을 찾아
    알파벳 순으로 정렬해서 반환.
    """
    answer = []
    
    for c in course:
        candidates = []
        for order in orders:
            # 각 주문에서 길이 c만큼의 조합을 모두 생성
            combos = combinations(sorted(order), c)
            candidates += combos
        
        # 해시(Counter)로 조합별 등장 횟수 집계
        counter = Counter(candidates)
        
        if counter:
            max_count = max(counter.values())
            if max_count > 1:  # 2번 이상 함께 주문된 조합만
                for menu, cnt in counter.items():
                    if cnt == max_count:
                        answer.append(''.join(menu))
    
    return sorted(answer)