"""
범위가 10억명 이하라 사실상 이분탐색이 강제됨...
즉 10억 명을 한 명씩 다 집어 넣으며 시뮬레이션 할 게 아니라
mid분이 주어졌을 때 n명을 전부 처리 가능한가? 라는 지극히 이분탐색적인 사고로 접근해야 함.
"""
def solution(n, times):
    left = 1

    # 가장 빠른 심사관이 n을 모두 처리하는 시간은 반드시 정답 이상이 되니까 충분한 상한이 된다.
    right = min(times) * n

    # 이분탐색 시작
    while left < right:
        mid = (left + right) // 2

        # mid분 동안 모든 심사관이 처리할 수 있는 사람 수
        people = 0

        for time in times:
            people += mid // time

        # mid분 안에 n명 이상 처리할 수 있다면 더 작은 시간 범위에서 다시 탐색
        if people >= n:
            right = mid

        # n명을 처리할 수 없다면
        # mid 이하의 시간은 전부 불가능하므로 제외한다.
        else:
            left = mid + 1

    # left == right가 되는 순간,
    # n명을 처리할 수 있는 최초의 시간이 된다.
    return left