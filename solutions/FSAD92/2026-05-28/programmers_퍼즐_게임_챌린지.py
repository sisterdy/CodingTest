"""
1씩 증가하는 식으로 반복문을 도는 건 시간복잡도(10의 15승)를 생각했을 때 불가능

최솟값이니까 투 포인터?
투 포인터를 사용해서 범위를 줄여나가야 한다
limit보다 작으면 숙련도를 낮춰보고, 크면 늘리는 방식으로.
"""
def solution(diffs, times, limit):
    low = 1
    high = max(diffs)
    answer = high

    # 단일 퍼즐의 소요 시간만 계산하는 함수
    def get_puzzle_time(diff, cur_time, prev_time, level):
        if diff <= level:
            return cur_time
        
        # 숙련도 부족 시 발생하는 패널티 시간 계산
        fail_count = diff - level
        return fail_count * (cur_time + prev_time) + cur_time

    # 모든 퍼즐을 순회하며 총 합계 계산
    def get_total_duration(level):
        total = 0
        prev_time = 0
        for i in range(len(diffs)):
            total += get_puzzle_time(diffs[i], times[i], prev_time, level)
            prev_time = times[i]
            
            # 중간에 limit을 넘으면 더 계산할 필요 없음
            if total > limit:
                return total
        return total

    # 이진 탐색 메인 루프
    while low <= high:
        mid = (low + high) // 2
        if get_total_duration(mid) <= limit:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return answer