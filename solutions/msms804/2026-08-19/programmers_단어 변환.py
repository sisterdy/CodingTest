# 최소변환 과정 -> bfs
# 한글자만 다른 단어 찾기
from collections import deque

def diff_one(a, b):
    cnt = 0 # 다른 갯수를 카운트
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
    return cnt

def solution(begin, target, words):
    answer = 0
    queue = deque([])
    visited = [False] * len(words)
    
    queue.append((begin, 0)) 
    
    while queue:
        word, cnt = queue.popleft() # 현재 단어, 변환 횟수
        
        if word == target:
            return cnt
        
        for i, next_word in enumerate(words):
            if diff_one(word, next_word) == 1 and not visited[i]:
                visited[i] = True
                queue.append((next_word, cnt + 1))

    return answer