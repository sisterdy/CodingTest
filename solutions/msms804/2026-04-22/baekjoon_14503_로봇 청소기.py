import sys

# 주변 인접 4칸을 보면서, 청소 안된곳이 있으면 청소

N, M = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split()) # 현재 위치, 방향
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 북 동 남 서(d = 0, 1, 2, 3)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def clean(r, c, d):
    answer = 0
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
    while True:
        if room[r][c] == 0:
            room[r][c] = -1
            answer += 1

        found = False # 청소할 곳을 찾앗는지 판별하는 플래그

        for _ in range(4):
            # 반시계 방향으로 회전
            d = (d - 1) % 4
            
            ny = r + dy[d]
            nx = c + dx[d]
        
            # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
            if 0 <= ny < N and 0 <= nx < M and room[ny][nx] == 0:
                r, c = ny, nx
                found = True
                break # 1번으로 돌아감

        # 4방향 다 막힌 경우 -> 후진
        if not found:
            # 후진
            back = (d + 2) % 4
            ny = r + dy[back]
            nx = c + dx[back]

            # 벽이라서 후진할 수 없는 경우 종료
            if not (0 <= ny < N and 0 <= nx < M) or room[ny][nx] == 1:
                print(answer)
                return
            else:
                r, c = ny, nx


clean(r, c, d)