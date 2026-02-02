"""
0 또는 양의 정수
정수를 이어 붙여 만들 수 있는 가장 큰 수

numbers로 만들 수 있는 모든 경우의 수를 만들어야 하는데...

근데 좀 더 시간 복잡도를 줄일 수 있는 방법이 있을까
일단 모든 원소를 문자열로 변환 후
해당 문자열 숫자의 첫번째 문자가 가장 큰 게 앞으로 와야 한다.

사실 이 문제는 풀지 못했다. 로직적으로도 생각이 나지 않았다.
제미나이를 이용해 물어보니, 
"""

def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key = lambda x: x * 3, reverse = True)
    answer = "".join(str_numbers)
    return str(int(answer)) # numbers의 원소는 0 이상부터니까, '000'같은 사례를 방지하기 위해 int로 한번 변환했다가 다시 str로 변환