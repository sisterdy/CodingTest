import sys
from itertools import combinations
# 조합?
# 21개 중 k - 5개를 뽑야야
# 비트마스킹으로도 할 수 있다고 함
# 가능한 알파벳 조합을 하나씩 시도하면서, 그 조합으로 읽을 수 있는 단어 개수를 세고, 최댓값을 찾는다

N, K = map(int, sys.stdin.readline().split()) # 단어 개수 , 알파벳 개수
chars = {'a', 'n', 't', 'i', 'c'} # 필수 글자들

if K < 5:
    print(0)
    exit()
if K == 26:
    print(N)
    exit()

words = []
answer = 0

# 단어들의 anta, tica만 빼고 무슨 문자로 이루어져 있는지
for i in range(N):
    word = sys.stdin.readline().strip()
    word = word[4:-4]
    words.append(set(word))
# print(words)
candidates = set('abcdefghijklmnopqrstuvwxyz') - chars

# 배울 수 있는 알파벳 모든 경우의 수
for comb in combinations(candidates, K - 5):
    learned = set(comb) | chars # 배운 조합의 문자들(선택글자와 필수 글자의 합집합)
    count = 0

    for word in words:
        # word가 배운것에 포함되는지 체크(부분집합인지) word와 learned모두 set이기 때문에 파이썬에서 이렇게 쓸 수 있다고 함
        if word <= learned:
            count += 1

    answer = max(answer, count)

print(answer)