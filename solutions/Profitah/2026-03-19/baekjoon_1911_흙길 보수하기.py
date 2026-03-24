"""
문제 요약:
N개의 물웅덩이를 길이 L인 널빤지로 모두 덮을 때 필요한 최소 널빤지 개수를 구한다.

사용한 자료구조: list
사용한 알고리즘: 그리디

풀이 과정:
1. 물웅덩이를 시작 위치 기준으로 정렬
2. 왼쪽부터 순서대로 각 웅덩이를 덮어나간다
3. 이전 널빤지가 이미 현재 웅덩이를 일부 덮었을 수 있으므로
   current = max(current, start) 로 실제 덮어야 할 시작점을 계산 // 이미 덮은 부분을 계산하면 낭비이다.
4. 남은 길이 (end - current) 를 L로 나눠 올림하여 필요한 널빤지 수 계산
5. current를 실제로 덮은 끝 위치(planks * L)만큼 이동
   // ceil로 올림했으므로 널빤지가 웅덩이 끝보다 더 멀리 덮일 수 있다.
   // 다음 웅덩이 계산 시 이미 덮인 부분을 반영하기 위해 current를 갱신한다.

6. 모든 웅덩이를 처리한 후 총 널빤지 개수를 출력
"""

import math

N, L = map(int, input().split()) #  N은 물웅덩이의 개수, L은 물웅덩이를 덮을 수 있는 널빤지의 길이이다.
puddles = [list(map(int, input().split())) for i in range(N)] # 물 웅덩이가 시작된 좌표와 끝난 좌표를 입력받아 리스트로 저장
puddles.sort() # 물웅덩이들을 시작 위치 기준으로 오름차순정렬

count = 0 # 필요한 널빤지의 개수를 세는 변수이다.
current = 0 # 현재까지 덮은 널빤지 길이의 끝을 나타내는 변수.  처음에는 아무것도 덮지 않았으므로 0으로 초기화한다.
for start, end in puddles: # 물웅덩이들의 시작 좌표와 끝 좌표를 차례로 탐색하며
    current = max(current, start) # 현재까지 덮은 널빤지 길이의 끝과 물웅덩이의 시작점 중 더 큰 값을 current에 저장한다.
    # 이미 덮은 곳이면 current 유지하고 아직 안 덮은 곳이면 start부터 시작해서 널빤지 개수 측정하기 위해

    length = end - current # 이후 물웅덩이의 끝 좌표 - current(현재까지 덮은 널빤지 길이의 끝)
    planks = math.ceil(length / L) # 자릿수 올림으로 지금 필요한 널빤지 개수 계산. 남은길이 / 물웅덩이를 덮을 수 있는 널빤지의 길이
    count += planks  # 필요한 널빤지 개수를 count에 더한다.
    current += planks * L  # 실제로 덮은 끝 위치로 current 갱신
print(count) # 필요한 널빤지의 최종 개수를 출력한다.