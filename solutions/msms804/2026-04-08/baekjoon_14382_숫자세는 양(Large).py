import sys

# 이미 적은 숫자는 또 적지 않으므로 set?
# 0 이 아니라면 무조건 0~9 나온다.

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    N = int(sys.stdin.readline())

    if N == 0:
        print(f"Case #{t}: INSOMNIA")
        continue

    nums = set()
    i = 1

    while True:
        num = N * i

        # 자리수 하나씩 추가
        for digit in str(num):
            nums.add(digit)

        
        # 0~9 다 모였으면 종료
        if len(nums) == 10:
            print(f"Case #{t}: {num}")
            break

        i += 1