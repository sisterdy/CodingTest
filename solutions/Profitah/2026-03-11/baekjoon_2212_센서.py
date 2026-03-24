"""
센서 문제 (그리디)

센서들이 일직선 위에 있다.
집중국을 k개 설치하여
센서들과 집중국 사이 거리의 합을 최소로 하자.

핵심 아이디어

센서들을 정렬한 후
센서 사이 거리 차이를 계산한다.

예시

센서
1 3 6 7 9

거리 차이
2 3 1 2

큰 간격을 기준으로 그룹을 나누면
총 거리를 최소로 만들 수 있다.

즉

가장 큰 간격 k-1개를 제거하면 된다.
"""

n = int(input())  # 센서 개수
k = int(input())  # 집중국 개수

sensors = list(map(int, input().split()))  # 센서 위치

# 센서 위치 정렬
sensors.sort()

# 센서 사이 거리 계산
gaps = []

for i in range(1, n):
    gaps.append(sensors[i] - sensors[i-1])

# 거리 차이 정렬
gaps.sort(reverse=True)

# 가장 큰 간격 k-1개 제거
answer = sum(gaps[k-1:])

print(answer)