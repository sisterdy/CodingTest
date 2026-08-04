def solution(players, m, k):
    answer = 0
    expiresAt = [0] * 24
    alive = 0
    for i in range(len(players)):
        # 1. 종료되는 서버 제거
        alive -= expiresAt[i]
        
        # 2. 필요한 서버 계산
        need = players[i] // m
        
        # 3. 부족하면 증설
        if need > alive:
            add = need - alive
            alive += add
            answer += add
            
            endTime = i + k
            if endTime < 24:
                expiresAt[endTime] += add
    return answer