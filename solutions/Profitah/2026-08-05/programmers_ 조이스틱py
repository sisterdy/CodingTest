"""
이스틱으로 알파벳 문자열을 원하는 이름으로 바꾸는데 필요한 최소 조작 횟수

"""



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
