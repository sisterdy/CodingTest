"""
기존 코드는 start, now, i를 함께 써서 이번 작업 사이에 들어온 요청을 관리
이번에는 인덱스 하나만 사용해서 아직 힙에 넣지 않은 작업을 관리하는 방식
"""
import heapq

def solution(jobs):
    now = 0
    total_time = 0
    job_idx = 0     # 아직 힙에 넣지 않은 작업 중 가장 앞에 있는 작업의 인덱스
    done = 0
    heap = []
    n = len(jobs)
    
    numbered_jobs = []
    for idx, (request_time, duration) in enumerate(jobs):
        numbered_jobs. append((request_time, duration, idx))
        
    # request_time 기준으로 정렬
    numbered_jobs.sort()

    while done < n:
        # 현재 시각 now까지 요청된 작업 전부 힙에 넣기
        while job_idx < n and numbered_jobs[job_idx][0] <= now:
            request_time, duration, original_idx = numbered_jobs[job_idx]
            heapq.heappush(heap, (duration, request_time, original_idx))
            job_idx += 1
            
        if heap:
            duration, request_time, original_idx = heapq.heappop(heap)
            
            now += duration
            total_time += now - request_time
            done += 1
        # 힙이 비어있으면 다음 요청 시각으로 점프. 굳이 기존 코드처럼 now += 1을 할 필요가 없다.
        else:
            now = numbered_jobs[job_idx][0]
    
    return total_time // n
