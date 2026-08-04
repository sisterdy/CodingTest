import sys

# 배열 A와 B의 크기
N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# 배열 합친후 정렬한 결과
res = sorted(A + B)
print(*res)