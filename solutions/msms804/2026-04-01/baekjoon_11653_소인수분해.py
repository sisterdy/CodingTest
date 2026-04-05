import sys
# 소수들의 곱으로만 나누기

N = int(sys.stdin.readline())

if N == 1:
    print()
    exit()

# N보다 작은수들로 for문 돌면서(작은 수부터 나눠보면 소인수만 남음)
i = 2

while N > 1 and i <= N:
    # 나누어 떨어진다면
    if N % i == 0:
        N //= i
        print(i)
    else:
        i += 1