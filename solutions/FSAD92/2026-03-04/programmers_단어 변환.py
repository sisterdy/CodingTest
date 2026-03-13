"""
가장 짧은 변환 과정? bfs?
근데... 한 번에 한 개의 알파벳만 바꿀 수 있다?
어떻게 하지?
"""
from collections import deque

def solution(begin, target, words):    
    # 큐 초기화(시작 단어, 현재까지의 단계)
    queue = deque([(begin, 0)])
    
    # 방문 체크(이미 거쳐온 단어 재방문 방지)
    visited = set([begin])
    
    while queue:
        # 큐에서 가장 오래된 데이터를 꺼냄
        curr_word, step = queue.popleft()
        
        # 목표에 도달했으면 바로 현재까지의 단계를 반환
        if curr_word == target:
            return step
        
        # 현재 단어에서 갈 수 있는 다음 단어들을 탐색
        for word in words:
            if word not in visited:
                # 한 글자만 다른지 확인하는 로직(문제에서 한번의 변환 당 한 글자만 변환할 수 있다고 제한했기 때문)
                diff_count = 0
                for i in range(len(curr_word)):
                    if curr_word[i] != word[i]:
                        diff_count += 1
                
                if diff_count == 1:
                    # 조건을 만족(글자 차이가 정확히 1개)하면 방문 처리 후 큐에 추가
                    visited.add(word)
                    queue.append((word, step + 1))
    
    # 큐가 빌 때까지 목표를 못 찾으면 0을 return 하라고 문제에 써있다
    return 0