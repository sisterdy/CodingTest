"""
구해야 하는 것
: 상품을 받을 수 있는 직원의 수

---

minute(출근마감시간) 과 실제 출근기록을 확인하고
근태가 멀쩡한 직원에게만 상품을 준다!

---

구하는 방법
1. 직원마다 '출근 인정 마감 시간(희망 출근 시간 + 10분)'을 미리 계산한다.
2. 각 직원의 일주일 출근 기록을 확인한다.
3. 토요일과 일요일은 검사하지 않는다.
4. 평일에 단 하루라도 마감 시간을 넘겨 출근했다면 상품을 받을 수 없다.
5. 모든 평일을 통과한 직원 수를 반환한다.

"""


def solution(schedules, timelogs, startday):
    # 최종적으로 상품을 받을 직원 수
    answer = 0

    # 직원별 출근 인정 마감 시간을 저장하는 리스트
    deadline_times = []

    # 1. 직원별 마감 시간 계산
    for schedule in schedules:

        # HHMM 형태를 시와 분으로 분리 (750에 10더하면 760 이런식으로 되는거 방지)
        hour = schedule // 100
        minute = schedule % 100

        # 출근 인정 시간(+10분) 
        minute += 10

        # 분이 60 이상이 되면 시간을 1 증가시키고 분 조정
        if minute >= 60:
            hour += 1
            minute -= 60

        # ! 다시 HHMM 형태(예: 910)로 저장
        deadline_times.append(hour * 100 + minute)

    # 2. 모든 직원 검사
    for employee in range(len(schedules)):

        # 현재 직원이 상품을 받을 수 있는지 여부
        is_success = True

        # 일주일(7일) 출근 기록 확인
        for day in range(7):

            # 현재 날짜가 무슨 요일인지 계산
            # 월=1 화=2 수=3 목=4 금=5 토=6 일=7
            weekday = (startday + day - 1) % 7 + 1

            # 토요일, 일요일은 이벤트 대상이 아니므로 건너뛴다.
            if weekday in (6, 7):
                continue

            # 실제 출근 시간이 마감 시간을 초과하면 상품 지급 대상에서 제외
            if timelogs[employee][day] > deadline_times[employee]:
                is_success = False
                break

        # 평일을 모두 통과했다면 상품 지급
        if is_success:
            answer += 1

    return answer