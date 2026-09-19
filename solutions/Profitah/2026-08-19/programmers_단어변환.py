"""
[구해야 할 것]
- begin 단어에서 target 단어로 변환하기 위한 최소 단계 수 (변환 불가능 시 0)

[풀이 흐름]
1. target이 words 목록에 없으면 변환 불가능하므로 바로 0 반환
2. BFS를 활용해 (현재 단어, 변환 횟수)를 큐에 넣고 최단 경로 탐색
3. 아직 방문하지 않은 단어 중 알파벳이 딱 1개만 다른 단어로만 이동하며 큐에 삽입
4. target 단어에 도달하는 즉시 현재까지의 변환 횟수 반환
"""

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current, count = queue.popleft()

        if current == target:
            return count

        for word in words:
            if word not in visited:
                # 한 글자만 다른 단어인지 검사
                diff = sum(1 for a, b in zip(current, word) if a != b)

                if diff == 1:
                    visited.add(word)
                    queue.append((word, count + 1))

    return 0