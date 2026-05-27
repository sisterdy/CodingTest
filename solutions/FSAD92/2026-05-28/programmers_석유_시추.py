"""
len(land) = 땅의 세로길이 = n
len(land[i]) = 땅의 가로길이 = m
land[i][j]는 i+1행 j+1열 땅의 정보를 나타내며 0 또는 1이다. 0은 빈 땅, 1은 석유가 있는 땅

시추기는 세로 방향으로 시추를 하고
석유는 덩어리로 되어있어서 시추기가 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있다

모든 행을 순회하며 가장 많은 석유량을 리턴해야 하는데
덩어리를 어떻게 관리하지?

1. land[i]에 시추기를 꽂는다
2. land[i][j] 2중 for문으로 순회한다.
3. 시추기가 지나간 덩어리의 석유량을 더하고 그 값을 리턴한다.

큰 맥락으로 보면 이렇게 될 것 같다.

"""
from collections import deque

def solution(land):
    answer = 0
    n = len(land)      # 세로(y 범위)
    m = len(land[0])   # 가로(x 범위)
    
    # 석유 덩어리 관리
    oil_size = {}      # 석유 덩어리 사이즈를 담을 딕셔너리. {oil_id: size} 형태
    oil_id = -1    # 덩어리에 붙일 id, -1로 초기화해서 -1씩 감소시킴. id가 음수 = 석유 덩어리로 간단하게 식별 가능. 0으로 왜 안 했냐면, 0은 석유 없는 땅으로 이미 정해졌기 때문...
    
    # 석유 덩어리 식별 BFS 시작
    for i in range(n):      # 세로를 먼저 돌고
        for j in range(m):  # 가로를 돈다
            if land[i][j] == 1:     # 새로운 석유를 발견하면
                size = 0
                # 처음 시작점 설정, i는 y(세로), j는 x(가로)
                queue = deque([(j, i)]) # 현재 위치를 큐에 넣고
                land[i][j] = oil_id     # 방문 처리 겸 oil_id 부여. 기존의 석유 체크 플래그인 1은 이제 없다!
                
                while queue:
                    curr_x, curr_y = queue.popleft()
                    size += 1   # 큐에서 꺼낼 때마다 덩어리 사이즈를 1 업
                    
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:   # 상하좌우 탐색
                        nx = curr_x + dx
                        ny = curr_y + dy
                        
                        # 경계를 안 넘고 아직 안 가본 석유(1)라면?
                        if 0 <= nx < m and 0 <= ny < n and land[ny][nx] == 1:
                            land[ny][nx] = oil_id # 즉시 방문 처리 및 똑같은 id 부여.
                            queue.append((nx, ny))
                            
                oil_size[oil_id] = size     # 딕셔너리에 {oil_id: size}를 저장
                oil_id -= 1 # 다음 덩어리는 -2, -3, ...
                
                
    for x in range(m):      # 시추기는 가로 방향(x)으로 한 칸씩 이동하며 꽂음
        found_oil = set()       # 이번 시추에서 지나간 석유 덩어리 id들을 담을 바구니(중복 제거해야되니 set으로)
        oil_sum = 0
            
        for y in range(n):      # 위에서 아래로(y) 시추기가 뚫고 내려감
            if land[y][x] < 0:      # 음수 id, 즉 석유 덩어리를 만나면
                found_oil.add(land[y][x])       # '이번 시추에서 지나간 석유 덩어리 id들을 담을 바구니'에 id를 넣어버림
                    
        for oil in found_oil: # 이번 열에서 발견된 모든 id들을 키에 해당하는
            oil_sum += oil_size[oil]    # 덩어리 크기 딕셔너리에서 값들을 모두 더함
                
        answer = max(answer, oil_sum)   # 지금까지 뚫어본 것 중 가장 많은 석유량을 갱신
            
    return answer