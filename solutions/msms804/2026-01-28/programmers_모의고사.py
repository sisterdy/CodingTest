# 나머지 계산(%)하면 되는거같은데
# 찾아보니 enumerate라는 함수를 쓸 수 있는듯

def solution(answers):
    answer = []
    scores = [0, 0, 0]
    supoja_1 = [1, 2, 3, 4, 5]
    supoja_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == supoja_1[i % len(supoja_1)]:
            scores[0] += 1
        if answers[i] == supoja_2[i % len(supoja_2)]:
            scores[1] += 1
        if answers[i] == supoja_3[i % len(supoja_3)]:
            scores[2] += 1
    
    for i in range(len(scores)):
        if scores[i] == max(scores): # scores중 max와 같다면 answer에 추가
            answer.append(i + 1)
    return answer