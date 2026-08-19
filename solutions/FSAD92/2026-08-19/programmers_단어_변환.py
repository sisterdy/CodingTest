"""
기존 풀이는 bfs + 매번 전체 words를 순회하는 방식
이번에는 단어를 그래프로 만들어서 bfs 하는 형식으로 풀이
"""

from collections import deque

def solution(begin, target, words):
    # target이 words에 없으면 변환 불가
    if target not in words:
        return 0

    # begin도 하나의 노드니까 추가
    all_words = [begin] + words

    # 각 단어와 한 글자만 다른 단어들을 연결할 그래프
    graph = [[] for _ in range(len(all_words))]

    # 모든 단어 쌍을 비교해 정확히 한 글자만 다르면 서로 연결
    for i in range(len(all_words)):
        for j in range(i + 1, len(all_words)):
            diff_count = 0

            for k in range(len(begin)):
                if all_words[i][k] != all_words[j][k]:
                    diff_count += 1

            if diff_count == 1:
                graph[i].append(j)
                graph[j].append(i)

    # begin은 all_words의 0번 인덱스
    queue = deque([(0, 0)])
    visited = [False] * len(all_words)
    visited[0] = True

    while queue:
        current, step = queue.popleft()

        # 현재 단어가 target이면 바로 step 반환
        if all_words[current] == target:
            return step

        # 현재 단어랑 한 글자만 다른 단어들을 탐색
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, step + 1))

    return 0