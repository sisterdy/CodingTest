"""
기존 풀이: permutations 사용

이번에는 dfs, 백트래킹으로 풀어보기
"""

def solution(numbers):
    answer = 0
    digit_counts = [0] * 10
    
    for char in numbers:
        digit = int(char)
        digit_counts[digit] += 1
        
    max_length = len(numbers)
    
    def is_prime(value):
        if value < 2:
            return False
        
        # 2부터 시작
        num = 2
        
        # 제곱근 이하에서 약수 존재하는지 확인
        while num * num <= value:
            if value % num == 0:
                return False
            
            num += 1
            
        return True
    
    def dfs(current_number, used_count):
        prime_count = 0

        # 숫자를 하나 이상 사용했다면 현재 숫자도 후보
        if used_count > 0 and is_prime(current_number):
            prime_count += 1

        if used_count == max_length:
            return prime_count

        for digit in range(10):
            if digit_counts[digit] == 0:
                continue

            # 첫 자리 0은 같은 정수를 중복 생성하므로 제외
            if used_count == 0 and digit == 0:
                continue

            digit_counts[digit] -= 1
            next_number = current_number * 10 + digit

            prime_count += dfs(next_number, used_count + 1)
            
            # 백트래킹 위한 숫자 복구
            digit_counts[digit] += 1
        return prime_count

    return dfs(0, 0)