"""
기존 코드 : 테스트 케이스는 통과했으나, 효율성 테스트는 실패함.

def solution(phone_book):
    answer = 0
    
    sorted_book = sorted(phone_book)
    
    
    for i in range(len(sorted_book)):    # phone_book을 순회한다.
        standard = sorted_book[i]    # i번째 전화번호를 standard로 삼는다
        for j in range(len(sorted_book)):   # standard 외 다른 번호를 비교하러 간다
            if i != j:  # 같은 전화번호가 아닌 경우만
                if standard.startswith(sorted_book[j]): # 만약 standard가 sorted_book[j]로 시작한다면
                    answer += 1 # answer에 1을 추가한다
                    break   # 그리고 for문을 나온다
            else:   # 같은 전화번호일 경우에는 그냥 패스한다
                pass
            
    return answer == 0   # 만약 answer가 0보다 크면 True를, 아니면 False를. 
"""

def solution(phone_book):
    phone_set = {num for num in phone_book}
    
    for phone_number in phone_book: # 모든 전화번호를 순회
        prefix = ''
        
        for number in phone_number: # 각 번호의 글자를 하나씩 붙여가며 접두어를 만듦
            prefix += number 
            
            if prefix in phone_set and prefix != phone_number:   # 만약 만든 접두어가 set에 존재하고, 그 접두어가 자기 자신, 즉 phone_number 가 아닌 경우
                return False    # False 출력
    return True # 아닐 경우 True 출력