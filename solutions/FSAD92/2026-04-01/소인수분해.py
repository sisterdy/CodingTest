"""
1주차 때인가 2주차 때 풀었던 건가봐.
"""
import sys
N = int(sys.stdin.readline())

if N == 1:
    sys.exit()

divider = 2

while True:
    if N <= 1:
        break

    if N / divider == N // divider:
        print(divider)
        N //= divider

    else:
        divider += 1