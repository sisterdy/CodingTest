# e를 기준으로 오름차순 정렬
def solution(targets):
    answer = 0
    last = -1 # 마지막으로 발사한 위치
    
    targets.sort(key=lambda x: x[1])
    
    for s, e in targets:
        if s < last:
            continue
        answer += 1
        last = e
    return answer