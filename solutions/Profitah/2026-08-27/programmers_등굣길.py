def solution(m, n, puddles):
    answer = 0  # (1,1)에서 (m,n)까지 이동하는 경우의 수

    # 시작점 (1,1)에서 한 번 이동한 두 칸의 경우의 수를 미리 초기값으로 설정.(점화식 적용을 위해)
    info = dict([((2, 1), 1), ((1, 2), 1)]) # 1,1로 시작하면  dp 점화식이 참조하는 값이 생기지 않아, 문제풀이를 할 수 없음.

    # # 웅덩이 좌표를 튜플로 변환하여 info 딕셔너리에 0으로 저장 (해당 위치로 갈 수 없음)
    for puddle in puddles: 
        info[tuple(puddle)] = 0 

    def func(m, n): # 탑다운(재귀+ 메모제이션) 방식으로 경우의 수 계산

        # 격자 밖이면 0 반환
        if m < 1 or n < 1:
            return 0

        # 이미 계산된 좌표면 바로 반환 (메모이제이션) 
        if (m, n) in info:
            return info[(m, n)]
        
        # 현재 좌표 = 위에서 등교하는 경우 + 왼쪽에서 등교하는 경우
        return info.setdefault(
            (m, n),
            func(m - 1, n) + func(m, n - 1)
        )

    # 최종 결과는 MOD 적용
    return func(m, n) % 1000000007

