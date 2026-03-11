"""
이중 우선순위 큐 (Dual Priority Queue)
- 최소값과 최대값을 모두 빠르게 관리하는 자료구조 구현

🎯 우리가 구하는 것
→ 모든 연산이 끝난 후
   [최댓값, 최솟값] 반환
→ 만약 큐가 비어있다면 [0, 0] 반환

📌 핵심 전략

1. 최소 힙(min_heap)과 최대 힙(max_heap)을 모두 유지
2. 각 원소에 고유 인덱스(idx)를 부여
3. visited 딕셔너리로 해당 원소가 "유효한지" 관리 (Lazy Deletion)
4. 삭제 시 실제로 양쪽 힙에서 동시에 제거하지 않고
   visited[idx] = False 로 논리 삭제 처리
5. 힙에서 값을 꺼낼 때 이미 삭제된 값은 while문으로 정리

👉 왜 이렇게?
힙은 중간 삭제가 O(n)이므로
두 힙을 동기화하려면 Lazy Deletion 방식이 필요하다.
"""

import heapq

def solution(operations):
    min_heap = []   # 최소 힙 (최솟값 빠르게 꺼내기)
    max_heap = []   # 최대 힙 (최댓값 빠르게 꺼내기 → 음수 저장)
    visited = {}    # 각 인덱스의 유효 여부 저장
    idx = 0         # 원소 구분용 고유 인덱스

    for op in operations:
        if op[0] == 'I':  # 삽입 연산
            num = int(op.split()[1])

            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))

            visited[idx] = True
            idx += 1

        else:  # 삭제 연산
            if op == "D 1":  # 최댓값 삭제
                # 이미 삭제된 값 제거
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            else:  # 최솟값 삭제
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # -------- 최종 동기화 --------
    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)

    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    # 큐가 비어있으면
    if not min_heap:
        return [0, 0]

    # [최댓값, 최솟값] 반환
    return [-max_heap[0][0], min_heap[0][0]]