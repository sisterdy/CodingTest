# 큐임
# 제일 우선순위 높은것 찾고, 앞에 있는게 그것보다 작다면 앞에 요소들 뒤로보낸다
# 아이디어는 알겠는데 구현이 어려웟음. 나중에 다시 해볼것
# any()

from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque((p, i) for i, p in enumerate(priorities))
    
    while q:
        p, idx = q.popleft()
        
        # pop한 요소보다 더 큰게 있다면 다시 push
        if any(other_p > p for other_p, _ in q): 
            q.append((p, idx))
        else: # 없다면 카운트
            answer += 1
            if idx == location:
                return answer
