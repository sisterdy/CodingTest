"""
 n개의 원판을 조건에 맞게 최소 횟수로 3번 기둥까지 옮기는 이동 경로 전체 목록 구하기
 
 가장 큰 원판을 목적지로 보내기 위해, 위의 n-1개 원판을 경유지로 대피시키는 과정을 
 재귀 함수로 반복 구현.
 
 점화식 : T(n) = 2^n - 1
"""

def solution(n):
    answer = []
    
    # num: 옮길 원판 개수, from_col: 출발 기둥, to_col: 목적 기둥, other_col: 나머지 경유 기둥
    def hanoi(num, from_col, to_col, other_col):
        # [기저 조건] 옮길 원판이 1개뿐이라면 목적지로 바로 이동 후 재귀 종료
        if num == 1:
            answer.append([from_col, to_col])
            return
        
        # 1. 맨 밑의 가장 큰 원판을 제외한 (num - 1)개 원판을 경유지(other_col)로 대피시킴
        hanoi(num - 1, from_col, other_col, to_col)
        
        # 2. 맨 밑에 혼자 남은 가장 큰 원판 1개를 원래 목적지(to_col)로 이동시킵니다.
        answer.append([from_col, to_col])
        
        # 3. 경유지(other_col)에 대피해 있던 (num - 1)개 원판을 다시 목적지(to_col)로 이동시킴
        hanoi(num - 1, other_col, to_col, from_col)
    
    # 1번 기둥에 있는 n개의 원판을 2번을 거쳐 3번 기둥으로 옮기기 시작
    hanoi(n, 1, 3, 2)
    return answer