"""정답 배열과 각 수포자의 찍기 패턴을 비교한다.
모든 문제를 순회하며 정답 개수를 세고(완전탐색),
가장 높은 점수를 받은 수포자들을 오름차순으로 반환한다."""

def solution(answers):
    # 각 수포자의 찍기 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 점수 계산: 각 패턴별로 정답과 일치하는 개수 합산 (완전탐색)
    scores = [
        sum(pattern[i % len(pattern)] == answer 
            for i, answer in enumerate(answers))
        for pattern in patterns
    ]
    
    # 최고점 찾기
    max_score = max(scores)
    
    # 최고점을 받은 수포자들을 answer에 담기 (자동으로 오름차순)
    answer = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return answer