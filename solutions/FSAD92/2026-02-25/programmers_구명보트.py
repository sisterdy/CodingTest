"""
0. 오름차순으로 정렬해야 할까?
1. 무인도에 갇힌 사람들 중 가장 무거운 한 명을 태운다.
2. 더 태울 수 있는 사람 중 가장 가벼운 사람이 있는지 체크.
3. 있으면 추가하고, 없으면 출발 후 보트에서 내린다.
"""
def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        # 무거운 사람은 반드시 태운다
        if people[left] + people[right] <= limit:
            left += 1          # 가장 가벼운 사람도 같이 태울 수 있으면 태운다
        right -= 1             # 무거운 사람은 출발(혼자든 둘이든)
        boats += 1

    return boats