def solution(clothes):
    answer = 1
    clothes_set = {}
    
    # 초기화
    for name, kind in clothes:
        if kind not in clothes_set:
            clothes_set[kind] = 1
        else:
            clothes_set[kind] += 1
    
    # 각 종류 + 1 가지수를 곱한다
    for kind in clothes_set:
        answer *= (clothes_set[kind] + 1)
        
    # 아무것도 선택 안하는 경우 1개 제거
    return answer - 1