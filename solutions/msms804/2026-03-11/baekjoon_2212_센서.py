import sys
# 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 문제
# 센서를 k개의 그룹으로 나눈다. -> 큰 간격 K-1개 제거(그 간격에서 그룹을 나눔)
# 집중국의 위치는 고려하지 x
# 1 3 | 6 7 9
# 그리디인 이유는 가장 큰 간격부터 끊는 선택이 항상 최적
n = int(sys.stdin.readline()) # 센서의 개수
k = int(sys.stdin.readline()) # 집중국 개수

sensors = list(set(map(int, sys.stdin.readline().split()))) # 중복제거 후 리스트
sensors.sort()

# 집중국이 센서보다 많으면 길이 0
if k >= n:
    print(0)
    exit()

gaps = []
# 1 . 간격들을 구한다
for i in range(1, len(sensors)):
    gaps.append(sensors[i] - sensors[i - 1])

# 2. 간격들 내림차순 정렬
gaps.sort(reverse=True)
# 3. 앞에있는 k-1개 제거
print(sum(gaps[k - 1: ]))