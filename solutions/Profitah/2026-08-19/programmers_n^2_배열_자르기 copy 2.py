def solution(n, left, right):
    """
    [구해야 하는 것]
    n×n 크기의 배열(array[i][j] = max(i, j) + 1)을 한 줄로 이어붙인
    1차원 배열에서, left번째 인덱스부터 right번째 인덱스까지 잘라낸 값들을 구한다.

---
    [풀이 흐름]
    1. n이 최대 10^7이라 실제 n×n 배열을 만들면 메모리 초과가 나므로,
       배열을 직접 만들지 않고 필요한 구간의 값만 즉석에서 계산한다.
    2. left ~ right 범위의 각 1차원 인덱스(index)에 대해,
       divmod(index, n)으로 몫과 나머지를 구하면
       - 몫  = 원래 2차원 배열에서의 행(row) 번호
       - 나머지 = 원래 2차원 배열에서의 열(col) 번호
       가 된다. (한 행에 n개씩 원소가 들어있기 때문)
    3. 그 위치의 값은 문제 규칙대로 max(row, col) + 1 로 계산한다.
    4. 계산한 값들을 순서대로 리스트에 담아 반환한다.
    """
    # 정답(잘라낸 구간의 값들)을 담을 리스트
    result = []

    # 1차원으로 펼친 배열에서 left번째부터 right번째 인덱스까지 반복
    for index in range(left, right + 1):
        # index를 n으로 나눈 몫(row)과 나머지(col)를 동시에 구함
        row, col = divmod(index, n)

        # 문제 규칙: array[row][col] = max(row, col) + 1
        result.append(max(row, col) + 1)

    # left ~ right 구간에 해당하는 값들을 순서대로 반환
    return result