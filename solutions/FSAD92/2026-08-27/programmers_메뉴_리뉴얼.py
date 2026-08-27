"""
같은 조합을 주문한 손님 >= 2
course의 각 길이마다 '가장 많이' 주문된 조합을 '모두' 선택

음 백트래킹?
"""
def solution(orders, course):
    # course 길이별로 메뉴 조합의 등장 횟수 저장
    answer = []
    menu_count = {}
    
    for size in course:
        menu_count[size] = {}

    # 한 주문에서 target_size개의 메뉴를 선택하는 조합을 생성
    def dfs(order, target_size, start, selected):
        if len(selected) == target_size:
            combination = ''.join(selected)

            # 해당 combination의 등장 횟수 증가시키기
            menu_count[target_size][combination] = (
                menu_count[target_size].get(combination, 0) + 1
            )
            return

        # start부터 뒤쪽 메뉴 선택하기
        for i in range(start, len(order)):
            selected.append(order[i])

            # 현재 선택 메뉴 뒤쪽부터 dfs 시작
            dfs(order, target_size, i + 1, selected)
            # 백트래킹
            selected.pop()

    # 모든 손님의 주문 하나씩 확인하기
    for order in orders:
        order = ''.join(sorted(order))  # 순서만 다른 중복 메뉴 방지

        for size in course:
            if size <= len(order):
                dfs(order, size, 0, [])

    # course 길이별로 최다 주문 조합 조회
    for size in course:
        counts = menu_count[size]

        if not counts:
            continue

        max_count = max(counts.values())

        # 최소 2명 이상의 손님이 주문했는지 체크
        if max_count < 2:
            continue

        for combination, count in counts.items():
            if count == max_count:
                answer.append(combination)

    return sorted(answer)