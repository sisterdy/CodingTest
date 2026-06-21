"""모든 날짜를 28일 기준으로 환산하여 계산
개인정보별 만료일을 구한 뒤
오늘 날짜 기준 파기 대상 번호 찾기
"""

def solution(today, terms, privacies):
    answer = []

    # 1. 약관 종류별 유효기간 저장
    term_dict = {}

    for term in terms:
        t, month = term.split()
        term_dict[t] = int(month)

    # 2. 날짜를 일(day) 단위로 변환
    def to_days(date):
        y, m, d = map(int, date.split("."))
        return y * 12 * 28 + m * 28 + d

    today_day = to_days(today)

    # 3. 개인정보별 만료일 계산
    # 4. 오늘 날짜와 비교하여 파기 대상 찾기
    for idx, privacy in enumerate(privacies, start=1):
        date, term = privacy.split()

        expire_day = (
            to_days(date)
            + term_dict[term] * 28
        )

        if expire_day <= today_day:
            answer.append(idx)

    return answer