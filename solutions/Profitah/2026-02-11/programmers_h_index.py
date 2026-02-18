"""“h번 이상 인용된 논문이 h편 이상일 때,
그 중 최대 h값을 구하자.

완전탐색을 통해 조건이 만족될 때마다
점점 더 큰 h값이 가능한지 확인하는 과정을 거치도록 하자.

h인덱스 : 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값
(https://school.programmers.co.kr/questions/64629)

[10, 8, 5, 4, 3] 의 인용횟수를 가진 교수가 있다면
10번 이상 인용 횟수를 가진 논문은 1편입니다. 이때 H-Index는 1입니다.
8번 이상 인용 횟수를 가진 논문은 2편입니다. 이때 H-Index는 2입니다.
5번 이상 인용 횟수를 가진 논문은 3편입니다. 이때 H-Index는 3입니다.
4번 이상 인용 횟수를 가진 논문은 4편입니다. 이때 H-Index는 4입니다.
3번 이상 인용 횟수를 가진 논문은 5편입니다. 이때 H-Index는 3입니다.

"""

def solution(citations):
    # 전체 논문 개수
    num_documents = len(citations)
    
    # 인용 횟수를 내림차순 정렬
    # 가장 많이 인용된 논문부터 확인해야하기에 가장많이 인용된 논문부터 앞에 오도록 정렬 
    citations.sort(reverse=True)

    # H-Index 값을 저장할 변수
    H = 0

    # 정렬된 논문을 앞에서부터 하나씩 확인
    for i in range(num_documents):
        # 현재 논문의 인용 횟수
        cit_num = citations[i]

        # H-index 조건:
        # (i+1)편 이상의 논문이 각각 (i+1)번 이상 인용되었는가?
        # i는 0부터 시작하므로 논문 수는 i+1
        if cit_num >= i + 1:
            # 조건을 만족하면 H 값을 i+1로 갱신
            H = i + 1
        else:
            # 조건을 만족하지 않으면 이후는 더 작은 값이므로 종료
            break

    # 최종 H-index 반환
    return H
