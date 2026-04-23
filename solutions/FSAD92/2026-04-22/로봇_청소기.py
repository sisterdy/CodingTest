"""
grid
바라보는 방향
후진
90도 회전

"""
import sys

N, M = map(int, sys.stdin.readline().strip().split())
curr_r, curr_c, direction = map(int, sys.stdin.readline().strip().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

clean_count = 0

while True:
    # 현재 칸이 아직 청소되지 않은 경우 청소함
    if grid[curr_r][curr_c] == 0:
        grid[curr_r][curr_c] = 2      # 청소한 칸은 2로 표시
        clean_count += 1

    moved = False   # 4방향 모두 실패했을 때 후진 여부를 판별하기 위한 플래그

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸 찾기
    for _ in range(4):
        # 반시계 방향으로 90도 회전(북,동,남,서니까 -1을 해야 반시계 방향임)
        # 모듈로 연산으로 인덱스 순환
        direction = (direction - 1) % 4

        next_r = curr_r + dx[direction]
        next_c = curr_c + dy[direction]

        # 회전한 방향 앞 칸이 청소되지 않은 빈 칸이면 전진
        if grid[next_r][next_c] == 0:
            curr_r = next_r
            curr_c = next_c
            moved = True
            break

    # 네 방향 모두 청소할 곳이 없다면
    if not moved:
        # 현재 방향을 유지한 채 후진
        back_direction = (direction + 2) % 4
        back_r = curr_r + dx[back_direction]
        back_c = curr_c + dy[back_direction]

        # 뒤쪽 칸이 벽이면 작동 종료
        if grid[back_r][back_c] == 1:
            break

        # 벽이 아니면 후진
        curr_r = back_r
        curr_c = back_c

print(clean_count)