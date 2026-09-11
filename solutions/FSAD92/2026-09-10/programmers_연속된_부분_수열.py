"""
당연하겠지만 이중 for문으로 완전탐색 하면 편하겠지만...

수열과 k의 범위를 보니 결국 투포인터? 슬라이딩 윈도우?
사실상 숫자의 표현 문제의 업그레이드 버전이구나
"""
def solution(sequence, k):
    left = 0
    total = 0

    best_start = 0
    best_end = len(sequence) - 1
    best_length = len(sequence) + 1

    for right in range(len(sequence)):
        total += sequence[right]

        while total > k:
            total -= sequence[left]
            left += 1

        if total == k:
            current_length = right - left + 1

            # 더 짧은 구간을 발견하면 갱신
            if current_length < best_length:
                best_start = left
                best_end = right
                best_length = current_length

            # 길이가 같다면 시작 인덱스가 작은 구간 선택
            elif current_length == best_length and left < best_start:
                best_start = left
                best_end = right

    return [best_start, best_end]