"""
모듈러 사용해서 찍기 패턴과 정답을 동기화하고...
문제 계산하는 함수를 따로 작성해보자
"""
def solution(answers):
    scores = []         
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 수포자 점수 계산 함수
    def get_score(pattern):
        score = 0

        for i in range(len(answers)):
            # 현재 문제 번호 i를 패턴 길이로 나눈 나머지를 모듈러로 사용
            pattern_index = i % len(pattern)
            
            # 찍기 성공하면 점수 상승
            if answers[i] == pattern[pattern_index]:
                score += 1

        return score

    for pattern in patterns:
        scores.append(get_score(pattern))

    max_score = max(scores)
    result = []

    # 점수가 최고점과 같은 수포자를 result에 넣기
    for i in range(len(scores)):
        if scores[i] == max_score:
            result.append(i + 1)

    return result