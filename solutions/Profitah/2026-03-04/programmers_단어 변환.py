"""
BFS (너비 우선 탐색) + 그래프 (최단 변환 단계)

🎯 우리가 구하는 것
→ begin 단어를 target 단어로 변환하는
   "최소 변환 횟수"

📌 문제 해석
- 한 번에 한 글자만 변경 가능
- 변경된 단어는 words 안에 존재해야 함
- begin → target 으로 갈 수 없다면 0 반환

📌 핵심 전략

1. target이 words에 없으면 애초에 도달 불가 → 0 반환
2. BFS를 사용하여 단계(level)별 탐색
3. 현재 단어와 한 글자만 다른 단어를 찾아 큐에 추가
4. target에 도달하면 그때의 변환 횟수 반환

👉 왜 BFS인가?
BFS는 "최단 거리"를 보장한다.
단어 변환 횟수의 최소값을 구해야 하므로 BFS가 적합하다.
"""

from collections import deque

def solution(begin, target, words):
    # target이 words에 없다면 변환 불가능
    if target not in words:
        return 0
    
    queue = deque()
    queue.append((begin, 0))  # (현재 단어, 변환 횟수)
    visited = set()          # 이미 방문한 단어 저장
    
    while queue:
        current, count = queue.popleft()  # 현재 단어와 변환 횟수
        
        # 목표 단어에 도달했다면 최소 변환 횟수 반환
        if current == target:
            return count
        
        # words 목록에 있는 단어들과 비교
        for word in words:
            if word not in visited:  # 아직 방문하지 않았다면
                diff = 0  # 다른 글자 개수
                
                # 한 글자씩 비교
                for i in range(len(word)):
                    if current[i] != word[i]:
                        diff += 1
                
                # 한 글자만 다르다면 변환 가능
                if diff == 1:
                    visited.add(word)                 # 방문 처리
                    queue.append((word, count + 1))  # 다음 단계 추가
    
    # 끝까지 도달 못하면 0 반환
    return 0