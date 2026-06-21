"""
지민이가 펼칠 수 있는 정사각형 돗자리의 한 변 길이 구하기
1. mats(지민이 돗자리 한 변의 길이)를 내림차순 정렬해 큰 돗자리부터 확인
2. park 영역이 전부 비어있는지(-1) 확인
3. 모든 칸이 비어있으면 해당 크기 반환, 끝까지 불가능하면 -1 반환
"""
def solution(mats, park):
    # 1. 가장 큰 돗자리부터 확인해야 가장 큰 돗자리를 빠르게 찾을 수 있음
    mats.sort(reverse=True)

    rows = len(park)     # 공원 세로 길이
    cols = len(park[0])  # 공원 가로 길이
    
    # 2. 돗자리 너비 측정
    for mat in mats:  # 답을 구할 때까지 mats를 모두 살펴보자.
        
        # 시작점 (i,j)의 범위를 mat만큼 줄여 효율적인 탐색 ㄱㄱ
        for i in range(rows - mat + 1):  # 세로 시작점
            for j in range(cols - mat + 1):  # 가로 시작점

                # 3. 사람들이 미리 차지한 자리는 제외
                #(i,j)에서 시작하는 mat x mat 영역을
                # r(세로 방향)과 c(가로 방향)으로 한 칸씩 이동하며 전부 확인
                # 하나라도 "-1"이 아니면 (사람이 있으면) False → 다음 위치로
                if all(park[i+r][j+c] == "-1"
                       for r in range(mat)   # 세로 0 ~ mat-1
                       for c in range(mat)): # 가로 0 ~ mat-1
                    return mat  # 전부 비어있으면 해당 크기 반환

    return -1  # 어떤 돗자리도 깔 수 없는 경우