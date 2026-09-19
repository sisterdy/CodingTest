"""
[해시] 주차 요금 계산

입·출차 기록을 바탕으로 차량별 총 주차 시간을 계산한 뒤,
요금표에 따라 차량별 주차 요금을 반환하는 문제.

- 해시(딕셔너리): 차량번호를 Key로 사용하여 입차 시간과 누적 주차 시간을 빠르게 조회·저장

"""

import math

def solution(fees, records):
    # 기본시간, 기본요금, 단위시간, 단위요금
    basic_time, basic_fee, unit_time, unit_fee = fees

    in_car = {}      # 현재 주차 중인 차량 {차량번호: 입차시간}
    total_time = {}  # 차량별 누적 주차시간 {차량번호: 총 주차시간}

    # 1. 입·출차 기록을 순회하며 차량별 누적 주차시간 계산
    for record in records:

        # "05:34 5961 IN" → 시간, 차량번호, 상태 분리
        time, car, state = record.split()

        # "HH:MM" 형식을 분(minute)으로 변환
        h, m = map(int, time.split(":"))
        minute = h * 60 + m

        # 입차라면 입차 시간 저장
        if state == "IN":
            in_car[car] = minute

        # 출차라면 주차 시간 계산
        else:
            parked = minute - in_car[car]  # 이번 주차 시간
            total_time[car] = total_time.get(car, 0) + parked  # 누적 시간 합산
            del in_car[car]  # 출차했으므로 주차 목록에서 제거

    # 2. 출차 기록이 없는 차량은 23:59 출차로 처리
    end = 23 * 60 + 59

    for car, in_time in in_car.items():
        parked = end - in_time  # 23:59까지 주차한 시간
        total_time[car] = total_time.get(car, 0) + parked  # 누적 시간 합산

    answer = []

    # 3. 차량번호를 오름차순으로 정렬하여 요금 계산
    for car in sorted(total_time):

        time = total_time[car]  # 해당 차량의 총 주차 시간

        # 기본 시간 이하면 기본 요금
        if time <= basic_time:
            fee = basic_fee

        # 기본 시간을 초과하면 추가 요금 계산
        else:
            extra = time - basic_time  # 초과한 시간
            fee = basic_fee + math.ceil(extra / unit_time) * unit_fee

        answer.append(fee)  # 계산된 요금 저장

    # 4. 차량번호 순으로 요금 반환
    return answer