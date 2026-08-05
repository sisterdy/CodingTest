"""
(s,e) 개구간. 즉 s < x < e 를 만족하는 좌표에서만 쏠 수 있음.
일단 s를 기준으로 오름차순 정렬한다고 가정하고 미사일(구간)을 하나씩 만나보면...

if 새 구간의 시작점 s < 지금까지의 end
기존 묶음과 겹침
즉, end = min(end, e)

if 새 구간의 시작점 s >= 지금까지의 end
기존 묶음과 겹치지 않음
그러니 미사일이 한 발 더 필요함
즉, 새 묶음의 end = e
"""

def solution(targets):
    targets.sort()
    count = 1
    end = targets[0][1]
    
    for s,e in targets[1:]:
        if s < end:
            end = min(end, e)
        else:
            count += 1
            end = e
    
    return count