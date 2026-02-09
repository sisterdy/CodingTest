"""
ASCII
A = 65
Z = 90

총 조작 횟수는 업다운과 가로방향의 합.

맨 처음 A로 시작
A부터 N까지는 조이스틱을 위로 입력 -> up = ord(ch) - ord('A')
O부터 Z까지는 조이스틱을 아래로 입력하는 게 유리함 -> down = ord('Z') - ord(ch) + 1
즉 min(up, down)을 이용하면 업다운은 최소 경로를 찾을 수 있음

여기까지는 생각했는데 그 이후로는 gpt의 도움을 받았다.
가로 방향을 어떻게 그리디로 접근해야 할지 도달하지 못했다.
"""

def solution(name):
    n = len(name)
    
    vertical = 0
    for ch in name:
        up = ord(ch) - ord('A')
        down = ord('Z') - ord(ch) + 1
        vertical += min(up, down)
    
    
    # 가로 방향 프로세스
    horizontal = n - 1  # 시작 커서부터 끝 커서까지 가는 비용으로 초기화.
    
    # 하지만 'A'가 연속된 구간이 있다면 우회(되돌아가기 or 반대편 먼저 처리하기)하는 게 더 이득이 될 수 있음
    # 즉 기본 horizontal 값보다 더 작은 값을 찾을 수도 있다.
    
    # 연속된 'A' 구간을 찾는 여정
    for i in range(n):
        j = i + 1
        
        # i + 1, 즉 i 다음부터 연속된 'A'를 최대한 건너뜀
        while j < n and name[j] == 'A':
            j += 1  # 'A' 구간 바로 다음 인덱스 위치가 j가 된다.
            
        #BAAAB    
        # 후보1 : 오른쪽으로 i까지 갔다가 되돌아오고, 남은 구간(끝쪽)을 처리
        candidate_1 = 2 * i + (n - j)
        
        # 후보2 : 끝쪽을 먼저 처리하고(왼쪽으로 이동해서), 다시 i까지 가기.
        candidate_2 = i + 2 * (n - j)
        
        horizontal = min(horizontal, candidate_1, candidate_2)
    
    return vertical + horizontal