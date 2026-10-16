"""

구해야할 것 : 폰켓몬이 주어졌을 때, 몇 마리의 포켓몬을 가져갈 수 있는지

- 서로 종류가 다른 포켓몬
- 주어진 포켓몬의 절반

"""


def solution(nums):
    solution = set() # 리스트를 set으로 변경 (자동중복제거, 서로 다른 원소의 개수를 바로 구할 수 있는 자료구조)

    for num in nums:
        solution.add(num) # 입력받은 값을 차례대로 set에 추가

    return min(len(solution), len(nums) // 2) # (서로 다른 종류 수)와 (고를 수 있는 최대 마리 수 = 전체의 절반) 중 더 작은 값을 반환