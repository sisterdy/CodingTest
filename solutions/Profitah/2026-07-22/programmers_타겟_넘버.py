"""

주어진 numbers 배열의 각 숫자 앞에 + 또는 - 를 붙여
target 값을 만드는 모든 경우의 수를 구하는 문제.


재귀함수를 이용한 타겟 넘버 문제 풀이.

"""

def solution(numbers, target):
    n = len(numbers)

    def prefixSum(idx, result):
        
        # 기저조건
        if idx == n: 
            if result == target: 
                return 1 
            else: 
                return 0
            
        return (
            prefixSum(idx + 1, result + numbers[idx]) 
            +  prefixSum(idx + 1, result - numbers[idx]) # + - 인 경우 모두 구하고, 함수 실행 결과값 더하기.
        )

    return prefixSum(0, 0) # 재귀로 n (numbers) 모두 순회