"""
로프 개수는 10만개까지

주어진 로프들의 정보를 이용해
들어올릴 수 있는 '최대 중량'을 구하기

100
110
120

간단히 생각해보면
가장 쬐끄만 로프가 버틸 수 있는만큼은 걸을 수 있을 거고...
로프는 여러 개니까
(가장 쬐끄만 로프가 버틸 수 있는 만큼 * 로프의 갯수) 만큼은 최소한으로 버틸 수 있겠지
minimum_weight = ropes[0] * N

아 모든 로프를 다 쓸 필요는 없구나...?
그럼 가장 쬐끄만 로프를 버려가면서 최대로 들 수 있는 중량을 찾아볼까

예를 들어

10, 100 이렇게 있으면 10을 버리는 게 무조건 이득이니까
"""
import sys
N = int(sys.stdin.readline().strip())

ropes = []
for _ in range(N):
    ropes.append(int(sys.stdin.readline().strip()))

ropes.sort()

max_weight = 0

for i in range(N):
    # 지금 들 수 있는 총 무게 = 현재 로프의 무게 * 남은 로프의 개수
    current_capable_weight = ropes[i] * (N - i)    

    if current_capable_weight > max_weight:
        max_weight = current_capable_weight

print(max_weight)