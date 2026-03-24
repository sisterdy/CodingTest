"""
소수 경로 (그래프 + BFS)

4자리 소수를 다른 소수로 바꾸는 최소 횟수를 구하자.

규칙
한 번에 한 자리 숫자만 변경 가능
변경 후에도 반드시 소수여야 한다.

예시

1033 → 1733
→ 한 자리만 변경

이 문제는
최소 변경 횟수를 구하는 문제이므로
BFS(너비 우선 탐색)를 사용한다.

각 숫자를 노드로 보고
한 자리만 바뀐 소수로 이동한다.
"""

from collections import deque

# 소수 판별 배열
prime = [True] * 10000

prime[0] = False
prime[1] = False

for i in range(2, 100):
    if prime[i]:

        for j in range(i*i, 10000, i):
            prime[j] = False


def bfs(start, target):

    queue = deque()
    queue.append((start, 0))  # 숫자, 변경 횟수

    visited = set()

    while queue:

        num, count = queue.popleft()

        if num == target:
            return count

        num = str(num)

        # 네 자리 각각 변경
        for i in range(4):

            for d in '0123456789':

                new_num = num[:i] + d + num[i+1:]
                new_num = int(new_num)

                if new_num >= 1000 and prime[new_num] and new_num not in visited:

                    visited.add(new_num)
                    queue.append((new_num, count + 1))

    return "Impossible"


t = int(input())

for _ in range(t):

    a, b = map(int, input().split())

    print(bfs(a, b))