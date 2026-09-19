from collections import deque

def solution(n, infection, edges, k):
    # 각 배양체(노드) 간의 파이프 연결 상태를 저장할 인접 리스트
    # network_graph[노드] = [(이웃 노드, 파이프 종류), ...]
    network_graph = [[] for _ in range(n + 1)]
    for node_u, node_v, pipe_kind in edges:
        network_graph[node_u].append((node_v, pipe_kind))
        network_graph[node_v].append((node_u, pipe_kind))

    def propagate_virus(current_infected_set, target_pipe_kind):
        """
        [바이러스 확산 시뮬레이션 함수]
        현재 감염된 배양체 집합(current_infected_set)에서 특정 종류의 파이프(target_pipe_kind)를
        열었을 때, 파이프를 통해 새롭게 연결되어 전파된 전체 감염 배양체 집합을 반환합니다.
        """
        # 원본 집합 보존 및 수정을 위해 set 구조로 복사
        updated_infected = set(current_infected_set)
        search_queue = deque(updated_infected)

        # BFS(너비 우선 탐색)를 이용해 열린 파이프 종류와 일치하는 경로를 타고 감염 전파
        while search_queue:
            curr_node = search_queue.popleft()
            for neighbor_node, edge_pipe_kind in network_graph[curr_node]:
                # 연결된 파이프가 현재 열린 종류와 같고, 아직 감염되지 않은 배양체라면 감염 처리
                if edge_pipe_kind == target_pipe_kind and neighbor_node not in updated_infected:
                    updated_infected.add(neighbor_node)
                    search_queue.append(neighbor_node)

        # set 집합의 중복을 제거하고 set의 set 관리를 위해 불변 객체인 frozenset 형태로 반환
        return frozenset(updated_infected)

    # current_states: 현재 단계까지 도달 가능한 모든 감염 상태(배양체 집합들)를 저장하는 집합(Set)
    # 초기 상태는 [infection] 배양체 단 하나만 감염된 상태
    current_states = {frozenset([infection])}
    max_infected_count = 1  # 감염된 배양체의 최댓값 (초기값은 최소 1개)

    # 파이프를 열었다 닫는 행위를 최대 k번 수행
    for _ in range(k):
        next_step_states = set()

        # 현재 단계에 존재할 수 있는 모든 감염 상태들을 순회
        for state in current_states:
            # 현재 상태의 감염된 배양체 수로 최댓값 갱신
            max_infected_count = max(max_infected_count, len(state))

            # 1(A타입), 2(B타입), 3(C타입) 파이프를 각각 열었을 때의 다음 상태를 탐색
            for pipe_type in (1, 2, 3):
                new_infected_state = propagate_virus(state, pipe_type)
                next_step_states.add(new_infected_state)

        # 다음 단계를 위해 상태 집합 갱신 (중복된 감염 상태는 자동 제거되어 탐색량 감소)
        current_states = next_step_states

    # k번의 모든 행동이 끝난 후 최종 도달한 상태들에 대해서도 최댓값 최종 검증
    for final_state in current_states:
        max_infected_count = max(max_infected_count, len(final_state))

    return max_infected_count