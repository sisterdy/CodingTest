"""
선물을 가장 많이 받을 친구가 받을 선물의 수를 리턴
준 사람 / 받은 사람 간의 선물 정보를 저장
friends의 원소들의 선물 지수를 저장

gifts를 순회하며 giver를 키, receiver들로 이루어진 리슽트를 값으로 갖는 defaultdict 딕셔너리를 하나 만들자. -> gift_dict
이 gift_dict를 순회하면서 각 friends들의 선물 지수를 계산하자. enumerate를 이용하면 될 것 같고... 선물 지수는 gift_index로 하자.
"""
from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    
    gift_dict = defaultdict(list)
    history = defaultdict(dict)
    
    for gift in gifts:
        giver, receiver = gift.split()
        gift_dict[giver].append(receiver)
        
        if receiver not in history[giver]:
            history[giver][receiver] = 0
        history[giver][receiver] += 1
        
    gift_index = [0] * len(friends)
    
    for i, friend in enumerate(friends):
        given_count = len(gift_dict[friend])    # 준 선물 수
        received_count = 0                      # 받은 선물 수
        for receivers in gift_dict.values():
            received_count += receivers.count(friend)
        gift_index[i] = given_count - received_count    # 선물 지수
        
    next_month_count = [0] * len(friends)
    
    # 모든 친구 쌍 비교
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            A = friends[i]
            B = friends[j]
            
            # 다음 달 선물 받을 사람 결정
            AtoB = history[A].get(B, 0)
            BtoA = history[B].get(A, 0)
            
            if AtoB > BtoA:
                next_month_count[i] += 1
            elif AtoB < BtoA:
                next_month_count[j] += 1
            
            # 주고 받은 게 같다면?
            else:
                if gift_index[i] > gift_index[j]:
                    next_month_count[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_month_count[j] += 1
        
    return max(next_month_count)
