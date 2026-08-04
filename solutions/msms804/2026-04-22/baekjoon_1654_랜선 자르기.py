import sys

# 길이가 작아지면 작아질수록 랜선 개수 커짐

# 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
K, N = map(int, sys.stdin.readline().split())
lans = []

for i in range(K):
    lans.append(int(sys.stdin.readline()))

# left, right 는 랜선 길이의 범위
left = 1
right = max(lans)
answer = 0

while left <= right:
    mid = (left + right)//2 # 중간 랜선의 길이
    lines = 0 # 랜선 수

    for lan in lans:
        lines += lan // mid
    
    # 랜선의 개수가 N보다 크다면 mid의 범위를 더 키운다,
    # 길이가 커질수록 랜선 개수는 작아지므로
    if lines >= N:
        answer = mid # 가능한 값 저장
        left = mid + 1 # 더 큰 값 탐색
    else:
        right = mid - 1

print(answer)


