"""
체육 수업을 들을 수 있는 학생의 최댓값을 return

간단하게
i가 1일 때는 lost[i+1]이 reserve에 존재하는지 확인하고 없으면 count--
i > 1 일 때는 lost[i-1] 또는 lost[i+1]이 reserve에 존재하는지 확인하고 없으면 count --

기존 코드 : 이렇게 하니 인덱스 에러가 떴다. 일단 for i in lost에서 i는 잃어버린 학생의 번호(값)이 되기 때문에 인덱스를 벗어나는 에러가 나는 것.

def solution(n, lost, reserve):
    answer = 0
    count = n
    
    for i in lost:
        if len(lost) >= 2: 
            if i == 1:
                if lost[i+1] in reserve:
                    count -= 1
            elif i > 1:
                if not (lost[i-1] or lost[i+1] in reserve):
                    count -= 1
    answer = count
    return answer

"""

def solution(n, lost, reserve):
    # 여벌이 있지만 도난당한 학생은 제외한 리스트를 만들자
    real_reserve = []
    for r in reserve:
        if r not in lost:
            real_reserve.append(r)
            
    real_lost = []
    for l in lost:
        if l not in reserve:
            real_lost.append(l)
    
    # 그리디는 매 순간 최선의 선택을 해야함. 그래서 오름차순으로 정렬.
    real_reserve.sort()
    real_lost.sort()
            
    answer = n
    
    # 내 앞사람에게 빌릴 수 있는지, 아니라면 뒷사람에게 빌릴 수 있는지 확인하고 둘 다 불가능하면 수업 인원에서 -= 1
    for student in real_lost:
        if student - 1 in real_reserve:
            real_reserve.remove(student - 1)
        elif student + 1 in real_reserve:
            real_reserve.remove(student + 1)
        else:
            answer -= 1
    
    return answer