"""
dfs 대신 라이브러리를 사용해보자.
from itertools import product를 사용하면 repeat 파라미터에 입력하는만큼 문자열을 만들어 줌
"""
from itertools import product

def solution(word):
    dictionary = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    # 여기까지는 동일
    
    # 길이 1~5개의 단어 모두 생성
    for length in range(1, 6):
        for chars in product(vowels, repeat = length):
            dictionary.append(''.join(chars))   # 튜플 chars를 문자열로 바꿔서 저장
            
    dictionary.sort()   # 사전 순서니까
    
    return dictionary.index(word) + 1
