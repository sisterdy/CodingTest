# 모든 숫자 순열들을 뽑아낸다
# is_prime으로 소수인지 아닌지 판별
from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_sets = set() # 중복방지
    
    # numbers로부터 순열 구하기
    for i in range(1, len(numbers) + 1):
        for p in list(permutations(numbers, i)):
            num_sets.add(int(''.join(p))) # int를 사용하여 앞에 0이 오는 경우 제거

    # 소수라면 카운트 + 1
    for s in num_sets:
        if is_prime(s):
            answer += 1
    
    return answer