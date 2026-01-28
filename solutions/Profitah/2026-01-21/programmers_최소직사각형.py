"""
명함의 가로, 세로가 주어졌다.
모든 명함을 [큰 값, 작은 값]으로 정렬하라

"면적 줄이기.
가로와 세로의 길이를 비교해 더 작은 수를 택하는 재귀함수 만들고
그 안에서 최대 수 선택.
    너비를 구한다. "
-로 풀려 하였으나 불필요한 방식이라는 생각이 들어 리스트 원소 탐색으로 코드 수정.
}"""


def solution(sizes):
    
    # 지갑의 가로(큰 쪽) 최대값을 저장할 변수
    wallet_weight = 0
    
    # 지갑의 세로(작은 쪽) 최대값을 저장할 변수
    wallet_height = 0
    
    # 각 명함에서 큰 값을 뽑아 그 중 가장 큰 값을 지갑의 가로로 결정
    for max_int in sizes:
        wallet_weight = max(wallet_weight, max(max_int))
        # max(max_int)는 해당 명함의 긴 변
        # wallet_weight에는 지금까지 본 명함들 중 가장 긴 변이 저장됨
        
    # 각 명함에서 작은 값을 뽑아 그 중 가장 큰 값을 지갑의 세로로 결정
    for second_max_int in sizes:
        wallet_height = max(wallet_height, min(second_max_int))
        # min(second_max_int)는 해당 명함의 짧은 변
        # wallet_height에는 지금까지 본 명함들 중 가장 긴 '짧은 변'이 저장됨
    
    # 지갑의 최종 면적 = 가로 * 세로
    answer = wallet_weight * wallet_height
    return answer
