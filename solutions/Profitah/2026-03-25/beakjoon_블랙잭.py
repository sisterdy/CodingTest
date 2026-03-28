"""
우리는 블랙잭 문제에서 카드 3장을 골라서 M 이하인 값 중에서 가장 큰 값을 구하려고 한다.

완전 탐색을 사용해서 카드 3장을 고르는 모든 경우의 수를 탐색하자.

"""



N, M = map(int, input().split()) # 카드 개수 N, 최대 값 M

lst = sorted(map(int, input().split())) # 카드리스트를 sorted로 정렬하여 입력받은 뒤, 오름차순으로 정렬한다.
# 정렬하는 이유: 뒤로 갈수록 값이 커져서, 합이 M을 넘으면 break 가능하도록 하기 위해서.

max_sum = 0 # 최대값을 0으로 초기화하고

# ## < 카드 3장을 차례대로 탐색해보자>## #

# lst에서 인덱스와 카드값을 enumerate(리스트에서 인덱스넘버와 값을 함께 출력해주는 내장함수) 로 받아서, 3중 for문으로 카드 3장을 고르는 모든 경우의 수를 탐색
for idx, first_card in enumerate(lst): # idx : 카드의 인덱스 , first_card : 카드의 값 으로 두고 lst를 탐색.
    for j, second_card in enumerate(lst[idx+1:], idx+1): # 두번째 카드 값이 오면 첫번째 탐색 이후 범위부터 탐색.
        for third_card in lst[j+1:]: # 세번째 카드 값이 오면 두번째 탐색 이후 범위부터 탐색.
            card_total = first_card + second_card + third_card # 세 카드의 합을 구해서
            if card_total <= M: # 카드의 합이 M보다 작거나 같으면
                max_sum = max(max_sum, card_total) # 원래 있던 max_sum과 새롭게 구한 card_total을 비교해서 더 큰 값을 max_sum에 저장한다.
            else: # 카드의 합이 M보다 커지면
                break # 멈춘다. 카드리스트가 오름차순으로 정렬되어 있기에 세 카드의 합이 M보다 커지면, 이후 카드의 합도 M보다 커질 수밖에 없기 때문이다.

print(max_sum) # 이후 최종값을 출력한다.
