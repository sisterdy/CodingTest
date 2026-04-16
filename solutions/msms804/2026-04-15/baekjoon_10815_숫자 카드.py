import sys

# 이터레이터 = 한 방향으로만 흐르는 컨베이어 벨트(값을 저장하지 않고 소모함?)
# 배열인 경우에는 시간복잡도 O(N * M)
# set이면 o(1) 헤시테이블
N = int(sys.stdin.readline())

card_nums = set(map(int, sys.stdin.readline().split()))
answer = []

M = int(sys.stdin.readline())

check_nums = map(int, sys.stdin.readline().split())


for n in check_nums:
    if n in card_nums:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
