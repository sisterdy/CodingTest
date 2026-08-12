"""
dfs로 풀려다가 경우의 수가 4^7 정도면 완탐으로 가도 되지 않나 싶어서 완탐으로 접근.
"""
def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]

    # 가능한 할인율 조합을 저장
    discount_cases = [[]]

    # 가능한 모든 할인율 조합을 만들기
    for _ in range(len(emoticons)):
        next_cases = []

        for case in discount_cases:
            for rate in discount_rates:
                next_cases.append(case + [rate])

        discount_cases = next_cases

    best_subscribers = 0
    best_sales = 0

    for discounts in discount_cases:
        subscribers = 0
        sales = 0

        # 각 사용자가 현재 할인율에서 어떤 이모티콘을 구매하는지 계산
        for min_discount, subscribe_price in users:
            total_price = 0

            for i in range(len(emoticons)):
                # 사용자가 원하는 할인율 이상인 이모티콘만 구매
                if discounts[i] >= min_discount:
                    discounted_price = (
                        emoticons[i] * (100 - discounts[i]) // 100
                    )
                    total_price += discounted_price

            # 구매 금액이 기준 이상이면 이모티콘 플러스에 가입
            if total_price >= subscribe_price:
                subscribers += 1
            else:
                # 가입하지 않은 사용자의 구매 금액만 매출에 포함
                sales += total_price

        # 1순위: 이모티콘 플러스 가입자 수, 2순위: 가입자 수가 같다면 판매 금액
        if subscribers > best_subscribers:
            best_subscribers = subscribers
            best_sales = sales

        elif subscribers == best_subscribers and sales > best_sales:
            best_sales = sales

    return [best_subscribers, best_sales]