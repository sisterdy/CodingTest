"""
우선순위? heapify?
"""
from collections import deque
import heapq

def solution(priorities, location):
    count = 0
    
    # (우선순위, 인덱스)를 큐에 저장
    queue = deque((p, i) for i, p in enumerate(priorities))
    
    # heapq는 민힙이 디폴트라 맥스힙으로 만들기 위해 마이너스를 붙여서 저장
    max_heap = [-p for p in priorities]
    heapq.heapify(max_heap)
    
    while queue:
        p, i = queue.popleft()  # 큐에서 프로세스를 하나 꺼낸다
        
        if p == -max_heap[0]:   # 꺼낸 프로세스의 우선순위가 맥스힙의 최대 우선순위와 같다면
            heapq.heappop(max_heap)     # 맥스힙에서 해당 '우선순위'를 pop한다
            count += 1  # 프로세스 실행 카운트를 1 증가
            
            if i == location:   # 만약 해당 프로세스의 인덱스가, 우리가 찾는 location과 같다면
                return count    # 프로세스 실행 카운트를 그대로 리턴한다. 결국 이 count 변수가 몇 번째로 실행되는지에 대한 답이 되니까.
        else:
            queue.append((p, i))    # 꺼낸 프로세스의 우선순위가 맥스힙의 최대 우선순위가 아니라면 뒤로 보낸다.