# 두명 이상 공통으로 주문한 메뉴 조합 중, 각 코스 크기별로 가장 많이 주문된 조합 찾기
# 여러 손님의 주문에서 똑같은 조합이 몇번 등장했는지 세기 -> set?
# 조합
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        counter = Counter()
        for order in orders:
            # 조합을 만들기 전에 알파벳순으로 정렬
            order = sorted(order)
            
            for comb in combinations(order, c):
                menu = ''.join(comb) # 결과가 튜플형태이기 때문에 문자열로 변환
                counter[menu] += 1
                
        if not counter:
            continue
            
        max_count = max(counter.values())
        
        for menu, count in counter.items():
            if count == max_count and count >= 2:
                answer.append(menu)
                
    answer.sort()
        
    return answer