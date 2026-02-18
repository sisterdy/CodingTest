"""
우리가 구해야할 것은 모든 트럭이 다리를 건너려면 최소 몇 초가 필요한지 ...
시간과 무게를 기준으로
큐를 사용하여 다리 위의 상황을 시뮬레이션


큐의 왼쪽 = 다리의 입구쪽 (앞부분, 곧 나갈 부분)
큐의 오른쪽 = 다리의 뒷부분 (새 트럭이 들어오는 쪽)
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리를 나타내는 큐 (다리 길이만큼 0으로 초기화 - 0은 빈 공간)
    queue = deque([0] * bridge_length)
    
    # 대기 중인 트럭들을 큐로 관리
    orders = deque(truck_weights)
    
    # 경과 시간
    time = 0
    
    # 현재 다리 위에 있는 트럭들의 총 무게
    total = 0
    
    # 대기 중인 트럭이 있는 동안 반복
    while orders:
        time += 1  # 1초 경과
        
        # 다리의 맨 앞에 있는 트럭(또는 빈 공간)이 다리를 빠져나감
        total -= queue[0]
        queue.popleft()
        
        # 다음 대기 트럭이 다리에 올라갈 수 있는지 무게 확인
        if total + orders[0] > weight:
            # 무게 초과: 빈 공간(0)을 다리에 추가 (트럭은 대기)
            queue.append(0)
        else:
            # 무게 OK: 다음 트럭을 다리에 올림
            w = orders.popleft()  # 대기 트럭 꺼내기
            total += w             # 다리 위 총 무게 갱신
            queue.append(w)        # 다리에 트럭 추가
    
    # 마지막 트럭이 다리를 완전히 건너는 시간 추가
    # (마지막 트럭이 다리에 올라간 후 다리 길이만큼 더 가야 함)
    return time + bridge_length


# ===== 동작 예시 =====
# bridge_length=2, weight=10, truck_weights=[7,4,5,6]
#
# 초기: queue=[0,0], orders=[7,4,5,6], total=0
#
# 1초: queue=[0,7], orders=[4,5,6], total=7
# 2초: queue=[7,0], orders=[4,5,6], total=7 (4는 무게초과로 대기)
# 3초: queue=[0,4], orders=[5,6], total=4
# 4초: queue=[4,0], orders=[5,6], total=4 (5는 무게초과로 대기)
# 5초: queue=[0,5], orders=[6], total=5
# 6초: queue=[5,0], orders=[6], total=5 (6은 무게초과로 대기)
# 7초: queue=[0,6], orders=[], total=6
# 
# orders가 빈 후 bridge_length(2)초 추가 → 7+2=9초