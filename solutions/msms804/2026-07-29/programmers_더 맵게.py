# 우선순위큐로 제일 작은거부터 두개 고르면 될듯
# 만약 맨 앞에 숫자가 K보다 크다면 끝
# 파이썬 우선순위큐는 최소힙

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
        
    return answer