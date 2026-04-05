import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
jido = []
dice = [0, 0, 0, 0, 0, 0] # 윗면, 아랫면, 북, 남, 동, 서

# 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    jido.append(arr)

commands = list(map(int, sys.stdin.readline().split()))

for cmd in commands:
    ny = y + dy[cmd]
    nx = x + dx[cmd]

    # 범위 체크
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue 

    if cmd == 1: # 동쪽
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif cmd == 2:  # 서
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif cmd == 3:  # 북
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif cmd == 4:  # 남
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

    # 위치 갱신
    x, y = nx, ny

    # 이동한 칸에 쓰여있는 수가 0이라면, 주사위 바닥면에 잇는 수가 칸에 복사
    if jido[x][y] == 0:
        jido[x][y] = dice[1]
    #  0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    else:
        dice[1] = jido[x][y]
        jido[x][y] = 0

    # 윗면 출력
    print(dice[0])