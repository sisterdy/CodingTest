"""
우선순위가 가장 높은 프로세스가 맨 앞에 올 때까지 뒤에 다시 넣기...
근데 location이 주어지고, 해당하는 프로세스가 몇 번째 실행되는지를 return 해야 하므로
enumerate를 써서 (원래 인덱스, 우선순위) 이렇게 관리해야겠다.
"""

from collections import deque

def solution(priorities, location):
    count = 0
    queue = deque(enumerate(priorities))
    
    while queue:
        current_original_index, current_priority = queue.popleft()
        
        if any(priority > current_priority for _, priority in queue):
            queue.append((current_original_index, current_priority))
        else:
            count += 1
            
            if current_original_index == location:
                return count
