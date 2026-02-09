"""
모든 음식의 스코빌 지수를 K 이상으로 만들고 싶다.
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
섞어야 하는 최소 횟수를 return

일단 heapify로 scoville을 최소 힙 구조로 만든다.
while로 반복한다. 최소 힙 구조가 된 scoville[0]이 K보다 작은 동안.
만약 scoville[0]이 K보다 크거나 같다면 count를 return
아니라면 fisrt = heapq.heapify(scoville)
second = heapq.heapify(scoville)
new = first + (second * 2)
heapq.heappush(scoville, new)

"""
import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        count += 1
    
    return count if scoville[0] >= K else -1