"""
첫 번째 행은 케이스의 개수, T이다. 다음 행부터는 T개의 케이스들.
블리트릭스는 N에서 시작해서 i × N 후에는 (i + 1) × N을 떠올리게 된다.

비트 마스킹 쓰면 될 것 같기도?
N부터 시작해서 i x N으로 증가
언제까지?
visited 가 1111111111(2)가 될 때까지 <- 종료 조건
처음 시작인 N을 포함한 i x N(str)은 매번 각 자릿수를 for문으로 돌며 int로 변환한 걸 인덱스로
visited에 1이 체크되어 있는지 확인한다
"""
import sys

FULL_MASK = 0b_11111_11111              # 종료 조건을 위한 상수
T = int(sys.stdin.readline().strip())

# 정수와 현재 마스킹 상태를 매개변수로 입력하면 해당 마스킹에 마스킹 해주는 함수
def do_mask(num, current_mask):
    while num > 0:
        digit = num % 10                # 첫 번째 자리의 값을 추출
        current_mask |= (1 << digit)    # 첫 번째 자리의 값에 해당하는 비트를 마스킹
        num //= 10                      # 다음 자리의 값으로 이동
    return current_mask

for i in range(T):
    init_num = int(sys.stdin.readline().strip())    # 초기값 N
    N = init_num
    count = 1
    status_mask = 0b_00000_00000

    if N == 0:                                  # 일단 상식적으로 0은 절대 안 될 거고...
        print(f"Case #{count}: INSOMNIA")
        continue
    else:                                       # 0이 아니면
        while status_mask != FULL_MASK:         # 모든 비트가 켜질 때까지
            N = count * init_num                # N, 2N, 3N, ...
            status_mask = do_mask(N, status_mask)
            count += 1
            
    print(f"Case #{i + 1}: {N}")