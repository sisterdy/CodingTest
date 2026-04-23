"""
"""
import sys
N, M = map(int, sys.stdin.readline().split())

arr_A = list(map(int, sys.stdin.readline().split()))
arr_B = list(map(int, sys.stdin.readline().split()))

result = arr_A + arr_B
result.sort()

print(*result)