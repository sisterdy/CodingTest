"""
노력없이 풀 수 있는 알고리즘이 좋다.
itertools.permutations
를 사용해 날먹했다.
"""

import itertools

N = int(input())

for p in itertools.permutations(range(1, N+1)): # 1부터 N까지의 숫자들로 만들 수 있는 모든 순열을 오름차순으로 생성
    print(*p)