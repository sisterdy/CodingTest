"""
큐 그리디

가장 무거운 사람과 가장 가벼운 사람을 함께 다뤄야 함으로
양방향 삽입 삭제가 가능한 큐 구조가 적합하며.

어떤 경우에도 가장 큰 값과 가장 작은 값을 찾는 그리디 알고리즘을 사용하는 문제이다.

1. people 리스트를 덱으로 만든 후 내림차순 정렬

2. 무거운 사람(왼쪽)과 가벼운 사람(오른쪽)을 인덱스로 매칭

3. 합이 보트 무게보다 가벼우면 둘 빼냄

4. 보트 무게보다 무거우면 무거운 사람만 빼냄

전형 적인 큐 문제
"""

from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    deq = deque(people)
    answer = 0

    while deq:
        if len(deq) == 1:  # deq[0],  deq[-1] 이 같은 사람인 경우를 가정해 예외처리
            answer += 1
            break

        if deq[0] + deq[-1] > limit:
            deq.popleft()
        else:
            deq.popleft()
            deq.pop()

        answer += 1 #people이 한명 이상임으로, 한 번 이상 구명보트 사용할 것.

    return answer