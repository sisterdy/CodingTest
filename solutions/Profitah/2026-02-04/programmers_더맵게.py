"""
더 맵게 문제는 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해
가장 맵지 않은 음식 2개를 섞는 과정을 최소 횟수로 구하는 문제이다.

항상 가장 작은 스코빌 지수를 빠르게 꺼내야 하므로
최소 힙(min heap)을 사용한다.
"""

import heapq

def solution(scoville, K):
    answer = 0

    # 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)

    # 가장 작은 값이 K 이상이 될 때까지 반복
    while scoville[0] < K:
        # 음식이 하나만 남았는데 K 미만이면 더 이상 섞을 수 없음
        if len(scoville) < 2:
            return -1

        # 가장 맵지 않은 음식 2개 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 새로운 음식 스코빌 계산
        new_scoville = first + (second * 2)

        # 힙에 다시 삽입
        heapq.heappush(scoville, new_scoville)

        # 섞은 횟수 증가
        answer += 1

    return answer
