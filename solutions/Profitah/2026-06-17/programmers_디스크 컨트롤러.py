"""
[최소힙] [구해야 할 것]
각 작업의 요청부터 종료까지 걸린 소요 시간의 '최소 평균 시간' 구하기.


하드디스크가 작업을 수행하지 않고 쉬고 있을 때(Idle)와 수행 중일 때를 고려하여, 
모든 작업의 요청부터 종료까지 걸린 소요 시간의 평균을 가장 최소화했을 때의 
'평균 소요 시간(소수점 아래 버림)' 구하기.
"""
# 우선순위가 가장 높은 작업을 꺼내 실행시키는 우선순위 디스크 컨트롤러
import heapq as controller  


def solution(jobs):
    answer, time, idx, waiting = 0, 0, 0, []
    n = len(jobs)

    # 1. 요청 시간 기준으로 오름차순 정렬
    jobs.sort() 

    while idx < n or waiting:

         # 2. "현재 시간까지 들어온 작업만" heap에 추가
        while idx < n and jobs[idx][0] <= time:
            request, work = jobs[idx]
            controller.heappush(waiting, (work, request)) # 소요시간이 짧은 순으로 정렬되도록 push
            idx += 1

        # 3. 대기큐에 작업이 있으면, 가장 짧은 작업을 꺼내서 실행 후 시간 갱신
        if waiting:
            work, request = controller.heappop(waiting)
            time += work
            answer += time - request # (종료 시간 - 요청 시간) 누적
            
        # 4. 대기큐가 비어있다면, 다음 작업의 요청 시간으로 바로 점프
        else:
            time = jobs[idx][0]

    return answer // n