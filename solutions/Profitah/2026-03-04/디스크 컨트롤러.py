"""
그리디 + 힙 (우선순위 큐)

🎯 우리가 구하는 것
→ 모든 작업의 "평균 반환 시간"
→ (작업 완료 시간 - 요청 시간)의 평균

📌 핵심 전략 (SJF : Shortest Job First)

1. 현재 시간 time을 기준으로
2. jobs에서 요청시간 <= time 인 작업들을
3. 힙(대기큐)에 넣는다 (작업시간 기준 최소 힙)
4. 힙에서 가장 짧은 작업을 꺼내 실행
5. 완료 시간 - 요청 시간을 누적
6. 모든 작업이 끝나면 평균 반환 시간 계산

👉 왜 이렇게?
짧은 작업을 먼저 처리하면
전체 평균 반환 시간이 최소가 된다. (그리디 최적 선택)
"""


import heapq as controller  # 우선순위가 가장 높은 작업을 꺼내 실행시키는 우선순위 디스크 컨트롤러


def solution(jobs):
    answer = 0
    disk = 0 # 작업을 실행하는 하드디스크 
    time = 0 # 현재 시점
    waiting = [] # 대기큐
    idx = 0
    n = len(jobs)

    jobs.sort() 

    while idx < n or waiting: # idx가 n보다 작거나 웨이팅 대기큐가 비어있다면 

        # 현재 시간까지 들어온 작업을 힙에 추가
        while idx < n and jobs[idx][0] <= time:
            request, work = jobs[idx]
            controller.heappush(waiting, (work, request))
            idx += 1

        if waiting:
            work, request = controller.heappop(waiting)
            time += work
            answer += time - request
        else:
            # idx < n 이 보장된 상태
            time = jobs[idx][0]

    return answer // n