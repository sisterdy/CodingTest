"""
구간을 저장하지 않고 풀려고 했으나 그렇게는 안 되는 듯... 단순히 구간의 distance만으로는 풀 수 없는 것 같다.

센서 문제? 그리디 회의실... 
힌트를 보면 구간 맨 왼쪽부터 널빤지를 놔야 하는 듯?
"""
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pool = []

for _ in range(N):
    s, e = map(int, input().split())
    pool.append((s, e))

pool.sort()   # 시작점 기준 정렬

answer = 0
covered_end = 0   # 지금까지 널빤지로 덮은 가장 오른쪽 끝. 즉 이 좌표보다 왼쪽은 이미 처리.

for s, e in pool:
    start = max(s, covered_end)   # 이미 덮인 부분은 건너뛰어야 하니까...

    if start >= e:
        continue   # 이 물웅덩이는 이미 전부 덮임

    remain = e - start  # 아직 안 덮인 진짜 길이
    count = remain // L
    if remain % L != 0:
        count += 1

    answer += count
    covered_end = start + count * L

print(answer)