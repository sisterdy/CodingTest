# 일단 b + y 전체 개수 구함.
# brown + yellow = 가로 * 세로
# Yellow = (가로 - 2) * (세로 - 2)
# 언제 가능한지 전체 탐색
# 카펫의 가로길이 >= 세로길이

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for h in range(3, int(total ** 0.5) + 1):
        # 나누어 떨어지지 않는다면 무시
        if total % h != 0:
            continue
            
        w = total // h
        if (h - 2) * (w - 2) == yellow:
            return [w, h]