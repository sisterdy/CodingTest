"""
1. 시작 기둥에서 가장 큰 원판을 옮기기 위해 위 n-1개의 원판을 보조 기둥으로 옮긴다.
2. 가장 큰 원판을 종료 기둥으로 옮긴다.
3. 보조 기둥에 있는 원판을 종료 기둥으로 옮긴다.
"""
def solution(n):
    answer = []

    def move(count, start, end, middle):
        # 베이스 케이스
        if count == 1:
            answer.append([start, end])
            return

        move(count - 1, start, middle, end)
        answer.append([start, end])
        move(count - 1, middle, end, start)

    move(n, 1, 3, 2)

    return answer