"""
문제 요약:
'antartica' 단어를 읽으려면 a, n, t, i, c 5글자는 반드시 가르쳐야 한다.
K개의 글자를 가르쳐서 읽을 수 있는 단어의 최대 개수를 구한다.

사용한 자료구조: set, list

풀이 과정:
1. a, n, t, i, c는 필수 글자이므로 base set에 저장
2. K < 5 이면 필수 글자조차 못 가르치므로 0 출력
3. K >= 5 이면 나머지 21글자(learnable) 중 K-5개를 선택하는 모든 조합을 탐색
4. 각 조합마다 base | 조합 = known set을 만들고
   known set으로 읽을 수 있는 단어 수를 카운트
5. 모든 조합 중 최대 카운트를 출력
"""


import sys
from itertools import combinations # 조합을 구하는 함수인 combinations를 itertools 모듈에서 가져온다. 
# combinations(iterable, r)은 iterable에서 r개의 요소를 뽑는 모든 조합을 반환하는 함수이다.

input = sys.stdin.readline 

N, K = map(int, input().split()) # N은 단어의 개수, K는 가르칠 수 있는 글자의 개수이다. map() 함수를 사용하여 입력받은 문자열을 정수로 변환한다.
words = [set(input().rstrip()) for _ in range(N)] # N개의 단어를 입력받아 각 단어를 set으로 변환하여 리스트에 저장한다. rstrip()을 사용하여 개행문자를 제거한다.

base = {'a','n','t','i','c'} # a, n, t, i, c는 반드시 가르쳐야 하는 글자이므로 base set에 저장한다.

if K < 5: # K가 5보다 작으면 a, n, t, i, c를 모두 가르칠 수 없으므로 어떤 단어도 읽을 수 없다. 
    print(0) # 따라서 0을 출력한다.
else: # K가 5 이상이면 a, n, t, i, c를 가르칠 수 있으므로 나머지 글자 중에서 K-5개를 선택하여 가르칠 수 있다.
    alphabet = set(chr(i) for i in range(ord('a'), ord('z')+1)) # a부터 z까지의 모든 글자를 아스키코드로 변환해 (ord함수 사용) set으로 저장한다.
    learnable = alphabet - base # base를 제외한 나머지 글자들을 learnable set에 저장한다.

    answer = 0 # 가르칠 수 있는 글자 조합 중에서 읽을 수 있는 단어의 최대 개수를 저장할 변수 answer를 0으로 초기화한다.

    for comb in combinations(learnable, K-5): # learnable에서 K-5개의 글자를 선택하는 모든 조합을 구한다. combinations 함수는 learnable에서 K-5개의 요소를 뽑는 모든 조합을 반환한다.
        known = base | set(comb) # base와 선택한 글자 조합을 합쳐서 known set을 만든다. | 연산자는 두 집합의 합집합을 구하는 연산자이다.

        count = 0 # known set에 포함된 글자들로 읽을 수 있는 단어의 개수를 세는 변수 count를 0으로 초기화한다.
        for word in words: # words 리스트에 있는 각 단어에 대해 known set이 그 단어의 부분집합인지 확인한다.
            if word <= known:   # word가 known의 부분집합인가
                count += 1 # word가 known의 부분집합이면 count를 1 증가시킨다.

        answer = max(answer, count) # 현재 조합에서 읽을 수 있는 단어의 개수 count가 answer보다 크면 answer를 count로 업데이트한다. max() 함수는 두 값 중에서 큰 값을 반환한다.

    print(answer) # 모든 조합을 확인한 후에 answer에는 읽을 수 있는 단어의 최대 개수가 저장되어 있으므로 이를 출력한다.