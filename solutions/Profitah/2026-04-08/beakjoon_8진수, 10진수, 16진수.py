#백준 11816
"""
파이썬 startswith() 메서드는 문자열이 특정 접두사로 시작하는지 여부를 확인하는 데 사용됩니다.
이 메서드는 문자열이 지정된 접두사로 시작하면 True를 반환하고, 그렇지 않으면 False를 반환합니다.

true인 경우 파이썬 자체 기능을 사용하여 16진수 또는 8진수를 10진수로 변환합니다.

return int(문자열, 진법)

파이썬, 해죠!

"""

# 8진수를 10진수로 변환하는 함수
def jinsu8_to_jinsu10(x):
    return int(x, 8)

#16진수를 10진수로 변환하는 함수
def jinsu16_to_jinsu10(x):
    return int(x, 16)

#10진수는 그대로 출력
def jinsu10_to_jinsu10(x):
    return int(x)

x = input() # 입력값 받기

if x.startswith('0x'): # 16진수인 경우 
    #startswith(): 문자열이 특정 접두사로 시작하는지 여부를 확인하는 메서드
    print(jinsu16_to_jinsu10(x))
elif x.startswith('0') and len(x) > 1: # 8진수
    print(jinsu8_to_jinsu10(x))
else: # 10진수
    print(jinsu10_to_jinsu10(x))
