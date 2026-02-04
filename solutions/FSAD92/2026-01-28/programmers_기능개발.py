"""
progress 원소의 작업 진도를 관리하기 위해 인덱스 역할을 할 pointer를 만들자.
for 루프를 돌며 해당 progresses의 원소에 대응하는 speeds 값을 더해야 한다. 이걸 하루치 업무라 생각하자.
업무가 끝나면 오늘 배포가 가능한 기능이 있는지 체크.
"""
def solution(progresses, speeds):
    answer = []
    pointer = 0     # 현재 배포되어야 할 가장 앞선 기능의 인덱스
    n = len(progresses)

    
    while pointer < n:  # 모든 기능이 배포될 때까지 (포인터가 progress의 끝에 도달할 때까지)
        # 하루치 작업 진행
        for i in range(pointer, n):
            progresses[i] += speeds[i]

        # 작업이 끝나면 오늘 배포 가능한 기능이 있는지 확인
        if progresses[pointer] >= 100:
            count = 0
            # 현재 포인터부터 연속으로 완료된 기능이 몇 개인지 카운트
            while pointer < n and progresses[pointer] >= 100:
                count += 1
                pointer += 1  # 배포했으므로 다음 기능으로 포인터 이동
            
            # 오늘 배포에 나간 기능의 개수를 추가
            answer.append(count)
            
    return answer