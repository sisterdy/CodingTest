"""
그리디 + 투 포인터

모든 배달·수거를 마치기 위한 트럭의 최소 이동 거리를 구하는 것


"""

def solution(cap, n, deliveries, pickups):
    answer = 0
    end_delivery = n - 1   # 배달 남은 물량 중 가장 먼 집의 인덱스
    end_pickup = n - 1     # 수거 남은 물량 중 가장 먼 집의 인덱스

    while end_delivery >= 0 or end_pickup >= 0:
        # 물량이 0인 뒤쪽 집들은 건너뛰기
        while end_delivery >= 0 and deliveries[end_delivery] == 0:
            end_delivery -= 1
        while end_pickup >= 0 and pickups[end_pickup] == 0:
            end_pickup -= 1

        if end_delivery < 0 and end_pickup < 0:
            break

        # 이번 왕복에서 가야 하는 가장 먼 지점까지의 왕복 거리
        answer += 2 * (max(end_delivery, end_pickup) + 1)

        # 배달: cap만큼 뒤에서부터 채워서 처리
        cap_left = cap
        while end_delivery >= 0 and cap_left > 0:
            if deliveries[end_delivery] <= cap_left:
                cap_left -= deliveries[end_delivery]
                deliveries[end_delivery] = 0
                end_delivery -= 1
            else:
                deliveries[end_delivery] -= cap_left
                cap_left = 0

        # 수거: cap만큼 뒤에서부터 채워서 처리
        cap_left = cap
        while end_pickup >= 0 and cap_left > 0:
            if pickups[end_pickup] <= cap_left:
                cap_left -= pickups[end_pickup]
                pickups[end_pickup] = 0
                end_pickup -= 1
            else:
                pickups[end_pickup] -= cap_left
                cap_left = 0

    return answer