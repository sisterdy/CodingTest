"""
sort 함수로 인덱스 번호에 있는 알파벳을 넘겨 정렬한다.
n번째 글자가 같으면 문자열 전체를 사전순으로 비교한다.
"""


def solution(strings, n):
    def sort_key(s):
        return (s[n], s)

    answer = sorted(strings, key=sort_key)
    return answer