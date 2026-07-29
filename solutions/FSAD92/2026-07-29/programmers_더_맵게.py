"""
저번 문제는 heap으로 풀었지만...
앞으로도 힙으로 풀 것 같지만...
이번에는 큐 두개를 써서 풀어보겠다.
"""
import heapq
from collections import deque


def solution(scoville, K):
    # 처음 주어진 음식은 오름차순으로 정렬해서 큐에 저장한다.
    original = deque(sorted(scoville))

    # 섞어서 새로 만든 음식들을 저장할 큐
    mixed = deque()

    mix_count = 0

    def pop_smallest():
        # original이 비어 있으면 mixed의 맨 앞이 최솟값이다.
        if not original:
            return mixed.popleft()

        # mixed가 비어 있으면 original의 맨 앞이 최솟값이다.
        if not mixed:
            return original.popleft()

        # 두 큐의 맨 앞을 비교해서 더 작은 값을 꺼낸다.
        if original[0] <= mixed[0]:
            return original.popleft()

        return mixed.popleft()

    while original or mixed:
        # 현재 남아 있는 음식 중 가장 작은 스코빌 지수를 확인한다.
        if original and mixed:
            current_min = min(original[0], mixed[0])
        elif original:
            current_min = original[0]
        else:
            current_min = mixed[0]

        # 가장 작은 음식이 K 이상이면 모든 음식이 K 이상이다.
        if current_min >= K:
            return mix_count

        # K보다 작은 음식이 남았는데 음식이 하나뿐이면
        # 더 이상 두 음식을 섞을 수 없다.
        if len(original) + len(mixed) < 2:
            return -1

        # 전체 음식 중 가장 작은 두 음식을 꺼낸다.
        first = pop_smallest()
        second = pop_smallest()

        # 문제에서 주어진 공식으로 새로운 음식을 만든다.
        new_scoville = first + second * 2

        # 새로 만든 음식들은 만들어지는 순서대로 오름차순이므로
        # mixed의 뒤에 그대로 추가할 수 있다.
        mixed.append(new_scoville)

        mix_count += 1

    return -1