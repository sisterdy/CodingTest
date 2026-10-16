"""
공백을 기준으로 숫자를 분리한다.
최솟값과 최댓값을 찾는다.
이어 붙여 출력한다.
"""


def solution(s):
    answer = list(map(int, s.split(' ')))
    return str(min(answer)) +  " " + str(max(answer)) # 숫자는 이어 붙일 수 없으니 형변환