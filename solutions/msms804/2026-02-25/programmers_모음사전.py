# 백트래킹? dfs?

def solution(word):
    alphabets = ["A", "E", "I", "O", "U"]
    answer = 0
    found = False
    def dfs(current):
        nonlocal answer, found
        
        # true 인 경우 전체 중단, 안하면 카운트 계속 증가
        if found:
            return
        
        # 0보다 큰 경우인 이유는 첫 시작을 ""로 하기 때문
        if len(current) > 0:
            answer += 1
            if current == word:
                found = True
                return
        
        if len(current) == 5:
            return
        
        for a in alphabets:
            dfs(current + a)
            
    dfs("")
    return answer