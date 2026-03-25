"""
그리디구만

A : 5분
B : 1분
C : 10초

T초를 맞출 수 없다면 -1 출력

ABC 조작 횟수를 차례대로 출력(각각의 횟수 사이에는 빈 칸)
"""
import sys

T = int(sys.stdin.readline())

A, B, C = 300, 60, 10
count_A, count_B, count_C = 0, 0, 0

#print(A,B,C)
#print(T)
count_A = T // A
T = T % A
count_B = T // B
T = T % B
count_C = T // C
T = T % C

if T == 0:
    print(count_A, count_B, count_C)
else:
    print(-1)