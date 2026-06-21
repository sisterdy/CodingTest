""" 두 친구를 비교하여
1) 더 많이 선물을 준 사람이 다음 달 선물 1개 획득
# 2) 주고받은 수가 같다면 선물 지수가 높은 사람이 획득
이를 주어진 모든 친구 쌍에 대해 계산하여 누군가가 가장 많이 받는 선물 개수 구하기

friends : 친구들
gifts : 선물내역
"""
def solution(friends, gifts):
    answer = 0
    n = len(friends)

    friend_dict = dict()
    for i in range(n):
        friend_dict[friends[i]] = i

    # table[i][j] : i가 j에게 준 선물 개수
    table = [[0] * n for _ in range(n)]

    # 선물 지수 저장
    # (준 선물 수 - 받은 선물 수)
    gift_indices = [0] * n

    for gift in gifts:
        giver, receiver = gift.split()
        idx1, idx2 = friend_dict[giver], friend_dict[receiver]

        # 선물 지수 갱신
        gift_indices[idx1] += 1
        gift_indices[idx2] -= 1

        # 선물 교환 내역 기록
        table[idx1][idx2] += 1

    # 다음 달 받을 선물 개수
    get_gift = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            # i가 j보다 선물을 더 많이 줬다면
            # 다음 달 i가 선물 1개 받음
            if table[i][j] > table[j][i]:
                get_gift[i] += 1

            # 주고받은 선물 수가 같다면
            # 선물 지수가 더 높은 사람이 선물 1개 받음
            elif table[i][j] == table[j][i]:
                if gift_indices[i] > gift_indices[j]:
                    get_gift[i] += 1

    # 가장 많이 받는 사람의 선물 개수 반환
    return max(get_gift)