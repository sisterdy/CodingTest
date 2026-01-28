"""
! 체육수업에 참여할 수 있는 학생의 최대 인원 수를 출력하자!

n을 입력받아 1부터 n까지 학생 리스트를 만든다.
lost와 reserve를 반영해 각 학생의 체육복 수를 조정한다.
체육복이 없는 학생은 앞이나 뒤 학생에게 빌린다.
체육복이 1벌 이상인 학생은 1, 아니면 0으로 계산한다.
이 값들을 모두 더한 결과를 answer로 반환한다."""

def solution(n, lost, reserve):
    # 1부터 n이 마지막 원소인 학생 번호 리스트 생성
    students = list(range(1, n+1))
    
    # 모든 학생이 처음에 체육복 1벌씩 가지고 있다고 가정
    clothes = {i: 1 for i in students}
    
    # 체육복을 도난당한 학생 
    for l in lost:
        clothes[l] -= 1
    
    # 여벌 체육복이 있는 학생 
    for r in reserve:
        clothes[r] += 1
    
    # 체육복이 없는 학생에게 빌려주기 과정
    for i in students:
        if clothes[i] == 0:   # 현재 학생이 체육복이 없을 때
            # 앞 번호 학생에게서 빌릴 수 있는지 확인
            if i-1 >= 1 and clothes[i-1] == 2:
                clothes[i-1] -= 1   # 앞 학생의 여벌 사용
                clothes[i] += 1     # 현재 학생이 체육복 받음
            # 앞에서 못 빌렸다면, 뒤 번호 학생에게서 빌리기
            elif i+1 <= n and clothes[i+1] == 2:
                clothes[i+1] -= 1   # 뒤 학생의 여벌 사용
                clothes[i] += 1     # 현재 학생이 체육복 받음
    
    # 체육복을 입을 수 있는 학생 수 세기
    answer = 0
    for i in students:
        if clothes[i] >= 1:   # 체육복이 1벌 이상이면 수업 가능
            answer += 1
        else:                 # 체육복이 없으면 수업 불가
            answer += 0
    
    return answer
