"""
이번에도 괴상한 형태로 주어진 입력을 분단위로 바꾸는 함수가 필요하다
startday라는 게 있어서 케이스마다 시작 요일이 다른데 이건 모듈러를 사용해야 하나...
"""

def solution(schedules, timelogs, startday):
    answer = 0
    
    # hhmm 형태로 주어진 시간을 분 단위로 바꾸기
    def time_to_minutes(time):
        hour = time // 100
        minute = time % 100
        
        return hour * 60 + minute
    
    # 직원 순회하며 일주일 출근 기록 확인
    for schedule, timelog in zip(schedules, timelogs):
        preferred_time = time_to_minutes(schedule)
        deadline = preferred_time + 10
        
        gift_available = True
        
        for offset in range(7):
            # startday에서 offset일이 지난 실제 요일 계산하는 모듈러
            today = (startday - 1 + offset) % 7 + 1
            
            # 주말이면 제외
            if today == 6 or today == 7:
                continue
                
            arrival_time = time_to_minutes(timelog[offset])
            
            if arrival_time > deadline:
                gift_available = False
                break
                
        if gift_available:
            answer += 1
            
    return answer