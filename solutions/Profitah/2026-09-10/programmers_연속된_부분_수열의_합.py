"""
구해야 하는 것 : sequence가 k가 되는 연속된 부분 수열 중, 조건을 만족하는 구간의 [시작 인덱스, 끝 인덱스]

사용한 자료구조 및 알고리즘 : map , 누적합
"""

def solution(sequence, k):
    n = len(sequence)
    
    # 1. 0번 인덱스가 0인 표준 누적합 배열 생성 (크기 n + 1)
    # P[i]는 sequence의 앞 i개 원소의 합 (P[0]=0, P[1]=seq[0], P[2]=seq[0]+seq[1] ...)
    P = [0] * (n + 1)
    for i in range(n):
        P[i + 1] = P[i] + sequence[i]
        
    # 2. 누적합 값의 '최초 등장 인덱스'를 기록하는 Map
    # P[i]의 i 값(0~n)을 그대로 저장
    pos_map = {}
    
    min_len = float('inf')
    answer = [0, 0]
    
    # 3. 누적합 배열 P를 순회하며 구간합 k 확인
    for j in range(n + 1):
        current_p = P[j]
        
        # P[j] - P[i] = k  =>  P[i] = P[j] - k
        target = current_p - k
        
        if target in pos_map:
            i = pos_map[target]
            # 누적합 성질: P[j] - P[i] = k 이면 실제 원소 구간은 [i, j-1]
            left = i
            right = j - 1
            current_len = right - left + 1  # 실제 구간의 길이
            
            if current_len < min_len:
                min_len = current_len
                answer = [left, right]
                
        # 각 누적합의 최초 등장 인덱스(j)만 저장
        if current_p not in pos_map:
            pos_map[current_p] = j
            
    return answer