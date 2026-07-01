"""
기존 방식: 하루씩 진도 올리기
신규 방식: 각 기능이 며칠 뒤 완료되는지를 먼저 계산.. 그 다음에 배포 묶음을 만든다
"""
def solution(progresses, speeds):
    # 각 기능이 완료되기까지 필요한 날짜를 저장한다.
    answer = []
    complete_days = []
    
    for progress, speed in zip(progresses, speeds):
        remaining_work = 100 - progress
        required_day = (remaining_work + speed - 1) // speed

        complete_days.append(required_day)

    # 첫 번째 기능의 완료일이 첫 배포 묶음의 기준일
    release_day = complete_days[0]
    release_count = 1

    # 두 번째 기능부터 체크
    for day in complete_days[1:]:
        # 현재 배포 기준일 안에 완료되는 기능이면 같이 묶기
        if day <= release_day:
            release_count += 1

        # 현재 배포 기준일보다 늦게 완료되면 배포 묶음 새롭게 만들기
        else:
            answer.append(release_count)

            release_day = day
            release_count = 1

    # 세고 있던 마지막 배포 묶음이 있다면 추가!
    answer.append(release_count)

    return answer