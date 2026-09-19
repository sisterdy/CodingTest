def solution(users, emoticons):
    # 이모티콘에 적용 가능한 할인율 후보 (10%, 20%, 30%, 40%)
    discount_rates = [10, 20, 30, 40]
    n = len(emoticons)  # 이모티콘 개수 (최대 7개)

    # 정답 저장 변수: [플러스 서비스 가입자 수, 이모티콘 매출액]
    # 우선순위: 가입자 수 최대화 > 매출액 최대화
    answer = [0, 0]

    def calculate(rates):
        """
        주어진 할인율 조합(rates)에 대해
        전체 사용자를 순회하며 (가입자 수, 매출액)을 계산하는 함수
        rates[i] = i번째 이모티콘의 할인율
        """
        subscribers = 0    # 이모티콘 플러스 서비스 가입자 수
        total_sales = 0     # 이모티콘 개별 구매로 발생한 총 매출액

        # 사용자 한 명씩 확인
        for min_rate, target_amount in users:
            # min_rate: 이 사용자가 구매를 고려하는 최소 할인율 조건
            # target_amount: 이 금액 이상 구매하면 플러스 서비스에 가입함

            purchase_amount = 0  # 이 사용자가 실제로 구매하는 금액 합계

            # 이모티콘을 하나씩 확인하며, 사용자의 조건을 만족하는 것만 구매
            for i in range(n):
                if rates[i] >= min_rate:
                    # 할인율이 사용자의 최소 조건 이상이면 구매 대상
                    # 정가 * (100 - 할인율) / 100 = 할인 적용된 가격
                    purchase_amount += emoticons[i] * (100 - rates[i]) // 100

            # 구매 금액이 목표 금액 이상이면 -> 이모티콘 구매 대신 플러스 서비스 가입
            if purchase_amount >= target_amount:
                subscribers += 1
                # 주의: 이 경우 개별 이모티콘 구매 매출은 발생하지 않음 (0으로 처리)
            else:
                # 목표 금액 미만이면 계산된 금액만큼 실제 매출로 집계
                total_sales += purchase_amount

        return subscribers, total_sales

    def dfs(index, rates):
        """
        각 이모티콘(index번째)에 대해 할인율을 하나씩 정해가며
        모든 조합을 완전탐색하는 백트래킹 함수
        rates: 현재까지 정해진 할인율 리스트 (백트래킹으로 채워나감)
        """
        nonlocal answer

        # 모든 이모티콘에 대해 할인율을 다 정한 경우 (리프 노드 도달)
        if index == n:
            subscribers, total_sales = calculate(rates)

            # 더 나은 조합인지 비교
            # 1순위: 가입자 수가 더 많으면 갱신
            # 2순위: 가입자 수가 같다면 매출액이 더 크면 갱신
            if subscribers > answer[0] or (subscribers == answer[0] and total_sales > answer[1]):
                answer = [subscribers, total_sales]
            return

        # 현재 인덱스의 이모티콘에 4가지 할인율을 하나씩 대입해보며 재귀 호출
        for rate in discount_rates:
            rates.append(rate)          # 할인율 선택 (트리에서 한 단계 내려감)
            dfs(index + 1, rates)       # 다음 이모티콘에 대해 재귀적으로 탐색
            rates.pop()                 # 백트래킹: 선택 취소하고 다른 할인율 시도

    # index=0부터 시작해서 빈 리스트에 할인율을 하나씩 채워나가며 완전탐색 시작
    dfs(0, [])

    return answer