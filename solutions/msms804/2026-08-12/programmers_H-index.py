# 0편 이상 인용된 논문 5
# 1편 이상 ...      4
# 3편 이상 ...      3 -> 정답

def solution(citations):
    answer = 0
    
    # 인용 횟수를 오름차순 정렬
    citations.sort()
    
    n = len(citations)
    
    for i in range(n):
        # 현재 위치부터 끝까지 남은 논문 개수(n - i) 이상이라면 h index 반환
        if citations[i] >= n - i:
            return n - i
    return answer