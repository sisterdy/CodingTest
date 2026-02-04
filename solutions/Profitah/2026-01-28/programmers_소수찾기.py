from itertools import permutations  
from collections import deque  

def solution(numbers):
    # 소수 판별 함수 (주어진 로직 사용)
    def is_prime(num):
        if num < 2:  # 0과 1은 소수가 아니므로 False 반환
            return False
        
        check = deque()  # 약수를 저장할 deque 생성
        
        # num이 소수인지 확인: 2부터 num의 제곱근까지 확인하며
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:  # num이 i로 나누어떨어지면 (약수 발견)
                check.append(i)  # 약수를 check에 추가
        
        return len(check) == 0  # 약수가 없으면(= 소수이면) True, 있으면 False
    
    # 만들 수 있는 모든 숫자 조합 생성
    possible_numbers = set()  # 같은 조합 출력되는 것 막기 위해 중복을 자동으로 제거하는 set 사용.
    
    # 1자리부터 len(numbers)자리까지 모든 순열 생성
    for length in range(1, len(numbers) + 1):  # 자릿수: 1자리, 2자리, ..., 전체 자리
        for perm in permutations(numbers, length):  # 해당 자릿수의 모든 순열 생성
            num_str = ''.join(perm)  #튜플을 문자열로 반환한뒤 공백없이 합치기.
            num = int(num_str)  # 문자열을 정수로 변환 
            possible_numbers.add(num)  # set에 추가 (중복은 자동 제거됨)
    
    # 소수 개수 세기
    answer = 0  # 소수 개수를 저장할 변수
    for num in possible_numbers:  # 만들어진 모든 숫자를 순회
        if is_prime(num):  # 해당 숫자가 소수인지 확인
            answer += 1  # 소수면 카운트 증가
    
    return answer  # 최종 소수 개수 반환