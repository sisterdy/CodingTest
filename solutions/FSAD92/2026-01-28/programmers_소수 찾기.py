"""
문자열의 모든 문자를 순회하며 리스트로 만들어야 한다.
그리고 해당 리스트로 만들 수 있는 모든 경우의 수를 리스트로 만든다.
해당 리스트의 원소를 int형으로 변환 후 소수인지를 체크 후 소수라면 카운트해서 리턴한다.
"""

from itertools import permutations

def is_prime(n):    # 소수인지 판별하는 함수
    if n < 2:   # 소수의 정의는 1과 자기 자신만으로 나누어떨어지는 1보다 큰 양의 정수
        return False
    for i in range(2, int(n ** 0.5) + 1):   # 제곱근보다 작은 범위에서 약수를 하나도 찾지 못했다면, 그보다 큰 범위에서도 약수는 절대 존재할 수 없다. 큰 약수가 있으려면 반드시 그와 짝을 이루는 작은 약수가 있어야 하기 때문
        if n % i == 0:  # 제곱근보다 작은 범위에서 약수를 찾았다면 약수가 존재하네?
            return False    # 바로 False
    return True # 못찾으면 True

def solution(numbers):
    answer = 0
    nums = list(numbers)    # 문자열을 list에 넣는 것만으로도 단순하게 각각의 문자가 원소인 리스트로 만들 수 있다.
    all_combinations = set()    # 011 같은 케이스에서 11과 11은 같지만 서로 다른 조합이다. 이런 경우를 방지하기 위해 중복 방지를 위한 set을 사용
    
    for i in range(1, len(nums) + 1):   # start를 1로 설정한 이유는, 0으로 할 경우 공백이들어가 int("".join(p))에서 ValueError를 낼 것이기 때문. 
        for p in permutations(nums, i): # permutations는 iterable에서 i개를 뽑아 순서를 고려하여 나열해 튜플 형태로 반환하는 함수. 즉 순열을 만들어주는 함수.
            num = int("".join(p))   # permutations가 반환한 원소를 순회하면서, 반환한 원소가 튜플 형태이기 때문에 join으로 붙여줌.
            all_combinations.add(num)
    
    for num in all_combinations:    # 모든 조합 리스트를 순회하면서
        if is_prime(num):   # 소수이면
            answer += 1 # 카운트
    
    return answer