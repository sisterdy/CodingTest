"""
관리해야 할 것

트럭마다 이동한 거리
현재 다리 위 트럭들의 무게
타이머
다리 건넌 트럭 수
"""


from collections import deque

def solution(bridge_length, weight, truck_weights):   
    distances = [0] * len(truck_weights)
    trucks_on_bridge = deque()
    
    total_weight = 0
    timer = 0
    next_idx = 0
    count = 0
    
    while count < len(truck_weights):
        timer += 1
        
        for i in trucks_on_bridge:
            distances[i] += 1
            
        if trucks_on_bridge and distances[trucks_on_bridge[0]] > bridge_length:
            finished_index = trucks_on_bridge.popleft()
            total_weight -= truck_weights[finished_index]
            count += 1
            
        if next_idx < len(truck_weights):
            if total_weight + truck_weights[next_idx] <= weight:
                trucks_on_bridge.append(next_idx)
                total_weight += truck_weights[next_idx]
                distances[next_idx] = 1
                next_idx += 1
    
    return timer