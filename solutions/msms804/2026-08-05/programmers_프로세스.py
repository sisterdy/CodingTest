from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([])
    # 큐에 우선순위랑 인덱스 넣기
    for i, p in enumerate(priorities):
        q.append((p, i))
        
    while q:
        first = q.popleft()
        if any(first[0] < p[0] for p in q):
            q.append(first) # 다시 큐에 푸시
        else: # 큰게 없다면
            answer += 1
            if first[1] == location:
                break
            
    return answer
