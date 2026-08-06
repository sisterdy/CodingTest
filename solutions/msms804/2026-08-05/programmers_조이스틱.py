def solution(name):
    answer = 0
    n = len(name)
    
    # 세로 이동
    for c in name:
        answer += min(ord(c)-ord('A'), ord('Z')-ord(c) + 1)
    
    # 가로 이동
    move = n - 1
    
    for i in range(n):
        next = i + 1
        # i의 다음부터 시작해 연속된 A를 지난 다음 문자를 next로.
        while next < n and name[next] == 'A':
            next += 1
        # 오른쪽 끝까지, 오른쪽 i까지 갔다가 돌아오기, 먼저 왼쪽 끝으로 가서 뒤를 처리 <- 이 셋을 비교
        move = min(move, i * 2 + (n - next), i + 2 * (n - next))
        
    answer += move
    
    return answer