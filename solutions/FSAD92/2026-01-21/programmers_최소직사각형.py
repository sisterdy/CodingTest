"""
모든 명함을 담을 수 있는 지갑 중 가장 작은 지갑

경우의 수
- 한 명함의 w,h가 다른 명함보다 크거나 같을 경우에는 해당 명함의 크기로 지갑 크기가 결정됨
- 그렇지 않은 경우, 가로가 가장 긴 명함을 제외한 명함 중 세로가 가장 긴 명함을 뒤집음.
- 재정렬된 명함들의 크기 중 가장 세로가 긴 명함이 최종 지갑 크기의 세로 크기가 됨.

def solution(sizes):
    # 가로가 가장 긴 명함의 길이를 기준으로 설정
    max_w = 0
    for w, h in sizes:
        if w > max_w:
            max_w = w

    # 세로가 가장 긴 명함을 찾아서 뒤집기
    for _ in range(len(sizes)):
        current_max_h = 0
        max_h_idx = -1
        
        # 현재 리스트에서 세로가 가장 긴 명함의 위치 탐색
        for i in range(len(sizes)):
            if sizes[i][1] > current_max_h:
                current_max_h = sizes[i][1]
                max_h_idx = i
        
        # 가로가 가장 긴 명함이 아니면서, 뒤집었을 때의 가로가 max_w를 넘지 않는다면 뒤집음
        if sizes[max_h_idx][0] < max_w:
            # 뒤집기 실행 (w <-> h)
            sizes[max_h_idx][0], sizes[max_h_idx][1] = sizes[max_h_idx][1], sizes[max_h_idx][0]
        else:
            # 더 이상 뒤집어서 이득을 볼 수 없다고 판단하면 중단
            break

    # 최종 지갑 크기 계산
    final_w = max(s[0] for s in sizes)
    final_h = max(s[1] for s in sizes)
    
    return final_w * final_h


기본 코드는 이건데, 이렇게 하면 for 루프 안에서 max()를 다시 호출하여 계산 복잡도가 O(N^2)가 됨...
게다가 통과도 못했음

기본 코드의 문제는 가로가 가장 긴 명함을 미리 고정하는 전제를 박아버린 것.
추후 명함을 뒤집었을 때 그 값이 새로운 '가장 긴 가로'가 될 수도 있는데 이 케이스에 대한 대처를 하지 못함

"""

def solution(sizes):
    max_w = 0  # 긴 변들 중 최댓값
    max_h = 0  # 짧은 변들 중 최댓값

    for w, h in sizes:
        # 현재 명함의 긴 쪽과 짧은 쪽을 구분
        longer = max(w, h)
        shorter = min(w, h)
        
        # 모든 명함을 넣으려면 당연히 지갑의 가로는 명함들의 긴 변들 중 최대여야 한다
        if longer > max_w:
            max_w = longer
            
        # 똑같이 모든 명함을 넣으려면 지갑의 세로는 명함들의 짧은 변들 중 최대여야 한다
        if shorter > max_h:
            max_h = shorter
            
    return max_w * max_h