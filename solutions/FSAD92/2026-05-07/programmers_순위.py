def solution(n, results):
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    
    for win, lose in results:
        matrix[win][lose] = 1
        matrix[lose][win] = -1
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i][k] == 1 and matrix[k][j] == 1:
                    matrix[i][j] = 1
                    matrix[j][i] = -1
                    
                elif matrix[i][k] == -1 and matrix[k][j] == -1:
                    matrix[i][j] = -1
                    matrix[j][i] = 1
                    
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if matrix[i][j] != 0:
                count += 1
        
        # count == n - 1이라는 건
        # i번 선수가 다른 모든 선수와의 승패 관계를 알고 있다
        if count == n - 1:
            answer += 1     # 순위를 알 수 있는 선수이므로 정답 개수를 1 증가
                        
    return answer