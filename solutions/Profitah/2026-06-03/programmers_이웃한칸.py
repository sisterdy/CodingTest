"""
현재 위치와 같은 색을 가진 인접한 칸(상·하·좌·우)의 개수를 구하는 문제

"""

def solution(board, h, w):
    n = len(board) # 1. board의 길이를 저장 ## 보드판 범위 밖을 탐색하는 걸 막기위해, 이차원배열을 n에 넣을 경우 h_check w_check와 값 비교 불가능 하므로 len() 사용 이후 보드 크기를 n에 저장
    count = 0  # 2. 같은 색으로 색칠된 칸의 개수 
    answer = count
    dh, dw =[0, 1, -1, 0], [1, 0, 0, -1] # 3. h와 w의 변화량 // 가로세로
    for i in range(0, 4): # 4. 반복문  ## 상하좌우를 확인하며 같은색으로 칠해진 칸 찾기
        h_check, w_check = h + dh[i], w + dw[i] # 4-1 체크할 칸의 h, w 좌표를 나타내는 변수
        
        if n > h_check >= 0 and n > w_check >= 0: # 4-2 지금 체크한 h w 범위가 0이상 n 미만일때만
            if board[h][w] == board[h_check][w_check]: #4-2-a 선택한 칸의 색과 동일한지 확인하고, 동일하다면
                answer += 1 # answer 에 + 1
    return answer # 5. count값 return