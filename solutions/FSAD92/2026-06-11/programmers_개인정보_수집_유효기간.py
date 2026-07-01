"""
사실상 YYYY.MM.DD를 어떻게 계산할 것인가 가 메인인 문제 아닌가.
한 달이 28일
1년이 336일

date_to_int
    YYYY의 마지막 문자열 2개를 int로 바꾸고(2000 <= YYYY <= 2022) 336일을 곱하고
    MM을 int로 바꾸고 28일을 곱하고
    DD를 int로 바꾸고 더함
    
int_to_date
    int를 336으로 나눈 몫을 문자열로 변환 -> 문자열 '20'의 뒤에 붙임
    그 나머지를 28로 나눈 몫을 문자열로 변환 -> 그 뒤에 붙임
    그 나머지를 문자열로 변환 -> 그 뒤에 변환
    
terms를 언패킹해서 딕셔너리에 저장
today를 date_to_int 함수에 넣음

privacies를 순회하면서 date_, term으로 언패킹하고
date_를 date_to_int함수에 넣은 반환값 + (terms[term] * 28) 한 값과 비교해서
today가 그 값보다 크면 유효기간이 지났다는 거니까 result에 answer에 append
"""
def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    privacies_list = []
    
    for i in range(len(terms)):
        kind, duration = terms[i].split()
        term_dict[kind] = int(duration)
    
    for i in range(len(privacies)):
        date_, term_ = privacies[i].split()
        privacies_list.append((date_, term_))
    
    def date_to_int(date):
        year = int(date.split('.')[0][2:4])
        month = int(date.split('.')[1])
        day = int(date.split('.')[2])
        
        return (year * 336) + (month * 28) + day
    
    today_int = date_to_int(today)
    
    for i in range(len(privacies_list)):
        # 유효기간 끝나는 날 = 수집일 + 약관기간 - 1일
        if date_to_int(privacies_list[i][0]) + (term_dict[privacies_list[i][1]] * 28) <= today_int:
            answer.append(i + 1)
    
    return answer
