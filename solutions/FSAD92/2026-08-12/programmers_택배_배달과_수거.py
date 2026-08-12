"""
그리디?
가장 먼 집에 배달이나 수거할 택배가 있다면 어차피 그 위치까지 가서 왕복을 해야 한다.
어차피 거기까지는 왕복을 해야 하니 남는 트럭 용량으로 가까운 집의 배달과 오는 길의 수거까지 같이 처리를 하는 그리디 방식.
"""
def solution(cap, n, deliveries, pickups):
    answer = 0

    delivery_need = 0
    pickup_need = 0

    # 가장 먼 집부터 가까운 집 방향으로 체크
    for i in range(n - 1, -1, -1):
        delivery_need += deliveries[i]
        pickup_need += pickups[i]

        # 현재 위치까지 와야 하는 최소 왕복 횟수 계산
        delivery_trips = (
            max(delivery_need, 0) + cap - 1) // cap

        pickup_trips = (
            max(pickup_need, 0) + cap - 1) // cap

        # 한 번의 왕복에서 배달/수거 모두 cap개 처리 가능하므로 더 큰 왕복 횟수에 맞춤
        trips = max(delivery_trips, pickup_trips)

        if trips > 0:
            # i번째 집까지 왕복하는 실제 거리
            answer += (i + 1) * 2 * trips

            # 방금 계산한 trips번만큼 배달/수거 처리
            delivery_need -= cap * trips
            pickup_need -= cap * trips

    return answer