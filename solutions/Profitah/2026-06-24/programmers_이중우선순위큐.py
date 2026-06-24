"""
힙

큐에있는 최댓값과 최솟값을 구하자.

→ 삽입 연산, 방문체크를 이용한 삭제연산이 끝난 후
   [최댓값, 최솟값] 반환
→ 만약 큐가 비어있다면 [0, 0] 반환

---
1. 최소 힙과 최대 힙을 동시에 관리한다.

2. 삽입 연산 시 두 힙에 모두 같은 원소를 넣는다.

3. 삭제는 visited를 이용한 Lazy Deletion 방식으로 처리한다. (false 로 무효처리 하고 while문으로 힙에서 추후제거)

4. 모든 연산 후 두 힙을 최종 동기화하여 결과를 반환한다.
"""

import heapq  # 파이썬 기본 최소 힙(우선순위 큐) 모듈


def solution(operations):
    min_heap = []   # 최소값을 빠르게 꺼내기 위한 최소 힙
    max_heap = []   # 최대값을 빠르게 꺼내기 위한 힙 (음수로 저장해서 구현)
    visited = {}    # 각 원소가 아직 유효한지(True/False) 저장 (Lazy Deletion용)
    idx = 0         # 각 원소를 구분하기 위한 고유 번호 (인덱스)

    for op in operations:  # 주어진 모든 연산을 순회
        if op[0] == 'I':   # 첫 글자가 'I'이면 삽입 연산
            num = int(op.split()[1])  # 삽입할 숫자 추출

            # 최소 힙에는 (값, 고유번호) 형태로 저장
            heapq.heappush(min_heap, (num, idx))

            # 최대 힙에는 (-값, 고유번호) 형태로 저장
            # 파이썬은 최소 힙만 지원하므로 음수로 바꿔서 최대 힙처럼 사용
            heapq.heappush(max_heap, (-num, idx))

            visited[idx] = True  # 현재 원소는 유효하다고 표시
            idx += 1             # 다음 원소를 위해 고유번호 증가

        else:  # 삭제 연산 (D 1 또는 D -1)
            if op == "D 1":  # 최댓값 삭제
                # 이미 삭제된(visited=False) 값은 제거하면서 정리
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)

                if max_heap:  # 삭제할 값이 존재하면
                    visited[max_heap[0][1]] = False  # 해당 원소를 무효 처리
                    heapq.heappop(max_heap)          # 최대 힙에서 제거

            else:  # 최솟값 삭제 ("D -1")
                # 이미 삭제된 값 정리
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)

                if min_heap:  # 삭제할 값이 존재하면
                    visited[min_heap[0][1]] = False  # 무효 처리
                    heapq.heappop(min_heap)          # 최소 힙에서 제거

    # -------- 최종 동기화 --------
    # 반복이 끝난 뒤에도 invalid 값이 남아 있을 수 있으므로 정리

    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)

    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    # 모든 값이 삭제된 경우
    if not min_heap:
        return [0, 0]

    # 최대 힙은 음수로 저장했으므로 다시 양수로 변환
    # [최댓값, 최솟값] 형태로 반환
    return [-max_heap[0][0], min_heap[0][0]]