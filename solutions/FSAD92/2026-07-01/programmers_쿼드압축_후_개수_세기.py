"""
예전에 백준에서 비슷한 문제를 풀었던 것 같은데...
누적합 배열로 풀어보자
"""
def solution(arr):
    n = len(arr)

    # prefix_sum[r][c] = arr의 (0, 0)부터 (r - 1, c - 1)까지 포함한 영역의 1 개수
    prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

    # 2차원 누적합 생성
    for r in range(n):
        for c in range(n):
            prefix_sum[r + 1][c + 1] = (
                arr[r][c]   # 현재 값
                + prefix_sum[r][c + 1]  # 위쪽까지의 합
                + prefix_sum[r + 1][c]  # 왼쪽까지의 합
                - prefix_sum[r][c]      # 겹쳐서 두 번 더해버린 왼쪽 위 영역
            )

    answer = [0, 0]  # [0의 압축 개수, 1의 압축 개수]

    def compress(row, col, size):
        # 현재 영역 안에 있는 1의 개수를 누적합으로 구하기
        one_count = (
            prefix_sum[row + size][col + size]  # 전체 큰 영역
            - prefix_sum[row][col + size]   # 위쪽 영역
            - prefix_sum[row + size][col]   # 왼쪽 영역
            + prefix_sum[row][col]          # 두 번 빼버린 왼쪽 위 영역
        )

        total_count = size * size

        # 1의 개수가 0개라면, 이 영역은 전부 0
        if one_count == 0:
            answer[0] += 1
            return

        # 1의 개수가 전체 칸 수와 같다면, 이 영역은 전부 1
        if one_count == total_count:
            answer[1] += 1
            return

        # 0과 1이 섞여 있다면 4등분해서 다시 압축 -> 재귀
        half = size // 2

        compress(row, col, half)                  # 좌상
        compress(row, col + half, half)           # 우상
        compress(row + half, col, half)           # 좌하
        compress(row + half, col + half, half)

    compress(0, 0, n)

    return answer