"""
프로그래머스 단어 변환?
bfs

비밀번호는 네자리 9999?

근데 소수를 어떻게... 1000부터 9999까지...?
"""

from collections import deque
import sys

input = sys.stdin.readline

def make_prime_table():
    is_prime = [True] * 10000
    is_prime[0] = False
    is_prime[1] = False

    i = 2
    while i * i < 10000:
        if is_prime[i]:
            j = i * i
            while j < 10000:
                is_prime[j] = False
                j += i
        i += 1

    return is_prime

def bfs(begin, target, is_prime):
    # like 단어 변환 문제
    queue = deque([(begin, 0)])

    visited = set([begin])

    while queue:
        curr_num, step = queue.popleft()

        # 목표 숫자에 도달했으면 현재 단계 반환
        if curr_num == target:
            return step

        # 현재 숫자에서 갈 수 있는 다음 숫자들을 탐색 -> 한 자리만 바꿔서 만들 수 있는 네자리 숫자들
        for i in range(4):  # 일십백천
            for digit in "0123456789":
                # 같은 숫자로 바꾸는 건 의미 없으니 패스
                if curr_num[i] == digit:
                    continue

                # 1000 미만 비밀번호는 허용 x
                if i == 0 and digit == "0":
                    continue

                # 슬라이싱 써서 i번째 자리만 digit으로 바꾼 후보 생성
                next_num = curr_num[:i] + digit + curr_num[i + 1:]

                # 아직 방문 안했고, 소수라면 이동 가능
                if next_num not in visited and is_prime[int(next_num)]:
                    visited.add(next_num)
                    queue.append((next_num, step + 1))

    # 끝까지 못 찾으면 임파서블 출력
    return "Impossible"


def main():
    is_prime = make_prime_table()

    test_count = int(input())
    answers = []

    for _ in range(test_count):
        begin, target = input().split()
        answers.append(str(bfs(begin, target, is_prime)))

    print("\n".join(answers))

main()