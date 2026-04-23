"""
정답 비율 22%? OMG

K: 갖고 있는 랜선 개수
N: 필요한 랜선 개수

N개를 만들 수 있는 랜선의 '최대 길이'를 출력해야 한다.

투 포인터로 범위를 좁혀볼까. 최소값은 당연히 1이고, 최대값은 당연히 가장 긴 랜선의 길이일 거고
함수 하나를 만들자. 무슨 함수? 정수를 매개변수로 받고, 해당 매개변수로 랜선들을 잘랐을 때 나오는 개수를 반환하는 함수.
"""
import sys
K, N = list(map(int, sys.stdin.readline().split()))

cables = []
for _ in range(K):
    cables.append(int(sys.stdin.readline().strip()))
cables.sort()

left = 1
right = max(cables)

def go_and_count(n):
    cable_count = 0

    for i in range(K):
        temp = cables[i] // n
        cable_count += temp
    return cable_count

while left <= right:
    mid = (left + right) // 2

    # 만들어진 랜선 개수가 N보다 작으면, 너무 크게 잘랐다는 것 -> right를 줄인다.
    if go_and_count(mid) < N:
        right = mid - 1

    # 만들어진 랜선 개수가 N보다 크면, 너무 잘게 잘랐다는 것 -> left를 키운다.
    else:
        left = mid + 1

print(right)