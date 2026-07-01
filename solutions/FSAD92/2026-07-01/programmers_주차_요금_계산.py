"""
차량별로 딕셔너리를 만들고 입차 시간은 빼고, 출차 시간은 더하자.
"""
def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees

    # hh:mm으로 된 시각 문자열을 분 단위 정수로 바꾸는 함수
    def time_to_minute(time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)

    # 차량별 누적 주차 시간 계산용 딕셔너리
    parking_time = {}

    # 마지막에 출차 기록 없는 차량을 찾기 위해 현재 주차장에 있는 차량을 저장하는 set
    parked_cars = set()

    for record in records:
        time, car_number, status = record.split()
        minute = time_to_minute(time)

        # 처음 주차하는 차량 정보 등록
        if car_number not in parking_time:
            parking_time[car_number] = 0

        if status == "IN":
            # 입차 시간은 나중에 출차 시간과 빼야 하므로 미리 음수로 저장
            parking_time[car_number] -= minute
            parked_cars.add(car_number)

        else:
            # 출차 시간은 더한다
            parking_time[car_number] += minute
            parked_cars.remove(car_number)

    # 출차 기록이 없는 차량은 23:59에 출차한 것으로 처리
    end_of_day = time_to_minute("23:59")

    for car_number in parked_cars:
        parking_time[car_number] += end_of_day

    
    # 차량 번호가 작은 순서대로 요금을 계산
    for car_number in sorted(parking_time.keys()):
        total_time = parking_time[car_number]

        if total_time <= base_time:
            fee = base_fee
        else:
            extra_time = total_time - base_time

            # 초과 시간이 단위 시간으로 나누어떨어지지 않으면 올림 처리
            extra_count = (extra_time + unit_time - 1) // unit_time
            fee = base_fee + extra_count * unit_fee

        answer.append(fee)

    return answer