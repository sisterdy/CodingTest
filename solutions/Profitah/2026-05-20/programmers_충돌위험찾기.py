"""
구해야 할 것:
같은 시간, 같은 위치에 로봇이 2대 이상 있는 횟수

풀이 과정
1. 포인트 번호 -> 좌표 저장
2. 각 로봇 경로를 순서대로 이동 시뮬레이션
3. (시간, 위치)별 로봇 수 기록
4. 2대 이상이면 충돌 위험 +1
"""

from collections import defaultdict

def solution(points, routes):
    # 1. 포인트 정보 및 시간대별 위치 기록 준비
    # 포인트 번호를 Key로, (r, c) 좌표를 Value로 저장
    point_dict = {i + 1: (points[i][0], points[i][1]) for i in range(len(points))}
    # (시간, r, c)를 키로 하여 해당 시점에 해당 위치에 있는 로봇 수를 카운트
    time_position_count = defaultdict(int)

    # 2. 각 로봇의 전체 이동 경로 시뮬레이션
    for route in routes:
        current_time = 0
        # 0초일 때의 시작 위치 기록
        start_r, start_c = point_dict[route[0]]
        time_position_count[(current_time, start_r, start_c)] += 1

        # 경유지 순서대로 이동
        for i in range(len(route) - 1):
            r_start, c_start = point_dict[route[i]]
            r_end, c_end = point_dict[route[i + 1]]

            # 3. 최단 경로 이동 기록 (r 우선 이동 후 c 이동)
            # r 좌표 이동
            while r_start != r_end:
                if r_start < r_end: r_start += 1
                else: r_start -= 1
                current_time += 1
                time_position_count[(current_time, r_start, c_start)] += 1

            # c 좌표 이동
            while c_start != c_end:
                if c_start < c_end: c_start += 1
                else: c_start -= 1
                current_time += 1
                time_position_count[(current_time, r_start, c_start)] += 1

    # 4. 동일 시간/위치에 2대 이상 존재하는 '충돌' 횟수 합산
    danger_count = 0
    for count in time_position_count.values():
        if count > 1:
            danger_count += 1

    return danger_count