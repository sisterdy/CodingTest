"""
최대한 많은 바이러스 감염
한 번 열 때 같은 파이프를 한 번에 열고 닫으므로 dfs...?
"""
def solution(n, infection, edges, k):
    # 각 노드에 연결된 [다음 노드, 파이프 타입]을 저장하는 인접 리스트
    graph = [[] for _ in range(n + 1)]

    for node1, node2, pipe_type in edges:
        graph[node1].append((node2, pipe_type))
        graph[node2].append((node1, pipe_type))

    answer = 1

    # 현재 상태에서 특정 타입의 파이프를 열었을 때 새 감염 노드를 dfs로 찾기
    def spread(infected, target_type):
        new_infected = infected.copy()

        # 이미 감염된 모든 노드가 감염 확산의 시작점이 될 수 있음
        stack = list(infected)

        while stack:
            current = stack.pop()

            for next_node, pipe_type in graph[current]:
                # 현재 열어둔 타입의 파이프만 이동 가능
                if pipe_type != target_type:
                    continue

                # 이미 감염된 노드는 다시 방문할 필요가 없음
                if next_node in new_infected:
                    continue

                new_infected.add(next_node)
                stack.append(next_node)

        return new_infected

    # 어떤 타입의 파이프를 어떤 순서로 열지 DFS로 완탐
    def dfs(depth, infected):
        nonlocal answer

        # 현재까지 감염시킨 최대 배양체 수 갱신
        answer = max(answer, len(infected))

        # 최대 행동 횟수에 도달했으면 종료
        if depth == k:
            return

        # 이미 전부 감염시켰다면 더 탐색할 필요가 없음
        if len(infected) == n:
            return

        # A, B, C 타입을 하나씩 열어보기
        for pipe_type in range(1, 4):
            next_infected = spread(infected, pipe_type)
            dfs(depth + 1, next_infected)

    # 초기값은 infection번 배양체 하나만 감염
    dfs(0, {infection})

    return answer