"""
n명의 사람이 입국심사를 받는 데 걸리는 최소 시간을 구하자

입력값 : n : 심사를 받아야 하는 사람 수
         times : 각 심사관이 한 명을 심사하는 데 걸리는 시간 리스트

풀이 : 이진 탐색 (Binary Search)

특정 시간 mid 안에 n명을 처리할 수 있는지 확인하면서
조건을 만족하는 최솟값을 탐색한다.

mid 시간 동안 각 심사관이 처리할 수 있는 인원 = mid // time
모든 심사관의 처리 인원 합계 >= n 이면 가능

탐색 범위 :
  left  = min(times)      # 최소 1명을 처리하는 시간
  right = max(times) * n  # 가장 느린 심사관이 n명 전부 처리하는 최악의 시간

출력값 : n명 모두 심사를 마치는 데 걸리는 최소 시간
"""

def solution(n, times):
    answer = 0  # 최종 정답(최소 시간)을 저장할 변수
    
    left = min(times)       # 이진 탐색 시작값: 가장 빠른 심사관 1명 처리 시간
    right = max(times) * n  # 이진 탐색 끝값: 가장 느린 심사관이 n명 전부 처리하는 최악의 시간
    
    while left <= right:  # 탐색 범위가 유효한 동안 반복
        mid = (left + right) // 2  # 현재 탐색 중인 시간(후보 정답)
        checked = 0  # mid 시간 동안 전체 심사관이 처리할 수 있는 총 인원 수
        
        for time in times:          # 각 심사관을 순회
            checked += mid // time  # 해당 심사관이 mid 시간 동안 처리할 수 있는 인원 누적
            if checked >= n:        # 이미 n명 이상 처리 가능하면 더 볼 필요 없으므로 조기 종료
                break
        
        if checked >= n:      # mid 시간 안에 n명 모두 처리 가능한 경우
            answer = mid      # 일단 정답 후보로 저장
            right = mid - 1   # 더 작은 시간도 가능한지 탐색 범위를 왼쪽으로 줄임
            
        elif checked < n:   # mid 시간으로는 n명을 다 처리 못하는 경우
            left = mid + 1  # 시간을 늘려야 하므로 탐색 범위를 오른쪽으로 줄임
            
    return answer  # 조건을 만족하는 최솟값 반환