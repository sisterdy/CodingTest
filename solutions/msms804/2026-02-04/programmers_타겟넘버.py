# 그래프 탐색(dfs 일거같은데)
# 그럼 재귀 돌려야하나?

answer = 0 # 전역으로 뺌
def dfs(numbers, target, depth, sum):
    global answer
    
    # 기저 사례
    if depth == len(numbers):
        if sum == target:
            answer += 1
        return
    dfs(numbers, target, depth + 1, sum + numbers[depth])
    dfs(numbers, target, depth + 1, sum - numbers[depth])

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer