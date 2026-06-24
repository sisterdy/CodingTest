"""
문자열에 포함된 숫자와 영단어("zero" ~ "nine")를 모두 숫자로 변환하여
최종 정수 값을 반환하라.
"""

def solution(s): 
    dic = { # 문제에 제시된 대로 문자열을 읽고 숫자를 반환할 수 있도록 매핑
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = ""
    word = ""

    for strings in s:
        if strings.isdigit(): # 숫자라면
            answer += strings # 그대로 answer에 넣고
        else: # 아니면
            word += strings # 문자열 누적을 위해 word에 넣는다.
            if word in dic:  # 이후 누적된 문자열이 dic에 있는 것을 확인
                answer += dic[word] # word와 매칭되는 key의 value를 반환받아 answer에 집어 넣고
                word = "" # 다음 탐색을 위해 word 초기화

    return int(answer) # answer 반환