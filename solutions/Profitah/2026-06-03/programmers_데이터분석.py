from operator import itemgetter # itemgetter는 리스트나 튜플에서 특정 인덱스의 값을 추출하는 함수

def solution(data, ext, val_ext, sort_by):
    # 1. 항목명을 인덱스 번호로 변환하기 위한 인덱스 매핑
    mapping = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    filter_idx = mapping[ext] # 필터링 기준이 되는 항목의 인덱스 추출
    
    filtered = []
    
    # 2. 기준값(val_ext)보다 작은 데이터만 추출하는 데이터 필터링
    for i in data:
        if i[filter_idx] < val_ext: # 조건에 부합하는 데이터인 경우
            filtered.append(i)       # 추출 리스트에 추가
    
    # 3. 지정된 정렬 기준(sort_by)에 따라 오름차순 정렬
    sort_idx = mapping[sort_by]            # 정렬 기준이 되는 항목의 인덱스 추출
    filtered.sort(key=itemgetter(sort_idx)) # 해당 인덱스를 기준으로 리스트 정렬
    
    return filtered