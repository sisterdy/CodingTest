# 만약 w < h 라면 뒤바꾼다.

def solution(sizes):
    maxW = 0
    maxH = 0
    for e in sizes:
        print(e)
        if e[0] < e[1]:
            maxW = max(maxW, e[1])
            maxH = max(maxH, e[0])
        else:
            maxW = max(maxW, e[0])
            maxH = max(maxH, e[1])
    return maxW * maxH