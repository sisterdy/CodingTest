"""
기존 방식은 h를 이진 탐색하고, 매번 전체 배열을 세는 방식이었음
이번에는 citations를 내림차순 정렬해서, i번째 논문이 i번 이상 인용되었다는 사실을 '그럼 당연히 그 앞의 논문들도 i번 이상 인용됐겠군'이라는 가설을 토대로 푼다.
"""
def solution(citations):
    # 인용 횟수가 많은 논문부터 확인하기 위해 내림차순
    citations.sort(reverse=True)

    answer = 0

    # i = 현재까지 확인한 논문 개수 -> 1부터 시작
    for i, citation in enumerate(citations, start=1):
        
        # i번째 논문도 i번 이상 인용되었다 -> i번 이상 인용된 논문이 최소 i편 존재한다.
        if citation >= i:
            answer = i

        else:
            break

    return answer