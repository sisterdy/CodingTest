import math

def solution(progresses, speeds):
    answer = []  # 각 배포마다 배포되는 기능의 개수를 저장할 리스트
    
    # 각 작업이 완료되는 데 필요한 일수를 계산
    # math.ceil로 올림 처리 (예: 7.1일 → 8일)
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    i = 0  # 현재 처리 중인 작업의 인덱스
    
    # 모든 작업을 처리할 때까지 반복
    while i < len(days):
        기준일 = days[i]  # 현재 배포의 기준이 되는 첫 번째 작업의 완료일
        count = 1  # 현재 배포에 포함될 기능 개수 (최소 1개, 자기 자신)
        
        # 기준일 이하로 완료되는 뒤의 작업들을 찾아서 카운트
        # 조건: (1) 배열 범위 내 + (2) 기준일보다 빨리 또는 같은 날 완료
        while i + count < len(days) and days[i + count] <= 기준일:
            count += 1  # 함께 배포 가능한 기능 +1
        
        answer.append(count)  # 이번 배포에서 배포되는 기능 개수 추가
        i += count  # 다음 배포의 시작점으로 이동 (처리한 작업들은 건너뜀)
    
    return answer