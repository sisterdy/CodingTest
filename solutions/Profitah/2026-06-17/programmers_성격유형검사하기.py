"""
4개의 지표(RT, CF, JM, AN)가 있고 각 지표는 2가지 유형으로 나뉨.
설문(survey)과 선택지(choices)를 기반으로 성격 점수를 계산하여 최종 MBTI를 구한다.

구해야할것:
- 4개 지표별 더 높은 점수의 유형 선택
- 최종 4글자 성격 결과

특이사항:
- survey는 두 글자 문자열 (왼쪽/오른쪽 유형)
- choices는 1~7 (4는 중립)
- 딕셔너리로 점수 관리
"""

def solution(survey, choices):

    # 1. 유형별 점수 딕셔너리 초기화
    score = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }

    # 2. survey + choices 순회하며 점수 계산
    for i in range(len(survey)):
        left = survey[i][0]
        right = survey[i][1]
        choice = choices[i]

        # 3. 선택지에 따른 점수 반영
        # 4 미만이면 왼쪽 점수 증가
        if choice < 4:
            score[left] += 4 - choice

        # 4 초과면 오른쪽 점수 증가
        elif choice > 4:
            score[right] += choice - 4

    # 4. 지표별 비교 후 결과 생성
    answer = ""

    answer += 'R' if score['R'] >= score['T'] else 'T'
    answer += 'C' if score['C'] >= score['F'] else 'F'
    answer += 'J' if score['J'] >= score['M'] else 'M'
    answer += 'A' if score['A'] >= score['N'] else 'N'

    return answer