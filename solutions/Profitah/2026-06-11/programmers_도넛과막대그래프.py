"""
주어지는 것
- 여러 개의 도넛 그래프, 막대 그래프, 8자 그래프를
  하나의 새로운 정점에 연결하여 만든 전체 그래프의 간선 정보

구해야 할 것
- 그래프들을 연결하기 위해 추가된 생성 정점 번호
- 생성 정점에 연결된
  도넛 그래프 개수
  막대 그래프 개수
  8자 그래프 개수

즉, 완성된 그래프의 간선 정보만 보고
원래 어떤 종류의 그래프가 몇 개 연결되어 있었는지 추론하는 문제
"""

from collections import defaultdict

def solution(edges):
    indegree = defaultdict(int)
    outdegree = defaultdict(int)

    # 1. 각 정점의 진입 차수(indegree),
    #    진출 차수(outdegree) 계산
    for a, b in edges:
        outdegree[a] += 1
        indegree[b] += 1

    center = stick = eight = 0

    # 2. 차수 조건을 이용하여
    #    생성 정점, 막대 그래프, 8자 그래프 판별
    for node in set(indegree) | set(outdegree):

        # 생성 정점
        if indegree[node] == 0 and outdegree[node] >= 2:
            center = node

        # 막대 그래프의 끝점
        elif indegree[node] >= 1 and outdegree[node] == 0:
            stick += 1

        # 8자 그래프의 중심점
        elif indegree[node] >= 2 and outdegree[node] == 2:
            eight += 1

    # 3. 생성 정점의 진출 차수는
    #    연결된 전체 그래프 수와 같다.
    #    따라서 도넛 = 전체 그래프 - 막대 - 8자
    donut = outdegree[center] - stick - eight

    return [center, donut, stick, eight]