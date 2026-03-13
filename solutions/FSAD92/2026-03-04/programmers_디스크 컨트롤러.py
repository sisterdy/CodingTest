"""
작업의 소요 시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높다.

[s, l] 형태에서 s는 작업이 요청되는 시점, l은 작업의 소요 시간.
그렇다면 주어진 jobs 리스트를 요청시간 기준으로 정렬해야 할까?

가장 우선적으로 대기 큐가 비어있을 때는 jobs[i]
우선 순위는 jobs[i][1]을 기준으로 오름차순, 만약 중복된다면 jobs[i][0], 또 중복된다면 jobs[i]순으로 정렬해야 하는 것 같은데.
이걸 최소 힙으로 바꾸는 게 의미가 있나? 물론 순서는 보장할 수 없어도 최소값을 heappop으로 바로 가져올 수 있다는 건 장점이긴 하지만...

일단 while문으로 시작해야 할 것 같은데...
일단 대기 큐에 아무 것도 없다면, jobs의 0번쨰 원소를 꺼내 대기 큐에 넣는다
"""
import heapq

def solution(jobs):
    answer = 0  
    now = 0 # 현재 시각
    i = 0   # 정렬된 jobs 리스트에서 다음에 검사할 작업 인덱스
    start = -1  # 바로 이전에 완료된 작업의 종료 시간
    heap = []   # 현재 시점에서 처리 가능한 작업들을 담을 최소 힙
    
    jobs.sort() # 요청 시간 기준으로 오름차순 정렬
    
    # 처리한 작업이 jobs의 전체 개수보다 적거나, 힙에 대기 중인 작업이 있으면 반복
    while i < len(jobs) or heap:
        # 현재 시점까지 들어온 요청들을 힙에 push
        for j in range(i, len(jobs)):
            if start < jobs[i][0] <= now:   # 이전 작업 시작 ~ 종료 사이에 도착한 작업들
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])  # '소요시간' 기준 최소 힙 만들기
                i += 1
            else:
                break   # 요청 시간이 현재 시점보다 뒤라면 break
        
        if heap:
            # 대기 중인 작업 중 가장 짧은 것을 꺼내서 처리
            duration, request_time = heapq.heappop(heap)
            start = now     # 작업을 시작하는 시점
            now += duration     # 현재 시각 -> 작업 끝난 시점으로 갱신
            answer += (now - request_time)  # 종료 시점 - 요청 시점
        else:   # 현재 처리할 수 있는 작업이 없는 idle 상태면 1초 딸깍
            now += 1
    return answer // len(jobs)  # 모든 반환 시간의 합 / 작업 개수