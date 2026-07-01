"""
k개를 고를 때 크기가 '서로 다른 종류의 수'의 최솟값을 return
개수 순으로 정렬하고, 이진탐색으로 최솟값을 찾아보자.
"""
from collections import Counter

def solution(k, tangerine):
    size_count = Counter(tangerine)
    counts = sorted(size_count.values(), reverse=True)

    prefix = [0]

    for count in counts:
        prefix.append(prefix[-1] + count)
    
    # k개를 만들기 위해서
    # 내림차순으로 귤 크기 별로 사이즈를 정리
    # 내림차순일 수록 좋다!
    left = 1
    right = len(counts)
    answer = len(counts)

    while left <= right:
        mid = (left + right) // 2

        if prefix[mid] >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
