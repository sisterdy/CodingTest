# 큐를 써서 해야할듯
# 다리를 큐로 생각
# bridge_length 만큼 큐를 0 으로 채운다
# 큐에 푸시하면서 answer + 1

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0 # 다리 위 무게
    
    while bridge:
        # 다리를 지나감
        out = bridge.popleft()
        current_weight -= out
        
        # 현재 다리위 무게와 truck_weights[0] 의 합이 weight보다 작으면 push
        if truck_weights and current_weight + truck_weights[0] <= weight:
            t = truck_weights.popleft() # 대기트럭에서 팝
            bridge.append(t) # 다리 건너는중
            current_weight += t # 다리 위 무게 증가
        else:
            bridge.append(0)
        answer += 1
        
        # 더 올릴 트럭도 없고, 다리도 비었다면 종료
        if not truck_weights and current_weight == 0:
            break
    return answer