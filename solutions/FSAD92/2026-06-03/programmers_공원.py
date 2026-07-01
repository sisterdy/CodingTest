"""
정사각형 모양 돗자리. 한 변의 길이가 여러 개 주어지네.. -> mats
예제에는 4x4가 제일 크지만, 5,3,2 밖에 갖고 있지 않으므로 지민이가 깔 수 있는 가장 큰 돗자리는 3x3이구나
현재 공원의 자리 배치도 -> park, 아무런 돗자리도 깔 수 없으면 -1 리턴

핵심은 빈 자리 중 가장 큰 정사각형의 크기를 구하는 거구나.
park를 순회하면서 park[i][j]가 -1인 곳을 발견하면 bfs로 최대 돗자리 크기를 구해야 하나?
bfs가 끝나면 max함수로 기존의 최대 크기와 지금 발견한 후보 크기를 갱신하고.
"""
from collections import deque

def solution(mats, park):
    n = len(park)
    m = len(park[0])
    max_found = -1  # 찾은 빈 공간 중 가장 큰 한 변의 길이. -1인 이유는 돗자리를 깔 수 없을 때를 대비해서.
    
    def get_max_square(r, c):   # (세로, 가로). 돗자리를 깔기 시작할 좌상단 꼭짓점. 
        size = 1    # 이미 park[r][c]가 -1임을 확인하고 이 함수를 호출하니 최소 크기는 1임
        
        while True:
            new_r, new_c = r + size, c + size
            
            if new_r >= n or new_c >= m:    # 경계 체크
                break
                
            is_possible = True
            
            # 오른쪽으로 새로 추가되는 세로줄 검사
            for i in range(r, new_r + 1):
                if park[i][new_c] != '-1':  # 다른 돗자리가 깔렸으면 False
                    is_possible = False
                    break
            if not is_possible:     # while문 break용
                break
                
            # 아래쪽으로 새로 추가되는 가로줄 검사
            for j in range(c, new_c + 1):
                if park[new_r][j] != '-1':
                    is_possible = False
                    break
            if not is_possible:     # while문 break 용
                break
                
            size += 1   # 모든 검사를 통과했다면 정사각형을 한 겹 키움
        return size
    
    # 모든 돗자리 칸을 순회하며 -1일 때만 확장 시도
    for i in range(n):
        for j in range(m):
            if park[i][j] == '-1':
                max_found = max(max_found, get_max_square(i, j))
    
    mats.sort(reverse=True)
    for size in mats:   # 내림차순으로 정렬된 돗자리 리스트를 하나씩 꺼내 검사.
        if size <= max_found:
            return size
                    
    return -1
