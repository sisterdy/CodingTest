"""
각 성격 유형에 점수를 누적해서 더 높은 점수를 가진 유형을 고르는 문제
R/T
C/F
J/M
A/N

zip 함수를 써서 설문조사와 선택지를 동시에 순회
RT, 5

4가 기준임
"""
def solution(survey, choices):
    answer = ''
    type_score = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0,
    }

    for question, choice in zip(survey, choices):
        disagree_type = question[0]
        agree_type = question[1]

        # 점수 계산
        score = abs(choice - 4)
        
        # 선택지 방향에 따라 점수 누적(4는 포함 X)
        if choice < 4:
            type_score[disagree_type] += score
        elif choice > 4:
            type_score[agree_type] += score

    for left, right in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if type_score[left] >= type_score[right]:
            answer += left
        else:
            answer += right

    return answer
