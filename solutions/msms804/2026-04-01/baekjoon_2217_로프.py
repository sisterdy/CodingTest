import sys

# 로프들을 이용하여 들어오릴 수 있는 물체의 최대 중량 구하기
# 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
# 작은것 기준으로 생각하기
N = int(sys.stdin.readline()) # 로프의 개수
ropes = []
answer = 0


for _ in range(N):
    ropes.append(int(sys.stdin.readline()))

# 오름차순 정렬
ropes.sort()

for i in range(N):
    weight = ropes[i] * (N - i)
    answer = max(weight, answer)

print(answer)