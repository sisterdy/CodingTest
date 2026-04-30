"""
일단 먼저 줄 선 놈이 먼저 나가니까 자료구조는 queue인가?
애초에 중요한 건 n과 times의 원소라 pop 할 이유가 딱히 없으니 자료구조는 상관 없으려나.

일단 극단적으로 예를 들어보자
times = [1, 7]
n = 6이더라도 모든 사람이 첫 번째 심사대에 가서 심사를 받는 게 제일 빠르다.

이때의 로직을 어떻게 해야 할까
심사대에 보내기 전에 어떤 심사대를 보낼지에 대한 로직을...

일단 첫번째 사람.
모든 심사대가 비어있다면 가장 빠른 심사대로 보낸다.
그렇다면 모든 심사대마다 상태 추적이 필요할까?

그리고 두번째 사람을 보낼 차례다.
일단 모든 심사대가 비어있다면, 가장 빠른 심사대로 보내야겠지.
하지만 그렇지 않다면, 두번 째로 빠른 심사대로 보낼지, 아니면 '대기'를 통해 더 빠른 결과를 얻을 수 있을지 비교를 해야 한다.

내 생각에는 현재 시간을 관리하는 변수도 있어야 할 것 같다.
그래야 (현재 시간 + '대기해야 하는 시간' + '대기가 끝나고 들어간 심사대에서 소요되는 시간') vs (현재 시간 + 비어있는 심사대 중 가장 빨리 심사되는 시간)을 비교할 수 있을 것 같기 때문이다.

즉, 그리디로 풀 수 있지 않을까?

import heapq

def solution(n, times):
    # (심사가 끝나는 시점, 심사 소요 시간)
    # 처음에는 모든 심사대가 0분에서 시작하므로 (소요시간, 소요시간)으로 초기화
    heap = [(t, t) for t in times]
    heapq.heapify(heap)
    
    answer = 0

    for _ in range(n):
        finish_time, process_time = heapq.heappop(heap)
        answer = finish_time # 현재 배치된 사람의 종료 시간이 곧 전체 소요 시간의 후보
        
        # 해당 심사대에서 다음 사람을 처리할 경우의 종료 시간을 계산하여 다시 넣음
        # (현재 종료 시점 + 심사 소요 시간)을 계산하는 것이 곧 '대기'를 포함한 논리
        heapq.heappush(heap, (finish_time + process_time, process_time))
        
    return answer

근데 지금 보니 입국심사를 기다리는 사람이 최대 10억명이다... 이런 식으로는 절대 시간 안에 문제를 풀 수 없다.
무조건 이분탐색으로 풀어야겠는데.
"""
def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        people = 0
        for time in times:
            people += mid // time
        
        if people >= n:
            answer = mid
            right = mid - 1
            
        else:
            left = mid + 1
    return answer