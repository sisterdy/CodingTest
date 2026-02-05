# 일단 며칠 걸리는지를 다 배열에 계산해서 담아둔다.
# 큐에 넣고 다음것보다 큰 경우에만 카운트
from collections import deque

def solution(progresses, speeds):
    answer = []
    days_q = deque()
    cnt = 0
    
    # 며칠 더 수행해야하는지를 큐에 담기
    for i in range(len(progresses)):
        days = (100 - progresses[i]) // speeds[i]
        if  (100 - progresses[i]) % speeds[i] != 0:
            days += 1
        days_q.append(days)

    # 제일 큰 수를 기준점으로 두고, 그보다 작은것들을 count하여 answer에 넣기
    while days_q:
        base = days_q.popleft()
        cnt = 1
        while days_q and base >= days_q[0]:
            cnt += 1
            days_q.popleft()
        
        answer.append(cnt)
    
    return answer