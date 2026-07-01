"""
기존 코드는 삽입 순서 idx로 관리했다면 이번에는 숫자 값의 개수로 관리.
alive[value] = 0이면 삭제 여부 판별
이번에도 Counter 함수 사용
"""
import heapq
from collections import Counter

def solution(operations):
    min_heap = []   # 최소 힙
    max_heap = []   # 최대 힙
    
    # 현재 큐 안에 몇 개 있는지 체크
    alive = Counter()
    size = 0

    # min_heap의 맨 위 값이 이미 삭제된 값이면 제거한다.
    # 즉, 실제 큐에는 없는데 힙에만 남아 있는 값을 정리한다.
    def clean_min_heap():
        while min_heap and alive[min_heap[0]] == 0:
            heapq.heappop(min_heap)

    def clean_max_heap():
        while max_heap and alive[-max_heap[0]] == 0:
            heapq.heappop(max_heap)

    for operation in operations:
        command, number = operation.split()
        number = int(number)

        if command == "I":
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            alive[number] += 1
            size += 1

        else:
            if size == 0:
                continue

            if number == 1:
                clean_max_heap()

                deleted_value = -heapq.heappop(max_heap)
                alive[deleted_value] -= 1
                size -= 1

            else:
                clean_min_heap()

                deleted_value = heapq.heappop(min_heap)
                alive[deleted_value] -= 1
                size -= 1

    if size == 0:
        return [0, 0]

    clean_min_heap()
    clean_max_heap()

    return [-max_heap[0], min_heap[0]]
