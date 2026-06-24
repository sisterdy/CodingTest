"""
구해야 할 것:
호명 순서(callings) 대로 추월을 반영했을 때, 최종 선수 순서

hash로 선수이름을 통해 선수순서를 찾고 호명되었을 때 swap이 핵심.
"""

def solution(players, callings):
    # 인덱스(순위)에 해당하는 선수 이름을 저장하는 리스트 0 : "mumu"
    rank_to_player = []

    # 선수이름이 키값인 딕셔너리 "mumu" : 0
    player_to_rank = {}

    # 초기 순위 정보 저장
    for rank, player in enumerate(players): #players를 순회하며 
        player_to_rank[player] = rank #현재 인덱스는 rank에 더하고
        rank_to_player.append(player) #player의 값은 rank_to_player에 더한다.

    # 호명된 선수들을 순서대로 처리
    for called_player in callings:

        # 추월한 선수의 현재 순위 조회
        current_rank = player_to_rank[called_player]

        # 바로 앞 선수 조회
        front_player = rank_to_player[current_rank - 1]

        # 앞 선수를 한 칸 뒤로 이동
        player_to_rank[front_player] = current_rank
        rank_to_player[current_rank] = front_player

        # 추월한 선수를 한 칸 앞으로 이동
        rank_to_player[current_rank - 1] = called_player
        player_to_rank[called_player] = current_rank - 1

    # 최종 선수 순서 반환
    return rank_to_player