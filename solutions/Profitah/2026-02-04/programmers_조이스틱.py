"""조이스틱 문제는 각 문자 변경 비용을 계산한 뒤, 
연속된 A 구간을 기준으로 커서 이동 경로를 최소화하는 탐욕법을 적용하여 해결한다."""

def solution(name):
    answer = 0
    n = len(name)
    
    # 위아래 조작
    for char in name:
        answer += min(ord(char) - ord('A'),
                      ord('Z') - ord(char) + 1)
    
    # 좌우 이동 최소 계산
    move = n - 1
    
    for i in range(n):
        next_idx = i + 1
        
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        distance = min(i * 2 + n - next_idx,
                       (n - next_idx) * 2 + i)
        move = min(move, distance)
    
    return answer + move
