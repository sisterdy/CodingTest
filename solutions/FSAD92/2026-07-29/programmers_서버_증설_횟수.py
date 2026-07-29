"""
시뮬레이션 문제...
deque에 (서버 반납 시간,그 때 반납할 서버의 대수)를 넣어서 관리하자
서버 증설할 때마다 answers에 추가하고
추가한 시간에 k를 더해서 또 deque에 넣고 반복
"""
from collections import deque

def solution(players, m, k):
    answer = 0
    active_servers = 0
    server_batches = deque()    # (반납 시각, 반납 서버 수) 저장
    # players[hr]
    for hr in range(len(players)):
        # 현재 시각에 운영 기간이 끝난 서버들을 먼저 반납
        while server_batches and server_batches[0][0] <= hr:
            expire_hr, server_count = server_batches.popleft()
            active_servers -= server_count
            
        required_servers = players[hr] // m
        
        if active_servers < required_servers:
            added_servers = required_servers - active_servers   # 서버 부족하면 scale-out
            
            active_servers += added_servers
            answer += added_servers
            
            # hr시에 추가한 서버는 hr + k시에 반납
            expire_hr = hr + k
            server_batches.append((expire_hr, added_servers))
    
    return answer