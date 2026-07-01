"""
data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return

data[i]의 원소는 [코드 번호(code), 제조일(date), 최대 수량(maximum), 현재 수량(remain)] 형태
data[i][1]은 yyyymmdd 형태의 값을 가지며, 올바른 날짜만 주어집니다. (yyyy : 연도, mm : 월, dd : 일)

ext와 sort_by의 값은 다음 중 한 가지를 가집니다.
"code", "date", "maximum", "remain"
순서대로 코드 번호, 제조일, 최대 수량, 현재 수량을 의미

예제에서는 ext가 'date'니까, data[i][1]을 기준으로 val_ext보다 작은 값들을 찾아야 한다.

"""
def solution(data, ext, val_ext, sort_by):
    answer = []
    
    # ext와 sort_by는 문자열로 들어오기에 인덱스로 접근하기 위해 딕셔너리로!
    dict_data = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    dict_idx = dict_data.get(ext)
    sort_idx = dict_data.get(sort_by)
    
    for i in range(len(data)):
        if data[i][dict_idx] < val_ext:
            answer.append(data[i])
    
    answer.sort(key=lambda x: x[sort_idx])
    #print(type(val_ext))
    return answer
