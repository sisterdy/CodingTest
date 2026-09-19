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