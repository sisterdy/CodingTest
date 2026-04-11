"""
뱀 게임 시뮬레이션 문제.
N×N 보드에서 뱀이 오른쪽 방향으로 출발하며,
사과를 먹으면 길이가 늘어나고, 벽이나 자기 몸에 충돌하면(=새 머리가 이동하려는 칸에 이미 뱀 몸이 있는 순간) 게임이 종료된다.
특정 시간마다 방향 전환 명령이 주어질 때, 게임이 몇 초 만에 종료되는지 구한다.

---

**뱀의 머리와 꼬리를 효율적으로 관리하기 위해 deque를 사용**
- 머리: append
- 꼬리: popleft

사과가 있으면 꼬리를 제거하지 않고, 없으면 꼬리를 제거하며 이동한다.
방향은 시계방향 4방향(0=오른쪽, 1=아래, 2=왼쪽, 3=위)으로 관리하며
'D'(오른쪽 회전), 'L'(왼쪽 회전) 명령으로 전환한다.
---
최종 코드 흐름:
- 보드에 사과 위치를 표시하고, 방향 전환 정보를 딕셔너리로 저장
- 매 초마다 이동을 시도하고, 충돌 시 해당 시간을 출력 후 종료
- 이동 성공 시 해당 시간에 방향 전환 명령이 있으면 방향을 갱신
"""

from collections import deque

def turn(d, c):
    # 현재 방향(d)에서 'D'면 오른쪽(+1), 'L'이면 왼쪽(-1)으로 90도 회전
    return (d + 1) % 4 if c == 'D' else (d - 1) % 4


def move(b, s, d, n):
    # 방향 벡터: 0=오른쪽, 1=아래, 2=왼쪽, 3=위 (시계방향)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    # 현재 뱀의 머리 위치에서 다음 이동 위치 계산
    x, y = s[-1]
    nx, ny = x + dx[d], y + dy[d]

    # 충돌 체크: 벽 또는 뱀의 몸통(2)과 겹치면 게임 종료
    if not (0 <= nx < n and 0 <= ny < n) or b[nx][ny] == 2:
        return False

    # 사과(1)가 있으면 꼬리 제거 없이 머리만 추가 (뱀 길이 증가)
    if b[nx][ny] == 1:
        b[nx][ny] = 2
        s.append((nx, ny))
    else:
        # 빈 칸이면 꼬리를 제거하고 머리를 추가 (뱀 길이 유지)
        tx, ty = s.popleft()
        b[tx][ty] = 0
        b[nx][ny] = 2
        s.append((nx, ny))

    return True


def sol():
    n = int(input())
    b = [[0]*n for _ in range(n)]  # 0: 빈칸, 1: 사과, 2: 뱀 몸통

    # 사과 위치를 보드에 표시
    for _ in range(int(input())):
        x, y = map(int, input().split())
        b[x-1][y-1] = 1

    # 방향 전환 정보: {시간: 방향} 으로 저장
    d_info = {}
    for _ in range(int(input())):
        t, c = input().split()
        d_info[int(t)] = c

    # 뱀의 초기 상태: (0,0)에서 시작, 오른쪽(d=0) 방향
    s = deque([(0,0)])
    b[0][0] = 2

    d, time = 0, 0

    while 1:
        time += 1

        # 이동 실패(충돌) 시 현재 시간이 곧 게임 종료 시간
        if not move(b, s, d, n):
            print(time)
            return

        # 해당 시간에 방향 전환 명령이 있으면 방향 갱신
        if time in d_info:
            d = turn(d, d_info[time])


sol()