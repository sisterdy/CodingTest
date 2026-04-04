"""
주사위 굴리기 문제 - 주사위를 굴릴 때마다 윗면의 값을 출력하는 문제.

문제 설명:
- N×M 지도 위에 주사위가 놓여 있으며, 초기 상태는 모든 면이 0이다.
- 주사위 전개도:
      2
    4 1 3     <- 윗면:1, 동:3, 서:4, 북:2, 남:5, 아랫면:6
      5
      6
- 명령(동/서/남/북)에 따라 주사위를 굴리며, 이동 시 칸의 값과 주사위 바닥면을 교환한다.
  · 이동한 칸의 값이 0이면  -> 주사위 바닥면 값을 칸에 복사
  · 이동한 칸의 값이 0이 아니면 -> 칸의 값을 주사위 바닥면에 복사, 칸은 0으로 초기화
- 지도 밖으로 나가는 명령은 무시하며, 출력도 하지 않는다.
- 매 이동 후 주사위 윗면의 값을 출력한다.

풀이 방식:
- 주사위의 6개 면을 리스트로 관리하고, 방향에 따라 면의 인덱스를 재배치하여 굴리기를 구현한다.
- 이동 방향별 dx/dy로 다음 좌표를 계산하고, 범위를 벗어나면 해당 명령을 건너뛴다.

흐름:
- 명령 수신 -> 범위 확인(벗어나면 무시) -> 이동 -> 주사위 굴리기
  -> 칸 값과 바닥면 교환 -> 윗면 출력
"""

import sys
input = sys.stdin.readline

# 주사위 6개 면의 인덱스 정의
# 전개도 기준:  윗면=0, 북=1, 동=2, 서=3, 남=4, 아랫면=5
TOP, NORTH, EAST, WEST, SOUTH, BOTTOM = 0, 1, 2, 3, 4, 5

def roll_dice(direction):
    """
    주사위를 주어진 방향으로 굴리는 함수.
    굴리면 면들의 위치가 바뀌므로, 변환된 순서로 dice 리스트를 재구성한다.
    """
    global dice
    t, n, e, w, s, b = dice  # 현재 TOP, NORTH, EAST, WEST, SOUTH, BOTTOM

    if direction == 1:    # 동쪽으로 굴리기: 서면->위, 위->동, 동->아래, 아래->서
        dice = [w, n, t, b, s, e]
    elif direction == 2:  # 서쪽으로 굴리기: 동면->위, 위->서, 서->아래, 아래->동
        dice = [e, n, b, t, s, w]
    elif direction == 3:  # 북쪽으로 굴리기: 남면->위, 위->북, 북->아래, 아래->남
        dice = [s, t, e, w, b, n]
    elif direction == 4:  # 남쪽으로 굴리기: 북면->위, 위->남, 남->아래, 아래->북
        dice = [n, b, e, w, t, s]


# 입력
N, M, row, col, K = map(int, input().split())  # 지도 크기, 초기 위치, 명령 수
board = [list(map(int, input().split())) for _ in range(N)]  # N×M 지도
commands = list(map(int, input().split()))  # K개의 이동 명령

# 주사위 초기 상태 (모든 면 0)
dice = [0] * 6  # [TOP, NORTH, EAST, WEST, SOUTH, BOTTOM]

# 방향별 이동 벡터 (인덱스: 동=0, 서=1, 북=2, 남=3 → 명령값 -1로 접근)
dy = [0, 0, -1, 1]   # 행(row) 변화량
dx = [1, -1, 0, 0]   # 열(col) 변화량

for cmd in commands:
    ny = row + dy[cmd - 1]  # 이동 후 행 좌표
    nx = col + dx[cmd - 1]  # 이동 후 열 좌표

    # 지도 밖으로 나가는 명령은 무시 (출력도 하지 않음)
    if not (0 <= ny < N and 0 <= nx < M):
        continue

    # 주사위 이동
    row, col = ny, nx

    # 방향에 맞게 주사위 굴리기 (면 재배치)
    roll_dice(cmd)

    # 칸 값과 주사위 바닥면 교환
    if board[row][col] == 0:       # 이동한 칸의 값이 0이면
        board[row][col] = dice[BOTTOM]  # 주사위 바닥면 값을 칸에 복사
    else:                               # 이동한 칸의 값이 0이 아니면
        dice[BOTTOM] = board[row][col]  # 칸의 값을 주사위 바닥면에 복사
        board[row][col] = 0             # 칸의 값은 0으로 초기화

    # 이동 후 주사위 윗면 출력
    print(dice[TOP])