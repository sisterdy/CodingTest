"""
그리디
프로그래머스 '단속카메라' 문제가 생각나는데

센서 좌표 정렬부터!
"""
import sys
input = sys.stdin.readline

n = int(input())    # 센서 갯수
k = int(input())    # 집중국 갯수

sensors = list(map(int, input().split()))
sensors.sort()

# 집중국이 센서 개수 이상일 때 케이스
# 각 센서마다 하나씩 맡기면 되므로 거리 합 = 0
if k >= n:
    print(0)
else:
    distances = []

# 1 2 3 0 3

    # 인접한 센서들 사이의 거리들
    for i in range(1, n):
        distance = sensors[i] - sensors[i - 1]
        distances.append(distance)

    # 긴 distance부터 끊는 게 그리디하니까
    distances.sort(reverse = True)

    # 처음엔 전체를 하나의 구간으로 본다
    answer = sensors[n - 1] - sensors[0]

    # 집중국이 k개면, 총 k개의 구간으로 나눌 수 있다 ->  큰 distances를 k-1개 끊어낸다
    for i in range(k - 1):
        answer -= distances[i]

    print(answer)