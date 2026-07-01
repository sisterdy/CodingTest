def solution(board, h, w):
    count = 0
    n = len(board)
    
    # 12시부터 시계 방향
    dh = [-1, 0, 1, 0]  # 세로
    dw = [0, 1, 0, -1]  # 가로
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count
