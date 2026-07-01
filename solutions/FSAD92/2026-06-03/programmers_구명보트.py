"""
전체 사람 수 - 같이 탄 쌍의 수
"""
def solution(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1
    pairs = 0

    while left < right:
        if people[left] + people[right] <= limit:
            # 가장 가벼운 사람과 가장 무거운 사람이 같이 탈 수 있음
            pairs += 1
            left += 1
            right -= 1
        else:
            # 가장 무거운 사람은 누구와도 못 탐
            right -= 1

    return len(people) - pairs
