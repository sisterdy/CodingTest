"""
1번 노드에서 가장 멀리 떨어진 노드의 개수를 구하자

입력값 : n : 노드의 개수
         edge : 간선 정보 리스트 [출발, 도착]

풀이 : BFS (너비 우선 탐색)

1번 노드에서 BFS 탐색을 시작하여
각 노드까지의 최단 거리를 distances 배열에 저장한다.

distances 배열에서 최댓값을 구하고
해당 최댓값과 같은 거리를 가진 노드의 개수를 반환한다.

출력값 : 1번 노드에서 가장 멀리 떨어진 노드의 개수
"""

from collections import defaultdict


def bfs(graph, start, distances):
    q = [start]             # 탐색할 노드를 담는 큐, 시작 노드로 초기화
    visited = set([start])  # 방문한 노드를 저장하는 집합, 중복 방문 방지

    while len(q) > 0:                    # 큐가 빌 때까지 반복
        current = q.pop(0)               # 큐의 맨 앞 노드를 꺼냄 (FIFO)
        for neighbor in graph[current]:  # 현재 노드의 인접 노드를 순회
            if neighbor not in visited:              # 아직 방문하지 않은 노드라면
                visited.add(neighbor)                # 방문 처리
                q.append(neighbor)                   # 큐에 추가
                distances[neighbor] = distances[current] + 1  # 현재 노드 거리 + 1


def solution(n, edge):

    # 양방향 그래프 생성
    graph = defaultdict(list)       # 키가 없어도 빈 리스트로 초기화되는 딕셔너리
    for e in edge:
        graph[e[0]].append(e[1])    # 출발 → 도착 방향 추가
        graph[e[1]].append(e[0])    # 도착 → 출발 방향 추가 (양방향)

    # 1번 노드에서 BFS 탐색 시작
    distances = [0] * (n + 1)       # 각 노드까지의 거리 배열, 인덱스 1~n 사용
    bfs(graph, 1, distances)        # 1번 노드 기준으로 모든 노드까지의 거리 계산

    # 가장 먼 거리 및 해당 노드 개수 계산
    max_distance = max(distances)   # distances 배열에서 최댓값(가장 먼 거리) 추출
    answer = 0                      # 최댓값과 같은 거리를 가진 노드 개수

    for distance in distances:          # 모든 노드의 거리를 순회
        if distance == max_distance:    # 최댓값과 같은 거리면
            answer += 1                 # 카운트 증가

    return answer  # 가장 멀리 떨어진 노드의 개수 반환