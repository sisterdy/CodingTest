def solution(arr):
    answer = []
    for x in arr:
        if not answer or answer[-1] != x:
            answer.append(x)
    return answer