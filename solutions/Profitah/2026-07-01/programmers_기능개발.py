"""
배포마다 몇 개의 기능이 개발되는지 구하자.

- 각 기능이 완료되기까지 남은 일수를 계산한다.
- 앞 기능이 배포되어야 뒤 기능도 함께 배포될 수 있다.
- 배포 시점마다 함께 배포되는 기능의 개수를 반환한다.

[자료구조] 리스트(Queue처럼 사용)
"""

import math

def solution(progresses, speeds):
    remaining_days = []

    # 1. 각 기능의 완료까지 남은 일수 계산
    for p, s in zip(progresses, speeds):
        days = math.ceil((100 - p) / s)
        remaining_days.append(days)

    result = []

    # 2. 앞 기능을 기준으로 함께 배포 가능한 기능 묶기
    while remaining_days:
        current = remaining_days.pop(0)
        count = 1

        while remaining_days and remaining_days[0] <= current:
            remaining_days.pop(0)
            count += 1

        result.append(count)

    # 3. 배포마다 배포된 기능 개수 반환
    return result