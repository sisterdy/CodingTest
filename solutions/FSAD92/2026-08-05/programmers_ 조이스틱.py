"""
A~Z를 하나의 원형이라고 생각하자

각 문자 ch의 상하 조작 횟수는 다음 두 값 중 작은 값이다.
up = ord(ch) - ord('A')
down = 26 - up

좌우 조작이 어려운데, 연속된 A 때문에 총 세 가지 경우를 생각해야 되기 때문이다.
1. 계속 오른쪽으로 이동
2. 오른쪽을 갔다가 되돌아와 왼쪽 끝으로 이동
3. 왼쪽 끝을 먼저 갔다가 되돌아와 오른쪽으로 이동


"""
def solution(name):
    vertical_moves = 0
    horizontal_moves = len(name) - 1    # 좌우 이동의 초기값은 계속 오른쪽으로만 이동하는 비용이어야 한다.
    
    # 상하 이동 계산
    for ch in name:
        up = ord(ch) - ord('A')
        down = 26 - up
        
        vertical_moves += min(up, down)
        
    for i in range(len(name)):
        next_index = i + 1
        
        while next_index < len(name) and name[next_index] == 'A':
            next_index += 1
            
        horizontal_moves = min(horizontal_moves,
                              2 * i + len(name) - next_index,
                              2 * (len(name) - next_index) + i)
    
    return vertical_moves + horizontal_moves