"""
정수로 이루어진 테이블 data와 정수 col, row_begin, row_end가 주어졌을 때,
아래 규칙으로 계산한 테이블의 해시 값을 return 할 것.

※ col, row_begin, row_end는 모두 1부터 시작하는 번호이다.


"""

def solution(data, col, row_begin, row_end):
    # col번째 컬럼 오름차순, 같으면 첫 번째 컬럼 내림차순으로 정렬
    # (col은 1부터 시작하므로 인덱스는 col-1, 내림차순은 부호를 뒤집어 처리)
    data.sort(key=lambda row: (row[col-1], -row[0]))
    
    answer = 0
    
    # row_begin번째 행부터 row_end번째 행까지 확인
    for i in range(row_begin, row_end + 1):
        # i번째 행의 각 컬럼 값을 i로 나눈 나머지의 합 (i번째 행의 인덱스는 i-1)
        s_i = sum(value % i for value in data[i-1])
        
        # 구한 S_i를 answer에 누적 XOR
        answer ^= s_i
    
    return answer