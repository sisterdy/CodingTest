# left~right 의 요소들을 2차원배열에서 몇행 몇열인지 알아내기
# 행과 열 중 큰 것 고른다 
def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        
        answer.append(max(row, col) + 1)
        
    return answer