"""
옷장에 상의 하의 겉옷 악세사리가 있다.
종류별로 최대 1가지 의상만 착용할 수 있을 때, 입을 수 있는 모든 조합을 구하라.

"""

# 1. 옷을 입을 수 있는 전체 경우의 수 구하기
# (한 옷의 종류수 + 1(안입는경우의수)) * (한 옷의 종류수 + 1(안입는경우의수)) * (악세사리 + 1(안입는경우의수)) 

def solution(clothes):
    from collections import Counter 
    answer = 1 # 최종 결과 출력을 위한 변수. (1로 초기화)
    cnt = Counter() 
    
    for cloth in clothes: # clothes의 각 원소에 대해
        cnt[cloth[1]] += 1 # 옷의 종류별 개수 세기
    
    for v in cnt.values(): # 종류별 경우의 수 계산
        answer *= (v + 1) # (한 옷의 종류수 + 1(안입는경우의수)) 
    
    return answer - 1 # 2. 이 아이는 최소 1개의 옷을 입고 다니기 때문에, 아무것도 안 입는 경우의 수는 카운트 하지 않기로 한다. 더한 값에서 빼주자.