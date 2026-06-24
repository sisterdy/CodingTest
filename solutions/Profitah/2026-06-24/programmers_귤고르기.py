"""
귤 k개를 선택했을 때, 선택한 귤의 크기(종류) 수의 최솟값을 구하라.
"""
from collections import defaultdict

def solution(k, tangerine):
    # defaultdict(int)를 사용. (defalutdict는 value가 존재하지 않을 때 
    #                         자동으로 default값을 반환하는 딕셔너리)  이게 맞지 않냐 키말고?
    #
    # size_count에 들어온 모든 값을 value가 정수인 딕셔너리로 초기화
    # == value가 없는 key값에 접근하면 0이 value인 딕셔너리가 됨.
    size_count = defaultdict(int) 

    # 귤 크기별 개수 세기
    for size in tangerine:
        size_count[size] += 1 # 해시테이블 구조로 key찾고 value값 1씩 증가

    # 크기별 개수(values) 만 리스트로 추출
    counts = list(size_count.values())

    # 개수가 많은 순으로 정렬
    counts.sort(reverse=True)

    # 선택한 귤의 종류 수
    kind = 0

    # 개수가 많은 종류부터 선택
    for count in counts:

        # 현재 종류의 귤을 모두 선택
        k -= count

        # 선택한 종류 수 증가
        kind += 1

        # k개 이상 선택했다면 종료
        if k <= 0:
            break

    # 최소 종류 수 반환
    return kind