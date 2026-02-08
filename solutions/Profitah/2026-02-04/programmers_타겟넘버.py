"""
재귀함수와 dfs를 이용한 타겟 넘버 문제 풀이

주어진 numbers 배열의 각 숫자 앞에 + 또는 - 를 붙여
target 값을 만드는 모든 경우의 수를 구하는 문제.


"""


def solution(numbers, target):
    n = len(numbers)  # 숫자 리스트의 길이 저장
    answer = 0       # 타겟을 만드는 경우의 수를 저장할 변수

    def dfs(idx, result):
        # idx: 현재 몇 번째 숫자까지 사용했는지 나타내는 인덱스
        # result: 지금까지 계산된 누적 합
        
        if idx == n:  # 모든 숫자를 다 사용했다면 (리프 노드 도달)
            if result == target:  # 누적 합이 목표값과 같으면
                nonlocal answer   # 바깥 함수의 answer 변수를 사용하겠다고 선언
                answer += 1       # 경우의 수 1 증가
            return  # 더 이상 탐색하지 않고 종료
        
        else:
            # 현재 숫자를 더하는 경우
            dfs(idx+1, result+numbers[idx])
            
            # 현재 숫자를 빼는 경우
            dfs(idx+1, result-numbers[idx])

    dfs(0,0)  # 인덱스 0부터, 누적합 0으로 탐색 시작
    return answer  # 최종 경우의 수 반환
