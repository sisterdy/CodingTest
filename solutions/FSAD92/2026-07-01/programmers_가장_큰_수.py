"""
기존 방식: 문자열을 x*3 반복해서 정렬 기준을 맞췄다.
3 -> 333
30 -> 303030
이런 식으로.

신규 방식은 3,30이 있다면 a+b(330), b+a(303) 이런 식으로 만들어서 a+b vs b+a 로 비교를 해서
두 숫자 중 어떤 걸 앞으로 오게 할지 결정하는 로직.
"""
from functools import cmp_to_key

def solution(numbers):
    str_numbers = list(map(str, numbers))

    # 두 숫자 문자열 a, b의 순서를 정하는 비교 함수
    def compare(a, b):
        case1 = a + b
        case2 = b + a

        # case1이 더 크면 a가 b보다 앞에 와야 한다.
        if case1 > case2:
            return -1

        if case1 < case2:
            return 1
        
        # 두 숫자가 같을 때 case
        return 0

    # 정렬 기준을 compare 함수로 사용
    str_numbers.sort(key=cmp_to_key(compare))

    answer = ''.join(str_numbers)

    # 전체가 '0'인 case 대비
    if answer[0] == '0':
        return '0'

    return answer