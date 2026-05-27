"""
저번에는 tick 단위로 계산했다면
이번에는 트럭별로 다리를 떠나는 시간을 중점으로 고려함
(트럭 무게, 나갈 시간)
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks_on_bridge = deque()
    
    time = 0
    curr_weight = 0
    index = 0
    n = len(truck_weights)
    
    while index < n or trucks_on_bridge:
        time += 1
        
        if trucks_on_bridge and trucks_on_bridge[0][1] == time:
            truck_weight, exit_time = trucks_on_bridge.popleft()
            curr_weight -= truck_weight
            
        if index < n and curr_weight + truck_weights[index] <= weight:
            curr_weight += truck_weights[index]
            trucks_on_bridge.append((truck_weights[index], time + bridge_length))
            index += 1
    return time