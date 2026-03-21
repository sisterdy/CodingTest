import sys
# 널빤지의 최소 개수..
# 뭔가 웅덩이들을 배열에 좌표로 넣어야할듯?
# 웅덩이 개수가 L개 보다 크면 -> 몫으로 구한다?
# 만약 웅덩이와 웅덩이 사이에 길이 있으면?
# 웅덩이 리스트를 오름차순으로 정렬하고, 널빤지로 덮은 가장 오른쪽 위치 기억한다.

# 웅덩이 개수 , 널빤지 길이
N, L = map(int, sys.stdin.readline().split())
pools = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    pools.append((start, end))

# start를 기준으로 오름차순 정렬
pools.sort()

# 지금까지 널빤지로 덮은 가장 오른쪽 위치
current = 0
answer = 0

for start, end in pools:
    if current > start:
        start = current

    if start >= end:
        continue

    length = end - start
    cnt = (length + L - 1) // L # 덮는 널빤지 개수 카운트

    answer += cnt
    current = start + cnt * L

print(answer)


