"""
논문의 인용 횟수를 담은 배열 citatitons
발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 h-index
list의 가운데 인덱스부터 구하는 이진 탐색을 할까?
"""
def solution(citations):
    answer = 0
    
    # start, end 포인터 초기화
    start = 0
    end = len(citations)
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        
        # 배열 전체 순회하며 mid번 이상 인용된 논문 개수 카운팅
        for citation in citations:
            if citation >= mid:
                count += 1
        
        # mid번 이상 인용된 논문이 mid개 이상이어야 함
        if count >= mid:
            answer = mid    # 현재 mid는 가능한 답이니 일단 저장하고
            start = mid + 1     # 더 큰 값도 가능한지?
        else:
            end = mid - 1   # mid번 이상 인용된 논문이 mid개 이상이 아니면 값을 줄여서 다시 트라이
            
    return answer