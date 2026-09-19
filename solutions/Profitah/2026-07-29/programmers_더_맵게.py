"""
힙 / 가장 매운맛이 낮은 음식 2개 꺼내기

---
1.가장 스코빌 지수가 낮은 음식 2개를 찾는다.
2.섞어서 새로운 음식을 만든다 ((문제제시 : )첫 번째 + 두 번째 * 2)
.모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복한다.

"""

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    # 가장 안 매운 음식(가장 작은 값)이 K 이상이 될 때까지 반복
    while scoville[0] < K:
        # 음식 수가 2개 미만인데 K 이상을 못 만들면 불가능한 경우
        if len(scoville) < 2:
            return -1

        # 가장 스코빌 지수가 낮은 두 음식을 꺼냄
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 섞은 음식의 스코빌 지수 계산 후 힙에 삽입
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        
        answer += 1

    return answer