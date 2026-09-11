"""
2중 for문으로 완전탐색 하면 금방 찾을 것 같기는 한데
투포인터? 슬라이딩 윈도우?
"""
def solution(n):
    answer = 0
    left = 1
    total = 0

    for right in range(1, n + 1):
        total += right

        while total > n:
            total -= left
            left += 1

        # 현재 연속 구간의 합이 n이면 경우의 수 추가
        if total == n:
            answer += 1

    return answer