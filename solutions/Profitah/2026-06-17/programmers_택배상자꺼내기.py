"""
[스택/시뮬레이션] 택배 상자 꺼내기

구해야할것: 꺼낸 상자 개수
"""
def solution(n, w, num):
    answer = 0
    h = n//w+1      # 높이
    x = 1           # 상자 번호
    storage = []    # 창고
    
    for i in range(h):
        t = []
        for j in range(w):
            if x <= n:  # n보다 작은 상자들
                t.append(x)
                x += 1
            else:       # n보다 큰 빈 공간은 0으로
                t.append(0)
        
        if i % 2 == 0:  # 정방향 라인
            storage.append(t)
        else:           # 역방향 라인
            t.reverse()
            storage.append(t)
            
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j] == num:
                d = i
                while d < h and storage[d][j]:    # 꺼낼 박스가 있으면
                    answer += 1
                    d += 1	# 아래로 내려감
    
    return answer