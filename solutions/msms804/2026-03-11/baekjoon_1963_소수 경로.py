# 네자리 소수 두개를 입력받아서 바꾸는데 몇단계 걸리는지 -> 최단거리니까 bfs인듯
# 한 숫자씩 바꾸면서 소수인지 체크?
# 4자리 수를 0~9로 변경, 소수인지 체크
# 에라토스테네스의 체로 풀면 더 빠르다고함
import sys
from collections import deque

T = int(sys.stdin.readline())

# 소수 판별 함수
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


for _ in range(T):
    first, second = map(int, sys.stdin.readline().split())
    q = deque()
    visited = [False] * 10000
    found = False # 찾았다면 True로, impossible출력 위해
    
    q.append((first, 0)) # 시작숫자, 단계
    visited[first] = True

    while q:
        num, dist = q.popleft()

        if num == second:
            print(dist)
            found = True
            break
        
        for i in range(4):
            for j in range(10):
                # i 번째 자리를 j로 바꾸기
                num_str = str(num)
                new = num_str[:i] + str(j) + num_str[i + 1: ]
                new = int(new)

                # 첫째자리수가 0인 경우
                if i == 0 and j == 0:
                    continue
                # 소수가 아닌경우
                if not isPrime(new):
                    continue

                if not visited[new]:
                    q.append((new, dist + 1))
                    visited[new] = True

    if not found:
        print("Impossible")

