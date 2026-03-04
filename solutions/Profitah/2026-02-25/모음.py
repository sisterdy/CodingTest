"""
완전탐색 (모음사전)

길이 1~5까지 모든 모음 조합을 생성하고
사전순 정렬 후 해당 단어의 위치를 구하는 문제이다.
"""

from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    for i in range(1, 6):                               # 1. 길이 1~5 설정
        for comb in product(vowels, repeat=i):          # 2. 모든 조합 생성
            dictionary.append(''.join(comb))

    dictionary.sort()                                   # 3. 사전순 정렬
    index = dictionary.index(word)                      # 4. 단어 위치 찾기

    return index + 1                                    # 5. 1부터 시작하므로 +1