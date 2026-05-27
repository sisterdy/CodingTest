"""
points: 포인트의 좌표
routes: point to point를 정한 경로. 해당 routes는 최단 거리로 이동한다.

이 때 최단 경로가 여러 가지일 경우, (r,c)에서 r좌표가 변하는 이동을 우선한다.
이동 '중' 같은 좌표에 로봇이 2대 이상 모인 위험한 상황의 횟수를 리턴해야 한다.

최단 경로니까 bfs를 활용해야 하려나
bfs를 이용해서

같은 좌표에 로봇이 2대 이상 모인 위험한 상황은 어떻게 카운트할까
로봇의 좌표를 관리해야 하나? 로봇의 수가 최대 100개이긴 한데...
"""
from collections import defaultdict

def solution(points, routes):
    answer = 0
    position = {i+1: (r,c) for i, (r,c) in enumerate(points)}   # 각 좌표에 넘버링을 한다
    
    spacetime_index = defaultdict(list)     # 
    
    for robot_number, route in enumerate(routes):
        time = 0
        curr_r, curr_c = position[route[0]]
        spacetime_index[(curr_r, curr_c)].append((robot_number, time))  # 시작점 기록
        
        for next_point in route[1:]:
            target_r, target_c = position[next_point]
            
            while curr_r != target_r:
                curr_r += 1 if target_r > curr_r else -1
                time += 1
                spacetime_index[(curr_r, curr_c)].append((robot_number, time))
                
            while curr_c != target_c:
                curr_c += 1 if target_c > curr_c else -1
                time += 1
                spacetime_index[(curr_r, curr_c)].append((robot_number, time))
                
    for (r,c), visits in spacetime_index.items():
        time_map = defaultdict(int)
        for robot_number, t in visits:
            time_map[t] += 1
            
        for count in time_map.values():
            if count >= 2:
                answer += 1
    return answer