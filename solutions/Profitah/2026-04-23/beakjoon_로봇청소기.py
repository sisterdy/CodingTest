"""
우리는 로봇 청소기와 방의 상태가 주어졌을 때, 청소한 영역의 개수를 구하는 프로그램을 작성해야함

풀이방법

     북(0)
       ↑
서(3) ← → 동(1)
       ↓
      남(2)

의 위치를 오가는 로봇청소기 !
벽을 만나면 뒤로, 청소한 곳이 있다면 반시계 방향으로 회전하며 
청소한 영역의 개수를 구하자.

로봇 청소기는 갈 곳이 없을 때 뒤로 이동하므로
bfs보다는 dfs가 직관적일 것이라고 생각한다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 방의 크기 N, M
r, c, d = map(int, input().split()) # 로봇 청소기의 좌표 (가로 r, 세로 c)와 바라보는 방향 d

room = [list(map(int, input().split())) for i in range(N)] # 방 전체의 상태를 list로  저장

# 북 동 남 서 (= 0, 1, 2, 3 ) 순서로 방향을 표현
dirs = [(-1,0), (0,1), (1,0), (0,-1)]


def robot_clean(r, c, d): 
    count = 0 # 청소한 칸의 개수

    # 0. 현재 칸이 빈 칸이면 청소
    if room[r][c] == 0: # 현재칸이 청소 안된 칸이면(0 이면)
        room[r][c] = 2  # 즉시 청소한다. 2로 표시하고
        count += 1      # 청소 횟수 +1

    # 1. 청소된 칸에서 4방향 탐색 (반시계 방향으로 회전하며 확인)
    for i in range(4):
        d = (d + 3) % 4      # 반시계 회전 (0->3->2->1->0)
        nr = r + dirs[d][0]  # 다음 이동 행 좌표 계산
        nc = c + dirs[d][1]  # 다음 이동 열 좌표 계산

        if room[nr][nc] == 0:         # 이동중 다음 청소 안 된 빈 칸 발견하면
            count += robot_clean(nr, nc, d)   # 그 칸으로 이동해서 robot_clean함수 재귀, 청소횟수 반환값 누적
            return count              # 이동했으면 바로 반환 (더 이상 회전 안 함)

    # 2. 4방향 모두 이동 불가할 때 (빈 칸이 없을 때) 뒤로 이동
    back = (d + 2) % 4        # 뒤로 방향 전환
    nr = r + dirs[back][0] # 뒤로 이동할 행 좌표 계산
    nc = c + dirs[back][1] # 뒤로 이동할 열 좌표 계산

    if room[nr][nc] == 1:     # 그런데 갈 곳이 없고 뒤가 벽(=1) 이면 바로 종료
        return count      # 즉시 청소한 칸의 개수 반환

    count += robot_clean(nr, nc, d)  # 뒤 칸으로 이동해 재귀 호출, 반환된 청소 칸 개수를 count에 누적
    return count # 청소한 칸의 개수 반환


print(robot_clean(r, c, d)) # count 반환값 출력