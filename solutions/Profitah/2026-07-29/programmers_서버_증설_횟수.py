"""
목표: 24시간 동안 사용자 수에 맞춰 서버를 늘릴 때, 하루 동안 새로 증설해야 하는 '총 서버 건수(횟수)'를 구하는 문제

조건:사용자 m명당 서버 1대가 필요합니다.
증설된 서버는 k시간 동안 작동한 뒤 자동으로 반납(수거)됩니다.

"""


def solution(players, m, k):
    answer = 0
    # 현재 시각 t에 만료되어 반납될 서버의 수
    server_returns = [0] * 24
    
    current_servers = 0  # 현재 가동 중인 증설 서버 수

    for t in range(24):
        # 1. t시각에 만료된 서버 반납
        current_servers -= server_returns[t]

        # 2. t시각에 필요한 최소 증설 서버 수
        required_servers = players[t] // m

        # 3. 현재 서버가 부족한 경우 추가 증설
        if current_servers < required_servers:
            add_count = required_servers - current_servers
            answer += add_count
            current_servers += add_count
            
            # t + k 시점에 서버 반납 예약 (24시 이전인 경우만)
            if t + k < 24:
                server_returns[t + k] += add_count

    return answer