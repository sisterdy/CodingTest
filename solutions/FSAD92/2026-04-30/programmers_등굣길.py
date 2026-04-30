"""
DP로 풀어야 한다고? 탑다운? 바텀업? 최단경로의 개수는 뭐로 해야 좋지?
애초에 최단경로면 그냥 BFS로 풀면 되는 것 아닌가?
아 근데 return 해야 하는 게 최단 거리를 구하는 게 아니라 경로의 가짓수를 구하는 거라 DP가 맞나...?

일단 dp[i][j] = 시작점에서 i,j 지점까지 최단 거리로 도달할 수 있는 경로의 총 가짓수

오른쪽과 아래쪽으로만 움직일 수 있으니 dx,dy는 안 써도 되는 것 같다.

(1,1)부터 시작이니까 (x,y) 지점에 최단거리로 도달하는 경우의 수는 두 가지.
즉 위에서 오는 경우와 왼쪽에서 오는 경우.
"""
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    # grid 모든 칸마다 puddle인지 체크해야 하니 set에 넣어서 탐색 시간을 줄이기
    puddle_set = set([(y, x) for x, y in puddles])
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # dp[1][1] = 1 보호 목적
            if i == 1 and j == 1:
                continue  
        
            if (i, j) in puddle_set:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            
    return dp[n][m]