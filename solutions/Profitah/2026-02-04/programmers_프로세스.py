"""

/////////

큐만 사용

1. 맨 앞 꺼냄
2. 더 높은 게 있으면 뒤로 보냄
3. 없으면 실행
4. 내가 찾는 놈이면 종료

"""
from collections import deque

def solution(priorities, location):
    answer = 0
    
    # queue에 (우선순위, 인덱스(원래위치) 형태로 저장 (priorities,index )
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    
    # queue가 빌 때까지 반복. 우선순위 비교 이벤트는 동적임으로 while문 사용해야함. 
    while queue:
        current = queue.popleft()  # 맨 앞 원소 꺼내기
        
        # queue로 양방향에 있는 원소 비교. 우선순위가 더 높은 프로세스 찾기
        higher = False #current 보다 우선순위가 더 높은 게 있는지 탐색할 변수. 초기값은 False, 
        for j in range(len(queue)):
            if current[0] < queue[j][0]:  # current 의 우선순위가 큐 안에 있는 원소보다 낮으면 
                higher = True # higer는 true로 변환.
                break
        
        # current보다 더 높은 우선순위가 없으면 실행
        if higher:
            queue.append(current) # current를 큐에 넣는다.
        else:
            # 실행
            answer += 1
            # location 위치의 프로세스면 반환
            if current[1] == location:
                return answer
    
    return answer