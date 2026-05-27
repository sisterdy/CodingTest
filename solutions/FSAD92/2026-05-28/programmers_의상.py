"""
서로 다른 옷의 조합의 수를 return

해시니까 딕셔너리를 써야할 거 같고, 그 어떤 아이템도 사용하지 않은 경우를 제외했던 것으로 기억함
옷 종류마다 (입기 후보수 + 안 입는 경우의 수 1개)를 곱함
거기에 그 어떤 아이템도 사용하지 않는 경우인 1을 뺌
"""
def solution(clothes):
    closet = {}
    answer = 1
    
    for item_name, item_kind in clothes:
        if item_kind not in closet:
            closet[item_kind] = 0
        closet[item_kind] += 1
    
    for cloth in closet.values():
        answer *= cloth + 1
    
    return answer - 1