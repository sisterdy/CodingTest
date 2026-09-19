"""
targets: 폭격 미사일의 x 좌표 범위 목록
s:  start. 폭격 미사일의 x좌표 첫 시작
e : end. 폭격 미사일의 x좌표 끝점
"""

# 미사일 1개의 끝점을 가지고 오는 함수 매개변수의 이름은 ms로 함..ㅋㅋㅋ  mㅣ sㅏ 일
def get_end(ms):
    return ms[1] 
    
# 미사일들을 끝점 기준으로 정렬한 뒤,
# 그리디하게 순회하며 필요한 최소 요격 횟수를 구하는 함수
def solution(targets):
    targets.sort(key=get_end) # get_end 함수가 반환하는 값을 key값으로 정렬 (= ms[1]. 즉, 미사일 끝점을 기준으로 정렬)
    
    result = 0 # 요격횟수
    last_pos = None # 마지막 요격 위치
    
    for s, e in targets: # targets의 각 원소 [시작점, 끝점]을 s, e로 구조분해하여 전체 순회
        if last_pos is None or s >= last_pos: # 첫 요격이거나, 시작점(s)이 이전 요격 위치 이상이면 요격되지 않은 미사일이므로
            result += 1 # 요격횟수를 증가시키고 
            last_pos = e # 마지막 요격 위치를 현재 미사일의 끝점(e)으로 갱신
    
    return result # 이후 결과 반환