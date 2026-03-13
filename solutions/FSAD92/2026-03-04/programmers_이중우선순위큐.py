"""
최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시

입력은 "명령어 데이터" 형식이니 명령어와 데이터를 분리해야 한다. 튜플로 저장할까?

heap을 만들어야 할 것 같은데... heapify로 하면 최소 힙이 되잖아.
이렇게 되면 어떻게 최댓값을 삭제 하지?

min_heap과 max_heap을 모두 만든다
inputs에 저장된 튜플 원소들을 하나씩 순회한다.

기존 코드 :

import heapq

def solution(operations):
    answer = []
    inputs = []
    min_heap = []
    max_heap = []
    is_deleted = []
    n = len(operations)
    
    
    for op in operations:
        command, data = op.split()
        inputs.append((int(data), command))
        
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    
    for i in range(n):
        if inputs[i][1] == 'I':
            heapq.heappush(min_heap, inputs[i][0])
            heapq.heappush(max_heap, -inputs[i][0])
            is_deleted.append(여기에 대체 뭘 넣어야 하지... 방금 push한 data와 매칭되는 고유한 ID를 False와 함께 넣어야 하는데...)
        else:
            if min_heap and max_heap:   # 우선순위 큐에 원소가 비어있지 않을 때 
                if inputs[i][0] == 1:   # 최댓값 삭제일 때
                    max_delete = heapq.heappop(max_heap)
                else:   # 최솟값 삭제일 때
                    min_delete = heapq.heappop(min_heap)
                    
    
    print(min_heap, max_heap)
    return answer
"""
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    n = len(operations)
    is_deleted = [False] * n
    
    
    for i in range(n):
        command, data = operations[i].split()
        value = int(data)
    
        if command == 'I':
            heapq.heappush(min_heap, (value, i))
            heapq.heappush(max_heap, (-value, i))
            
        else:
            if value == 1:  # 최댓값 삭제
                while max_heap and is_deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    is_deleted[idx] = True
            else:   # 최솟값 삭제
                while min_heap and is_deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    is_deleted[idx] = True
    
    while min_heap and is_deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and is_deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if not min_heap:
        return [0, 0]
    
    
    return [-max_heap[0][0], min_heap[0][0]]