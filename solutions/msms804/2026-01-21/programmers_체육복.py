# 차이가 1이 난다면 빌려준다
# 2중 for문?
# 큐를 써야하나?

def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost)
    reserve_set = set(reserve)
                
    # 겹치는 애 제거
    lost_only = lost_set - reserve_set
    reserve_only = reserve_set - lost_set
    
    for i in lost_only:
        if i - 1 in reserve_only:
            reserve_only.remove(i - 1)
        elif i + 1 in reserve_only:
            reserve_only.remove(i + 1)
        else: 
            n -= 1
    return n