"""
기존 풀이는 개수만 저장하는 풀이
이번에는 종류별로 옷 이름 저장해서 분류하기
"""
from collections import defaultdict


def solution(clothes):
    # key: 옷 종류, 해당 종류에 속하는 옷 이름들을 리스트로 저장
    closet = defaultdict(list)

    for item_name, item_kind in clothes:
        closet[item_kind].append(item_name)

    answer = 1

    # 각 종류를 순회하며 해당 종류의 옷 중 하나를 입는 경우 + 아무것도 입지 않는 경우 1개를 모두 곱하기
    for items in closet.values():
        answer *= len(items) + 1

    # 모든 종류에서 아무것도 입지 않은 경우는 허용되지 않으므로 제외
    return answer - 1