"""
다리의 길이와 무게를 기준으로 두고 모든 트럭이 다리를 건너려면 최소 몇 초가 필요한지 구한다.

"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 빈 큐로 시작 - 0으로 채울 필요 없이 (무게, 나가는 시간)으로 관리
    bridge_queue = deque()

    # 대기 중인 트럭들 관리
    waiting_trucks = deque(truck_weights)

    # 현재 시간
    current_time = 0

    # 현재 다리 위 총 무게
    current_weight = 0

    while waiting_trucks or bridge_queue:

        # 1. 나가는 시간이 된 트럭만 골라서 제거
        while bridge_queue and bridge_queue[0][1] <= current_time:
            current_weight -= bridge_queue.popleft()[0]

        # 2. 다음 트럭을 올려도 무게 제한을 넘지 않는 경우
        if waiting_trucks and current_weight + waiting_trucks[0] <= weight:

            # 대기 트럭 꺼내기
            truck_weight = waiting_trucks.popleft()

            # 현재 다리 무게 증가
            current_weight += truck_weight

            # 트럭이 다리에 올라가는 시간

            # 3. (무게, 나가는 시간)을 함께 저장
            # 나가는 시간 = 현재 시간 + 다리 길이
            bridge_queue.append(
                (truck_weight, current_time + bridge_length)
            )

        else:
            # 4. 다음 트럭을 못 올리는 경우

            # 1초씩 자연 진행
            current_time += 1

            continue

        # 트럭 올린 경우에도 1초 진행
        current_time += 1

    # 마지막으로 저장했던 트럭이 다리를 완전히 건너는 시간 출력
    return current_time