"""
부등호 문제:
- 부등호의 개수와 방향이 주어졌을 때,
  0~9 정수 중 조건을 만족하는 숫자 조합의 최댓값과 최솟값을 구하는 문제.

풀이 방식:
- 백트래킹으로 0~9 숫자 조합을 탐색하며 부등호 조건을 만족하는지 확인.
- 0부터 오름차순으로 탐색하므로, 첫 번째 완성값 = 최솟값 / 마지막 완성값 = 최댓값.
- 조건을 만족하지 않으면 해당 경로의 탐색을 즉시 중단.
"""

n = int(input())                  # 부등호 개수
signs = input().split()           # 부등호 리스트 (예: ['<', '>', '<'])

visited = [0] * 10                # 숫자(0~9) 사용 여부 체크 (0: 미사용, 1: 사용 중)
max_value, min_value = "", ""     # 최댓값, 최솟값 저장 (문자열로 저장)


def is_valid(prev, curr, sign):
    """이전 숫자(prev)와 현재 숫자(curr)가 부등호(sign)를 만족하는지 확인하는 함수"""
    if sign == '<':
        return prev < curr  # '<' 조건: 이전 숫자가 현재 숫자보다 작아야 함
    if sign == '>':
        return prev > curr  # '>' 조건: 이전 숫자가 현재 숫자보다 커야 함
    return True             # 그 외의 부등호는 항상 통과 (확장성 고려)


def backtrack(depth, current_str):
    """
    백트래킹으로 숫자 조합을 탐색하는 함수
    - depth      : 현재 채우려는 자릿수 위치 (0번째 자리부터 시작)
    - current_str: 지금까지 확정된 자릿수들의 숫자 문자열
    """
    global max_value, min_value  # 함수 내부에서 외부 변수를 수정하기 위해 global 선언 필수

    # <-- 자릿수 완성 조건 --> #
    # depth == n+1 : 모든 자릿수(n+1개)가 채워진 상태
    if depth == n + 1:
        if not min_value:
            # min_value가 아직 비어 있으면 → 첫 번째 완성된 값이 최솟값
            # (0부터 오름차순으로 탐색하므로, 가장 먼저 완성된 값이 항상 최솟값)
            min_value = current_str
        else:
            # min_value가 이미 있으면 → 이후 완성되는 값으로 최댓값을 계속 갱신
            # (탐색이 진행될수록 더 큰 숫자 조합이 완성되므로, 마지막 완성된 값이 최댓값)
            max_value = current_str
        return  # 모든 자릿수가 확정됐으므로 탐색 종료

    # <-- 숫자 탐색 로직 --> #
    for num in range(10):  # 0~9 숫자 중 하나씩 선택 시도
        if not visited[num] and (                                                # 아직 사용하지 않은 숫자이고,
            depth == 0 or is_valid(current_str[-1], str(num), signs[depth - 1]) # 첫 번째 자리이거나 부등호 조건을 만족하면
        ):
            visited[num] = 1                                # 숫자 num을 사용 중으로 표시
            backtrack(depth + 1, current_str + str(num))   # 다음 자리 숫자 탐색
            visited[num] = 0                                # 탐색 후 사용 표시 해제 (백트래킹)


backtrack(0, "")  # 0번째 자리부터 탐색 시작

print(max_value)
print(min_value)