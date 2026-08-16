from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_set = defaultdict(int)
    
    # 초기화
    for name, kind in clothes:
        clothes_set[kind] += 1

    # 조합 개수 구하기
    for s in clothes_set:
        answer *= (clothes_set[s] + 1)
        
    return answer - 1