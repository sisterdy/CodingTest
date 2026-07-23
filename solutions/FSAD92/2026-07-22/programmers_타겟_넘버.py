"""
기존 풀이는 dfs였는데 상태를 stack에 직접 넣고 반복하는 방식이었고
이번에는 재귀형 dfs로 풀어보자
"""
def solution(numbers, target):

    def dfs(index, current_sum):
        # 모든 숫자에 부호를 붙였다면 최종 합 확인
        if index == len(numbers):
            if current_sum == target:
                return 1

            return 0

        current_number = numbers[index]

        # 현재 숫자에 +를 붙이는 경우
        plus_count = dfs(
            index + 1,
            current_sum + current_number
        )

        # 현재 숫자에 -를 붙이는 경우
        minus_count = dfs(
            index + 1,
            current_sum - current_number
        )

        # 두 갈래에서 찾은 성공 경우의 수를 합친다.
        return plus_count + minus_count


    return dfs(0, 0)