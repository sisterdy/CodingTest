def solution(arr):
    answer = []
    for i in arr:
        # 배열의 바로 이전원소와 다르거나, 배열이 비어있다면 값을 추가한다.
        if not answer or answer[-1] != i:
            answer.append(i)
    return answer
