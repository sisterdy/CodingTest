# 가입자 늘리기 -> 판매액 늘리기
# 모든 할인률 조합 완전탐색으로 (개수가 7개까지인게 힌트)
# 1. dfs돌리면서 모든 조합 만든다.
# 2. 그 조합 안에서 users로 for문돌린다.
# 3. 가입자 수가 더 많음 → 교체 / 가입자 수가 같음 + 매출이 더 많음 → 교체

def solution(users, emoticons):
    answer = [0, 0] # 플러스 가입 수, 이모티콘 매출액
    
    def dfs(discounts):
        # 모든 조합 나옴, users계산하기
        if len(discounts) == len(emoticons):
            plus = 0 # 플러스 가입자수
            sales = 0 # 매출
            for user in users:
                total = 0
                
                for i in range(len(emoticons)):
                    # 할인 조건 만족
                    if user[0] <= discounts[i]:
                        total += emoticons[i] * (100 - discounts[i]) // 100
                
                # 구매 비용이 기준 가격 이상이면
                if total >= user[1]:
                    # 구매취소, 플러스 가입
                    plus += 1
                else:
                    # 판매액 증가
                    sales += total
            
            # 가입자수가 기존보다 많은 경우
            if plus > answer[0]:
                answer[0] = plus
                answer[1] = sales
            # 가입자수는 같지만 매출이 큰경우
            elif plus == answer[0] and sales > answer[1]:
                answer[1] = sales
                
            return
        
        # 할인율 조합
        for discount in [10, 20, 30, 40]:
            dfs(discounts + [discount])
            
    # 파라미터에 할인율 조합 들어감
    dfs([]) 
    return answer