"""
구해야할 것 : 차량 진입/진출 구간이 주어질 때, 모든 구간을 감시하기 위한 최소 카메라 수

사용한 알고리즘 : 그리디(Greedy) - 구간 스케줄링
"""

def solution(routes):
    routes.sort(key=lambda x: x[1])  # 진출 지점 기준 정렬

    camera_count = 0
    last_camera = -10000000

    for start, end in routes:
        if start > last_camera:  # 현재 카메라로 커버 안 되는 구간이면
            camera_count += 1    # 새 카메라 설치
            last_camera = end    # 진출 지점에 설치

    return camera_count