# 백트래킹?

import sys

k = int(sys.stdin.readline().strip())
signs = sys.stdin.readline().split()

visited = [False] * 10
max_ans = ""
min_ans = ""

def check(i, j ,sign):
    if sign == "<":
        return i < j
    else:
        return i > j

def dfs(depth, s):
    global max_ans, min_ans
    
    if(depth == k + 1):
        # 아무 값 없으면 첫 값 저장
        if not min_ans:
            min_ans = s
        else: # 최댓값 갱신
            max_ans = s
        return # 종료
        
    for i in range(10):
        if not visited[i]:
            # 가지치기
            if depth == 0 or check(int(s[-1]), i, signs[depth - 1]):
                visited[i] = True
                dfs(depth + 1, s + str(i))
                visited[i] = False


dfs(0, '')
print(max_ans)
print(min_ans)