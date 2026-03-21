# 하나씩 다 해본다..?

import sys

N = int(sys.stdin.readline())

answer = 0

def make_sum(n):
    hap = n
    while n:
        rest = n % 10
        hap += rest
        n //= 10

    return hap

for i in range(1, N):
    if make_sum(i) == N:
        answer = i
        break

print(answer)