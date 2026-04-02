"""
문제 자체가 이해가 안 됐음. <- 증오

어떻게 보면 그냥 단순한 구현이었는데... <- 후회

'흥미' 재밌는 문제!
"""
import sys

# 주사위 클래스
class Dice:
    def __init__(self, x, y):
        # 처음에는 문제 조건상 전부 0으로 시작
        self.top, self.bottom, self.front, self.back, self.left, self.right = 0, 0, 0, 0, 0, 0

        self.x, self.y = x, y

    def roll_east(self):
        # 동쪽으로 굴릴 때 면 변화
        # 새 값 기준으로
        # new_top    = old_left
        # new_right  = old_top
        # new_bottom = old_right
        # new_left   = old_bottom
        self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom

    def roll_west(self):
        # 서쪽으로 굴릴 때
        self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom

    def roll_north(self):
        # 북쪽으로 굴릴 때
        self.top, self.back, self.bottom, self.front = self.front, self.top, self.back, self.bottom

    def roll_south(self):
        # 남쪽으로 굴릴 때
        self.top, self.front, self.bottom, self.back = self.back, self.top, self.front, self.bottom

    def update_at_location(self, game_map):
        # 현재 주사위 위치 칸의 값과 주사위 바닥면 상호 작용

        # 칸의 값이 0이면 -> 주사위 바닥면 값을 칸에 복사
        if game_map[self.x][self.y] == 0:
            game_map[self.x][self.y] = self.bottom
        else:
            # 칸의 값이 0이 아니면 -> 칸의 값을 주사위 바닥면에 복사 후, 칸은 0으로 변경
            self.bottom = game_map[self.x][self.y]
            game_map[self.x][self.y] = 0


def solve():
    input = sys.stdin.read().split()

    # N, M : 지도 크기
    # x, y : 주사위 시작 좌표
    # K    : 명령 개수
    N, M, x, y, K = map(int, input[:5])

    # 지도 데이터
    game_map = []
    idx = 5     # N M x y K 읽고 난 뒤 인덱스
    for i in range(N):
        game_map.append(list(map(int, input[idx:idx + M])))
        idx += M

    # 나머지는 명령 목록
    commands = list(map(int, input[idx:]))

    # 1: 동, 2: 서, 3: 북, 4: 남
    # 북쪽: x - 1
    # 남쪽: x + 1
    # 동쪽: y + 1
    # 서쪽: y - 1
    dx = [0, 0, 0, -1, 1]   # 행
    dy = [0, 1, -1, 0, 0]   # 열

    # 주사위 객체 생성
    dice = Dice(x, y)

    for cmd in commands:
        nx, ny = dice.x + dx[cmd], dice.y + dy[cmd]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        dice.x, dice.y = nx, ny

        if cmd == 1:
            dice.roll_east()
        elif cmd == 2:
            dice.roll_west()
        elif cmd == 3:
            dice.roll_north()
        elif cmd == 4:
            dice.roll_south()

        dice.update_at_location(game_map)

        # 이동할 때마다 주사위 윗면 출력
        print(dice.top)

solve()